import streamlit as st
x=0 
def calculate():
    st.write(f"value of x is: {x}")
    
x = st.number_input(label="", min_value=0, max_value=None, value=None, step=1, key="key1", on_change=calculate)

if st.button("Calculate"):
        st.write(f"value of x is: {x}")
        #calculate()
