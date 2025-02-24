import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
dataset_path = "Speed Dating Data.csv"
df = pd.read_csv(dataset_path, encoding="latin1")

# Selecting features based on correlation analysis
selected_features = ['fun3_3', 'intel3_3', 'amb3_3', 'sinc3_3']  # Most correlated predictors of attractiveness

df = df.dropna(subset=selected_features + ['attr3_3'])

# Define target variable
target = 'attr3_3'  # Predicting attractiveness
X = df[selected_features]
y = df[target]

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizing features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a regression model using selected features
regressor = LinearRegression()
regressor.fit(X_train_scaled, y_train)
y_pred = regressor.predict(X_test_scaled)

# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R-squared Score: {r2:.2f}")

# Feature Importance Plot
feature_importance = pd.Series(regressor.coef_, index=selected_features)
plt.figure(figsize=(10, 6))
feature_importance.plot(kind='barh', color='royalblue')
plt.title('Feature Importance in Predicting Attractiveness')
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.savefig("feature_importance.png", bbox_inches='tight', dpi=300)
plt.show()

# Gender-based Preference Analysis
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['gender'], y=df['attr3_3'])
plt.title('Attractiveness Ratings by Gender')
plt.xlabel('Gender (0 = Male, 1 = Female)')
plt.ylabel('Attractiveness Score')
plt.savefig("gender_attractiveness.png", bbox_inches='tight', dpi=300)
plt.show()

# Ethnic Group Interaction Analysis
ethnicity_matrix = df.pivot_table(index='race', columns='race_o', values='match', aggfunc='mean')
plt.figure(figsize=(8, 6))
sns.heatmap(ethnicity_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Match Likelihood Between Ethnic Groups')
plt.xlabel('Rated Ethnicity')
plt.ylabel('Rater Ethnicity')
plt.savefig("ethnicity_interactions.png", bbox_inches='tight', dpi=300)
plt.show()

print("Analysis complete. Check visualizations for insights.")