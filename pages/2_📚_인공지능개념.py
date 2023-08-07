import streamlit as st

st.title("인공지능(Artificial Intelligence)이란?")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2, tab3 = st.tabs(['인공지능 역사','머신러닝', '딥러닝'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write("")
    st.subheader('1. 인공지능이란?')
    st.markdown("인공지능이란 문제 해결을 위해 대상을 **인식**하고 필요한 부분을 **학습**하며, 논리적인 "
                " **판단**과 **추론**하는 능력을 말한다. ")
    st.markdown("인공지능(Ari Intelligenc)이란 용어는 1956년 다트머스 컨퍼런스에서 **존 매카시**가 최초로 주장하였다.")

    st.subheader('2. 인공지능의 역사')
    st.markdown('**① 인공지능의 탄생**: 인공지능이라는 용어는 1956년 다트머스 회의에서 존 매카시가 최초로 주장하였으며,'
                '1950년대 전후로 컴퓨터가 등장하고 **앨런 튜링**이 생각하는 기계에 대한 아이디어를 발표하면서 인공지능 기술이 주목받기 시작하였다. ')
    st.image('https://image.ahnlab.com/comm/info/1312260093411361.png')
    st.markdown('**② 전문가 시스템(Expert System)**: 1970년대 사람들은 전문가의 지식을 컴퓨터에 그대로 담을 수 있다면 훌륭한 인공지능이 될 것으로 생각하였다. '
                '그래서 지식 표현과 추론에 대한 연구 끝에 **전문가 시스템**을 구축하였다. '
                '전문가 시스템에 인간의 모든 규칙을 넣기에 불가능했기에 **의료 분야 같은 일부 전문 영역에서만 주로 사용**되었다. '
                '이 시기에 발달했던 지식의 표현과 추론의 핵심 이론은 현재 인공지능이 데이터를 바탕으로 결과를 예측하는 과정에 활용되 있다.')
    st.markdown('**③ 딥 블루(Deep Blue)**: 1977년 인공지능 **딥블루**가 세계 체스 챔피언과의 대결에서 승리를 거두었다.'
                '딥블루는 **가능한 모든 경우를 탐색하는 효율적인 알고리즘**을 이용해 문제를 해결할 뿐 스스로 학습하는 수준에는 이르지 못했다'
                '다만 탐색 알고리즘은 알파고와 같은 인공지능을 구현하는 핵심 개념이 되었다.')
    st.image('https://thumb.mt.co.kr/06/2016/05/2016051016244917713_2.jpg/dims/optimize/')
    st.caption('1997년 5월 11일 딥 블루와의 대국을 치르면서 고뇌하고 있는 게리 카스파로프,'
               '출처 https://thumb.mt.co.kr/06/2016/05/2016051016244917713_2.jpg/dims/optimize/')

    st.markdown('**④ 알파고(Alphago)**: 2016년 세계 최고 바둑 기사인 **이세돌과 알파고의 대결**은 인공지능 기술에 대해 대중에게 가증 크게 알린 사건이었다.'
                '알파고는 **인공신경망을 이용해 바둑 경기 16만건을 학습**하면서 스스로 규칙을 찾아냈기 때문에 **인간이 생각하지 못한 전략을 구사**할 수 있었다.')
    st.image('http://image.dongascience.com/Photo/2016/03/14575928244225.jpg')
    st.caption('2016년 3월 10일 알파고와 두 번째 대국을 하고 있는 이세돌 구단,'
           '출처 http://image.dongascience.com/Photo/2016/03/14575928244225.jpg')

    st.markdown('**⑤ ChatGPT(Chat Generative Pre-trained Trasformer)**: 2022년 11월 30일에 출시되어 현재까지 큰 반향을 일으키고 있는 **생성형 인공지능**이다.'
                '**Large Language Model**로 자연어 처리에 획기적인 발전을 이루었다는 평을 받으며, 출시 5일만에 사용자 1억명을 돌파했다.'
                '다른 LLM모델로 구글의 Bard, 메타의 LLaMA, 네이버 하이퍼클로바X 등이 있다. 챗GPT뿐만 아니라 DALL.E, Midjourney 등의 이미지 생성AI도 각광받고 있다.')
    st.image('https://cdn.eroun.net/news/photo/202304/31633_58340_5223.png')
    st.caption('출처: OpenAI 홈페이지')


with tab2:
    # tab B를 누르면 표시될 내용
    st.write("")
    st.subheader('1.인공지능&머신러닝&딥러닝')
    st.image("ai_structure.jpg")
    st.caption("▲인공지능, 머신러닝, 딥러닝의 관계도")

    st.subheader("2. 머신러닝(Machine Learning)")
    st.markdown('머신러닝은 인공지능을 구현하는 대표적인 방법 중의 하나로, **데이터에서 패턴을 찾아내 문제애 대한 답을 예측하는 알고리즘**이다. '
                '머신러닝의 활용 분야로 금융, 이미지프로세싱, 금융분석 및 탐지 분야, 음성인식, 로봇제어 분야 등이 있다.')
    st.write("")
    st.markdown("머신러닝의 학습 방법에는 지도 학습, 비지도 학습, 강화 학습의 3가지로 나뉠 수 있다.")
    st.write("")
    st.markdown("""
    - 지도 학습
    - 비지도 학습
    - 강화 학습
    """)
    st.markdown("**① 지도 학습(Supervised Learning)** : 지도 학습은 **데이터와 정답**을 함께 제시하여 학습하는 방법이다. 지도 학습에는 분류와 회귀 모델이 있다.")
    st.markdown("**② 비지도 학습(Unsupervised Learning)** : 비지도 학습은 정답이 없는 **데이터만** 주고 학습하게 방법이다. 정답이 없기 때문에 입력 데이터의 패턴이나 특성을 통해 학습하게 된다.")
    st.markdown("**③ 강화 학습(Reinforcement Learning)** : 강화 학습은 입력 데이터를 학습하여 **경험과 보상**을 통해 목표값을 찾도록 학습하는 방법이다. 즉 입-출려간의 상관관계를 찾는 것이 아니라, 시행착오에 대한 보상 체계를 바탕으로"
                "지속적인 경험에 통해 최선책을 찾도록 하는 방법이다. 주로 자율주행자동차나 게임, 주식 등에 활용된다.")

with tab3:
    # tab B를 누르면 표시될 내용
    st.write("")
    st.subheader('딥러닝(Deep Learning)')
    st.subheader("2. 머신러닝(Machine Learning)")
    st.markdown('머신러닝은 인공지능을 구현하는 대표적인 방법 중의 하나로, **데이터에서 패턴을 찾아내 문제애 대한 답을 예측하는 알고리즘**이다. '
                '머신러닝의 활용 분야로 금융, 이미지프로세싱, 금융분석 및 탐지 분야, 음성인식, 로봇제어 분야 등이 있다.')



