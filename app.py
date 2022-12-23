import streamlit as st
import src.containers.xray_deep_vision as x_ray
import src.containers.video_face_detector as v_detector
import src.containers.text_sentiment_analysis as t_analysis
import pandas as pd

if __name__ == '__main__':

    st.set_page_config(
        page_title='Libraria',
        page_icon='🗃'
    )

    list_app = [
        '💀 X-Ray Deep Vision',
        '🎥 Video Face Recognition',
        '✨ Text Sentiment Analysis'
    ]

    selected_app = st.selectbox('Select AI Application', list_app)
    st.markdown('---')

    if selected_app == '💀 X-Ray Deep Vision':
        x_ray.render()
    elif selected_app == '🎥 Video Face Recognition':
        v_detector.render()
    elif selected_app == '✨ Text Sentiment Analysis':
        df = pd.read_csv('./src/assert/dataset/Tweets.csv')
        t_analysis.render(df)
