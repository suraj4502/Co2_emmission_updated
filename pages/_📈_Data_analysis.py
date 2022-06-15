import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import helper

st.set_page_config(page_title='Data_Analysis', page_icon='📈', layout="wide", initial_sidebar_state="collapsed", menu_items=None)
st.title("Analysis of Carbon Dioxide Emission from Cars.")



st.markdown("- Analyzing the data which has around `7k` data points. The goal is to get some insights about the data for model Building. ")

df = helper.get_Data('Data/co2_emissions (1).csv')
    #dropping duplicates
df=df.drop_duplicates()


st.header("A small portion of the data")
st.dataframe(df.head())

st.markdown("___")

st.write(''' ### Feature Details:  
        ※  
        1. make ⇨ car brand under study.     
        2. model ⇨ the specific model of the car. 
        3. vehicle_class ⇨ car body type of the car.
        4. engine_size ⇨ size of the car engine, in Liters.    
        5. cylinders ⇨ number of cylinders.
        6. transmission ⇨ "A" for`Automatic', "AM" for ``Automated manual', "AS" for 'Automatic with select shift', "AV" for 'Continuously variable', "M" for 'Manual'.
        7. fuel_type ⇨ "X" for 'Regular gasoline', "Z" for 'Premium gasoline', "D" for 'Diesel', "E" for 'Ethanol (E85)', "N" for 'Natural gas'.
        8. fuel_consumption_city ⇨ City fuel consumption ratings, in liters per 100 kilometers.
        9. fuel_consumption_hwy ⇨ Highway fuel consumption ratings, in liters per 100 kilometers.
        10. fuel_consumption_comb(l/100km) ⇨ the combined fuel consumption rating (55% city, 45% highway), in L/100 km.
        11. fuel_consumption_comb(mpg) ⇨ the combined fuel consumption rating (55% city, 45% highway), in miles per gallon (mpg).
        12. co2_emissions ⇨ the tailpipe emissions of carbon dioxide for combined city and highway driving, in grams per kilometer.
    ''')
st.markdown("___")
st.write('''####  Basic info about the data: 
                 #   Column                          Non-Null Count  Dtype  
        ---  ------                          --------------  -----  
         0   make                            7385 non-null   object 
         1   model                           7385 non-null   object 
         2   vehicle_class                   7385 non-null   object 
         3   engine_size                     7385 non-null   float64
         4   cylinders                       7385 non-null   int64  
         5   transmission                    7385 non-null   object 
         6   fuel_type                       7385 non-null   object 
         7   fuel_consumption_city           7385 non-null   float64
         8   fuel_consumption_hwy            7385 non-null   float64
         9   fuel_consumption_comb(l/100km)  7385 non-null   float64
         10  fuel_consumption_comb(mpg)      7385 non-null   int64  
         11  co2_emissions                   7385 non-null   int64  
         dtypes: float64(4), int64(3), object(5)''')





st.header("Histogram For Getting to know about frequency.")
columns =['make', 'vehicle_class', 'engine_size', 'cylinders',
                          'transmission', 'fuel_type', 'fuel_consumption_city',
                          'fuel_consumption_hwy', 'fuel_consumption_comb(l/100km)',
                          'fuel_consumption_comb(mpg)', 'co2_emissions']
selected_feature=st.selectbox('Choose the feature',columns)
for column in columns:
        if selected_feature == column:
            fig = px.histogram(df, x=column,color_discrete_sequence=['#8B1A1A'])
            fig.update_layout(
                      autosize=True,
                      width=1300,
                      height=650,
                      margin=dict(
                          l=50,
                          r=50,
                          b=100,
                          t=100,
                          pad=4,
                      ),
                      paper_bgcolor="white",
                  )
            st.plotly_chart(fig)
        else:
            pass


st.header("Scatterplot with respect to Co2 emission.")
columns_for_scatterplot =['engine_size', 'cylinders',
                          'transmission', 'fuel_type', 'fuel_consumption_city',
                          'fuel_consumption_hwy', 'fuel_consumption_comb(l/100km)',
                          'fuel_consumption_comb(mpg)']
