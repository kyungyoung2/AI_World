import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("붓꽃 데이터 분석하기")
df = pd.read_csv("iris.csv")

tab1, tab2, tab3 = st.tabs(['붓꽃 데이터란?', '붓꽃 데이터 보기','붓꽃 데이터 필터링'])
with tab1 :
    st.subheader("붓꽃(Iris) 데이터란?")
    st.markdown('''
        안녕하세요.
        마크다운입니다.
        ''')

with tab2 :
    st.subheader('1.붓꽃 데이터(상위 5개 데이터)')
    st.table(df.head())

    # 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
    st.title('Iris Species🌸')

    # select_species 변수에 사용자가 선택한 값이 지정됩니다
    select_species = st.selectbox(
        '확인하고 싶은 종을 선택하세요',
        ['Iris-setosa','Iris-versicolor','Iris-virginica']
    )

    st.subheader('2.선택한 종류만 보여주기')
    st.write("🌷왼쪽 슬라이드바에서 원하는 붓꽃 종류를 선택하세요.")


    # 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
    tmp_df = df[df['iris']== select_species]
    # 선택한 종의 맨 처음 5행을 보여줍니다
    st.table(tmp_df.head(10))

with tab3 :
    # 여러개 선택할 수 있을 때는 multiselect를 이용하실 수 있습니다
    # return : list
    select_multi_species = st.multiselect(
        '확인하고자 하는 종을 선택해 주세요. 복수선택가능',
        ['Iris-setosa','Iris-versicolor','Iris-virginica']

    )

    # 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
    tmp_df = df[df['iris'].isin(select_multi_species)]
    # 선택한 종들의 결과표를 나타냅니다.
    st.table(tmp_df)
    # 라디오에 선택한 내용을 radio select변수에 담습니다
    radio_select =st.radio(
        "열의 종류를 선택하세요.?",
        ['sepal length', 'sepal width', 'petal length','petal width'],
        horizontal=True
        )
    # 선택한 컬럼의 값의 범위를 지정할 수 있는 slider를 만듭니다.
    slider_range = st.slider(
        "choose range of key column",
         0.0, #시작 값
         10.0, #끝 값
        (2.5, 7.5) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능
    )

    # 필터 적용버튼 생성
    start_button = st.button(
        "filter apply 📊 "#"버튼에 표시될 내용"
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