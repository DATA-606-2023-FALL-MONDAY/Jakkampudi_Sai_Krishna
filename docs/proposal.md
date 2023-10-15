## 1. Title and Author

**Project Title:** E-Commerce Customer Churn Prediction

Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang

**Author Name:** Sai Krishna Jakkampudi

**GitHub:** https://github.com/saikrishna-jakkampudi

**LinkedIn:** https://www.linkedin.com/in/saikrishnajakkampudi/

**PowerPoint presentation file:**

**Link to your YouTube video:** 

## 2. Background

Q1. **What is the Project about?**

It is a critical analysis for us and companies because they directly impact revenue and profitability.By understanding and anticipating customer churn, businesses can implement targeted retention strategies, reduce customer acquisition costs, make data-driven decisions, maintain a competitive edge, and ultimately maximize profitability.


Q2. **What questions do you have in mind and would like to answer?**

a. Identifying specific customer segments or individuals who are likely to churn is crucial for targeted retention efforts.

b. Understanding the behaviors, patterns, or triggers that precede customer churn can help in proactive intervention.

c. Analyzing past efforts and their impact can guide the selection of retention tactics that yield the best results.

d. Assessing the financial impact of retaining customers versus losing them provides insight into the value of churn reduction efforts.

## 3. DATA

Q3: **Where do you get the data to analyze and help answer your questions (credibility of source, quality of data, size of data, attributes of data, etc.)?**

**Data source**: [Kaggle - E-commerce Customer Churn Analysis and Prediction](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction)

- **Credibility of source**: The data is sourced from Kaggle, a reputable platform for datasets and data-related projects, known for its quality datasets contributed by the community.

- **Quality of data**: The dataset appears to be well-maintained and documented, providing a comprehensive set of features for analysis.

- **Size of data**: The dataset contains 5630 records, which is a reasonably sized dataset suitable for analysis.

**Attributes of data**:

- **CustomerID**

  - Data type: Continous
  - Description: Unique customer ID.
  - Possible data entries: "50001" to  "55630"
  
- **Churn**

  - Data type: Categorical ( Binary)
  - Description: Chrun Flag.
  - Possible data entries: "0" and  "1"
  
- **Tenure**

  - Data type: Continous ( Numerical)
  - Description: Tenure of customer in the organization.
  - Possible data entries Range: "0" to  "61"

- **PreferredLoginDevice**

  - Data type: Catergorical ( Nominal)
  - Description: Preferred Login Device of the Customer.
  - Possible data entries Range: "Phone", "Mobile Phone", "Computer"

- **CityTier** 

  - Data type: Catergorical ( Ordinal)
  - Description: City Ter.
  - Possible data entries Range: "1", "2", "3"
  
 
- **WarehouseToHome**

  - Data type: Continous ( Numerical)
  - Description: Distance between customer house to warehouse
  - Possible data entries Range: "5" to  "127"
  
- **PreferredPaymentMode**

  - Data type: Catergorical ( Nominal)
  - Description: Preferred payment method of the customer.
  - Possible data entries Range: "CC", "CREDIT CARD", "DEBIT CARD", "UPI", "E-WALLET", "COD"," CASH ON DELIVERY"

- **Gender**

  - Data type: Categorical ( Binary)
  - Description: Gender of the Customer.
  - Possible data entries: "Male" and  "Female".
  
- **HourSpendOnApp**

  - Data type: Continous 
  - Description: Number of hours customer spent on app or website.
  - Possible data entries: "0" to  "5".

- **NumberOfDeviceRegistered**

  - Data type: Continous 
  - Description: Total number of devices registered per customer.
  - Possible data entries: "0" to  "6".
  
- **PreferedOrderCat**

  - Data type: Catergorical ( Nominal)
  - Description: Preferred order category in the last month.
  - Possible data entries Range: "Fashion", "Grocery", "Laptop & Accessories", "Mobile", "MObile-Phone", "Others".

- **SatisfactionScore**

  - Data type: Continous 
  - Description: Customer Satisfaction Score.
  - Possible data entries: "1" to  "5".

- **MaritalStatus**

  - Data type: Catergorical ( Nominal)
  - Description: Marital status of the customer.
  - Possible data entries Range: "Single", "Married", "Divorce".

    
- **NumberOfAddress**

  - Data type: Continous ( Numerical)
  - Description: Total number of addresses added by customer
  - Possible data entries Range: "1" to  "22"

- **Complain**

  - Data type: Categorical ( Binary)
  - Description: Number of compliants received in the last month
  - Possible data entries Range: "0" to  "1"
  
  
- **OrderAmountHikeFromlastYear**

  - Data type: Continous ( Numerical)
  - Description: Percentage increase in order amount from last year
  - Possible data entries Range: "11" to  "26"


- **CouponUsed**

  - Data type: Continous ( Numerical)
  - Description: Total number of coupons used last month.
  - Possible data entries Range: "0" to  "16"

- **OrderCount**

  - Data type: Continous ( Numerical)
  - Description: Total number of orders place in last month.
  - Possible data entries Range: "0" to  "16"

- **DaySinceLastOrder**

  - Data type: Continous ( Numerical)
  - Description: Days since last order by the customer
  - Possible data entries Range: "0" to  "46"
  
- **CashbackAmount**

  - Data type: Continous ( Numerical)
  - Description: Average cashback in last month.
  - Possible data entries Range: "0" to  "325"


**Which variable/column will be your taget/label in your ML model?**

 - Customer Churn is the most effective target variable for creating machine-learning models from the dataset.
 - It is a binary variable that machine learning systems can classify with ease. 
 - Additionally, there is plenty of information and study on the subject because customer turnover is a regular and significant issue for organizations to address.


**Which variables may be selected as predictors for your ML models?**

 - Tenure
 - WarehouseToHome
 - OrderAmountHikeFromlastYear
 - CashbackAmount
 - avg_cashbk_per_order



```python

```


```python

```
