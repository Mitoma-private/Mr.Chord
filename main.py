import streamlit as st
import numpy as np
from PIL import Image

st.title("曲当てロボット コードくん")
st.text("コードくんはピアノ音源を読み込ませることでそれがなんの曲かを当てることができるよ！")

default = Image.open("./figure/default.png")
happy = Image.open("./figure/happy.png")
learning = Image.open("./figure/learning.png")
sad = Image.open("./figure/sad.png")

left, right = st.columns([3,1])
right.image(default, caption="コードくん", width=200)
left.subheader("①15曲の中から好きな曲を選んでね!")

