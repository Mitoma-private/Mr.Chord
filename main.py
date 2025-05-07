import streamlit as st
import numpy as np
from PIL import Image

st.title("曲当てロボット コードくん")
st.text("コードくんはピアノを引いた音源を読み込ませることでそれがなんの曲かを当てることができるよ！")

default = Image.open("./figure/default.png")
st.image(default, caption="コードくん")
st.subheader("①15曲の中から好きな曲を選んでみよう!")

