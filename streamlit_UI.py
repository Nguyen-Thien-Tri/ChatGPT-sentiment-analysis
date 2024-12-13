import time  # to simulate a real time data, time loop
import os
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

def get_diff_method(df1, df2):
  df_temp = pd.concat([df1,df2]).drop_duplicates(keep=False)
  return pd.concat([df1,df_temp], ignore_index=True)

def get_diff_length(df1,df2):
  num1 = df1.shape[0]
  num2 = df2.shape[0]
  extra = num2 - num1
  df_temp = df2.tail(extra)
  return pd.concat([df1, df_temp], ignore_index=True)

prev_mtime = os.stat('toxic_comment.csv').st_mtime
wait_time = 3

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
dataset_url = 'toxic_comment.csv'

# read csv from a URL
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()
df = df[['label','text']]

# dashboard title
st.title("Sentiment Analyst Demo")

# creating a single-element container
placeholder = st.empty()

loop_count = 0
while True:
    now_mtime = os.stat('toxic_comment.csv').st_mtime
    if loop_count == 0: 
        with placeholder.container():
            df1 = pd.read_csv(dataset_url)
            df_old = df.copy()
            df = get_diff_length(df,df1)
            # create three columns
            total, positive, negative = st.columns(3)

            # fill in those three columns with respective metrics or KPIs
            total.metric(
                label="Total",
                value= df['label'].count(),
                delta = df.shape[0] - df_old.shape[0]
            )

            positive.metric(
                label="Positive",
                value= df[df['label'] == 0]['label'].count(),
                delta = int(df[df['label'] == 0]['label'].count() - df_old[df_old['label'] == 0]['label'].count())
            )

            negative.metric(
                label="Negative",
                value=df[df['label'] == 1]['label'].count(),
                delta = int(df1[df1['label'] == 1]['label'].count() - df[df['label'] == 1]['label'].count())
            )

             # create two columns for charts
            fig_col1, fig_col2 = st.columns(2)
            with fig_col1:
                st.markdown("### Histogram Chart")
                fig1 = px.histogram(data_frame=df, x="label", height=400,width=600, text_auto=True, color='label')
                fig1.update_layout(bargap=0.2)
                st.write(fig1)
            with fig_col2:
                st.markdown("### Pie Chart")
                fig2 = px.pie(df, values=[i for i in df.groupby('label')['text'].count()], names=df['label'].unique(), height=400,width=600, color_discrete_sequence=px.colors.sequential.RdBu)
                st.write(fig2)

            # Dataframe
            # col1, col2, col3 = st.columns([1,3,1])
            # st.markdown("### Detailed Data View")
            # st.dataframe(df, 800,300)
            # loop_count += 1
            # time.sleep(5)

            # Dataframe
            st.markdown("### Detailed Data View")
            col1, col2, col3 = st.columns([1,3,1])
            with col1:
                st.write()
            with col2:
                st.dataframe(df, 800,300)
            with col3:
                st.write()
            loop_count += 1
            time.sleep(wait_time)
    else: 
        if now_mtime == prev_mtime:
            time.sleep(wait_time)
        else:
            with placeholder.container():
                df1 = pd.read_csv(dataset_url)
                df_old = df.copy() 
                df = get_diff_length(df,df1)
                # create three columns
                total, positive, negative = st.columns(3)

                # fill in those three columns with respective metrics or KPIs
                total.metric(
                    label="Total",
                    value= df['label'].count(),
                    delta = df.shape[0] - df_old.shape[0]
                )

                positive.metric(
                    label="Positive",
                    value= df[df['label'] == 0]['label'].count(),
                    delta = int(df[df['label'] == 0]['label'].count() - df_old[df_old['label'] == 0]['label'].count())
                )

                negative.metric(
                    label="Negative",
                    value=df[df['label'] == 1]['label'].count(),
                    delta = int(df[df['label'] == 1]['label'].count() - df_old[df_old['label'] == 1]['label'].count())
                )

                # create two columns for charts
                fig_col1, fig_col2 = st.columns(2)
                with fig_col1:
                    st.markdown("### Histogram Chart")
                    fig1 = px.histogram(data_frame=df, x="label", height=400,width=600, text_auto=True, color='label')
                    fig1.update_layout(bargap=0.2)
                    st.write(fig1)
                with fig_col2:
                    st.markdown("### Pie Chart")
                    fig2 = px.pie(df, values=[i for i in df.groupby('label')['text'].count()], names=df['label'].unique(), height=400,width=600, color_discrete_sequence=px.colors.sequential.RdBu)
                    st.write(fig2)

                # st.markdown("### Detailed Data View")
                # st.dataframe(df, 800,300)
                # loop_count += 1
                # time.sleep(5)

                # Dataframe
                st.markdown("### Detailed Data View")
                col1, col2, col3 = st.columns([1,3,1])
                with col1:
                    st.write()
                with col2:
                    st.dataframe(df, 800,300)
                with col3:
                    st.write()
                loop_count += 1
                time.sleep(wait_time)