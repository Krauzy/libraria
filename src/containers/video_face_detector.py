import streamlit as st
from streamlit_terran_timeline import generate_timeline, terran_timeline


@st.cache(persist=True, ttl=86_400, suppress_st_warning=True, show_spinner=False)
def _generate_timeline(video_path):
    timeline = generate_timeline(
        video_src=video_path,
        appearence_threshold=5,
        batch_size=32,
        framerate=8,
        output_directory="timelines",
        ref_directory=None,
        similarity_threshold=0.75,
        start_time=0,
        thumbnail_rate=1,
    )

    return timeline


def render():
    st.title('🎥 Video Face Recognition')

    video_path = st.text_input(
        "Link or path to video",
        "https://www.youtube.com/watch?v=Go8nTmfrQd8"
    )

    with st.spinner("Generating timeline"):
        timeline = _generate_timeline(video_path)

    start_time = terran_timeline(timeline)

    st.video(video_path, start_time=int(start_time))
