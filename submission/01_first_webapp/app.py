# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
# 가장 간단한 웹 사이트를 만드는 방법


# """ """ 여러 줄을 묶어서 표시할 수 있는 문자열
# ''' ''' (동일 기능)

st.balloons()

st.write(
    """
    ## 코딩 유튜브 채널 추천❗  
    ---
    """
)

st.sidebar.title('여러분의 추천 채널을 소개해 주세요! 👇')



col1,col2 = st.columns([1,1])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성

with col1 :
  # column 1 에 담을 내용
  st.write(
    """
    ##### 나에게 가장 도움이 될 것 같은 유튜브
    """)

  st.image("https://user-images.githubusercontent.com/71927533/221648720-65ccad13-0cc6-48cf-bf07-52411a9a515c.jpg")
  st.info('추천 이유 : 신기하고 재밌는 인공지능을 쉽게, 짧게 설명해주는 유튜브 입니다!', icon="ℹ️")

with col2 :
  # column 2 에 담을 내용
  st.write(
    """
    ##### 남이 보면 좋을 것 같은 유튜브
    """)
  st.image("https://user-images.githubusercontent.com/71927533/221631810-b72fa62f-2c41-4a86-a105-2f4a0c1e1b2c.jpg")
  st.info('추천 이유 : IT 트렌드 흐름을 알기 쉽고 빠르게 설명해주고, 간단 명료합니다!', icon="ℹ️")


  values = st.slider('추천 채널이 마음에 드셨다면 만족도를 평가해 주세요!', 1, 5, (2, 3, 4))
  st.write('Values:', values)

st.text_input()