import pandas as pd
import streamlit as st
import plotly.express as px

#Adjust Layout

st.set_page_config(page_title= 'Asylum EDA', layout= 'wide')

#Add Title

st.markdown("<h1 style='text-align: center; color: black;'>Dashboard KPIs</h1>", unsafe_allow_html= True)

#Add Image
st.image("https://myattorneyusa.com/wp-content/uploads/2026/01/asylum-seekers.jpg")

# load data
df = pd.read_csv('cleaned_df.csv')
tab1, tab2 = st.tabs(['Numerical', 'Categorical'])

with tab1:
    st.header('Numerical Univariate')

    num_cols = df.select_dtypes(include='number').columns

    col = st.selectbox('column', num_cols)

    st.plotly_chart(px.histogram(data_frame = df, x= col))

with tab2:
    st.header('Categorical Univariate')

    cat_cols = df.select_dtypes(include='object').columns

    col = st.selectbox('column', cat_cols)

    chart = st.radio('Chart', ['Bar Chart', 'Pie Chart'])

    if chart == 'Bar Chart':
        st.plotly_chart(px.histogram(data_frame = df, x= col, text_auto = True).update_xaxes(categoryorder = 'max descending'))

    elif chart == 'Pie Chart':
        st.plotly_chart(px.pie(data_frame = df, names= col, hole= 0.5))
