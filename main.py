import streamlit as st
import time

st.title("Streamlit 超入門")

st.write("レイアウトを整える")
サイドバー表示
text = st.sidebar.text_input('あなたの趣味は？')
condition = st.sidebar.slider("あなたの調子は？",0,100,25)

"あなたの趣味：",text
"コンディション：",condition

#2カラムにする
# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここが右カラムです')

#エクスパンダー
# expander1 = st.sidebar.expander('といあわせ1')
# expander1.write('ライト')
# expander2 = st.sidebar.expander('といあわせ2')
# expander2.write('ライト')
# expander3 = st.sidebar.expander('といあわせ3')
# expander3.write('ライト')

st.write('プレグレスバー')


#空の要素を追加
latest_iteration = st.empty()
 #0から100まで/0.0から1.0　パーセンテージの考え方
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)

'''
### for文が回ってる間は表示されないにゃん
'''