import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title("Sales Dashboard")
st.write("Interactive dashboard for sales data")

df=pd.read_csv('SampleSuperstore.csv')

with st.sidebar:

    st.write("PICE Project Assignment")
    st.write("Student Name: Aung Aung (Batch-3)")
    st.write("Parami University")

    city_names=['All']+df.City.unique().tolist()
    selected_city_name=st.selectbox("Select city",options=city_names)
    
    states_names=['All']+df.State.unique().tolist()
    selected_state_name=st.selectbox("Select state",options=states_names)

    region_names=['All']+df.Region.unique().tolist()
    selected_region_name=st.selectbox("Select region",options=region_names)

    category_names=['All']+df.Category.unique().tolist()
    selected_category_name=st.selectbox("Select category",options=category_names)


col1,col2,col3=st.columns(3)
total_sales=df.Sales.sum()
total_quan=df.Quantity.sum()
total_prof=df.Profit.sum()
col1.metric("Total Sales : $",np.round(total_sales,2))
col2.metric("Total Qunatity : ",total_quan)
col3.metric("Total Profit gained : $",np.round(total_prof,2))


if selected_city_name != 'All':
    df = df[df['City']==selected_city_name]
if selected_state_name != 'All':
    df = df[df['State']==selected_state_name]
if selected_region_name != 'All':
    df = df[df['Region']==selected_region_name]
if selected_category_name != 'All':
    df = df[df['Category']==selected_category_name]


#--------------Sales Data------------------
st.header("Sales & Profit Data  by Segment")
col1,col2 = st.columns(2)

data=df.groupby('Segment')['Sales'].sum().reset_index().sort_values(by='Sales',ascending=False)
fig1 = px.pie(data, values='Sales', names='Segment', title='Sales per Segment')
col1.plotly_chart(fig1,width='content')

data=df.groupby('Segment')['Profit'].sum().reset_index().sort_values(by='Profit',ascending=False)
fig2 = px.bar(data, x='Segment', y='Profit', title='Sales per Profit')
col2.plotly_chart(fig2,width='stretch')


#---------------------------------
st.header("Sales Data per region & Category")
col1,col2,col3 = st.columns(3)
data=df.groupby(['Region','Category'])['Sales'].sum().reset_index().sort_values(by='Region',ascending=False)
fig3 = px.bar(data, x="Region", y="Sales", color="Category")
col1.plotly_chart(fig3,width='stretch')

fig4 = px.bar(data, x="Region", y="Sales", color="Category", barmode='group')
col2.plotly_chart(fig4,width='stretch')

fig5=px.scatter(df,x='Sales',y='Discount')
col3.plotly_chart(fig5,width='stretch')

#-----------Table Data-------------
with st.expander("View Sales Data"):
    st.dataframe(df)


st.text("This is the conculsion of Sales EDA process. ....).")
