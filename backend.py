import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import plotly.express as px
import uuid
import re

# def analyze_age_variation_relation(df, age_column, variation_column):
#     st.subheader('Relation between User Age and User Variation')
    
#     # Scatter plot with regression line
#     fig, ax = plt.subplots()
#     sns.regplot(x=df[age_column], y=df[variation_column], ax=ax)
#     st.pyplot(fig)
    
# Function to plot age vs variation
def analyze_age_variation_relation(data):

    # Calculate the mean of client_age for each Variation
    mean_age_per_variation = data.groupby('Variation')['client_age'].mean().reset_index()

    fig_age_variation = px.bar(mean_age_per_variation, x= 'client_age', y= 'Variation', title="User age Distribution in different Variation" , color='Variation')
    
    # Add x and y labels
    fig_age_variation.update_xaxes(title_text='Client Age')
    fig_age_variation.update_yaxes(title_text='Variation')

    return fig_age_variation


# Function to plot gender vs variation
def analyze_gender_variation_relation(data):

    # Count the number of each gender for each variation
    gender_counts = data.groupby(['Variation', 'gender']).size().reset_index(name='count')

    # Create the bar chart
    fig_gender_counts = px.bar(gender_counts, x='Variation', y='count', color='gender', barmode='group',
                            title="Number of Each Gender for Each Variation")

    # Add x and y labels
    fig_gender_counts.update_xaxes(title_text='Variation')
    fig_gender_counts.update_yaxes(title_text='Count')

    return fig_gender_counts


# Function to plot date
def date_plot(data):
    # Count the number of each gender for each variation
    user_counts = data.groupby(['Variation', 'date_time']).size().reset_index(name='user_count')

    # Create the line chart
    fig_user_count = px.histogram(user_counts, x='date_time', y='user_count', color='Variation', title="User Count Over Time")

    # Add x and y labels
    fig_user_count.update_xaxes(title_text='date_time')
    fig_user_count.update_yaxes(title_text='User Count')

    return fig_user_count

def create_st_button(link_text, link_url, hover_color="#e78ac3", st_col=None):

    button_uuid = str(uuid.uuid4()).replace("-", "")
    button_id = re.sub("\d+", "", button_uuid)

    button_css = f"""
        <style>
            #{button_id} {{
                background-color: rgb(255, 255, 255);
                color: rgb(38, 39, 48);
                padding: 0.25em 0.38em;
                position: relative;
                text-decoration: none;
                border-radius: 4px;
                border-width: 1px;
                border-style: solid;
                border-color: rgb(230, 234, 241);
                border-image: initial;

            }}
            #{button_id}:hover {{
                border-color: {hover_color};
                color: {hover_color};
            }}
            #{button_id}:active {{
                box-shadow: none;
                background-color: {hover_color};
                color: white;
                }}
        </style> """

    html_str = f'<a href="{link_url}" target="_blank" id="{button_id}";>{link_text}</a><br></br>'

    if st_col is None:
        st.markdown(button_css + html_str, unsafe_allow_html=True)
    else:
        st_col.markdown(button_css + html_str, unsafe_allow_html=True)
