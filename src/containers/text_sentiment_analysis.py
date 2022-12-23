import streamlit as st
from src.data.nlp import TextSentimentAnalysis
from pandas import DataFrame


def _linespace():
    st.markdown('<br/>', True)


@st.cache
def _load_sentimental(data_frame: DataFrame):
    sentimental = TextSentimentAnalysis(data_frame)
    sentimental.train_model()
    return sentimental


def render(data_frame: DataFrame):
    sentimental = _load_sentimental(data_frame)
    st.title('✨ Text Sentiment Analysis')
    st.text('Sentiment recognitions text based on public tweets')

    template_text = ''

    _linespace()

    text = st.text_input('Input your message', template_text)

    _linespace()

    st.success('success')

    if (text is not None) & (text != ''):
        result = sentimental.is_positive_sentiment(text)

        if result:
            st.success('Happy')
        else:
            st.error('Angry')
