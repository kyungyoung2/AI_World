import streamlit as st

st.set_page_config(
    page_title="World With AI",
    page_icon="👋",
)

st.markdown("""
            <h2 style="text-align:center">AI와 함께하는 세상</h2>
            """, unsafe_allow_html=True)
st.markdown("""
            <h4 style="text-align:right">대상: 2학년</h4>
            """, unsafe_allow_html=True)
st.write(" ")
st.image("images/ai.jpg")
st.markdown('인공지능과 함께하는 세상에 오신 것을 환영합니다. 이 공간에서는 인공지능의 개념,'
            '인공지능 사례(생성형 인공지능)'
            '인공지능 윤리등에 대한 내용을 다룹니다.')
st.markdown("1. **인공지능 개념**: 인공지능 역사, 머신러닝, 딥러닝의 용어에 대해 알아봅니다.")
st.markdown("2. **데이터 분석**: 붓꽃 데이터셋을 활용한 데이터 분석 사례를 2가지 살펴봅니다.")
st.markdown("3. **딥러닝(MNIST)**: 대표적인 딥러닝 예시인 손글씨 숫자 인식 프로그램을 직접 경험해봅니다!")
st.markdown("4. **생성형 인공지능**: 기본 챗봇, 음성변환 챗봇, 이미지 생성 인공지능 등 생성형 AI를 직접 경험해보세요!")
st.markdown("5. **나도 질문왕!**: 챗GPT로 궁금한 내용을 질문하고 자신의 질문 내용을 공유해봅니다!")
st.markdown("6. **인공지능 윤리**: 트롤리 딜레마에 대해 어떻게 생각하는지 다양한 의견을 내봅니다.")
st.divider()