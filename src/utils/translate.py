import streamlit as st


@st.cache
def translate_disease(disease):
    if disease == 'Atelectasis':
        return ('Atelectasia', 'Pulmão')
    elif disease == 'Consolidation':
        return ('Consolidação', 'Pulmão')
    elif disease == 'Infiltration':
        return ('Infiltração', 'Pulmão')
    elif disease == 'Pneumothorax':
        return ('Pneumotórax', 'Pulmão')
    elif disease == 'Edema':
        return ('Edema', 'Generalizado')
    elif disease == 'Emphysema':
        return ('Enfisema', 'Pulmão')
    elif disease == 'Fibrosis':
        return ('Fibrose', 'Pulmão')
    elif disease == 'Effusion':
        return ('Efusão', 'Cardiovascular')
    elif disease == 'Pneumonia':
        return ('Pneumonia', 'Pulmão')
    elif disease == 'Pleural_Thickening':
        return ('Espessamento Pleural', 'Vísceras')
    elif disease == 'Cardiomegaly':
        return ('Cardiomegalia', 'Cardiovascular')
    elif disease == 'Nodule':
        return ('Nódulo', 'Tecido')
    elif disease == 'Mass':
        return ('Tumor', 'Câncer')
    elif disease == 'Hernia':
        return ('Hérnia', 'Tecido')
    elif disease == 'Lung Lesion':
        return ('Lesão Pulmonar', 'Pulmão')
    elif disease == 'Fracture':
        return ('Fratura', 'Generalizada')
    elif disease == 'Lung Opacity':
        return ('Opacidade Pulmonar', 'Pulmão')
    elif disease == 'Enlarged Cardiomediastinum':
        return ('Expansão do Cardiomediastino', 'Cardiovascular')
