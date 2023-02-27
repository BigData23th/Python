# streamlit 라이브러리 호출
import streamlit as st
from PIL import Image

def main() :
    
    video_file = open('video/mv1.mp4', 'rb')
    st.video(video_file)

if __name__ == "__main__" :
    main()

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(

    """

    ## 나에게 가장 도움이 될 것 같은 유튜브
    > ### _노마드 코더_ :smile:

    [![이미지](https://i.ytimg.com/vi/x_Yw2f161CU/hqdefault.jpg)](https://www.youtube.com/@nomadcoders)

    ```
    이유: 최신 IT트렌드와 이슈 등을 영어와 설명을 해주고 한글 자막까지 제공해줘서
    ```

    ~~영어 듣기 실력이 증가~~

    ---

    ## 다른 학생들에게 도움이 될 것 같은 유튜브
    > ### _드림코딩_ :+1:

    [![이미지](https://i.ytimg.com/vi/TTLHd3IyErM/hqdefault.jpg)](https://www.youtube.com/@dream-coding)

    ```
    이유: 프론트 웹 개발을 기초 공부 할 때 가장 도움이 되었던 유튜브채널
    ```
    

    ---

    ##### 참고 사이트 :point_down:
    - [icons8](https://icons8.com/)
    - [flaticon](https://www.flaticon.com/)
    - [pixabay](https://pixabay.com/ko/)
    - [MarshallK](https://marshallku.com/)
    - [Emoji](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#emotion)
    - [깃허브 마크다운](https://docs.github.com/ko/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

    """
)

   