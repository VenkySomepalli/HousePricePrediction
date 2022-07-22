Residential home prices across the United States over the next decade?.

A linear regression analysis of house prices in USA with 13 features selected on MECE Framework.

Certainly multiple different approaches:

Supply:
How many houses existing, how many newly built per year (net), split by reasonable geographic units (coastal cities, in-land cities, in-land rural)

Demand:
Development of population, development of household sizes, demographic shifts from rural to cities With that you could project development of supply and demand per region and project price developments.

Sales area of resident: Sales area of resident will affect the housing price to a certain extent.

Per-capita income: Increase in per-capita income will cause the rise of housing prices to from two aspects. On the one hand, increase in per-capita income is inseparable from economic development, and economic development means investment, production and business activities, etc. become active, thus the demand for shopping malls, factories, offices, etc. are increasing, which bring to the rise in house prices. On the other hand, rising incomes and improved living standards will bring
to higher living standards for people.

Quantity of urban population: Quantity of urban population plays a tremendous influence affect on housing price. The influence can be divided into two categories. The first one is direct influence, i.e., Higher quantity of urban population will bring to higher demand of house. The second one is the indirect influence, i.e., higher quantity of urban population will bring to higher demand of house. 

Housing Cost: Under certain circumstances that the supply and demand is fixed, the rising of land and construction materials are important factors in driving up housing prices. As land resources are limited, so the changes of housing price will not cause a large change in supply elasticity.
 
Data Set: Boston House Prices

The problem that we are going to solve here is that given a set of features that describe a house in Boston, our machine learning model must predict the house price. To train our machine learning model with boston housing data, we will be using scikit-learn’s boston data.



Boston house prices dataset
---------------------------

**Data Set Characteristics:**  

    :Number of Instances: 506 

    :Number of Attributes: 13 numeric/categorical predictive. Median Value (attribute 14) is usually the target.

    :Attribute Information (in order):
        - CRIM     per capita crime rate by town
        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
        - INDUS    proportion of non-retail business acres per town
        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        - NOX      nitric oxides concentration (parts per 10 million)
        - RM       average number of rooms per dwelling
        - AGE      proportion of owner-occupied units built prior to 1940
        - DIS      weighted distances to five Boston employment centres
        - RAD      index of accessibility to radial highways
        - TAX      full-value property-tax rate per $10,000
        - PTRATIO  pupil-teacher ratio by town
        - B        1000(Bk - 0.63)^2 where Bk is the proportion of black people by town
        - LSTAT    % lower status of the population
        - MEDV     Median value of owner-occupied homes in $1000's

    :Missing Attribute Values: None


This is a copy of UCI ML housing dataset.
https://archive.ics.uci.edu/ml/machine-learning-databases/housing/

Steps FOLLOWED:
1. Data understanding
2. Exploratory Data Analysis
3. Train Test Split
4. Model Comparison
5. Hyper Parameter Selection
6. Model Fitting
7. Variance & Bias-trade off Check
8. Error Analysis
9. OLS Summary Study

# LinearRegression-HousePricePrediction
Boston housing price prediction using Regression Algorithms  
