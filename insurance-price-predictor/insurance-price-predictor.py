import pandas as pd
import numpy as np

# Load data
data = pd.read_csv("insurance.csv")

# Features
numerical_features = ['age', 'bmi', 'children']
categorical_features  = ['sex','smoker','region']

# One-hot encoding
data = pd.get_dummies(data, columns=categorical_features, drop_first=True)

# Split X and y
X = data.drop('charges', axis=1)
y = data['charges']

# 🔥 Log transform target (VERY IMPORTANT)
y = np.log1p(y)

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
from xgboost import XGBRegressor

model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=4,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred_log = model.predict(X_test)

# Convert back to actual values
y_pred = np.expm1(y_pred_log)
y_actual = np.expm1(y_test)

# Evaluate
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_actual, y_pred)
print("MAE:", mae)



# New input
new_set = pd.DataFrame({
    'age' : [54],
    'sex':['female'],
    'bmi':[47.41],
    'children':[0],
    'smoker':['yes'],
    'region':['southeast']
})

# Apply same encoding
new_set = pd.get_dummies(new_set)

# Align columns
new_set = new_set.reindex(columns=X.columns, fill_value=0)

# Predict (log scale)
pred_log = model.predict(new_set)

# Convert back
pred_actual = np.expm1(pred_log)

print("Predicted Charges:", pred_actual[0])