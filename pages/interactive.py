import streamlit as st

st.title("상호작용 위한 앱 만들기")
st.link_button("포탈바로가기",'http://www.google.com')
st.image("https://cdn.imweb.me/thumbnail/20180109/5a5407d2d1e64.gif",width=300)

col1, col2 = st.columns(2)
with col1:
    st.image("https://cdn.imweb.me/thumbnail/20180109/5a5407d2d1e64.gif",width=300)
with col2:
    st.info("이 캐릭터의 이름은?")
    answer =st.text_input("캐릭터이름을 써주세요")
    #if answer == "피치" :
        # st.success("맞았습니다.")
    #else:
    #    st.warning("다시 생각해보세요")

# st.camera_input("사진을 찍어주세요")
st.latex("2x-1")

tab1, tab2 = st.tabs(['방학','개학'])
tab1.success("평안함")
tab2.warning("피곤함")

