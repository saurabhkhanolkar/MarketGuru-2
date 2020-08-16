import streamlit as st
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


#requirements: pickle file, stage2data(1)



html_temp = """
    <div style="background-color:black ;padding:10px">
    <h1 style="color:white;text-align:center;">Market Guru</h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)





st.sidebar.header("Stage 2: Recognize customers with maximum risk of churning out")

st.sidebar.markdown('<b>ABOUT:</b>', unsafe_allow_html=True)
st.sidebar.markdown("Enter the data of the customers you have newly acquired. Stage 2 will identify the customers with the highest potential of churning out. You can follow a personalized marketing approach towards such customers.")
st.sidebar.markdown('<b>How does Market Guru empower you?:</b>', unsafe_allow_html=True)  
st.sidebar.markdown("1.Prima facie analysis shows that Market Guru enables you to save 76% of time energy and resources spent on customer retention campaigns.")
st.sidebar.markdown("2.Enables you to employ a personalized marketing approach towards your customers, hence retaining them.") 
st.sidebar.markdown("3.Eliminates the need for a Third Party Analyst and thus, makes your organization Atmanirbhar!")
st.sidebar.markdown('<b>Built by:</b>', unsafe_allow_html=True)
st.sidebar.markdown('Team : Hackers101')
st.sidebar.markdown('<b>Happy Marketing!</b>', unsafe_allow_html=True)  

html_temp = """
    <div style="background-color:white ;padding:10px">
    <h3 style="color:black;text-align:left;">A model has been trained based on the Customer data uploaded.</h3>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)


html_temp = """
    <div style="background-color:white ;padding:10px">
    <h3 style="color:black;text-align:left;"> Now input the data of your recently acquired customers.</h3>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)




uploaded_file = st.file_uploader("upload your csv file here:", type=["csv"]) 
def upload():
    df1=pd.read_csv(uploaded_file)
    return(df1)
    

try:    

    if st.button("Analyse"):
            data_test=upload()
            
            daka=pd.read_csv('stage2data(1).csv')    
            data_test.drop(['Years since opening the account','years for cust'],axis=1,inplace=True)
            X = data_test.iloc[:, :-1].values
            y = data_test.iloc[:, -1].values
            le = LabelEncoder()
            X[:,0] = le.fit_transform(X[:,0])
            X[:,1] = le.fit_transform(X[:,1])
            X[:,2] = le.fit_transform(X[:,2])
            X[:,3] = le.fit_transform(X[:,3])
            X[:,4] = le.fit_transform(X[:,4])
            X[:,5] = le.fit_transform(X[:,5])
            X[:,6] = le.fit_transform(X[:,6])
            y = le.fit_transform(y)
            X_test=X
            y_test=y   
            load_clf=pickle.load(open('clss.pkl','rb'))
            y_pred=load_clf.predict(pd.DataFrame(X_test))
            st.header('Market Guru has recognised the following set of Customers who are at a high risk of churning out:  ')
            for i in range(len(y_pred)):
                if(y_pred[i]==1):
                    st.write('Custmer Number',daka['CustNo'][i],'using account number',daka['PrdAcctId'][i],'.' )
            st.header('Follow a personalised marketing approach towards these customers to retain them!')
                
            
    
except:
    st.write("Please enter valid customer data")
