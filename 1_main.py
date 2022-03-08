from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

# ２次元配列を作る
# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40],
# })

#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0))#heightやwidthを指定することも可能
#st.table(df) #staticな表を使いたい時はテーブルを使う。

# Magicコマンド
# """
# # MarkDownも使えちゃうンゴね
# ## キャア便利！
# ```python
# print('Hello! World')

# """
# st.latex(r'''
#      a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#      \sum_{k=0}^{n-1} ar^k =
#      a \left(\frac{1-r^{n}}{1-r}\right)
#      ''')


# #描画してみよう！
# df = pd.DataFrame(
#    np.random.rand(20,3),
#    columns=['a','b','c'],
#    )
# #折線グラフで描いてみよう
# st.line_chart(df)
# #エリアチャートを作ってくれたり
# st.area_chart(df)
# #棒グラフを生成したりもできる
# st.bar_chart(df)

#マップを作ってみる
# df = pd.DataFrame(
#    np.random.randn(1000,2)/[50,50]+[35.6,139.7],
#    columns=['lat','lon'],
# )
# st.map(df)

#画像を読み込んでみる
# st.write('Display Image')
# img = Image.open('.drawio.png')
# st.image(img,caption='drawio',use_column_width=True)