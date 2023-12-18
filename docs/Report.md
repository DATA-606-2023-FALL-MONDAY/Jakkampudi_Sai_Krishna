## DATA_606_CAPSTONE PROJECT

#### Professor: Dr. Chaojie Wang

#### Project Title:E-Commerce Customer Churn Prediction

Prepared for UMBC Data Science Master Degree Capstone under Guidance of Prof Dr Chaojie (Jay) Wang

#### Student Name: Sai Krishna Jakkampudi

#### Semester: FALL 2023


**PowerPoint presentation file:** https://github.com/DATA-606-2023-FALL-MONDAY/Jakkampudi_Sai_Krishna/blob/9246a4401af0498450687ffa05500d7455d703fd/docs/E_Commerce_Customer_Churn_Prediction.pptx

**Link to your YouTube video:** https://youtu.be/fWzjwLQ3Sfg

**GitHub:** https://github.com/saikrishna-jakkampudi

#### Background

*Customer churn analysis involves studying customer behavior to identify patterns and factors that contribute to customers discontinuing their relationship with a business. It aims to predict which customers are likely to churn in the future so that businesses can take preventive actions to retain them. This analysis is crucial across industries such as telecommunications, subscription services, e-commerce, and more. This topic matters in several ways. For instance, it impacts the revenue of a company. Customer churn has a significant impact on a company's revenue. When customers stop doing business with a company, it directly results in a loss of revenue.*

*These lost sales and transactions can accumulate quickly, especially for businesses with a large customer base. Furthermore, reducing churn can provide a competitive advantage in crowded and saturated markets. In competitive industries, customers have numerous options, making it easier for them to switch to a competitor if they are dissatisfied. By effectively managing churn, a business can differentiate itself from competitors and enhance its reputation for customer satisfaction. Customers are more likely to stay loyal to a brand that consistently meets their needs and expectations. This loyalty can translate into increased market share and a stronger position in the industry.*

## DATA

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


- **Dependent and independent variables**

Customer Churn is the most effective target variable for creating machine-learning models from the dataset. It is a binary variable that machine learning systems can classify with ease. Additionally, there is plenty of information and study on the subject because customer turnover is a regular and significant issue for organizations to address. On the other hand, for predictor variables, I used all the variables except customerID.

### EXPLORATORY DATA ANALYSIS (EDA)

#### Summary Stastics of Data

*The summary statistics above offer insights into various aspects of the dataset. From the summary, approximately 16.84% of the customers in the dataset have churned, indicating a class imbalance. The 'Tenure' feature suggests that the average customer has been associated with the company for approximately 10.19 units of time, with a wide range from 0 to 61 units. The 'CityTier' variable indicates that most customers are in CityTier 1, but there are others in Tier 2 and Tier 3 as well. 'WarehouseToHome' shows that the average distance from the warehouse to a customer's home is around 15.64 units. Customers tend to spend an average of 2.93 hours on the app, with 'NumberOfDeviceRegistered' averaging around 3.69 devices.*

*'SatisfactionScore' is generally moderate, with an average of 3.07. 'NumberOfAddress' reveals that the average customer has 4.21 addresses, but there is significant variability with a maximum of 22. The 'Complain' variable indicates that around 28.49% of customers have registered a complaint. 'OrderAmountHikeFromlastYear' suggests that the average increase in order amount from the previous year is approximately 15.71 units. Customers use an average of 1.75 coupons and place an average of 3.01 orders. 'DaySinceLastOrder' shows that the average time since the last order is around 4.54 units. Lastly, 'CashbackAmount' indicates that the average cashback amount received by customers is approximately 177.22 units, with some variability.*

![Summary_Stastics.jpg](attachment:Summary_Stastics.jpg)

#### Dealing  Missing Values

*There are missing values in several variables within the dataset as shown above. The variables with missing values and their respective counts of missing data include: "Tenure" with 264 missing values, "WarehouseToHome" with 251 missing values, "HourSpendOnApp" with 255 missing values, "OrderAmountHikeFromlastYear" with 265 missing values, "CouponUsed" with 256 missing values, "OrderCount" with 258 missing values, and "DaySinceLastOrder" with 307 missing values.* 

