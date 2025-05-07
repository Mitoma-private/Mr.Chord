from PIL import Image

##画像ファイル
default = Image.open("./figure/default.png")
happy = Image.open("./figure/happy.png")
learning = Image.open("./figure/learning.png")
sad = Image.open("./figure/sad.png")

##音声ファイル
def Voice_path(num):
    path = "./Voice/"
    if num < 10:
        num = "0" + str(num)
    else:
        num = str(num)
    
    return path+num+".wav"