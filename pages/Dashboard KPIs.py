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

# total asylum applications
total_applications = df['Applied during year'].sum()

#total decisions
total_decisions = df['Total decisions'].sum()

#total recognized cases
total_recognized = df['decisions_recognized'].sum()

#recognition rate
recognition_rate = (total_recognized / total_decisions * 100)

#pending cases
latest_year = df['Year'].max()

pending_latest = (df[df['Year'] == latest_year]
                ['Total pending end-year'].sum())

#total rejected cases
total_rejected = df['Rejected'].sum()

#rejection_rate 
rejection_rate = total_rejected / total_decisions * 100

#decision_rate :
decision_rate = total_decisions / total_applications * 100


#KPIs
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

with col1:
    st.metric('Total Applications', total_applications)

with col2:
    st.metric('Total Decisions', total_decisions)

with col3:
    st.metric('Recognized Cases', total_recognized)

with col4:
    st.metric('Recognition Rate', recognition_rate)

with col5:
    st.metric(f'Pending Cases ({latest_year})', pending_latest)

with col6:
    st.metric('Rejected Cases', total_rejected)

with col7:
    st.metric('Rejection Rate', rejection_rate)
with col8:
    st.metric('Decision Rate', decision_rate)


#Show trend lines

application_o_time = df.groupby('Year')[['Applied during year', 'Total decisions', 'Total pending end-year']].sum().reset_index()
application_o_time

st.plotly_chart(px.line(data_frame= application_o_time, x= 'Year', y= ['Applied during year', 'Total decisions', 'Total pending end-year'],
       title= 'Applications_by_Year',
       line_shape= 'spline').update_traces(textposition= 'top center'))

# pie charts

highest_asylum_Hosting = (df.groupby('Country / territory of asylum/residence')['Applied during year']
                        .sum().sort_values(ascending=False).reset_index().head(10))
highest_asylum_Hosting

decision_outcomes = pd.DataFrame({'Outcome': ['Recognized', 'Rejected'],
                   'Count': [df['decisions_recognized'].sum(),
                    df['Rejected'].sum()]})

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(px.pie(data_frame= highest_asylum_Hosting, names= 'Country / territory of asylum/residence', 
       values= 'Applied during year',
       title= 'Highest_Country_Asylum',
       hole= 0.3))

with col2:
    st.plotly_chart(px.pie(decision_outcomes,
            names='Outcome', values='Count',
            hole=0.5, title='Asylum Decision Outcomes'))