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


```python
!pip install sweetviz
```

    Collecting sweetviz
      Downloading sweetviz-2.2.1-py3-none-any.whl (15.1 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m15.1/15.1 MB[0m [31m66.0 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: pandas!=1.0.0,!=1.0.1,!=1.0.2,>=0.25.3 in /usr/local/lib/python3.10/dist-packages (from sweetviz) (1.5.3)
    Requirement already satisfied: numpy>=1.16.0 in /usr/local/lib/python3.10/dist-packages (from sweetviz) (1.23.5)
    Requirement already satisfied: matplotlib>=3.1.3 in /usr/local/lib/python3.10/dist-packages (from sweetviz) (3.7.1)
    Requirement already satisfied: tqdm>=4.43.0 in /usr/local/lib/python3.10/dist-packages (from sweetviz) (4.66.1)
    Requirement already satisfied: scipy>=1.3.2 in /usr/local/lib/python3.10/dist-packages (from sweetviz) (1.11.2)
    Requirement already satisfied: jinja2>=2.11.1 in /usr/local/lib/python3.10/dist-packages (from sweetviz) (3.1.2)
    Requirement already satisfied: importlib-resources>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from sweetviz) (6.0.1)
    Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2>=2.11.1->sweetviz) (2.1.3)
    Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.1.3->sweetviz) (1.1.0)
    Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.1.3->sweetviz) (0.11.0)
    Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.1.3->sweetviz) (4.42.1)
    Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.1.3->sweetviz) (1.4.5)
    Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.1.3->sweetviz) (23.1)
    Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.1.3->sweetviz) (9.4.0)
    Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.1.3->sweetviz) (3.1.1)
    Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.1.3->sweetviz) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas!=1.0.0,!=1.0.1,!=1.0.2,>=0.25.3->sweetviz) (2023.3.post1)
    Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.7->matplotlib>=3.1.3->sweetviz) (1.16.0)
    Installing collected packages: sweetviz
    Successfully installed sweetviz-2.2.1



```python
import pandas as pd
import sweetviz as sv
```


```python
# GitHub URL of the Excel file
github_url = 'https://github.com/DATA-606-2023-FALL-MONDAY/Jakkampudi_Sai_Krishna/raw/main/data/E%20Commerce%20Dataset.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(github_url)

# Generate EDA report with Sweetviz
eda_report = sv.analyze(df)

# Display the EDA report in the Jupyter Notebook
eda_report.show_notebook(layout='vertical', w=880, h=700, scale=0.8)
```


                                                 |          | [  0%]   00:00 -> (? left)



```python
from google.colab import drive
drive.mount('/content/drive')
```

# New Section


```python
%cd /content/drive/My Drive/Colab Notebooks

```


```python
!ls
```


```python
!jupyter nbconvert --to markdown Draft_Proposal.ipynb

```
