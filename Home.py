import pandas as pd
import streamlit as st

#Adjust Layout

st.set_page_config(page_title= 'Asylum EDA', layout= 'wide')

#Add Title

st.markdown("<h1 style='text-align: center; color: black;'>Asylum Seekers Project</h1>", unsafe_allow_html= True)

#Add Image
st.image("https://myattorneyusa.com/wp-content/uploads/2026/01/asylum-seekers.jpg")

#load dataframe

df = pd.read_csv('cleaned_df.csv')

# Column descriptions
column_descriptions = {
    "Year": "Year in which the asylum data was reported.",
    "Country / territory of asylum/residence": "Country or territory where the asylum seeker applied for asylum or resides.",
    "Origin": "Country or territory of origin of the asylum seeker.",
    "Applied during year": "Number of asylum applications submitted during the year.",
    "Total decisions": "Total number of asylum decisions made during the year.",
    "decisions_recognized": "Number of asylum decisions that resulted in recognition.",
    "Rejected": "Number of asylum applications that were rejected.",
    "Otherwise closed": "Number of asylum cases closed for reasons other than recognition or rejection.",
    "Total pending end-year": "Number of asylum cases still pending at the end of the year.",
    "of which UNHCR-assisted(start-year)": "Number of pending cases at the beginning of the year that were assisted by UNHCR.",
    "of which UNHCR-assisted(end-year)": "Number of pending cases at the end of the year that were assisted by UNHCR."
}

#Convert to DataFrame
description_df = pd.DataFrame({
    "Column": column_descriptions.keys(),
    "Description": column_descriptions.values()
})

st.subheader("Dataset Columns")
st.dataframe(description_df, use_container_width=True, hide_index=True) 


