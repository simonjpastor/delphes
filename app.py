import streamlit as st
from delphes.real_data import Delphes

st.markdown("""
    # POLITICAL PREDICTOR
    Political Predictor is an application that predicts the European group corresponding to a given ideology based on the twitter account of 473 deputies.
""")
st.markdown("""
    ## **DATA**
    - Political group
    - National Party
    - Country
    - Age
    - Gender(0: man, 1: woman)
    - tweets
""")


otpion = st.slider('nb of lines', 1, 10)
df = Delphes().get_data()
filt_df = df.head(otpion)
st.write(filt_df)

st.markdown("""
    ## **MODELS**
""")