*Deleting the rows with missing values would lead a substantial oss of the dataset, therefore, I have filled the the missing values with median before proceeding with the model training.*

![Missing_Values.jpg](attachment:Missing_Values.jpg)

#### Churn Distribution

*From the bar plot, there were more not-churned customers compared to churned customers. Furthermore, the predominance of "Not Churned" customers suggests that a substantial portion of the customer base has remained loyal or has not yet experienced churn. This insight is valuable for businesses as it indicates areas of strength in customer retention. However, it also highlights the need for strategies to reduce churn and retain a larger share of customers over time.*

![Chrun_Distribution.jpg](attachment:Chrun_Distribution.jpg)

#### Preffered Login Device

*Furthermore, I wanted to understand how preferred login device (PreferredLoginDevice) influence customer churn. it is evident that Mobile phone login users had the highest numbers of both churn and not churn customers. This was followed by Computer login users and then phone login users. Moreover, Mobile phone login users had the highest number of not-churn and churn customers followed by computer login users the phone login users who had the list number of not-churn users. This implies that a significant portion of customers prefer to use their mobile phones to log in. The fact that phone users have both the highest number of churn and not-churn customers suggests that this group is diverse, with some customers staying loyal and others churning.*

![Login_Device_Influence.jpg](attachment:Login_Device_Influence.jpg)

#### Customer Satisifaction Score

*Based on figure below, it is evident that a Satisfactory score of customer on service of 3 was the highest count. This was followed by a satisfactory score of 1, the 5 and 4 and finally satisfactory score of 2 which had the least number of counts.*

![Satisfaction_Score.jpg](attachment:Satisfaction_Score.jpg)

#### Order Amount Hike By City Tier

*It's evident that City Tier 1 exhibited the most substantial increase in average order amount, showcasing robust growth in consumer spending. This top-tier position could be attributed to factors such as higher average incomes, greater access to premium products and services, or a more developed retail environment, all of which may have encouraged residents in City Tier 1 to spend more. Following City Tier 1, City Tier 3 experienced a moderate increase in average order amount, indicating relatively steady or modest growth in consumer spending, which might be typical for smaller towns or less economically vibrant regions.*

*In contrast, City Tier 2 lagged behind, showing the lowest growth in the average order amount, suggesting that customers in medium-sized cities might not have experienced as significant a boost in their purchasing behavior. Understanding these disparities among different city tiers is important for businesses to tailor their marketing strategies and product offerings effectively, ensuring they meet the distinct needs and preferences of consumers in each tier.*

![Order_Hike_City_Tier.jpg](attachment:Order_Hike_City_Tier.jpg)

#### Distribution of Complaints

*Comparatively, we see that retained customers have more complaints compared to the churned customers. This is expected because retained customers are likely to face varying challenges with the services. Retained customers, who have an ongoing relationship with a company, are more engaged over time and thus more likely to encounter occasional issues. Their higher expectations, shaped by previous positive experiences, lead them to voice concerns when expectations aren't met. Companies also actively seek feedback from retained customers to ensure their continued satisfaction, contributing to the higher complaint count.*

![Customer_Complaint.jpg](attachment:Customer_Complaint.jpg)

#### Relationship Between Tenure and Churn Rate

*The correlation between a higher churn rate and lower customer tenure is a crucial insight in customer retention. When customers have a shorter tenure, it means they haven't been with the company or using its services for an extended period. This limited history with the company can result in a higher likelihood of churn for several reasons.*

![Tenure_Churn_Rate.jpg](attachment:Tenure_Churn_Rate.jpg)

#### Cashback for Customers

*The box plot you sent me shows the distribution of cashback amounts for customers. The cashback amount is likely some kind of financial reward or incentive given to customers for making purchases or engaging with a particular company or service. Majority of the customers requests a cashback of $163.*

![Cashback_Distribution.jpg](attachment:Cashback_Distribution.jpg)

#### Heat_Map

*it is evident that most variables are correlated with a correlation value above 0.5. There is a weak correlation between number of addresses (NumberOfAddress) and customer churn.*

