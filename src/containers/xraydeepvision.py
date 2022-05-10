import streamlit as st
from src.data.cnn import XRayDeepVision
from src.components.annotated_components import annotated_render


def render():
    with st.sidebar:
        st.title('⚙️ Settings')
        st.markdown('---')
        translate_state = st.radio('Translate Disease', ('PT-BR', 'EN-US'))
        st.markdown('---')
        error_state = st.slider('Select the error min-value', 0.00, 1.00, 0.70, 0.01)
        st.markdown('---')
        resize_state = st.checkbox('Resize image from best learning', True)

    st.title('💀 X-Ray Deep Vision')
    st.text('Disease reconginition in Torax X-Ray')
    st.text(' ')
    
    file_image = st.file_uploader(
        label='Upload X-Ray Image', 
        accept_multiple_files=False,
        type=['png', 'jpg', 'jpeg']
    )

    if file_image is not None:
        dinamic_container = st.empty()
        
        progress_bar = dinamic_container.progress(0)
        image_container, _, annotation_container = st.columns([1, 0.1, 1.5])

        with image_container:
            st.image(file_image, width=250)

        with annotation_container:
            progress_bar.progress(20)
            
            xray = XRayDeepVision(resize=resize_state, error=error_state)
            
            progress_bar.progress(40)
            
            xray.load_image(file_image)
            
            progress_bar.progress(60)
            
            _, dataset_filter = xray.run()

            progress_bar.progress(80)

            annotated_render(dataset_filter, translate_state)

            progress_bar.progress(100)
            dinamic_container.empty()
