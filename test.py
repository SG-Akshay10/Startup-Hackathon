import numpy as np
import pandas as pd
import spacy
import en_core_web_sm
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer

nlp = spacy.load('en_core_web_sm')
stop_words = nlp.Defaults.stop_words
ps = PorterStemmer()

import warnings
pd.set_option('display.max_columns', None)
warnings.filterwarnings('ignore')

#df = pd.read_csv(r'/content/drive/MyDrive/Colab Notebooks/Indian Startup.csv')

#df1 = df.copy()

#df_f = df1[['Company','Sector','Description','Amount']]

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

def preprocessing(df,column):
    df[column] = df[column].apply(lambda x:x.split())
    df[column] = df[column].apply(lambda x:[i.replace(" ","") for i in x])
    df[column] = df[column].apply(lambda x:" ".join(x))
    df[column] = df[column].apply(stem)
    df[column] = df[column].apply(lambda x: nlp(x.lower()))
    df[column] = [' '.join([token.lemma_ for token in doc]) for doc in df[column]]
    df[column] = [' '.join([word for word in doc.split() if word not in stop_words]) for doc in df[column]]
    df[column].replace("[^a-zA-Z]"," ",regex=True, inplace=True)

def desc_similarity(df,column1,column2):
      
    preprocessing(df,column1)

    df1 = df[['company',column1]]
    df2 = df[['company',column2]]

    tfidf = TfidfVectorizer(stop_words = "english")
    tfidf_matrix = tfidf.fit_transform(df1[column1])
    tfidf_matrix_df=pd.DataFrame.sparse.from_spmatrix(tfidf_matrix)
    df_final=tfidf_matrix_df

    x = df_final.iloc[[-1],:] 
    y = df_final.iloc[:-2,:]

    # Calculate the similarity matrix
    sim_matrix=cosine_similarity(x,y)
    df_sim_matrix = pd.DataFrame(sim_matrix)
    sim_scores = list(enumerate(sim_matrix[0]))
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse = True)
    s_idx  =  [i[0] for i in sim_scores]
    s_scores =  [i[1] for i in sim_scores]

    df_similar = pd.DataFrame(columns=["company", "score"])
    df_similar["company"] = df1.loc[s_idx, "company"]
    df_similar["score"] = s_scores
    df_similar=df_similar.loc[(df_similar['company'] !='')]
    df_similar=df_similar.drop_duplicates(subset='company', keep="first")
    df_similar = pd.DataFrame(df_similar)
    
    df_similar_N = df_similar.iloc[0:9+1,:]    
    df_similar_N = df_similar_N[df2['amount']<=df2['amount'].iloc[-1]]
    df_similar_index = list(df_similar_N.index)
    #df_similar_N = pd.merge(df_similar_N, df2, left_on='company', right_on='company')
    #df_similar_N.reset_index(inplace = True)
    #ca = df_similar_N['company'].values.tolist() 

        
    # Return the similarity matrix
    return df_similar_index


