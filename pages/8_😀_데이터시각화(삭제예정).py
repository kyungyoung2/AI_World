import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
data = pd.read_csv('bike.csv')

st.title('데이터 시각화(공공데이터 활용)')

st.write("인공지능에서 데이터를 분석하고 시각화하는 것은 매우 중요합니다.")

# 탭 생성
tab_titles = ['Bar Chart', 'Scatter Plot', 'Heatmap']
tabs = st.tabs(tab_titles)

# 각 탭에 콘텐츠 추가
with tabs[0]:
    st.header('Bar Chart')
    st.bar_chart(data)

with tabs[1]:
    st.header('Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(data['x'], data['y'])
    st.pyplot(fig)

with tabs[2]:
    st.header('Heatmap')
    st.heatmap(data.corr())