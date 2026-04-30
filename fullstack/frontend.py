import streamlit as st
import requests 


st.title(" testin a get request")

# url = "http://127.0.0.1:8000/"


# api_test = st.button("Test it")
# 
# if api_test == True:
#     url = "http://127.0.0.1:8000/"

#     try:
#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()
#             st.title(f"Message from fast API:  {data["message"]}")
#             st.write(data) 
#             st.success(f"message: {data['message']}")
#         else:
#             st.error("echec lors de la recuperation, verifie ton backend")
            

#     except Exception as e:
#         st.error(f"Exception Message:: Lance ton serveur --  {e}")

# post_button = st.button("Sauveguarger les donnees avec POST")


name = str(st.text_input("enter your name:  "))
age = st.number_input("enter your age:  ", min_value=0, max_value=100, step=1)
profession = str(st.text_input("enter your profession:  "))
IsMarried = bool(st.checkbox("Are you married?"))

if st.button("Sauveguarger"):

    url="http://127.0.0.1:8000/save"

  

    Data = {
        "name": name,
        "age": age,
        "profession": profession,
        "IsMarried": IsMarried
    }


    try:
        response = requests.post(url, json=Data)

        if response.status_code == 200:
            st.success("Donness envoyer avec succes!")
            data = response.json()
            st.success(f"Message: {data['message']}, Status: {data['status']}, Result_id: {data['result']}")
        else:
            st.write(f"{response.status_code}")
            


    except Exception as e:
        st.error(f"Message: {e}")

# PATCH Request Section
st.markdown("---")
st.subheader("Update Data with PATCH")

name = str(st.text_input("enter new name  "))
age = st.number_input("enter your new age:  ", min_value=0, max_value=100, step=1)
profession = str(st.text_input("enter your new profession:  "))
IsMarried = bool(st.checkbox("Are you married ?"))


if st.button("Update Data"):
    url = "http://127.0.0.1:8000/update"
    
    Data = {
        "name": name,
        "age": age,
        "profession": profession,
        "IsMarried": IsMarried
    }
    
    try:
        response = requests.patch(url, json=Data)
        
        if response.status_code == 200:
            st.success("Data updated successfully!")
            data = response.json()
            st.success(f"Message: {data['message']}, Status: {data['status']}, Result: {data['result']}")
        else:
            st.error(f"Error: {response.status_code}")
    
    except Exception as e:
        st.error(f"Exception: {e}")
        


#get all users in the database
if st.button("Get All Users"):
    
    url = "http://127.0.0.1:8000/users"
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            st.success("successfull")
            data = response.json()            
            st.json(data["message"])
            
        else: 
            st.error(f"error in the response status, Actual response status: --- {response.status_code}")
    
    
    except Exception as e:
        st.error(f"Error Message:- {e}")

