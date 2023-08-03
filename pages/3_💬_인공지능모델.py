import streamlit as st

st.title("인공지능이란?")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2= st.tabs(['랜덤포레스트','최근접이웃'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write("")
    st.subheader('1.램덤포레스트 모델')

with tab2:
    # tab B를 누르면 표시될 내용
    st.write("")
    st.subheader('최근접이웃 모델')

