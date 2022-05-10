import streamlit as st
from annotated_text import annotated_text
from src.utils.constant import COLORS
from src.utils.translate import translate_disease


def __handle_disease(item: tuple) -> tuple:
    disease, type = translate_disease(item[0])
    return (
        disease,
        type,
        COLORS['RED'],
        str(item[1] * 100)[:4] + '%'
    )

def __map_annotated(predictions: tuple) -> list:
    return list(map(__handle_disease, predictions))

def annotated_render(predictions: list, translated=True) -> None:
    if (predictions is not None) and (len(predictions) > 0):
        iterator = __map_annotated(predictions) if translated else predictions
        for item in iterator:
            st.text(' ')
            annotated_text(item[:-1], ' ', (item[-1], '', COLORS['BLUE']))
    else:
        annotated_text(
            (
                'Nada foi encontrado', 
                'Diagnóstico', 
                COLORS['GREEN']) if translated else (
                    'No disease found', 
                    'diagnostic', 
                    COLORS['GREEN']
                )
        )
