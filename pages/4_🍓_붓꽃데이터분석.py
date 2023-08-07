import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("붓꽃 데이터 분석하기")
df = pd.read_csv("iris.csv")

tab1, tab2, tab3, tab4 = st.tabs(['붓꽃 데이터란?', '붓꽃 데이터 보기','붓꽃 데이터 필터링','붓꽃 데이터 시각화'])
with tab1 :
    st.subheader("1. 붓꽃(Iris) 데이터 세트란?")
    st.markdown("""
        <p style="background-color:#EAEAEA">
            통계학자 R.A. 피셔가 1936년에 소개한 데이터 세트로, <b><font color="red">세 가지 다른 품종의 붓꽃(Setosa, Versicolor, Virginica)</font></b>의 
            형태적 특징으로 이루어진 수집한 <b>표준 데이터 세트</b>이다.<br>
            붓꽃 데이터 세트는 붓꽃의 꽃받침과 꽃잎에 대한 측정 자료로 구성된 데이터로, 통계학과 머신 러닝 분야에서 가장 널리 사용되는 
            데이터 세트들 중 하나이다. 각 샘플에는 <b><font color="blue">꽃잎의 길이와 너비</font></b>, 그리고 <b><font color="blue">꽃받침의 길이와 너비</font></b>에 대한 센티미터(cm) 단위의 측정치와 
            해당 샘플의 품종이 레이블 형태로 존재한다. 붓꽃 데이터 세트는 통계적 분류 문제의 대표적인 테스트 데이터로 쓰이고 있다.<br>
            <출처: 두산백과>
        </p>
        """, unsafe_allow_html=True)
    st.image("https://miro.medium.com/max/3500/1*f6KbPXwksAliMIsibFyGJw.png")
    st.image("https://content.codecademy.com/programs/machine-learning/k-means/iris.svg")
    st.caption("출처:https://www.kaggle.com/code/sunaysawant/iris-eda-k-means-clustering/")

    st.subheader("2. 붓꽃 데이터 세트의 구성")
    st.markdown("""
        <p style = "text-align:center;">
        <b><붓꽃 데이터 세트의 일부></b>
        </p>
    """, unsafe_allow_html=True)

    st.image("images/iris_table.jpg")
    st.write("① sepal length: 꽃받침 길이")
    st.write("② sepal width: 꽃받침 너비")
    st.write("③ petal length: 꽃잎 길이")
    st.write("④ petal width: 꽃잎 너비")
    st.write("⑤ species: 품종")
    st.image("https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbeUgB8%2FbtrVkeWxNAE%2FwlewLtdh9dktLOKa4junIk%2Fimg.png")


with tab2 :
    st.subheader('1.붓꽃 데이터🌸(상위 5개 데이터)')
    st.table(df.head())


    # select_species 변수에 사용자가 선택한 값이 지정됩니다



    st.subheader('2.선택한 품종만 보여주기')
    st.markdown("""
    <p style = "background-color : #EAEAEA; height:40px;">
    <font color=blue>🌷아래 선택 박스에서 원하는 붓꽃 종류를 선택하면 선택한 품종의 데이터를 볼 수 있습니다.</font>
    </p>""", unsafe_allow_html=True)
    select_species = st.selectbox(
        '확인하고 싶은 종을 선택하세요',
        ['Iris-setosa','Iris-versicolor','Iris-virginica']
    )


    # 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
    tmp_df = df[df['iris']== select_species]
    # 선택한 종의 맨 처음 5행을 보여줍니다
    st.table(tmp_df)

with tab3 :
    # 여러개 선택할 수 있을 때는 multiselect를 이용하실 수 있습니다
    # return : list
    #st.title("붓꽃 데이터 필터링")

    st.subheader("1.품종 선택하기(복수 선택)")
    select_multi_species = st.multiselect(
        '확인하고자 하는 종을 선택해 주세요. 복수선택가능',
        ['Iris-setosa','Iris-versicolor','Iris-virginica']

    )

    # 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
    tmp_df = df[df['iris'].isin(select_multi_species)]
    # 선택한 종들의 결과표를 나타냅니다.
    st.table(tmp_df)
    # 라디오에 선택한 내용을 radio select변수에 담습니다
    st.write("")
    st.subheader("2.열의 종류 선택하기")

    radio_select =st.radio(
        "열의 종류를 선택하세요.",
        ['sepal length', 'sepal width', 'petal length','petal width'],
        horizontal=True
        )
    # 선택한 컬럼의 값의 범위를 지정할 수 있는 slider를 만듭니다.
    st.write("")
    st.subheader("3.열의 값 슬라이드로 조정하기")
    slider_range = st.slider(
        "열의 값의 범위를 설정하세요.",
         0.0, #시작 값
         10.0, #끝 값
        (2.5, 7.5) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능
    )

    # 필터 적용버튼 생성
    start_button = st.button(
        "필터링하기 📊 "#"버튼에 표시될 내용"
    )

    # button이 눌리는 경우 start_button의 값이 true로 바뀌게 된다.
    # 이를 이용해서 if문으로 버튼이 눌렸을 때를 구현
    if start_button:
        tmp_df = df[df['iris'].isin(select_multi_species)]
        #slider input으로 받은 값에 해당하는 값을 기준으로 데이터를 필터링합니다.
        tmp_df= tmp_df[ (tmp_df[radio_select] >= slider_range[0]) & (tmp_df[radio_select] <= slider_range[1])]
        st.table(tmp_df)
        # 성공문구 + 풍선이 날리는 특수효과
        st.success("Filter Applied!")
        st.balloons()

with tab4 :
    #st.subheader('붓꽃 데이터 시각화하기')
    st.subheader('1.세토사 품종의 sepal length 빈도수')
    tmp_df2 = df.loc[df['iris']=='Iris-setosa']
    st.table(tmp_df2.head())
    fig, ax = plt.subplots()
    ax.hist(x="sepal length",data=tmp_df2)
    st.pyplot(fig)

    st.subheader('2.버지컬러 품종의 sepal length 빈도수')
    tmp_df3 = df.loc[df['iris'] == 'Iris-versicolor']
    st.table(tmp_df3.head())
    fig, ax = plt.subplots()
    ax.hist(x="sepal length",data=tmp_df3)
    st.pyplot(fig)

    st.subheader('3.버지니카 품종의 sepal length 빈도수')
    tmp_df4 = df.loc[df['iris'] == 'Iris-virginica']
    st.table(tmp_df4.head())
    fig, ax = plt.subplots()
    ax.hist(x="sepal length", data=tmp_df4)
    st.pyplot(fig)

    st.subheader('4.세가지 품종의 sepal length의 차이')
    fig, ax = plt.subplots()
    ax.hist(x="sepal length", data=tmp_df2)
    ax.hist(x="sepal length", data=tmp_df3)
    ax.hist(x="sepal length", data=tmp_df4)
    st.pyplot(fig)

    st.markdown("""
            <p style = "background-color:#EAEAEA; color:red;">
            <br>
            <b><시각화 후 분석 결과></b><br>
            붓꽃 데이터 시각화를 통해 세 가지 품종에서 sepal length의 길이가 차이가 있음을 알 수 있다.<br>
            세토사 품종의 sepal length가 짧은 편이고, 버지니카 품종의 sepal length가 다른 품종보다 조금 더 긴 것으로 나타났다.<br>
            데이터 시각화를 통해 데이터에 대한 분석을 좀 더 쉽게 할 수 있음을 단적으로 보여준다.<br><br>
            </p>""", unsafe_allow_html=True)
