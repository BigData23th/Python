# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 나에게 가장 도움이 될 것 같은 유튜브
    ## 노마드 코더
    > 이유: 기본적으로 영어로 설명을 해줘서

    # 다른 학생들에게 가장 도움이 될 것 같은 유튜브
    ## 드림코딩
    > 이유: 프론트 웹개발을 공부 할 때 가장 도움이 되었던 유튜브채널
    """
)

# https://pixabay.com/ko
st.image(
    "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_960_720.jpg"
)