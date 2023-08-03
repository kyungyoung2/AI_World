import streamlit as st


st.title("Projects")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2, tab3 = st.tabs(['지도학습', '비지도학습', '강화학습'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write('지도학습')

with tab2:
    # tab B를 누르면 표시될 내용
    st.write('비지도학습')

with tab3:
    # tab B를 누르면 표시될 내용
    st.write('강화학습')

st.write("You have entered")