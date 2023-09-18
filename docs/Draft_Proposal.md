<!DOCTYPE html>
<html>
<head>
    <title></title>
    <style>
        body {
            text-align: center;
        }
    </style>
</head>
<body>
    <center><h1>E-Commerce Customer Churn Prediction</h1></center><br>
    <p><strong><center>Prepared for UMBC Data Science Master Degree Capstone Under Guidance of Professor Dr Chaojie Wang</center></strong></p><br>
    <center><strong><p><center>SAI KRISHNA JAKKAMPUDI</center></p></strong></center><br>
    <center><a href="https://github.com/saikrishna-jakkampudi" target="_blank">Github</a></center><br>
    <p><center><a href="https://www.linkedin.com/in/saikrishnajakkampudi/" target="_blank">LinkedIn</a></center></p><br>
</body>
</html>


<details>
<summary><strong>Q1: Why is the issue important to you and/or to others?</strong></summary>

It is a critical analysis for us and companies because they directly impact revenue and profitability.By understanding and anticipating customer churn, businesses can implement targeted retention strategies, reduce customer acquisition costs, make data-driven decisions, maintain a competitive edge, and ultimately maximize profitability.

</details>


<details>
<summary><strong>Q2: What questions do you have in mind and would like to answer?</strong></summary>

a. Identifying specific customer segments or individuals who are likely to churn is crucial for targeted retention efforts.

b. Understanding the behaviors, patterns, or triggers that precede customer churn can help in proactive intervention.

c. Analyzing past efforts and their impact can guide the selection of retention tactics that yield the best results.

d. Assessing the financial impact of retaining customers versus losing them provides insight into the value of churn reduction efforts.

</details>

<details>
<summary><strong>Q3: Where do you get the data to analyze and help answer your questions (credibility of source, quality of data, size of data, attributes of data, etc.)?</strong></summary>

**Data source**: [Kaggle - E-commerce Customer Churn Analysis and Prediction](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction)

- **Credibility of source**: The data is sourced from Kaggle, a reputable platform for datasets and data-related projects, known for its quality datasets contributed by the community.

- **Quality of data**: The dataset appears to be well-maintained and documented, providing a comprehensive set of features for analysis.

- **Size of data**: The dataset contains 5630 records, which is a reasonably sized dataset suitable for analysis.

- **Attributes of data**:
  - CustomerID
  - Churn
  - Tenure
  - PreferredLoginDevice
  - CityTier
  - WarehouseToHome
  - PreferredPaymentMode
  - Gender
  - HourSpendOnApp
  - NumberOfDeviceRegistered
  - PreferedOrderCat
  - SatisfactionScore
  - MaritalStatus
  - NumberOfAddress
  - Complain
  - OrderAmountHikeFromlastYear
  - CouponUsed
  - OrderCount
  - DaySinceLastOrder
  - CashbackAmount

</details>

<details>
    <summary><strong>What does each row represent?</strong></summary>

**Data Dictionary**

| Column Name                     | Description                                        |
|---------------------------------|----------------------------------------------------|
| E Comm CustomerID               | Unique customer ID                                 |
| E Comm Churn                    | Churn Flag                                         |
| E Comm Tenure                   | Tenure of customer in the organization             |
| E Comm PreferredLoginDevice     | Preferred login device of the customer             |
| E Comm CityTier                 | City tier                                          |
| E Comm WarehouseToHome         | Distance between warehouse and customer's home     |
| E Comm PreferredPaymentMode     | Preferred payment method of the customer           |
| E Comm Gender                   | Gender of the customer                             |
| E Comm HourSpendOnApp           | Number of hours spent on mobile app or website    |
| E Comm NumberOfDeviceRegistered | Total number of devices registered for a customer  |
| E Comm PreferedOrderCat         | Preferred order category in the last month         |
| E Comm SatisfactionScore        | Customer satisfaction score                        |
| E Comm MaritalStatus            | Marital status of the customer                     |
| E Comm NumberOfAddress          | Total number of addresses added by the customer   |
| E Comm Complain                 | Complaint raised in the last month                 |
| E Comm OrderAmountHikeFromLastYear | Percentage increase in order amount from last year |
| E Comm CouponUsed               | Total number of coupons used in the last month    |
| E Comm OrderCount               | Total number of orders placed in the last month   |
| E Comm DaySinceLastOrder        | Days since the last order by the customer         |
| E Comm CashbackAmount           | Average cashback in the last month                 |

</details>


<details>
<summary><strong>Which variable/column will be your taget/label in your ML model?</strong></summary><br>
    Customer Churn is the most effective target variable for creating machine-learning models from the dataset. It is a binary variable that machine learning systems can classify with ease. Additionally, there is plenty of information and study on the subject because customer turnover is a regular and significant issue for organizations to address.
</details>

<details>
<summary><strong>Which variables may be selected as predictors for your ML models?</strong></summary>

<table align = left>
  <tr>
    <th>#</th>
    <th>Predictors</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Tenure</td>
  </tr>
  <tr>
    <td>2</td>
    <td>WarehouseToHome</td>
  </tr>
  <tr>
    <td>3</td>
    <td>OrderAmountHikeFromlastYear</td>
  </tr>
  <tr>
    <td>4</td>
    <td>CashbackAmount</td>
  </tr>
  <tr>
    <td>5</td>
    <td>avg_cashbk_per_order</td>
  </tr>
</table>

</details>



```python

```
