import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# 파일 로드
data_path = 'movies_2024.csv'
df = pd.read_csv(data_path)

# Streamlit 앱 구성
st.title('Movies Data Visualization')

# 데이터프레임 표시
st.header('Dataset Overview')
st.write(df)

# 데이터 요약
st.header('Data Summary')
st.write(df.describe())

# 컬럼 선택 기능 추가
graph_column = st.selectbox('Select a column to visualize', df.columns)

# 히스토그램 그리기
st.header(f'Histogram of {graph_column}')
fig, ax = plt.subplots()
df[graph_column].hist(ax=ax, bins=20, edgecolor='black')
ax.set_title(f'Histogram of {graph_column}')
ax.set_xlabel(graph_column)
ax.set_ylabel('Frequency')
st.pyplot(fig)

# # 상관관계 히트맵
# st.header('Correlation Heatmap')
# fig, ax = plt.subplots()
# corr_matrix = df.corr()
# cax = ax.matshow(corr_matrix, cmap='coolwarm')
# fig.colorbar(cax)
# ax.set_xticks(range(len(corr_matrix.columns)))
# ax.set_yticks(range(len(corr_matrix.columns)))
# ax.set_xticklabels(corr_matrix.columns, rotation=90)
# ax.set_yticklabels(corr_matrix.columns)
# st.pyplot(fig)

