from test import stem
from test import preprocessing
from test import desc_similarity

import streamlit as st
import psycopg2


import numpy as np
import pandas as pd
import spacy
import en_core_web_sm
import nltk
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer

#with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

nlp = spacy.load('en_core_web_sm')
stop_words = nlp.Defaults.stop_words
ps = PorterStemmer()


import warnings
pd.set_option('display.max_columns', None)
warnings.filterwarnings('ignore')

 # Connect to the database
conn = psycopg2.connect(host="localhost", user="postgres", password="sriheera", dbname="postgres")

# Create a cursor
cur = conn.cursor()

# Execute a SQL query
cur.execute("SELECT * FROM startup")

# Fetch the results
results = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()

columns = [desc[0] for desc in cur.description]
df = pd.DataFrame(results, columns=columns)

df1 = df.copy()
df_f = df1[['company','sector','description','amount']]

#a = desc_similarity(df_f,"description","amount")
st.sidebar.title("Capital Catalyst")
st.sidebar.markdown("Give us a few details about the domain you want to invest in:")
#st.sidebar.title("Filter Options")

# Add a select box for filtering by industry
options = ['100000 & below', '1000000 & below', '5000000 & below', '10000000 & below','50000000 & below','100000000 & below','1000000000 & below','5000000000 & below','50000000000 & below','10000000000 & below']
amount = st.sidebar.selectbox("Amount", options)
a1 = int(re.sub("[^0-9]", "", amount))

s1 = st.sidebar.selectbox("Sector", df_f["sector"].unique())

d1 = st.sidebar.text_area("Please enter a description of your app:")

st.title("Capital Catalyst")
st.markdown("Platform of Startup Fortunes")

if st.sidebar.button("Submit"):
    d = {}
    d['company'] = ''
    d['sector'] = s1
    d['description'] = d1
    d['amount'] = a1
    
    d = pd.DataFrame([d])
    df_f = pd.concat([df_f, d], axis=0, ignore_index=True)

    a = desc_similarity(df_f,"description","amount")
    #st.write(a)

# create a dropdown menu to select the row
#display the selected row
    num_rows = len(a)
    for i in range(num_rows):
       with st.container():
        st.title("#{} - {}".format(i+1,df['company'].iloc[a[i]]))
        st.text("Founded Year : {}".format(df['founded'].iloc[a[i]])) 
        st.text("Headquaters : {}".format(df['headquarters'].iloc[a[i]]))
        st.text("Sector : {}".format(df['sector'].iloc[a[i]]))
        st.write("Description : {}".format(df['description'].iloc[a[i]]))
        st.text("Founder : {}".format(df['founder'].iloc[a[i]]))
        st.text("Amount of investment required : {}".format(df['amount'].iloc[a[i]]))

