from cgitb import text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

#画像を読み込んでみる
st.write('Interactive Widgets')

#チェックボックスの使い方
# if st.checkbox('Show Image'):
#     img = Image.open('.drawio.png')
#     st.image(img,caption='drawio',use_column_width=True)

#セレクトボックス
# option = st.selectbox(
#     'tell me your favorite number',
#     list(range(1,11)),
# )
# 'your favorite number is',option,'.'

#テキスト入力 line_areaもあるよ
text = st.text_input('tell me your hobby')
'My hobby is',text,'.'

#スライダー入力
feel = st.slider('How is your feeling?',0,100,30)
'about:',feel