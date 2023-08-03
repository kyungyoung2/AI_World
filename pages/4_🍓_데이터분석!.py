import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import FinanceDataReader as fdr

st.title("데이터분석")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2, tab3= st.tabs(['성적분석  ', '삼성전 주식 조회  ', 'MNIST'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write("")
    st.write('''
        ## 점수 데이터
        3명의 학생의 국어, 영어, 수학 점수를 시각화하여 나타냅니다.''')
    plt.rcParams['font.family'] = "NanumGothic"
    plt.rcParams['axes.unicode_minus'] = False

    #DataFrame 생성
    data = pd.DataFrame({
        '이름' : ['이안','수현','지희'],
        '국어' : [95,75,80],
        '영어': [85, 90, 55],
        '수학': [100, 80, 90]
    })
    st.dataframe(data, use_container_width=True)
    fig, ax = plt.subplots()
    ax.bar(data['이름'], data['국어'])
    st.pyplot(fig)

with tab2:
    # tab B를 누르면 표시될 내용
    # Finance Data Reader
    # https://github.com/financedata-org/FinanceDataReader
    st.subheader("조회 시작을 선택하세요.")
    date = st.date_input(
        "조회 시작일을 선택해 주세요",
        datetime.datetime(2022, 1, 1)
    )
    st.subheader("알고 싶은 종목코드 입력하세요.")
    code = st.text_input(
        '종목코드예시: 삼성전자:005930',
        value='',
        placeholder='종목코드를 입력해 주세요'
    )

    if code and date:
        df = fdr.DataReader(code, date)
        data = df.sort_index(ascending=True).loc[:, 'Close']
        st.line_chart(data)

with tab3:
    # tab B를 누르면 표시될 내용
    st.write('비지도 학습')


