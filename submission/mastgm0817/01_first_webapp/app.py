# streamlit 라이브러리 호출
import streamlit as st


# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(

    """
    ![title](img/man.png){: width="100%" height="100%"}

    ## 나에게 가장 도움이 될 것 같은 유튜브
    > ### _노마드 코더_

    [![이미지](https://i.ytimg.com/vi/x_Yw2f161CU/hqdefault.jpg)](https://www.youtube.com/@nomadcoders)

    ```
    이유: 최신 IT트렌드와 이슈 등을 영어와 설명을 해주고 한글 자막까지 제공해줘서
    ```

    ---

    ## 다른 학생들에게 도움이 될 것 같은 유튜브
    > ### _드림코딩_

    [![이미지](https://i.ytimg.com/vi/TTLHd3IyErM/hqdefault.jpg)](https://www.youtube.com/@dream-coding)

    ```
    이유: 프론트 웹 개발을 기초 공부 할 때 가장 도움이 되었던 유튜브채널  
    ```
    

    ---

    ##### 참고 사이트
    - [icons8](https://icons8.com/)
    - [flaticon](https://www.flaticon.com/)
    - [pixabay](https://pixabay.com/ko/)
    - [MarshallK](https://marshallku.com/)

    """
)

