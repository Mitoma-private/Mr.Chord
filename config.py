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
def Voice_content_songs(name):
    path = "./Voice/song/"    
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