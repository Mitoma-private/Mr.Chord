from PIL import Image
import base64

##画像ファイル
default = Image.open("./figure/default.png")
happy = Image.open("./figure/happy.png")
learning = Image.open("./figure/learning.png")
sad = Image.open("./figure/sad.png")

##音声ファイル
def Voice_content(num):
    path = "./Voice/"
    if num < 10:
        num = "0" + str(num)
    else:
        num = str(num)
    
    voice_file = path+num+".wav"
    with open(voice_file, "rb")as f:
        contents = f.read()
        
    voice_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
    voice_html = """
                    <audio autoplay=True>
                    <source src="%s" type="audio/ogg" autoplay=True>
                    Your browser does not support the audio element.
                    </audio> 
                 """%voice_str

    return voice_html

##音声ファイル
def Voice_content_songs(num, song_name):
    if num < 10:
        num = "0" + str(num)
    else:
        num = str(num)
    path = "./Voice/"
    voice_file = path+num+".wav"
    song_file = path + "song/" + song_name + ".wav"
    with open(voice_file, "rb")as f:
        contents = f.read()
    with open(song_file, "rb")as f:
        contents_song = f.read()
        
    voice_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
    song_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents_song).decode())

    mime_type = "audio/wav"
    voice_html = """
                    <audio id="audio1" autoplay=True>
                        <source src="{song_str}" type="audio/ogg" autoplay=True>
                        Your browser does not support the audio element.
                    </audio> 
                    
                    <audio id="audio2">
                        <source src="{voice_str}" type="audio/ogg" autoplay=True>
                        Your browser does not support the audio element.
                    </audio> 
                    
                    <script>
                        const audio1 = document.getElementById("audio1");
                        const audio2 = document.getElementById("audio2");
                        
                        audio1.play();
                        audio1.onended = () => {{
                            audio2.play();
                        }};
                    </script>
                 """

    return voice_html

##音声ファイル
def YorN_content(YorN):
    path = "./Voice/"
    if YorN:
        name = "Yes"
    else:
        name = "No"
    
    voice_file = path+name+".wav"
    with open(voice_file, "rb")as f:
        contents = f.read()
        
    voice_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
    voice_html = """
                    <audio autoplay=True>
                    <source src="%s" type="audio/ogg" autoplay=True>
                    Your browser does not support the audio element.
                    </audio> 
                 """%voice_str

    return voice_html