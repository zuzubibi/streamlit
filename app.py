import streamlit as st
import pandas as pd


# 타이틀, 헤더, 서브헤더
st.title('Title *Markdown* 인식')
st.header('Title *Markdown* 인식')
st.subheader('Title *Markdown* 인식')

# 텍스트, 마크다운
st.text('title *Markdown* 인식 못함')
st.markdown('*Markdown* 출력')

# 텍스트 또는 다양한 Python 변수/객체 출력
st.text('This is some text.')
x = 10
y = 20
st.write('x =', x, 'y =', y)

# 데이터프레임
df = pd.DataFrame({'col1': [1,2,3]})
df
st.write('데이터프레임', df)

# 그래프 출력
import matplotlib.pyplot as plt
import numpy as np
arr = np.random.normal(1,1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
fig

# 코드 출력
code = '''def hello():
print("Hello Streamlit!")'''

st.code(code, language='python')

# 캡션 출력
st.caption('This is :blue[blue]')
st.caption('This is :red[red]')
st.caption('This is :green[green]')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# 이모티콘 삽입
'여름엔 딱 좋아 :sunglasses:'
':100:점~ :smile:'
':100:점! :smile:ㅎㅎ  :thumbsup:최고!!'


agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
    