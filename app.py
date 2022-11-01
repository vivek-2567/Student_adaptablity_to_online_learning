import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Adaptablity to Online Learning", layout = 'wide')
st.markdown("<h1 style='text-align: center; color: white;'>Student's Adaptablity to Online Learning </h1>", unsafe_allow_html=True)
st.write("")
st.write("")

c1,c2,c3 = st.columns(3)

gender = c1.selectbox(label = "Select the Gender",options = ['Boy','Girl'])
age = c2.selectbox("Select the age",['21-25', '16-20', '11-15', '26-30', '6-10', '1-5'])
edu_level = c3.selectbox("Select the educational level",['University', 'College', 'School'])
insti_level = c1.selectbox("Select the Intitution type",['Non Government', 'Government'])
it_student = c2.selectbox("Is the student is a IT Student",['No','Yes'])
loc = c3.selectbox("Is the student from Town",['Yes', 'No'])
load = c1.selectbox("Level of load shedding",['Low', 'High'])
Finan = c2.selectbox("Financial Condition",['Mid','Poor','Rich'])
net = c3.selectbox("Internet Connection Type",['Wifi', 'Mobile Data'])
network = c1.selectbox("Select the Network Type",['4G','3G','2G'])
duration = c2.selectbox("Selec the duration of the class (in hours)",['3-6','1-3','0'])
lms = c3.selectbox("Does the intitution has Learning Management System", ['No','Yes'])
device = c2.selectbox("Select the type of device used for classes",['Tab', 'Mobile', 'Computer'])

o1 = {'Boy' : 0,'Girl':1}
o2 = {'21-25':3, '16-20':2, '11-15':1, '26-30':4, '6-10':5, '1-5':0}
o3 = {'University' : 2, 'College' : 0, 'School' : 1}
o4 = {'Non Government' : 1, 'Government':0}
o5 = {'No':0,'Yes':1}
o6 = {'Yes' : 1, 'No':0}
o7 = {'Low':1, 'High':0}
o8 = {'Mid':0,'Poor':1,'Rich':2}
o9 = {'Wifi' :1, 'Mobile Data':0}
o10 = {'4G':2,'3G':1,'2G':0}
o11 = {'3-6':2,'1-3':1,'0':0}
o12 = {'No' :0,'Yes':1}
o13 = {'Tab' : 2, 'Mobile' : 1, 'Computer' : 0}

x = []
x.append(o1[gender])
x.append(o2[age])
x.append(o3[edu_level])
x.append(o4[insti_level])
x.append(o5[it_student])
x.append(o6[loc])
x.append(o7[load])
x.append(o8[Finan])
x.append(o9[net])
x.append(o10[network])
x.append(o11[duration])
x.append(o12[lms])
x.append(o13[device])

x = np.array([x])

ansdic = {2:'Moderately', 1:'Very Less', 0:'Highly'}
model = joblib.load("student_adaptablity.pkl")
ans = model.predict(x)

st.write("")
st.write("")
st.info("The student is "+ansdic[ans[0]]+" adopted with Online Learning.")