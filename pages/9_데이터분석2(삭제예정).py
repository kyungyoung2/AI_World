import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from streamlit_drawable_canvas import st_canvas

'''
st.title("데이터분석")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2, tab3= st.tabs(['성적분석  ', '삼성전자 주식 조회  ', 'MNIST'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write("")
    st.write('## 점수 데이터 3명의 학생의 국어, 영어, 수학 점수를 시각화하여 나타냅니다.')
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



with tab3:
    # tab B를 누르면 표시될 내용
    st.write('비지도 학습')


    @st.cache(allow_output_mutation=True)
    def load():
        return load_model('model.h5')


    model = load()

    st.write('# MNIST Recognizer')

    CANVAS_SIZE = 192

    col1, col2 = st.columns(2)

    with col1:
        canvas = st_canvas(
            fill_color='#000000',
            stroke_width=20,
            stroke_color='#FFFFFF',
            background_color='#000000',
            width=CANVAS_SIZE,
            height=CANVAS_SIZE,
            drawing_mode='freedraw',
            key='canvas'
        )

    if canvas.image_data is not None:
        img = canvas.image_data.astype(np.uint8)
        img = cv2.resize(img, dsize=(28, 28))
        preview_img = cv2.resize(img, dsize=(CANVAS_SIZE, CANVAS_SIZE), interpolation=cv2.INTER_NEAREST)

        col2.image(preview_img)

        x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        x = x.reshape((-1, 28, 28, 1))
        y = model.predict(x).squeeze()

        st.write('## Result: %d' % np.argmax(y))
        st.bar_chart(y)

'''

st.write("붓꽃 데이터 시각화")
import plotly.express as px

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)
fig.show()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
