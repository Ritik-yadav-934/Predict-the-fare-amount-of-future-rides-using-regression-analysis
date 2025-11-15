import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Load data
df = pd.read_csv('uber.csv')


# Data preprocessing
print("Loading and preprocessing data...")

# Remove rows with missing values
df = df.dropna()

# Convert pickup_datetime to datetime and extract features
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['pickup_month'] = df['pickup_datetime'].dt.month
df['pickup_day'] = df['pickup_datetime'].dt.day
df['pickup_hour'] = df['pickup_datetime'].dt.hour

# Select features and target
X = df[['pickup_month', 'pickup_day', 'pickup_hour', 'passenger_count', 
         'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']]
y = df['fare_amount']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
print("Training Random Forest model...")
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)

# Evaluate
train_score = model.score(X_train_scaled, y_train)
test_score = model.score(X_test_scaled, y_test)
print(f"Train R² Score: {train_score:.4f}")
print(f"Test R² Score: {test_score:.4f}")

# Save model and scaler
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/uber_fare_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
print("Model saved successfully!")
