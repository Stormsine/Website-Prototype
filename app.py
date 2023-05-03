from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
# more emojis here : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon="tada:", layout= "wide")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#load assets
lottie_Coding = "https://iconscout.com/lotties/smart-building"
img_contact_form = Image.open("images/")
img_lottie_animation = Image.open("images/")
#header section
with st.container():
    st.subheader("Hello my name is Jacqueline Lara :wave: ")
    st.title("I am a architect from Philadelphia")
    st.write("I am passionate about making buildings and adding my own twist to the design.")
    st.write("[Learn More >](link)")

    #what i do
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
st.write("##")
st.write(0)
st.write("[Renderings >](Link for rendering)")
with right_column: 
    st_lottie(lottie_Coding, height=300, key="coding" )

# projects
with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
            st.image(img)
    with text_column:
             st.subheader("-----")
    st.write(
            "-----------"
        )
    st.markdown("[could be a video here](link)")
