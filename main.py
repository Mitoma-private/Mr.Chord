import os
import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as stc
import time
import config
import base64
from act_btc import chord_estimation

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
    
##left, rightとbuttonの配置
left, right = st.columns([3,1])
l_button, c_button, r_button = st.columns(3)

##ボタン押下時の処理
if r_button.button("次へ"):
    st.session_state['page_control'] += 1
if  r_button.button("リセット"):
    st.session_state['page_control'] = 0
    st.session_state['upload'] = 0

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

    wav_file = left.file_uploader("音楽ファイルをアップロード", type=None)
    if wav_file is not None:
        st.session_state['upload'] += 1
        filename = wav_file.name
        if filename.lower().endswith(".wav"):
            left.success("ファイルを取得しました")
            st.session_state['file_pick'] = True
        else:
            left.error("wavファイルをアップロードしてください")

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
        chord_lines = chord_estimation(wav_file)
    st.text(chord_lines)
    

