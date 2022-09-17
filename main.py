from ssl import Options
import streamlit as st
header = st.container()
dataset = st.container()
features = st.container()
model_Training = st.container()
with header :
    st.title('gohr attack model ')
with model_Training :
    sel_col, display_col = st.columns(2)

    apha = sel_col.slider("please provide the alpha value", min_value = 2, max_value = 11)
    beta = sel_col.slider("please provide the beta value", min_value = 2, max_value = 11)
    epochs = sel_col.text_input('no of epochs', 50)
    rounds = sel_col.slider("please provide number of round", min_value = 2, max_value = 7)