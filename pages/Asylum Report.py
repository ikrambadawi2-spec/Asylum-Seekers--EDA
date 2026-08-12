import pandas as pd
import streamlit as st
import plotly.express as px

#Adjust Layout

st.set_page_config(page_title= 'Asylum EDA', layout= 'wide')

#Add Title

st.markdown("<h1 style='text-align: center; color: black;'>Marketing Report</h1>", unsafe_allow_html= True)

#Add Image
st.image("https://myattorneyusa.com/wp-content/uploads/2026/01/asylum-seekers.jpg")

# load data
df = pd.read_csv('cleaned_df.csv')

# Add Year Option:
years = st.sidebar.multiselect(
    'Select Year',
    sorted(df['Year'].unique()),
    default=sorted(df['Year'].unique()))

# Add Country of Origin Option:
origins = st.sidebar.multiselect('Country of Origin',
          df['Origin'].unique())

# Add Asylum Country Option:
asylum_countries = st.sidebar.multiselect('asylum_countries',
    df['Country / territory of asylum/residence'].unique())

filtered_df = df[
    (df['Year'].isin(years)) &
    (df['Origin'].isin(origins)) &
    (df['Country / territory of asylum/residence'].isin(asylum_countries))]

#Top Countries of Origin

top_origin = (df.groupby('Origin')['Applied during year']
        .sum().sort_values(ascending=False)
        .head(10).reset_index())
st.plotly_chart(px.bar(data_frame=top_origin, x='Origin',
       y='Applied during year',
    title='Top 10 Countries of Origin'))

df_procedure = df.groupby('RSD procedure type / level')['Total decisions'].sum().reset_index().sort_values('Total decisions', ascending= False)

st.plotly_chart(px.bar(data_frame= df_procedure, x= 'RSD procedure type / level',
       y= 'Total decisions', text_auto = True,
       title= 'RSD Procedure Type VS Total Decisions'))

highest_asylum_Hosting = (df.groupby('Country / territory of asylum/residence')['Applied during year']
                        .sum().sort_values(ascending=False).reset_index().head(10))

st.plotly_chart(px.pie(data_frame= highest_asylum_Hosting, names= 'Country / territory of asylum/residence', 
       values= 'Applied during year',
       title= 'Top Asylum-Hosting Countries',
       hole= 0.3))
