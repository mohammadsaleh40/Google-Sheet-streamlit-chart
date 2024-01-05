import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


# قسمت ورود

names = ["Mohammad Saleh Ali Akbari" ,  "valed_1"]

usernames = ["msaa" , "v1"]
adminlists = ["msaa"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
file_kcsv_path = Path(__file__).parent / "kol_nomarat.csv"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {"usernames":{}}

for un, name, pw in zip(usernames, names, hashed_passwords):
    user_dict = {"name":name,"password":pw}
    credentials["usernames"].update({un:user_dict})

authenticator = stauth.Authenticate(credentials, "app_home", "auth", cookie_expiry_days=30)

name , authenticator_status , username = authenticator.login("ورود" , "main")

if authenticator_status == False:
    st.error("نام کاربری یا رمز عبور اشتباه است.")
if authenticator_status == None:
    st.error("لطفا نام کاربری و رمز عبور خود را وارد کنید.")


if authenticator_status:

    if username in adminlists:
        sheet_id = "1vIV2Sl1Mad9e-lf24-iVqXs6gwuRij-bOUl7Iir2hQ8"
        
        # def load_from_google_sheet_(sheet_id):
        #     return pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
        # dfg = load_from_google_sheet_(sheet_id)

        load_data_button = st.button("بروزرسانی اطلاعات")        
        if load_data_button:
            dfg = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
            dfg.to_csv(file_kcsv_path , index = False)
        
        # dfg.to_csv("kol_nomarat.csv" , index = False)
            
    
    df = pd.read_csv(file_kcsv_path)
    
    fig1 = px.bar(df, x='y', y='x2', color='x3' ,animation_frame='x1', barmode='group',)
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.line(df, x='x3', y='x2' ,color='y' ,animation_frame='x1')
    fig2['layout']['yaxis'].update(autorange = True)
    st.plotly_chart(fig2, use_container_width=True)
    if username in adminlists:
        ddf = df.copy().pivot( index='y' ,columns=["x1","x3"])
        @st.cache_data
        def sta_df(df):
            return df.mean() , df.max() , df.min() , df.std()
        
        mean_df , max_df ,min_df ,std_df = sta_df(ddf)
        st.text("میانگین نمرات کلاس در آزمون‌ها و درس‌های مختلف")
        mean_df
        st.text("حداکثر نمرات کلاس در آزمون‌ها و درس‌های مختلف")
        max_df 
        st.text("حداقل نمرات کلاس در آزمون‌ها و درس‌های مختلف")
        min_df 
        st.text("انحراف معیار نمرات کلاس در آزمون‌ها و درس‌های مختلف")
        std_df



    # قسمت کناری
    st.sidebar.title(f"خوش آمدید {name}")
    authenticator.logout("خروج" , "sidebar")