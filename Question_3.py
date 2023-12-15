import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Age Histogram Plotter')

csv_file = st.file_uploader("Select a CSV file", type="csv")

if csv_file is not None:

    df = pd.read_csv(csv_file)

    if 'Name' in df.columns and 'Age' in df.columns:
        plt.hist(df['Age'], bins=10, edgecolor='black')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.title('Histogram of Ages')
        

        st.pyplot(plt)
    else:
        st.error('File seems invallid, Please make sure the column names in your csv are "Name" and "Age" ')
else:
    st.info('Please upload a CSV file.')
