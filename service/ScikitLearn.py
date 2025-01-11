import pandas as pd
import numpy as np
from sklearn.ensemble import *
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
import joblib
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

class ScikitLearn:

    # Initialize the MinMaxScaler
    global scaler
    
    def __init__(self, modelType, dataset):
        try:
            self.modelType = modelType
            self.dataset = dataset
            if modelType == 'rf':
                model = joblib.load('model/random_forest_model.pkl')
            elif modelType == 'linearRegression':
                model = joblib.load('model/linear_regression_model.pkl')
            self.model = model
        except:
            self.createModel()

    def createModel(self):
        if self.modelType == 'rf': 
            model = RandomForestClassifier(max_depth=9, 
                                        max_features="log2",
                                        max_leaf_nodes=9, 
                                        n_estimators=25)

            self.model = model
            self.defaultTrain()
            joblib.dump(self.model, 'model/random_forest_model.pkl')
        elif self.modelType == 'linearRegression':
            model = LinearRegression()
            self.model = model
            self.defaultTrain()
            joblib.dump(self.model, 'model/LinearRegression_model.pkl')
    
    def defaultTrain(self):
        dataset = pd.read_csv(self.dataset)
        dataset['date'] = pd.to_datetime(dataset['date'])
        dataset['dayStart'] = (dataset['date'] - dataset['date'].min()).dt.days
        dataset['normalizedValue'] = scaler.fit_transform(dataset[['landings']])


        xData = dataset[['dayStart']]
        yData = dataset['normalizedValue']
        print(xData)
        print(yData)

        # Split data into training and test sets
        self.model.fit(xData, yData)

        # Predict future values
        # Predict for a specific future date
        # future_date = '2024-01-01'
        # futureDays = (pd.to_datetime(future_date) - dataset['date'].min()).days

        # futureValue = self.model.predict([[futureDays]])
        # print(f'The future value is {futureValue}')
        X_train, X_test, y_train, y_test = train_test_split(xData, yData, test_size=0.3)
        y_pred = self.model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print()
        print("Model Performance Metrics:")
        print(f"Mean Squared Error (MSE): {mse:.2f}")
        print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
        print(f"Mean Absolute Error (MAE): {mae:.2f}")
        print(f"R-squared (R²): {r2:.2f}")
        print()

    def accuracy(self):
        dataset = pd.read_csv(self.dataset)

        dataset['date'] = pd.to_datetime(dataset['date'])
        dataset['dayStart'] = (dataset['date'] - dataset['date'].min()).dt.days
        dataset['normalizedValue'] = scaler.fit_transform(dataset[['landings']])

        xData = dataset[['dayStart']]
        yData = dataset['normalizedValue']

        X_train, X_test, y_train, y_test = train_test_split(xData, yData, test_size=0.3)
        y_pred = self.model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print()

        print("Model Performance Metrics:")
        print(f"Mean Squared Error (MSE): {mse:.2f}")
        print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
        print(f"Mean Absolute Error (MAE): {mae:.2f}")
        print(f"R-squared (R²): {r2:.2f}")
        print()
        return f"""
Model Performance Metrics
Mean Squared Error (MSE): {mse:.2f}
Root Mean Squared Error (RMSE): {rmse:.2f}
Mean Absolute Error (MAE): {mae:.2f}
R-squared (R²): {r2:.2f}\n\n"""

    def train(self, xTrain, yTrain):
        self.model.fit(xTrain, yTrain)
    
    
    def predict(self, date):
        dataset = pd.read_csv(self.dataset)
        dataset['date'] = pd.to_datetime(dataset['date'])
        future_day = (pd.to_datetime(date) - dataset['date'].min()).days
        futureValueNormalised = self.model.predict([[future_day]])
        futureValue = scaler.inverse_transform([futureValueNormalised])
        print(f'The future value is {futureValue}')
        return futureValue
