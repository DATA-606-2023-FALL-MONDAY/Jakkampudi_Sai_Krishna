# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
# from sklearn.model_selection import GridSearchCV
import streamlit as st
import joblib

# Load the data
data = pd.read_excel(r"C:\Users\saikr\Desktop\DATA-606\Version_4\file-539825604(4)\xgApp/E Commerce Dataset.xlsx",
                     sheet_name='E Comm')

data = data.drop(columns=['CustomerID'])

# Select only the numerical columns
numerical_columns = ["Tenure", "WarehouseToHome", "HourSpendOnApp", "OrderAmountHikeFromlastYear", "CouponUsed",
                     "OrderCount", "DaySinceLastOrder"]

# Calculate the median for each numerical column
median_values = data[numerical_columns].median()

# Fill missing/null values with their respective median values
data[numerical_columns] = data[numerical_columns].fillna(median_values)

# Encode categorical variables
label_encoders = {}
categorical_cols = ['PreferredLoginDevice', 'PreferredPaymentMode', 'Gender', 'PreferedOrderCat', 'MaritalStatus']
for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Define the columns to be one-hot encoded and scaled
categorical_columns = ['PreferredLoginDevice', 'PreferredPaymentMode', 'Gender', 'PreferedOrderCat', 'MaritalStatus']
numeric_columns = ['Tenure', 'CityTier', 'WarehouseToHome', 'HourSpendOnApp', 'NumberOfDeviceRegistered',
                   'SatisfactionScore', 'NumberOfAddress', 'Complain', 'OrderAmountHikeFromlastYear',
                   'CouponUsed', 'OrderCount', 'DaySinceLastOrder', 'CashbackAmount']

# Create transformers for one-hot encoding and standard scaling
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(drop='first'))  # 'drop' to avoid multicollinearity
])

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

# Create a column transformer to apply transformations to the appropriate columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_columns),
        ('cat', categorical_transformer, categorical_columns)
    ])

# Create a pipeline that applies preprocessing and scaling
pipeline = Pipeline(steps=[('preprocessor', preprocessor)])

# Fit and transform the dataset
data_scaled = pipeline.fit_transform(data)

# Convert the scaled data back to a DataFrame with appropriate column names
categorical_columns_encoded = pipeline.named_steps['preprocessor'].named_transformers_['cat'].named_steps[
    'onehot'].get_feature_names(input_features=categorical_columns)
column_names = list(numeric_columns) + list(categorical_columns_encoded)
data_scaled_df = pd.DataFrame(data_scaled, columns=column_names)

# adding the churn column
churn_column = data['Churn']
data_scaled_df = data_scaled_df.join(churn_column)

# Define X and y
X = data.drop(columns=['Churn'])
y = data['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE to balance the training data
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Define the XGBoost classifier
xgb_classifier = XGBClassifier(random_state=42)

# Define hyperparameter grid for tuning
# param_grid = {
#   'n_estimators': [100, 200, 300],
#  'max_depth': [3, 4, 5],
# 'learning_rate': [0.1, 0.01, 0.001]
# }

# Initialize GridSearchCV
# grid_search = GridSearchCV(xgb_classifier, param_grid, cv=5, scoring='roc_auc')

# Fit the model to the resampled training data
# grid_search.fit(X_train_resampled, y_train_resampled)

# Get the best model after hyperparameter tuning
# best_xgb_model = grid_search.best_estimator_


# Load the saved model
model_filename = r'C:\Users\saikr\Desktop\DATA-606\Version_4\file-539825604(4)\xgApp/decision_model.pkl'
clf = joblib.load(model_filename)

# Create a Streamlit app
st.title('Churn Prediction App')

# Define input fields
tenure = st.slider('Tenure', 0, 30, 15)
login_device = st.selectbox('Preferred Login Device', label_encoders['PreferredLoginDevice'].classes_)
city_tier = st.slider('City Tier', 1, 3, 2)
warehouse_to_home = st.slider('Warehouse to Home', 0, 30, 15)
payment_mode = st.selectbox('Preferred Payment Mode', label_encoders['PreferredPaymentMode'].classes_)
gender = st.selectbox('Gender', label_encoders['Gender'].classes_)
hour_spend_on_app = st.slider('Hour Spend On App', 1, 5, 3)
num_devices_registered = st.slider('Number Of Devices Registered', 1, 5, 3)
order_cat = st.selectbox('Preferred Order Category', label_encoders['PreferedOrderCat'].classes_)
satisfaction_score = st.slider('Satisfaction Score', 1, 5, 3)
marital_status = st.selectbox('Marital Status', label_encoders['MaritalStatus'].classes_)
num_address = st.slider('Number Of Address', 1, 10, 5)
complain = st.radio('Complain', [0, 1])
order_amount_hike = st.slider('Order Amount Hike From Last Year', 0, 50, 25)
coupon_used = st.slider('Coupon Used', 0, 10, 5)
order_count = st.slider('Order Count', 0, 10, 5)
days_since_last_order = st.slider('Days Since Last Order', 0, 30, 15)
cashback_amount = st.slider('Cashback Amount', 0, 200, 100)

# Create a feature vector
input_data = {
    'Tenure': [tenure],
    'PreferredLoginDevice': [label_encoders['PreferredLoginDevice'].transform([login_device])[0]],
    'CityTier': [city_tier],
    'WarehouseToHome': [warehouse_to_home],
    'PreferredPaymentMode': [label_encoders['PreferredPaymentMode'].transform([payment_mode])[0]],
    'Gender': [label_encoders['Gender'].transform([gender])[0]],
    'HourSpendOnApp': [hour_spend_on_app],
    'NumberOfDeviceRegistered': [num_devices_registered],
    'PreferedOrderCat': [label_encoders['PreferedOrderCat'].transform([order_cat])[0]],
    'SatisfactionScore': [satisfaction_score],
    'MaritalStatus': [label_encoders['MaritalStatus'].transform([marital_status])[0]],
    'NumberOfAddress': [num_address],
    'Complain': [complain],
    'OrderAmountHikeFromlastYear': [order_amount_hike],
    'CouponUsed': [coupon_used],
    'OrderCount': [order_count],
    'DaySinceLastOrder': [days_since_last_order],
    'CashbackAmount': [cashback_amount]
}

prediction_button = st.button('Predict Churn')

# Check if the button is clicked
if prediction_button:
    # Make predictions
    prediction = clf.predict(pd.DataFrame(input_data))

    # Display the prediction
    if prediction[0] == 1:
        st.write('Churn Prediction: Churn')
    else:
        st.write('Churn Prediction: No Churn')
