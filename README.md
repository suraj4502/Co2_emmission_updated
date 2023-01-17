
# Carbon Dioxide Emission Prediction.       

The main aim of the project is to predict the CO2 emmitted
from a vehicle using certain features of the car(vehicle).
  [WebApp Link ](https://suraj4502-co2-emmission-updated---home-c91abw.streamlit.app/)

The dataset had around 7k datapoints regarding cars and its
features and the corresponding co2 emmission value.
The features are :-
###   Column ----------------------- Non-Null Count - Dtype  
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
     dtypes: float64(4), int64(3), object(5)


After analyzing the data I found that :
- Most of the features are right skewed.
- Data has several outliers.
- There is multicollinearity between fuel_consumption_city fuel_consumption_hwy fuel_consumption_comb(l/100km).

I performed Feature Enginerring to get rid of these problems.
so for treating outliers I used the following methods :

    1. Z Score Treatment 
    2. IQR based filtering 
    3. Percentile

Then the next step involves Feature selection, that I did using ExtratreeClassifier from sklearn.

    
    Scores :-
    make	                        0.069412
    model	                        0.127926
    vehicle_class	                0.061699
    engine_size     	            0.061064
    cylinders	                    0.016866
    transmission	                0.052619
    fuel_type	                    0.030351
    fuel_consumption_city	        0.153587
    fuel_consumption_hwy	        0.160584
    fuel_consumption_comb(l/100km)	0.183290
    fuel_consumption_comb(mpg)	    0.082603

    * Importance of every Feature for predicting the target Variable.

Then I plotted Residual Plots for every feature to check the Assumption for linear Regression and found out that the last four Columns does not follow Homoscedasticity. So I had to transform them or don't use them in model building.
    
After Building various models with different features I came up with the best set of features for Final Model Building. The features were :-
    
    ● make
    ● model
    ● vehicle_class
    ● engine_size
    ● transmission
    ● fuel_type
    ● fuel_consumption_comb(l/100km).
    ● Cylinders.

Then I scaled the values using StanderScaler. Then build different Regression models and compared their scores :-

![image](https://user-images.githubusercontent.com/76464630/212909259-e8769e66-f5cb-42e6-a2ae-1809390d6c01.png)
---
![image](https://user-images.githubusercontent.com/76464630/212909416-67e5bf0f-6654-4134-8279-a00ea650b440.png)
---
![image](https://user-images.githubusercontent.com/76464630/212909568-10c99e0a-d948-4b51-8acd-43ffecf67a25.png)
---
![image](https://user-images.githubusercontent.com/76464630/212909687-1d1da0e4-3e45-44ec-b751-cb258b56fc0b.png)
---
![image](https://user-images.githubusercontent.com/76464630/212909778-1717b305-2eb4-46f4-b28a-b723a7249799.png)
---
![image](https://user-images.githubusercontent.com/76464630/212909843-c250fddb-5367-4f0d-a534-9cd5a1f244bf.png)
---
![image](https://user-images.githubusercontent.com/76464630/212909987-581f78bd-65c3-4b6a-9907-11ce393d27cb.png)
---
After All these models I created a Deep Learning (ANN) model which I found performed best with :-
- For Training data it gave 3.1 rmse value.
- for Testing data it gave 3.6 rmse value.

### After model building I created a webapp that takes various features of a new car and gives co2 emmission prediction of that car and also deployed it on the cloud.
WebApp Link :- https://suraj4502-co2-emmission-updated---home-c91abw.streamlit.app/

## Screenshots


![image](https://user-images.githubusercontent.com/76464630/212912871-009f6bd9-d4f6-4ee8-b00e-6fbf7ac53661.png)

![image](https://user-images.githubusercontent.com/76464630/212913102-73e06697-31da-4910-8363-870ce3f923b9.png)

![image](https://user-images.githubusercontent.com/76464630/212913272-0a124751-e04a-4a7c-acd5-653f53453abd.png)

![image](https://user-images.githubusercontent.com/76464630/212913398-377d6355-6e83-4343-aae6-f8acec415787.png)

![image](https://user-images.githubusercontent.com/76464630/212913500-cfc942c0-09bd-4205-a974-f11fad4099e3.png)

![image](https://user-images.githubusercontent.com/76464630/212913650-39bc0dfc-d862-41d0-8a86-3ae91e8388b6.png)

--- 