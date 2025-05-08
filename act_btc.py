import os 
from btc_model import *
from utils.mir_eval_modules import audio_file_to_features, idx2chord
import glob
import mir_eval

##パラメータ
config = HParams.load("run_config.yaml")
model_file = './test/btc_model.pt'
idx_to_chord = idx2chord
use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")

##モデルのロード
model = BTC_model(config=config.model).to(device)
if os.path.isfile(model_file):
    checkpoint = torch.load(model_file, map_location="cpu", weights_only=False)
    mean = checkpoint['mean']
    std = checkpoint['std']
    model.load_state_dict(checkpoint['model'])
    
##test.pyの内容を置き換えた関数
def chord_estimation(audio_path):
    feature, feature_per_second, song_length_second = audio_file_to_features(audio_path, config)
    feature = feature.T
    feature = (feature - mean) / std
    time_unit = feature_per_second
    n_timestep = config.model['timestep']
    
    num_pad = n_timestep - (feature.shape[0] % n_timestep)
    feature = np.pad(feature, ((0, num_pad), (0, 0)), mode="constant", constant_values=0)
    num_instance = feature.shape[0] // n_timestep
    
    start_time = 0.0
    lines = []
    with torch.no_grad():
        model.eval()
        feature = torch.tensor(feature, dtype=torch.float32).unsqueeze(0).to(device)
        for t in range(num_instance):
            self_attn_output, _ = model.self_attn_layers(feature[:, n_timestep * t:n_timestep * (t + 1), :])
            prediction, _ = model.output_layer(self_attn_output)
            prediction = prediction.squeeze()
            for i in range(n_timestep):
                if t == 0 and i == 0:
                    prev_chord = prediction[i].item()
                    continue
                if prediction[i].item() != prev_chord:
                    lines.append('%.3f %.3f %s\n' % (start_time, time_unit * (n_timestep * t + i), idx_to_chord[prev_chord]))
                    start_time = time_unit * (n_timestep * t + i)
                    prev_chord = prediction[i].item()
                if t == num_instance - 1 and i + num_pad == n_timestep:
                    if start_time != time_unit * (n_timestep * t + i):
                        lines.append('%.3f %.3f %s\n' % (start_time, time_unit * (n_timestep * t + i), idx_to_chord[prev_chord]))
                    break

    chord_time = []
    chords = []
    for line in lines:
        l = line.split(" ")
        start = float(l[0])
        end = float(l[1])
        chord = l[2].replace("\n", "")
        if not chord == "N":
            chords.append(chord)
            chord_time.append(end - start)
    all_time = sum(chord_time)
        
    return chord_time, chords, all_time 

##スコアの計算と一致率の比較
def score_calculate(chord_time, est_labels, all_time):
    GT_labs = glob.glob("./GT_labs/*")
    best_acc = 0
    
    full_score = []
    song_name = []
    for GT_lab in GT_labs:
        song_name.append(GT_lab.split("/")[-1].replace(".lab", ""))
        with open(GT_lab, "r")as f:
            lines = f.readlines()
            last_line = lines[-1]
        GT_all_time = float(last_line.split(" ")[1])
    
        ratio = GT_all_time / all_time
        for i in range(len(chord_time)):
            chord_time[i] = chord_time[i] * ratio
        
        start = 0.0
        end = 0.0
        est_intervals = []
        est_intervals.clear()
        for j in range(len(chord_time)):
            start = end
            end = start + chord_time[j]
            est_intervals.append([round(start, 3), round(end, 3)])
        est_intervals = np.array(est_intervals)
    
    
        ref_labels = []
        comparisons = []
        score, ref_label, comparison = root_score(GT_lab, est_intervals, est_labels)

        full_score.append(score)
        ref_labels.append(ref_label)
        comparisons.append(comparison)
        
    return full_score, song_name, ref_labels, comparisons

##スコアの計算
def root_score(GT_lab, est_intervals, est_labels):
    (ref_intervals, ref_labels) = mir_eval.io.load_labeled_intervals(GT_lab)
    est_intervals, est_labels = mir_eval.util.adjust_intervals(est_intervals, est_labels, ref_intervals.min(),
                                                                ref_intervals.max(), mir_eval.chord.NO_CHORD,
                                                                mir_eval.chord.NO_CHORD)
    (intervals, ref_labels, est_labels) = mir_eval.util.merge_labeled_intervals(ref_intervals, ref_labels,
                                                                                est_intervals, est_labels)
    durations = mir_eval.util.intervals_to_durations(intervals)
    comparisons = mir_eval.chord.majmin(ref_labels, est_labels)
    score = mir_eval.chord.weighted_accuracy(comparisons, durations)

    return score, ref_labels, comparisons
