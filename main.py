import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as stc
import time
import config

##タイトル
st.title("曲当てロボット コードさん")
st.text("コードさんはピアノ音源を読み込ませることでそれがなんの曲かを当てることができるよ！")

##変数の設定
if 'page_control' not in st.session_state:
    st.session_state['page_control'] = 0

##left, rightとbuttonの配置
left, right = st.columns([3,1])
l_button, c_button, r_button = st.columns(3)

left.text("tintin")

##ボタン押下時の処理
if r_button.button("次へ"):
    st.session_state['page_control'] += 1
if  r_button.button("リセット"):
    st.session_state['page_control'] = 0
    
if st.session_state['page_control'] == 0:
    left.subheader("やぁ! 私の名前はコードさんだよ!")
    right.image(config.happy, caption="コードさん", width=200)

if st.session_state['page_control'] == 1:
    left.subheader("今から曲あてクイズをやってみよう!")
    right.image(config.default, caption="こーどさん", width=200)

if st.session_state['page_control'] == 2:
    left.subheader("15曲の中から好きな曲を選んでね!")
    right.image(config.default, caption="コードさん", width=200)

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