selected_feature_for_scatterplot=st.selectbox('Choose the feature',columns_for_scatterplot)
for c in columns_for_scatterplot:
    if selected_feature_for_scatterplot== c:
        fig = px.scatter(data_frame=df,x=c,y='co2_emissions',color_discrete_sequence=['#8B1A1A'])
        fig.update_layout(
                      autosize=True,
                      width=1300,
                      height=650,
                      margin=dict(
                          l=50,
                          r=50,
                          b=100,
                          t=100,
                          pad=4,
                      ),
                      paper_bgcolor="white",
                  )
        st.plotly_chart(fig)
    else:
        pass








st.header("Boxplots with respect to co2 Emission.")
columns_for_boxplot =['make', 'vehicle_class', 'cylinders',
                          'transmission', 'fuel_type',
                          ]
selected_feature_for_boxplot=st.selectbox('Choose the feature',columns_for_boxplot)
for column in columns_for_boxplot:
    if selected_feature_for_boxplot == column:
          fig = px.box(df, x=column,y='co2_emissions',color_discrete_sequence=['#8B1A1A'])
          fig.update_layout(
                      autosize=True,
                      width=1300,
                      height=650,
                      margin=dict(
                          l=50,
                          r=50,
                          b=100,
                          t=100,
                          pad=4,
                      ),
                      paper_bgcolor="white",
                  )
          st.plotly_chart(fig)
    else:
         pass

st.header("Boxplots ")
columns_for_new = ['make', 'vehicle_class', 'engine_size', 'cylinders',
                'transmission', 'fuel_type', 'fuel_consumption_city',
                'fuel_consumption_hwy', 'fuel_consumption_comb(l/100km)',
                'fuel_consumption_comb(mpg)', 'co2_emissions'
                ]
new_features = st.selectbox('select a feature',columns_for_new)
for column in columns_for_new:
    if new_features == column:
        fig = px.box(df, x=column, color_discrete_sequence=['#8B1A1A'])
        fig.update_layout(
                autosize=True,
                width=1300,
                height=650,
                margin=dict(
                    l=50,
                    r=50,
                    b=100,
                    t=100,
                    pad=4,
                ),
                paper_bgcolor="white",
            )
        st.plotly_chart(fig)
    else:
        pass



#label Encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['make'] = le.fit_transform(df['make'])
df['model']  = le.fit_transform(df['model'])
df['vehicle_class']  = le.fit_transform(df['vehicle_class'])
df['transmission']  =le.fit_transform(df['transmission'])
df['fuel_type']  = le.fit_transform(df['fuel_type'])


st.header("Heatmap for knowing the correlation.")
fig, ax = plt.subplots(figsize=(4,2))
sns.set_context('paper',font_scale=0.4)
sns.heatmap(df.corr(), ax=ax,annot=True)
st.write(fig)



final_df=helper.get_Data1('Data/final_df.csv')
    #st.write(final_df)
st.header("Regression Plots.")
    #import statsmodels.api as sm

new_cols = ['engine_size', 'cylinders',
                'transmission', 'fuel_type', 'fuel_consumption_city',
                'fuel_consumption_hwy', 'fuel_consumption_comb(l/100km)',
                'fuel_consumption_comb(mpg)']
col = st.selectbox('select a feature.',new_cols)
for n_col in new_cols:
    if n_col == col:
        fig = px.scatter(final_df, x=n_col, y='co2_emissions', opacity=0.65,trendline='ols',
                             trendline_color_override='#030303',color_discrete_sequence=['#8B1A1A'])
        fig.update_layout(
                autosize=True,
                width=1300,
                height=650,
                margin=dict(
                    l=50,
                    r=50,
                    b=100,
                    t=100,
                    pad=4,
                ),
                paper_bgcolor="white",
            )
        st.plotly_chart(fig)

st.markdown("---")

st.markdown('## Some insights from the data:')
st.markdown('- #### Most of the features are `right skewed`.\n- #### Data has `several outliers`.''\n'
                '- #### There is multicollinearity between `fuel_consumption_city` `fuel_consumption_hwy` '
                '`fuel_consumption_comb(l/100km)`.')

st.markdown("---")
