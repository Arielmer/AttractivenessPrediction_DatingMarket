import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset (assuming speed_dating.csv is the dataset)
df = pd.read_csv("speed_dating.csv")

# Selecting relevant features for attractiveness prediction
features = ['sincerity', 'intelligence', 'fun', 'ambition', 'shared_interests', 'age']
target = 'attractiveness'

# Handling missing values
df = df.dropna(subset=features + [target])

# Splitting dataset
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizing features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Regression Model to Predict Attractiveness
regressor = LinearRegression()
regressor.fit(X_train_scaled, y_train)
y_pred = regressor.predict(X_test_scaled)

# Feature Importance Plot (using coefficients for regression)
feature_importance = pd.Series(regressor.coef_, index=features)
plt.figure(figsize=(10, 6))
feature_importance.plot(kind='barh', color='royalblue')
plt.title('Feature Importance in Predicting Attractiveness')
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.savefig("feature_importance.png", bbox_inches='tight', dpi=300)
plt.show()

# Gender-based Preference Analysis
gender_features = ['attractiveness', 'sincerity', 'fun', 'intelligence']
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['gender'], y=df['attractiveness'], data=df)
plt.title('Attractiveness Ratings by Gender')
plt.xlabel('Gender (0 = Male, 1 = Female)')
plt.ylabel('Attractiveness Score')
plt.savefig("gender_attractiveness.png", bbox_inches='tight', dpi=300)
plt.show()

# Ethnic Group Interaction Analysis
ethnicity_matrix = df.groupby(['ethnicity_1', 'ethnicity_2'])['match'].mean().unstack()
plt.figure(figsize=(8, 6))
sns.heatmap(ethnicity_matrix, annot=True, cmap='coolwarm')
plt.title('Match Likelihood Between Ethnic Groups')
plt.xlabel('Rated Ethnicity')
plt.ylabel('Rater Ethnicity')
plt.savefig("ethnicity_interactions.png", bbox_inches='tight', dpi=300)
plt.show()

print("Analysis complete. Check visualizations for insights.")
