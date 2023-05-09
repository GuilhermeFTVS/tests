# Test

import streamlit as st
from openpyxl import load_workbook

st.button('upload file',key='upload',)

if st.session_state.upload:
    filename = '1- Loss and Uncertainty_V2.0_V117 4.3MW.xlsm'
    workbook = load_workbook(filename=filename)
    'deu bom!'

    st.write(workbook['PastePark']['D6'].value) 