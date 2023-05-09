# Test

import streamlit as st
from openpyxl import load_workbook

st.button('upload file',key='upload',)

if st.session_state.upload:
    filename = 'files/2- Loss and Uncertainty_V2.0_N117 3.6MW.xlsm'
    workbook = load_workbook(filename=filename)
    'deu bom!'

    st.write(workbook['EYA']['E8'].value) 
