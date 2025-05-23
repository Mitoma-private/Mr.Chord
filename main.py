import os
import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as stc
import time
import config
import base64
from act_btc import chord_estimation, score_calculate
from io import BytesIO
import tempfile

os.environ["STREAMLIT_DISABLE_WATCHDOG_WARNINGS"] = "true"

##タイトル
st.title("曲当てロボット コードさん")
st.text("コードさんはピアノ音源を読み込ませることでそれがなんの曲かを当てることができるよ！")

##変数の設定
if 'page_control' not in st.session_state:
    st.session_state['page_control'] = 0
if 'upload' not in st.session_state:
    st.session_state['upload'] = 0
if 'file_pick' not in st.session_state:
    st.session_state['file_pick'] = False
if 'wav_file' not in st.session_state:
    st.session_state['wav_file'] = "まだ何も入ってないよ"
if 'max_score_song' not in st.session_state:
    st.session_state['max_score_song'] = ''
if 'max_score' not in st.session_state:
    st.session_state['max_score'] = 0.0
if 'YorN' not in st.session_state:
    st.session_state['YorN'] = False
if 'push_YorN' not in st.session_state:
    st.session_state['push_YorN'] = 0
    
##left, rightとbuttonの配置
left, right = st.columns([3,1])
l_button, c_button, r_button = st.columns(3)
Yes_button, No_button = st.columns(2)

##ボタン押下時の処理
if r_button.button("次へ"):
    st.session_state['page_control'] += 1
if  c_button.button("リセット"):
    st.session_state['page_control'] = 0
    st.session_state['upload'] = 0
    st.session_state['file_pick'] = False
    st.session_state['wav_file'] = "まだ何も入ってないよ"
    st.session_state['max_score_song'] = ''
    st.session_state['max_score'] = 0.0
    st.session_state['YorN'] = False
    st.session_state['push_YorN'] = 0
if l_button.button("戻る"):
    st.session_state['page_control'] -= 1

##画面遷移0
if st.session_state['page_control'] == 0:
    right.image(config.default, caption="コードさん", width=200)

##画面遷移1
if st.session_state['page_control'] == 1:
    left.subheader("やぁ! 私の名前はコードさんだよ!")
    right.image(config.happy, caption="コードさん", width=200)
    
    ##オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)
    
##画面遷移2
if st.session_state['page_control'] == 2:
    left.subheader("今から曲あてクイズをやってみよう!")
    right.image(config.default, caption="コードさん", width=200)
    
    ##オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)

##画面遷移3
if st.session_state['page_control'] == 3:
    left.subheader("15曲の中から好きな曲を選んでね!")
    right.image(config.default, caption="コードさん", width=200)

    ##オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)

    data_df = pd.DataFrame(
        {
            "曲リスト":["ライラック / Mrs Green Apple",
                    "美しい鰭 / スピッツ",
                    "マリーゴールド / あいみょん",
                    "水平線 / back number",
                    "若者のすべて / フジファブリック",],
            "曲リスト2":["さよならエレジー / 菅田将暉",
                    "怪獣の花唄 / Vaundy",
                    "シンデレラボーイ / Saucy dog",
                    "Lemon / 米津玄師",
                    "となりのトトロ / 井上あずみ"],
            "曲リスト3":["115万キロのフィルム / official髭男dism",
                    "ドライフラワー / 優里",
                    "奏(かなで) / スキマスイッチ",
                    "ホール・ニュー・ワールド / ディズニー",
                    "RPG / SEKAI NO OWARI"],
        }
    )
    left.dataframe(data_df)

##画面遷移4
if st.session_state['page_control'] == 4:
    left.subheader("じゃあ、次は実際に曲を演奏してみよう")
    right.image(config.default, caption="コードさん", width=200)
    
    ##オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)

