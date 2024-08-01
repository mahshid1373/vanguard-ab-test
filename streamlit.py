import pandas as pd
import streamlit as st
import pandas as pd
from backend import *
from datetime import datetime

#############################################################################################################################
######################################################## CSS ################################################################
#############################################################################################################################

# Apply custom theme
st.set_page_config(
    page_title="Vanguard A/B Test",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)



# # Custom CSS to inject
# custom_css = """
# <style>
#     body {
#         color: black;
#         background-color: white;
#     }
#     .stApp {
#         background-color: white;
#     }
#     .sidebar .sidebar-content {
#         background-color: white;
#     }
#     .Widget>label {
#         color: black;
#     }
#     .stTextInput>div>div>input {
#         color: black;
#     }
#     .stSelectbox>div>div>select {
#         color: white;
#     }
#     .stMarkdown strong {
#     color: black !important;
#     }
#     .stMarkdown p {
#         color: black !important;
#     }
#     p, .stText {
#         color: white !important;
#     }
#     h1, h2, h3, h4, h5, h6 {
#         color: black !important;
#     }
#     .stRadio > label {
#         color: white !important;
#     }
#     .stCheckbox > label {
#         color: white !important;
#     }
#     .stSlider > label {
#         color: white !important;
#     }
#     /* Make sidebar title white */
#     [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1 {
#         color: white !important;
#     }
#     /* Ensure other sidebar text remains visible */
#     [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
#         color: white;
#     }
#     [data-testid="stSidebar"] .stRadio label {
#         color: white !important;
#     }
#     [data-testid="stSidebar"] .stCheckbox label {
#         color: white !important;
#     }
# </style>
# """

# # Inject custom CSS
# st.markdown(custom_css, unsafe_allow_html=True)


# Rest of your Streamlit app code follows...

#############################################################################################################################
################################################## Load Data ################################################################
#############################################################################################################################

# Load the datasets
df_pt1 = pd.read_csv('Data/cleaned_pt_1.csv')
df_pt2 = pd.read_csv('Data/cleaned_pt_2.csv')
df_demo_cleaned = pd.read_csv('Data/df_final_demo_cleaned.txt')
df_experiment_clients = pd.read_csv('Data/df_final_experiment_clients.txt')

pt_general = pd.concat([df_pt1, df_pt2], axis=1)
pt_general = pt_general.loc[:,~pt_general.columns.duplicated()]
df_kpi = pt_general.dropna()

df_kpi = pd.concat([df_pt1, df_pt2, df_experiment_clients], axis=1)
df_kpi = df_kpi.loc[:,~df_kpi.columns.duplicated()]
df_kpi = df_kpi.dropna()

user_info_variation = pd.merge(df_demo_cleaned, df_experiment_clients, on='client_id')
user_info_variation = user_info_variation.dropna()

# App title
st.title('Vanguard A/b Test')
st.markdown("### The Digital Challenge")
st.markdown("**Created by Mahshid Khatami and Faheem Khan**")
st.markdown("**The digital world is evolving, and so are Vanguard’s clients. Vanguard believed that a more intuitive and modern User Interface (UI), coupled with timely in-context prompts (cues, messages, hints, or instructions provided to users directly within the context of their current task or action), could make the online process smoother for clients. The critical question was: Would these changes encourage more clients to complete the process?**")

#############################################################################################################################
################################################## Filter ###################################################################
#############################################################################################################################

# Sidebar for navigation
st.sidebar.title('Filters')

################################################ Data Filter #######################################################

options = st.sidebar.radio('Select a dataset to explore:', ['User Log', 'Client Information', 'Experiment Clients'])

# Display the selected dataset
if options == 'User Log':
    st.header('User Log')
    st.write(pt_general.head())
    st.write(f"Shape of the dataset: {pt_general.shape}")

    # Add some basic visualizations
    st.subheader('Statistics')
    st.write(df_pt1.describe())


elif options == 'Client Information':
    st.header('Client Information')
    st.write(df_demo_cleaned.head())
    st.write(f"Shape of the dataset: {df_demo_cleaned.shape}")

    # Add some basic visualizations
    st.subheader('Statistics')
    st.write(df_demo_cleaned.describe())


elif options == 'Experiment Clients':
    st.header('Experiment Clients Data')
    st.write(df_experiment_clients.head())
    st.write(f"Shape of the dataset: {df_experiment_clients.shape}")

    # Add some basic visualizations
    st.subheader('Statistics')
    st.write(df_experiment_clients.describe())


################################################ Age Filter #######################################################


# Create a radio button for selecting age range
age_range = st.sidebar.slider(
    'Select Age Range', min_value=int(user_info_variation['client_age'].min()), 
    max_value=int(user_info_variation['client_age'].max()), 
    value=(int(user_info_variation['client_age'].min()), 
           int(user_info_variation['client_age'].max()))
)


################################################ Gender Filter #######################################################
# Create a radio button for selecting Gender
age_range = st.sidebar.radio(
    "Select Gender",
    ('All', 'Female', 'Male', 'Undefined')
)

# Filter data based on selected age range
if age_range == 'Female':
    user_info_variation = user_info_variation[user_info_variation['gender'] == 'F']
elif age_range == 'Male':
    user_info_variation = user_info_variation[user_info_variation['gender'] == 'M']
elif age_range == 'Undefined':
    user_info_variation = user_info_variation[user_info_variation['gender'] == 'U']   
else:
    user_info_variation = user_info_variation



################################################ Date Filter #######################################################

# Ensure date_time is in datetime format
pt_general['date_time'] = pd.to_datetime(pt_general['date_time'])
df_kpi['date_time'] = pd.to_datetime(df_kpi['date_time'])

# Date filter
start_date = st.sidebar.date_input('Start date', value=pt_general['date_time'].min())
end_date = st.sidebar.date_input('End date', value=pt_general['date_time'].max())

# Filter data based on the selected date range
pt_general = pt_general[(pt_general['date_time'] >= pd.to_datetime(start_date)) & (pt_general['date_time'] <= pd.to_datetime(end_date))]
df_kpi = df_kpi[(df_kpi['date_time'] >= pd.to_datetime(start_date)) & (df_kpi['date_time'] <= pd.to_datetime(end_date))]


################################################ Related link #######################################################

database_link_dict = {
    "Ironhack": "https://www.ironhack.com/de",
    "GitHub Page for Mahshid Khatami": "https://github.com/mahshid1373",
    "GitHub Page for Faheem Khan": "https://github.com/fjkhan86",
}

st.sidebar.markdown("## Contributors Related Links")
for link_text, link_url in database_link_dict.items():
    create_st_button(link_text, link_url, st_col=st.sidebar)

#############################################################################################################################
################################################## Plot #####################################################################
#############################################################################################################################

# Plot age vs. Variation
st.title("User age Distribution in different Variation")
fig_age_variation = analyze_age_variation_relation(user_info_variation)
st.plotly_chart(fig_age_variation)


# Plot Gender vs. Variation
st.title("User gender Distribution in different Variation")
fig_gender_variation = analyze_gender_variation_relation(user_info_variation)
st.plotly_chart(fig_gender_variation)


# Plot User count number in different Time 
st.title("User Distribution Over Time")
fig_date = date_plot(df_kpi)
st.plotly_chart(fig_date)