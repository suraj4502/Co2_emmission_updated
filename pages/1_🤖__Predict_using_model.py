from sklearn.preprocessing import StandardScaler ,LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
import streamlit as st
import pandas as pd
import helper

st.set_page_config(page_title='Predictions', page_icon='🤔', layout="wide", initial_sidebar_state="expanded", menu_items=None)
st.header("Predict the amount of Co2 released from your car by entering the following aspects.")
model=st.sidebar.radio(" Select a model 🤗 :" ,['Model 1','Model 2'])

st.markdown("---")

df = helper.get_Data('Data/co2_emissions (1).csv')
if model == 'Model 2':

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7,col8 = st.columns([1,3])

    #### Taking inputs ####
    with col1:
        a = df.make.unique()
        a.sort()
        i1 = st.selectbox("Select Company :",a)
    #-------
    with col2:
        dfn = df[(df['make'] == i1)]
        b = dfn.model.unique()
        b.sort()
        i2 = st.selectbox("Select model :",b)
        #-----
    with col3:
        dfn1 = dfn[dfn['model'] == i2]
        c = dfn1['vehicle_class'].unique()
        i3=st.selectbox("Select veicle Class :" ,c)
    #-----
    with col4:
        dfn2 = dfn1[dfn1['vehicle_class'] == i3]
        d = dfn2['engine_size'].unique()
        i4 = st.selectbox("Engine size: ",d)
    #-----
    with col5:
        dfn3 = dfn2[dfn2['engine_size'] == i4]
        e = dfn2['cylinders'].unique()
        e.sort()
        i5 = st.selectbox("Cylinders :",e)
    #----
    with col6:
        dfn4 = dfn3[dfn3['cylinders'] == i5]
        f = dfn3['transmission'].unique()
        i6 = st.selectbox("Transmission :",f,help=("A = Automatic , AM = Automated manual , AV = Continuously variable , AS = Automatic with select shift , M = Manual. "))
    #----
    with col7:
        dfn5 = dfn4[dfn4['transmission'] == i6]
        i = dfn4['fuel_type'].unique()
        i7 = st.selectbox("Fuel Type :", i,help=("X = Regular gasoline, Z = Premium gasoline, D = Diesel, E= Ethanol(E85), N = Natural gas."))
    #------
    with col8 :
        milege = st.number_input("Enter the milege in km/litre.",
                                 min_value=float(1),max_value=float(100),step=float(1.0),help=("The number of Kilometers your vehicle covers in 1 Litre of fuel."))
        i8 = (100/milege)


    #data preprocessing

    df = helper.preprocessing1(df, 'co2_emissions')
    df = helper.preprocessing1(df, 'fuel_consumption_comb(l/100km)')
                #
    df = df.sample(frac=1, random_state=4)
                #
    le_make = LabelEncoder()
    le_model = LabelEncoder()
    le_veh = LabelEncoder()
    le_tran = LabelEncoder()
    le_fuel = LabelEncoder()
                #
    # label Encoding
    df['make'] = le_make.fit_transform(df['make'])
    df['model'] = le_model.fit_transform(df['model'])
    df['vehicle_class'] = le_veh.fit_transform(df['vehicle_class'])
    df['transmission'] = le_tran.fit_transform(df['transmission'])
    df['fuel_type'] = le_fuel.fit_transform(df['fuel_type'])
                #
    Xi = df[['make', 'model', 'vehicle_class', 'engine_size', 'cylinders', 'transmission', 'fuel_type',
                 'fuel_consumption_comb(l/100km)']]
    Y = df['co2_emissions']
                #
    scaler = StandardScaler()
    X = scaler.fit_transform(Xi)
                #
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=4)
                #
    #Loading the trained model
    st.cache()
    T_model = savedModel=load_model('Models/DL_1.h5')
        ########
    #Predictions
    input_data = pd.DataFrame({'make': i1, 'model': i2, 'vehicle_class': i3,
                                   'engine_size': i4, 'cylinders': i5, 'transmission': i6, 'fuel_type': i7,
                                   'fuel_consumption_comb(l/100km)': i8}, index=[1])
    input_data['make'] = le_make.fit_transform(input_data['make'])
    input_data['model'] = le_model.fit_transform(input_data['model'])
    input_data['vehicle_class'] = le_veh.fit_transform(input_data['vehicle_class'])
    input_data['transmission'] = le_tran.fit_transform(input_data['transmission'])
    input_data['fuel_type'] = le_fuel.fit_transform(input_data['fuel_type'])
    input_data = scaler.transform(input_data)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3:
        button=st.button("Predict 🦾")
    if button:
        pred = T_model.predict(input_data)
        pred = float(pred)
        pred = round(pred, 2)
        if pred > 150:
            st.error(f"The Co2 emmitted from your car is {pred} grams per kilometer.")
        else:
            st.success(f"The Co2 emmitted from your car is {pred} grams per kilometer.")
            st.balloons()