![Heat_Map.jpg](attachment:Heat_Map.jpg)

## Machine Learning Models

#### SMOTE ANALYSIS

*As the data is imbalanced i have implemented one of the well recognized technique smote analysis to make the data set balanced for more accurate results.*

![SMOTE.jpg](attachment:SMOTE.jpg)

#### Logistic Regression

*Achieves a decent accuracy of 80.94%, with balanced precision and recall. The F1-Score and ROC-AUC score are also respectable but not the highest among the models.*

*Model's performance in predicting whether or not a client would churn—or cancel their subscription—is displayed in the confusion matrix.*

*Above left and below right: These are the right guesses: It was correctly projected that 747 customers who did not churn would not, while 770 customers who did churn were expected to churn.*

*Bottom left and upper right: The inaccurate forecasts are as follows: faulty negative predictions meant that 164 churners would not churn, and faulty positive predictions meant that 192 non-churners would churn.*

*With many more accurate forecasts than inaccurate ones, the model appears to be performing well overall. There is, nevertheless, still need for development, particularly in lowering the quantity of false negatives (churners that are incorrectly classified).*


![Logistic_Regression.jpg](attachment:Logistic_Regression.jpg)

#### XGboost

*Delivers an outstanding accuracy of 98.56%, with high precision and recall for both classes. It boasts the highest F1-Score and ROC-AUC score among the models.*

*Upper left and lower right: These are the accurate forecasts. While 931 individuals predicted that "Churn" would actually churn, 923 predicted that "Not Churn" would truly not churn.*

*Top right and bottom left: These are the wrong guesses. False positives: 16 individuals predicted that "Churn" actually didn't churn, while 3 people anticipated that "Not Churn" actually did churn.*


![Xgboost.jpg](attachment:Xgboost.jpg)

#### Random Forest

*Upper left and lower right: These are the accurate forecasts. 912 persons with confusion were accurately predicted to be confused, whereas 27 persons in the "Not Confused" category were correctly projected to be not confused.*

*Top right and bottom left: These are the wrong guesses. erroneous negative predictions were made for 11 persons who were confused, whereas erroneous positive predictions were made for 27 people who were not confused.*


![Ranodm_Forest.jpg](attachment:Ranodm_Forest.jpg)

#### Comparison of Models

*Performance Ranking: XGBoost takes the top spot with the highest ROC-AUC score, followed by Random Forest and Naive Bayes. Logistic Regression lands at the bottom with the lowest score.*

*Accuracy Variation: The models' accuracy scores range from around 0.75 to 0.9, indicating moderate to good performance overall. XGBoost again leads with the highest accuracy, while Logistic Regression again shows the lowest.*

*Metric Focus: While ROC-AUC focuses on general classification performance, the graph also includes F1-Score and Accuracy as additional metrics for specific aspects like class balance and overall correctness.*

![Comaprison.jpg](attachment:Comaprison.jpg)

####  App Using Streamlit

![Churn_App1.jpg](attachment:Churn_App1.jpg)

![Churn_App2.jpg](attachment:Churn_App2.jpg)

#### Conlcusion

*Among the algorithms tested, XGBoost and Random Forest stand out as top performers with the highest accuracy, F1-Scores, and ROC-AUC scores. They are well-suited for this classification task and are recommended for predicting customer churn.*

*Decision Tree also performs excellently, while Logistic Regression and k-NN offer reasonable results. Naïve Bayes, however, lags behind in terms of accuracy and overall performance. Further optimization, such as hyperparameter tuning, can potentially enhance the model's predictive capabilities, particularly for XGBoost.*

#### Reference


*Chinnu, P. J., & Paul, P. M. (2020). Customer Churn Prediction: A Survey. International Journal of Advanced Research in Computer Science, 8(5), 2178-2181.*

*Kumar, A. (Year, Month Day of publication). A complete guide to building Streamlit data web apps with code examples. Medium. Retrieved from https://medium.com/@avikumart_/a-complete-guide-to-building-streamlit-data-web-apps-with-code-examples-6cc1e42b2397*

*E-commerce Customer Churn Analysis and Prediction. Kaggle. Retrieved from https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction*



```python

```
