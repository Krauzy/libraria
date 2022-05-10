import streamlit as st
import src.containers.xraydeepvision as xraydeepvision


if __name__ == '__main__':
    st.selectbox('Select AI Application', ['💀 X-Ray Deep Vision'])
    xraydeepvision.render()