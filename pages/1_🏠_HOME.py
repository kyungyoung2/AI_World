import streamlit as st

st.set_page_config(
    page_title="World With AI",
    page_icon="👋",
)

st.subheader("World With AI")
#st.sidebar.success("Select a page above.")
st.write(" ")
st.image('ai.jpg')
st.markdown('인공지능과 함께하는 세상에 오신 것을 환영합니다. 이 공간에서는 인공지능의 개념,'
            '인공지능 사례(생성형 인공지능)'
            '인공지능 윤리등에 대한 내용을 다룹니다.')
st.markdown("1. **인공지능 개념**: 머신러닝, 딥러닝")
st.markdown("2. **인공지능 모델**: 랜덤 포레스트, 최근접이웃")
st.markdown("3. **데이터 분석**: 데이터 분석 사례를 2가지 살펴봅니다.")
st.markdown("4. **생성형 AI**: 챗봇, 이미지생성, 네이버클로바더빙")
st.markdown("5. **나도 질문왕**: 챗GPT에서 주어진 주제애 대한 질문을 던져보세요!")
st.markdown("6. **인공지능 윤리**: 트롤리 딜레마에 대해 어떻게 생각하는지 다양한 의견을 내봅니다.")
st.divider()