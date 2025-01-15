import streamlit as st 
import math
from st_social_media_links import SocialMediaIcons

#import taipy.gui.builder as tbg
st.set_page_config(page_title="Area Calculator",
                   page_icon="images/icon.webp",
                )

st.title("Area Calculator - زمین کی پیمایش")
#st.write("By method of triangles.")
a = [0,0,0,0,0]
b = [0,0,0,0,0]
c = [0,0,0,0,0]
area = [0.0,0.0,0.0,0.0,0.0]

def triangleArea( x,  y,  z):
    #st.write(f"x,y, z: {x}, {y}, {z}")
    if(x==None or y==None or z==None or x==0 or y==0 or z==0):
      return 0.0
    else:
        s=(x+y+z)/2
        area=math.sqrt(s*(s-x)*(s-y)*(s-z))
        return area
tab_home, tab_about = st.tabs(
        ["Home",
        "About"
        ])

with tab_home: 
    col1, col2, col3 = st.columns(3)

    def calculate():
        totalArea =0.0
        try:
            for i in range(5):
                if(a[i]!=0 and a[i]!=None and b[i]!=None and c[i]!=None and b[i]!=0 and c[i]!=0):
                    #st.subheader(f"{i}")
                    #st.write(f"{i}: {a[i]:.0f} {b[i]:.0f} {c[i]:.0f}")
                    area[i] = triangleArea(a[i], b[i], c[i])
                    totalArea += area[i]
            st.session_state['area'] = totalArea
        except Exception:
            st.subheader("Data Provided is not correct!")
            st.subheader("دیا گیا ڈیٹا غلط")
    for i in range(5):
        with col1:
            a[i] = st.number_input(label="", placeholder=f"Side A", min_value=0.0, value=None, step=0.1, key=f"A{i}")
        with col2:
            b[i] = st.number_input(label="", placeholder=f"Side B", min_value=0.0, value=None, step=0.1, key=f"B{i}")
        with col3:
            c[i] = st.number_input(label="", placeholder=f"Side C",  min_value=0.0, value=None, step=0.1, key=f"C{i}")

    def display():
        #c1, c2 = st.columns(2)
        if 'area' in st.session_state:
            with col2:
                st.subheader(f"فٹ {st.session_state['area']:.2f} ")
            with col3:
                marla = st.session_state['area'] / 272.25
                st.header(f":blue[مرلہ {marla:.2f}] ")

    with col1:
        #st.write("###")
        if st.button("Calculate"):
            calculate()
            display()


with tab_about:
    st.subheader("Developed By Haider Ali")
    st.write("A Python Developer")
    social_media_links = [
        "https://www.linkedin.com/in/haiderkhalil",
        "https://www.medium.com/@haiderkhalil",
        "https://www.x.com/haiderhalil",
        "https://www.facebook.com/haideralikhalil",
        "https://www.youtube.com/@towncoder",
        "https://www.github.com/haideralikhalil",
        "https://wa.me/00923219032716"
    ]
    social_media_icons = SocialMediaIcons(social_media_links)

    social_media_icons.render()  
    st.divider()
    st.video("https://youtu.be/ZlLtP16jIM4") 
    #st.image("haider.png")        