if model == 'Model 1':
    col1, col2 = st.columns([1.5,3.5])
    col3, col4 = st.columns(2)
    col5, col6 = st.columns([2,3])
    with col1:
        a = df.vehicle_class.unique()
        a.sort()
        i1= st.selectbox("Select Vehicle type : ",a)
    with col2:
        i2=st.slider("Select Engine Size :", min_value=0.0, max_value=10.0, value=2.5, step=0.5,help =("Slide to select.."))
    with col3:
        i3 = st.number_input("Enter Number of Cylinders : ",min_value=2,max_value=18,step=1,format="%u")
    with col4:
        b = df.transmission.unique()
        b.sort()
        i4 = st.selectbox("Select the Transmission Type :",b,help=("A = Automatic , AM = Automated manual , AV = Continuously variable , AS = Automatic with select shift , M = Manual. "))
    with col5 :
        c = df.fuel_type.unique()
        c.sort()
        i5 = st.selectbox("Select Fuel Type :" , c,help=("X = Regular gasoline, Z = Premium gasoline, D = Diesel, E= Ethanol(E85), N = Natural gas."))
    with col6 :
        milege = st.number_input("Enter the milege in km/litre.",
                                 min_value=float(1),max_value=float(100),step=float(1.0),help=("The number of Kilometers your vehicle covers in 1 Litre of fuel."))
        i6 = (100/milege)


    #### Data preprocessing
    df = helper.preprocessing1(df, 'co2_emissions')
    df = helper.preprocessing1(df, 'fuel_consumption_comb(l/100km)')

    le_veh = LabelEncoder()
    le_tran = LabelEncoder()
    le_fuel = LabelEncoder()
    df['vehicle_class'] = le_veh.fit_transform(df['vehicle_class'])
    df['transmission'] = le_tran.fit_transform(df['transmission'])
    df['fuel_type'] = le_fuel.fit_transform(df['fuel_type'])

    Xi = df[['vehicle_class', 'engine_size', 'cylinders', 'transmission', 'fuel_type',
                 'fuel_consumption_comb(l/100km)']]
    Y = df['co2_emissions']

    scaler = StandardScaler()
    X = scaler.fit_transform(Xi)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=4)

    # Loading the trained model
    st.cache()
    T_model2 = savedModel = load_model('Models/DL_2.h5')
    # Predictions
    # Predictions
    input_data = pd.DataFrame({'vehicle_class': i1,'engine_size': i2, 'cylinders': i3,
                                   'transmission': i4, 'fuel_type': i5,
                                   'fuel_consumption_comb(l/100km)': i6}, index=[1])
    input_data['vehicle_class'] = le_veh.fit_transform(input_data['vehicle_class'])
    input_data['transmission'] = le_tran.fit_transform(input_data['transmission'])
    input_data['fuel_type'] = le_fuel.fit_transform(input_data['fuel_type'])
    input_data = scaler.transform(input_data)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3:
        button = st.button("Predict 🦾")
    if button:
        pred = T_model2.predict(input_data)
        pred = float(pred)
        pred = round(pred, 2)
        if pred > 150 :
            st.error(f"The Co2 emmitted from your car is {pred} grams per kilometer.")
        else:
            st.success(f"The Co2 emmitted from your car is {pred} grams per kilometer.")
            st.balloons()
