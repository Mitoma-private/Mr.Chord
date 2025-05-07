import streamlit as st
import numpy as np
from PIL import Image
import pandas as pd

st.title("曲当てロボット コードくん")
st.text("コードくんはピアノ音源を読み込ませることでそれがなんの曲かを当てることができるよ！")

default = Image.open("./figure/default.png")
happy = Image.open("./figure/happy.png")
learning = Image.open("./figure/learning.png")
sad = Image.open("./figure/sad.png")

left, right = st.columns([3,1])
right.image(default, caption="コードくん", width=200)
left.subheader("①15曲の中から好きな曲を選んでね!")

data_df = pd.DataFrame(
    {
        "曲リスト":["ライラック / Mrs Green Apple",
                  "美しい鰭 / スピッツ",
                  "マリーゴールド / あいみょん",
                  "水平線 / back number",
                  "若者のすべて / フジファブリック",
                  "RPG / SEKAI NO OWARI",
                  "さよならエレジー / 菅田将暉",
                  "怪獣の花唄 / Vaundy"],
        "曲リスト2":["シンデレラボーイ / Saucy dog",
                  "Lemon / 米津玄師",
                  "となりのトトロ / 井上あずみ",
                  "115万キロのフィルム / official髭男dism",
                  "ドライフラワー / 優里",
                  "奏(かなで) / スキマスイッチ",
                  "ホール・ニュー・ワールド / ディズニー",
                  ""],
    }
)
left.dataframe(data_df)

