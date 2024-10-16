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

import streamlit as st
import pandas as pd
import random

# 제목 설정
st.title("서울 지역 랜덤 데이터 지도")
# 사용자 입력
points_count = st.slider("지도에 표시할 점의 개수", min_value=10, max_value=1000, value=100, step=10)
# 데이터 생성 함수
def create_random_data(count):
    data = []
    for _ in range(count):
    # 서울의 대략적인 위도 경도 범위
        latitude = random.uniform(37.42, 37.70) # 서울 위도 범위
        longitude = random.uniform(126.76, 127.18) # 서울 경도 범위
        size = random.uniform(0, 1000) # 점의 크기
        color = []
    for _ in range(4):
        color.append(random.random())
        data.append([latitude, longitude, size, color])
    return data
# 데이터프레임 생성
df = pd.DataFrame(
    create_random_data(points_count),
    columns=["위도", "경도", "크기", "색상"]
)
# 지도 표시
st.map(df, latitude="위도", longitude="경도", size="크기", color="색상")
# 데이터 표시 (선택사항)
if st.checkbox("생성된 데이터 보기"):
    st.write(df)
# 서울 주요 지역 정보
seoul_landmarks = {
 "서울시청": (37.5665, 126.9780),
 "강남역": (37.4980, 127.0276),
 "명동": (37.5635, 126.9850),
 "여의도": (37.5216, 126.9242),
 "북한산": (37.6619, 126.9950)
}
# 주요 지역 선택 옵션
selected_landmark = st.selectbox("주요 지역 선택", ["없음"] + list(seoul_landmarks.keys()))
if selected_landmark != "없음":
    lat, lon = seoul_landmarks[selected_landmark]
    st.write(f"{selected_landmark}의 위치: 위도 {lat}, 경도 {lon}")
 
 # 선택된 지역을 지도에 표시
    df_landmark = pd.DataFrame({"latitude": [lat], "longitude": [lon]})
    st.map(df_landmark)