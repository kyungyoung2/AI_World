import streamlit as st


st.title("인공지능이란?")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2, tab3, tab4= st.tabs(['인공지능 역사','지도학습', '비지도학습', '강화학습'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write("")
    st.subheader('1. 인공지능이란?')
    st.markdown("인공지능이란 문제 해결을 위해 대상을 **인식**하고 필요한 부분을 **학습**하며, 논리적인 "
                " **판단**과 **추론**하는 능력을 말한다. ")
    st.markdown("인공지능(Ari Intelligenc)이란 용어는 1956년 다트머스 컨퍼런스에서 **존 매카시**가 최초로 주장하였다.")
with tab2:
    # tab B를 누르면 표시될 내용
    st.write('지도 학습')
    st.markdown('지도학습은 정답과 레이블을 주고....학습하는 방법을 말합니다. 지도학습 방법으로는....여기서 정리합시다.')

with tab3:
    # tab B를 누르면 표시될 내용
    st.write('비지도 학습')

with tab4:
    # tab B를 누르면 표시될 내용
    st.write('강화 학습')

