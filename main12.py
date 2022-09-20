
import streamlit as st
import pyperclip
from time import sleep
import re

st.write("공문분석프로그램")
checkbox = st.checkbox('agree')
text = st.text_area("Your text:")

btn_click=st.button("confirm",key='confirm_btn')


title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

p = re.compile('[a-z]+')


if btn_click:
    st.write(text)
    list=text.split('\n')







f=open("파일.txt","w", encoding='cp949')

