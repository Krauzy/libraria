import streamlit as st
from annotated_text import annotated_text, annotation
from src.utils.constant import COLORS
from src.utils.translate import translate_disease


def __handle_disease(item: tuple) -> tuple:
    disease, disease_type = translate_disease(item[0])
    return (
        disease,
        disease_type,
        str(item[1] * 100)[:4] + '%'
    )


def __map_annotated(predictions: list) -> list:
    return list(map(__handle_disease, predictions))


def annotated_render(predictions: list) -> None:
    if (predictions is not None) and (len(predictions) > 0):
        iterator = __map_annotated(predictions)
        for item in iterator:
            st.text(' ')
            disease_name, disease_type, porc_acc = item
            annotated_text(
                annotation(
                    disease_name,
                    disease_type,
                    background=COLORS['RED'],
                    color=COLORS['BLACK']
                ),
                ' ',
                annotation(
                    porc_acc,
                    '',
                    background=COLORS['BLUE'],
                    color=COLORS['BLACK']
                )
            )
    else:
        annotated_text(annotation(
            'Nada foi encontrado',
            'Diagnóstico',
            background=COLORS['GREEN'],
            color=COLORS['BLACK']
        ))
