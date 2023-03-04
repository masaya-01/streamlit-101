import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 101')

"""
## Progress Bar
"""
st.write("Wait for seconds")
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'**Iteration** {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)
st.write("Let's get started!")

"""
# What is streamlit
"""
st.markdown('Streamlit is **_really cool libraly_**.')
st.markdown("[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")


"""
## DataFrame
### DataFrame1
"""
df1 = pd.DataFrame({
    '1st': [1, 2, 3,4],
    '2nd': [10, 20, 30, 40]
})

left1, middle1, right1 = st.columns(3)
left1.write("write a dataframe")
left1.write(df1)
code_write = 'left1.write(df1)'
left1.code(code_write,language="python")

#dataframe->動的　　　列：axis=0 行：axis=1
middle1.write("show as a dataframe")
middle1.dataframe(df1.style.highlight_max(axis=0, color="red"), width=300, height=200)
code_df = 'middle1.dataframe(df1.style.highlight_max(axis=0, color="red"), width=300, height=200)'
middle1.code(code_df,language="python")

#table->静的
right1.write("show as a table")
right1.table(df1.style.highlight_min(axis = 0, color="green"))
code_table = 'right1.table(df1.style.highlight_min(axis = 0, color="green"))'
right1.code(code_table,language="python")



"""
### DataFrame2
"""
left2, middle2, right2 = st.columns(3)
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
left2.write("show as a line chart")
left2.line_chart(df2)
middle2.write("show as a area chart")
middle2.area_chart(df2)
right2.write("show as a bar chart")
right2.bar_chart(df2)


"""
### DataFrame3
"""
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
    columns=['lat', 'lon']
)
st.write("show map around Shinjuku")
st.map(df3)

"""
## Widget
"""
st.write("Display Image")
if st.checkbox('Show Image'):
    img = Image.open('sample.jpeg')
    st.image(img, caption='sample', use_column_width=True)

st.sidebar.write("# Interactive Widget")
st.sidebar.write("## **Questions**")

option = st.sidebar.selectbox('Q1. 好きな数字は？',list(range(1, 11)))
condition = st.sidebar.slider('Q2. あなたの幸福度は？', 0, 100, 50)
text = st.sidebar.text_input('Q3. 趣味は？')

st.sidebar.write("## **Your answers**")
st.sidebar.write("あなたの好きな数字は", option, "です")
st.sidebar.write("あなたの幸福度は", condition, "です")
if text:
    st.sidebar.write('あなたの趣味は', text, 'です')

"""
## おみくじ
"""
left_colums, right_column = st.columns(2)
botton = left_colums.button('おみくじを引く')
if botton:
    right_column.write('結果：大吉')

"""
## 問い合わせ
"""
expander1 = st.expander('あなたの名前は何ですか')
expander1.write('オオツカマサヤです')
expander2 = st.expander('あなたの出身はどこですか')
expander2.write('岐阜です')
expander3 = st.expander('あなたの専攻は何ですか')
expander3.write('CSです')