##画面遷移5
if st.session_state['page_control'] == 5:
    left.subheader("演奏は終わったかな？そしたら、そのファイルを私に頂戴！")

    wav_file = left.file_uploader("音楽ファイルをアップロード", type=["wav", "mp3", "flac"])
    if wav_file is not None:
        st.session_state['upload'] += 1
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav")as tmp:
            tmp.write(wav_file.read())
            tmp_path = tmp.name
            left.success("ファイルを取得しました")
            st.session_state['file_pick'] = True
            st.session_state['wav_file'] = tmp_path

    if st.session_state['upload'] == 0:
        ##オーディオを回す処理
        voice_placeholder = st.empty()
        voice_html = config.Voice_content(st.session_state['page_control'])
        voice_placeholder.empty()
        time.sleep(0.5)
        voice_placeholder.markdown(voice_html, unsafe_allow_html=True)
    right.image(config.happy, caption="コードさん", width=200)
    
##画面遷移6
if st.session_state['page_control'] == 6:
    if st.session_state['file_pick'] == False:
        st.error("ファイルを選んでください")
        st.error("もう一度やり直してね")
        st.stop()
    left.subheader("ファイルを読み込んだよ")
    right.image(config.default, caption="コードさん", width=200)
    
    ##オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)

##画面遷移7
if st.session_state['page_control'] == 7:
    left.subheader("では、ここから曲を推定するよ！少し待ってね！")
    right.image(config.default, caption="コードさん", width=200)
    
    ##オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)

##画面遷移8
if st.session_state['page_control'] == 8:
    left.subheader("ファイルを解析しています...")
    right.image(config.learning, caption="コードさん", width=200)
    
    ##オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)
    
    with st.spinner("処理中です..."):
        chord_time, chords, all_time = chord_estimation(st.session_state['wav_file'])
        full_score, song_name= score_calculate(chord_time, chords, all_time)
        st.session_state['max_score'] = full_score
        st.session_state['max_score_song'] = song_name
        left.success("推定が終了しました")
    
##画面遷移9
if st.session_state['page_control'] == 9:
    left.subheader("推定が完了したよ")
    right.image(config.default, caption="コードさん", width=200)
    
    #オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)

##画面遷移10
if st.session_state['page_control'] == 10:
    left.subheader("君の選んだ曲は...")
    right.image(config.default, caption="コードさん", width=200)
    
    #オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)

##画面遷移9
if st.session_state['page_control'] == 11:
    txt = st.session_state['max_score_song'].split("-")[-1] + "!!!"
    left.subheader(txt)
    right.image(config.default, caption="コードさん", width=200)
    left.text(st.session_state['max_score'])
    
    if Yes_button.button("正解"):
        st.session_state['YorN'] = True
        left.success("正解！")
        st.session_state['push_YorN'] += 1
    if No_button.button("不正解"):
        st.session_state['YorN'] = False
        left.error("不正解...")
        st.session_state['push_YorN'] += 1

    if st.session_state['push_YorN'] == 0:
        #オーディオを回す処理
        voice_placeholder = st.empty()
        song_html = config.Voice_content_songs(st.session_state['max_score_song'])
        voice_placeholder.empty()
        time.sleep(0.5)
        voice_placeholder.markdown(song_html, unsafe_allow_html=True)
        
if st.session_state['page_control'] == 12:
    if st.session_state['YorN']:
        left.subheader("やったー！正解だね！")
        right.image(config.happy, caption="コードさん", width=200)
    else:
        left.subheader("そっか...残念だね...")
        right.image(config.sad, caption="コードさん", width=200)
        
    
    #オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.YorN_content(st.session_state['YorN'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)
    
if st.session_state['page_control'] == 13:
    left.subheader("デモは以上になります。楽しんでくれたかな？")
    right.image(config.default, caption="コードさん", width=200)
    
    #オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)

if st.session_state['page_control'] == 14:
    left.subheader("ということで、ここからは三苫君にバトンタッチするね")
    right.image(config.default, caption="コードさん", width=200)
    
    #オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)

if st.session_state['page_control'] == 15:
    left.subheader("じゃあみんな、バイバーイ！")
    right.image(config.happy, caption="コードさん", width=200)
    
    #オーディオを回す処理
    voice_placeholder = st.empty()
    voice_html = config.Voice_content(st.session_state['page_control'])
    voice_placeholder.empty()
    time.sleep(0.5)
    voice_placeholder.markdown(voice_html, unsafe_allow_html=True)

if st.session_state['page_control'] == 16:
    left.header("終わり")
    right.image(config.happy, caption="コードさん", width=200)
    st.stop()
