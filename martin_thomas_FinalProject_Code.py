import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

housing = fetch_california_housing(as_frame=True)
housing = housing.frame
housing.head()

housing.hist(bins=50, figsize=(12, 8))
plt.show()

housing.plot(kind="scatter", x="Longitude", y="Latitude", c="MedHouseVal", cmap="jet", colorbar=True, legend=True,
             sharex=False, figsize=(10, 7), s=housing['Population'] / 100, label="population", alpha=0.7)
plt.title("Geographical Distribution of Housing")
plt.savefig('Geographical Distribution of Housing.png')
plt.show()

attributes = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'MedHouseVal']
scatter_matrix(housing[attributes], figsize=(12, 8))
plt.suptitle("Scatter Matrix of Selected Attributes")
plt.savefig('Scatter Matrix of Selected Attributes.png')
plt.show()

housing.plot(kind="scatter", x="MedInc", y="MedHouseVal")
plt.title("Median Income vs. Median House Value")
plt.savefig('Median Income vs. Median House Value.png')
plt.show()

corr = housing.corr()
print("Correlation with Median House Value:")
print(corr['MedHouseVal'].sort_values(ascending=True))

# Data Cleanup #1
print("Number of missing values in each column:")
print(housing.isna().sum())

# Data Cleanup #2
z_scores = np.abs((housing - housing.mean()) / housing.std())
outliers = (z_scores > 3).all(axis=1)
housing = housing[~outliers]

# Data Cleanup #3
housing['RoomsPerHousehold'] = housing['AveRooms'] / housing['AveOccup']

X = housing.iloc[:, :-1]
y = housing.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regression_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])
regression_pipeline.fit(X_train, y_train)

y_pred = regression_pipeline.predict(X_test)
print("R-squared score:", r2_score(y_test, y_pred))

# hyperparameter tuning
param_grid = {
    'regressor__fit_intercept': [True, False],
}

regression_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

grid_search = GridSearchCV(regression_pipeline, param_grid, cv=5, scoring='r2', n_jobs=-1)

grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
print("Best Hyperparameters:", best_params)

best_model = grid_search.best_estimator_

y_pred_tuned = best_model.predict(X_test)
print("R-squared score after hyperparameter tuning:", r2_score(y_test, y_pred_tuned))

# second regression estimator
forest_reg_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))  # Adjust hyperparameters as needed
])
forest_reg_pipeline.fit(X_train, y_train)

# Make predictions on the test set and evaluate the model
y_pred_forest = forest_reg_pipeline.predict(X_test)
print("R-squared score (Random Forest):", r2_score(y_test, y_pred_forest))

# Compare the performance of Linear Regression and RandomForestRegressor
print("R-squared score (Linear Regression):", r2_score(y_test, y_pred))
print("R-squared score (Random Forest):", r2_score(y_test, y_pred_forest))
