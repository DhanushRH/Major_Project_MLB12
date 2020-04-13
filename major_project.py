import pandas as pd
data=pd.read_excel('Data_Train.xlsx')
data.head(10)

#removing null values
data.dropna(inplace=True)
data=data[data['Power']!='null bhp']

#Splitting the name into 3 columns
s=['Range Rover','Land Rover','Corolla Altis','Indica Vista','Innova Crysta','Pajero Sport','Ssangyong Rexton','Vitara Brezza','Zest Revotron','Santo Xing','B Class','Cooper Convertible','Coutryman Cooper','Grand ilo','Grand Punto']
t=['Range_Rover','Land_Rover','Corolla_Altis','Indica_Vista','Innova_Crysta','Pajero_Sport','Ssangyong_Rexton','Vitara_Brezza','Zest_Revotron','Santo_Xing','B_Class','Cooper_Convertible','Coutryman_Cooper','Grand_ilo','Grand_Punto']
data['Name']=data['Name'].replace(s,t,regex=True)
new=data['Name'].str.split(' ',n=3,expand=True)
data['Company']=new[0]
data['Model']=new[1]
data['Version']=new[2]
data.drop(['Name'],axis=1,inplace=True)

#Removing units from the columns
new=data['Mileage'].str.split(' ',expand=True)
data['Mileage']=new[0]
new=data['Engine'].str.split(' ',expand=True)
data['Engine']=new[0]
new=data['Power'].str.split(' ',expand=True)
data['Power']=new[0]
