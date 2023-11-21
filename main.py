import streamlit as st
from ppt_data_gen import slide_data_gen
from ppt_gen import ppt_gen

st.title("PPT Generator")

topic = st.text_input("Enter a topic:")

if st.button("Generate"):
    data = slide_data_gen(topic)
    ppt_file = ppt_gen(data)

    file_name = f"Presentation.pptx"

    st.download_button(
        label="Download Presentation",
        data=ppt_file,
        file_name=file_name,
        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
    )
