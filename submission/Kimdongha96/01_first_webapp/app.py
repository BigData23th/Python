# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장 도움이 될 것 같은 유튜브
  ## 노마드 코더
  > 이유 : 무언가 전문적인 강의를 해주는 느낌인 것 같다.
  [https://i.ibb.co/cx9h9qY/1-9-2x-100.jpg]
  (https://www.youtube.com/@nomadcoders/videos)

  
  # 다른 학생들에게 가장 도움이 될 것 같은 유튜브
  ## 조코딩
  > 이유 : 구독자수와 조회수가 잘 나오고 이해하기 쉽게 설명을 해주는 느낌이다.
  (https://www.youtube.com/@jocoding)
  


  #참고사이트
  [icons8](https://icons8.com)
  [flaticon](https://flaticon.com)
  [pixabay](https://pixabay.com)
  """
)
