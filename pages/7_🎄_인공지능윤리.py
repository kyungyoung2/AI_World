import streamlit as st

st.title("😊인공지능 윤리")
tab1, tab2 = st.tabs(['인공지능 윤리','트롤리 딜레마 생각 나누기'])

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

    st.markdown("""
        <p style = "background-color:#EAEAEA;">
        트롤리 딜레마(Trolley Dilemma)란 윤리학 분야의 사고실험으로, 다섯 사람을 구하기 위해 한 사람을 죽이는 것이 도덕적으로 허용 가능한지에 대한 질문이다.(내용 출처: 네이버 지식백과)<br>
        인공지능 기술의 대표 사례인 '자율주행자동차'의 트롤리 딜레마에 대해 생각해보고 자신의 생각을 정리해보자!<br>
        </p>
        """, unsafe_allow_html=True)

    st.subheader("2. 모럴 머신")
    st.markdown("""
                모럴 머신(Moral Machine)은 자율주행자동차의 윤리적 딜레마를 해결하고자 MIT의 라환 교수가 개발한 플랫폼이다.<br>
                이 플랫폼은 다양한 딜레마를 설정하고, 각 딜레마에 대한 사람들의 의견을 수집한다. 수집한 데이터는 자율주행자동차의 개발에 반영된다고 한다.<br>
                """, unsafe_allow_html=True)
    st.image("images/moralmachine.jpg")
    st.markdown("""
                <h6 style="text-align:center">출처: 모럴 머신 사이트</h6>
                """, unsafe_allow_html=True)

    st.subheader("3. 트롤리 딜레마에 대한 생각 나누기")
    st.markdown("""
                <p style = "background-color:#EAEAEA;">
                모럴 머신(Moral Machine) 사이트에 접속하여 자율주행자동차의 트롤리 딜레마 상황에서 여러분의 선택은 어떠한지 결정해보세요!<br>
                결정된 내용을 아래 패들렛에 올려 친구들과 공유합니다..<br>
                <b><font color="red">패들렛 주소: <a href='https://padlet.com/shewill76/padlet-7o3xuer9ngydtv41'>https://bit.ly/43VDs7r</a></font></b>
                <br>                
                </p>
                """, unsafe_allow_html=True)

    st.markdown("""<b><font color="red">①</font></b> 모럴 머신 사이트에 접속합니다.(<a href="https://www.moralmachine.net/">https://www.moralmachine.net/</a>) 
        """, unsafe_allow_html=True)
    st.markdown("<b><font color='red'>②</font></b> 상단 메뉴의 [judge]를 클릭합니다.", unsafe_allow_html=True)
    st.markdown("<b><font color='red'>③</font></b> 나타나는 상황에 따라 선택합니다.(13가지 질문)", unsafe_allow_html=True)
    st.image("images/moralmachine2.jpg")
    st.markdown(
        "<b><font color='red'>④</font></b> 여러분의 판단 성향은 어땠나요? 패들렛에 공유해봅니다.",
        unsafe_allow_html=True)
    st.image("images/trolley.jpg")
