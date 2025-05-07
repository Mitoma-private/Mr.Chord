import streamlit as st
import numpy as np
from PIL import Image

st.title("曲当てロボット コードくん")
st.text("コードくんはピアノを引いた音源を読み込ませることでそれがなんの曲かを当てることができるよ！")

default = Image.open("./figure/default.png")
happy = Image.open("./figure/happy.png")
learning = Image.open("./figure/learning.png")
sad = Image.open("./figure/sad.png")

left, right = st.colmuns(2)
right.image(default, caption="コードくん", width=100)
left.subheader("①15曲の中から好きな曲を選んでみよう!")

