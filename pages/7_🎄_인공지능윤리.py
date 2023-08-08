import streamlit as st

st.title("😊인공지능 윤리")
tab1, tab2 = st.tabs(['인공지능 윤리','트롤리 딜레마'])

with tab1 :

    st.subheader("1. 인공지능 윤리")
    st.markdown("""
        <p style = "background-color:#EAEAEA;">
        인공지능 기술의 발전은 우리의 생활을 편리하게 바꿔 주고 있습니다. 하지만 인공지능의 발달과 더불어 윤리적인 쟁점들이 세간에 자주 오르내리곤 합니다.
        인공지능과 함께 살아가야 할 세상. 인공지능과 공존하기 위한 윤리적인 문제에 대해 생각해봅니다.<br>
        </p>
        """, unsafe_allow_html=True)

    st.markdown("""
    - 자율주행자동차가 사고를 낸다면 그 책임은 누구에게 물어야할까?
    - 인공지능 의사가 잘못된 판단을 내리면 누구의 책임일까?
    - 범죄 예측 인공지능이 범죄를 저지를 만한 사람을 미리 판단하여 감시하는 것은 괜찮은걸까?
    - 인간에게 해를 끼칠 수도 있는 군사용 로봇을 개발하는 것은 괜찮은걸까?
    """)

    st.subheader("2. 국가 인공지능 윤리기준의 3대 기본 원칙")
    st.markdown("우리나라는 2020년 12월 <b>인간성을 위한 인공지능(AI for Humanity)</b>을 위해 인공지능 개발에서 활용에 이르는 전 과정에서 고려되어야할 기준으로 3개 기본 원칙을 제시했습니다.")

    st.markdown("""
    - 인간 존엄성 원칙
    - 사회의 공공선 원칙
    - 기술의 합목적성 원칙
    """)

    st.subheader("3.국가 인공지능 윤리기준의 10대 핵심 요건")
    st.markdown("인공지능 윤리 3대 기본 원칙을 실천하고 이행할 수 있도록 인공지능 개발~활용 전 과정에서 충족되어야 할 10대 핵심 요건은 다음과 같습니다.")

    st.markdown("""
    - 인권 보장
    - 프라이버시 보호
    - 다양성 존중
    - 침해 금지
    - 공공성
    - 연대성
    - 데이터 관리
    - 책임성
    - 안전성
    - 투명성
    """)
    st.markdown("""
    ▶<a href='https://itwiki.kr/w/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5_%EC%9C%A4%EB%A6%AC'>인공지능 윤리</a><br>
    ▶<a href='https://itwiki.kr/w/%EA%B5%AD%EA%B0%80_%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5_%EC%9C%A4%EB%A6%AC%EA%B8%B0%EC%A4%80#3%EB%8C%80_%EA%B8%B0%EB%B3%B8%EC%9B%90%EC%B9%99'>국가 인공지능 윤리 기준 </a>
    """, unsafe_allow_html=True)

with tab2 :
    st.subheader("1. 트롤리 딜레마란?")