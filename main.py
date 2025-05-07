import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as stc
import time
import config

##タイトル
st.title("曲当てロボット コードくん")
st.text("コードくんはピアノ音源を読み込ませることでそれがなんの曲かを当てることができるよ！")

##変数の設定
st.session_state['page_control'] = 0


left, right = st.columns([3,1])
l_button, c_button, r_button = st.columns(3)
next_b = r_button.button("次へ")
reset_b = r_button.button("リセット")

right.image(config.default, caption="コードくん", width=200)
left.subheader("①15曲の中から好きな曲を選んでね!")

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


