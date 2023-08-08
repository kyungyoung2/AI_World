import cv2
from tensorflow.keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np

st.write('# 😊 MNIST Recognizer')
st.markdown("""
    <p style = "background-color:#EAEAEA;">
    MNIST(Modified National Institute of Standards and Technology)는 손으로 쓴 숫자 데이터 셋으로, 60,000개의 학습 데이터와 10,000개의 테스트 데이터로 되어 있으며, 딥러닝 데이터 셋으로 사용됩니다.
    아래 "MNIST Recognizer"는 여러분이 쓴 손글씨를 인식하는 인공지능 모델입니다.<br>
    왼쪽 칸에 0~9까지의 숫자 중 하나를 그려 보세요. <br>
    여러분이 쓴 숫자를 인식한 후 오른쪽 칸에 예측한 결과를 보여줍니다.<br>
    잘 맞히는지 여러분도 테스트해 보세요!!!
    </p>
    """, unsafe_allow_html=True)

st.spinner("Loading...")
@st.cache(allow_output_mutation=True)
def load():
    return load_model('model.h5')
model = load()



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