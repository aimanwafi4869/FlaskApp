import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

class ScikitLearn:
    
    def __init__(self):
        # self.saved_path = 'model_path_location'
        # self.model = tf.saved_model.load(self.saved_path)
        # self.predict = self.model.signatures["serving_default"]
        try:
            model = joblib.load('model/random_forest_model.pkl')
            self.model = model
        except:
            self.createModel()


    def createModel(self):
        # Initialize the Random Forest Classifier

        rf_classifier = RandomForestClassifier(max_depth=9, 
                                    max_features="log2", 
                                    max_leaf_nodes=9, 
                                    n_estimators=25)

        self.model = rf_classifier
        
        self.defaultTrain()
        joblib.dump(self.model, 'model/random_forest_model.pkl')
    
    def defaultTrain(self):
        dataset = pd.read_csv('dataset/dataset(Hackathon).csv')
        xData = dataset.iloc[:,1:]
        yData = dataset.iloc[:,0:1]

        # Split data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(xData, yData, test_size=0.3, random_state=100)
        self.model.fit(X_train, y_train)

    def accuracy(self):
        dataset = pd.read_csv('dataset/dataset(Hackathon).csv')
        # print(dataset.head())
        xData = dataset.iloc[:,1:]
        yData = dataset.iloc[:,0:1]
        X_train, X_test, y_train, y_test = train_test_split(xData, yData, test_size=0.3, random_state=100)
        y_pred = self.model.predict(X_test)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("\nClassification Report:\n", classification_report(y_test, y_pred))

    def train(self, xTrain, yTrain):
        self.model.fit(xTrain, yTrain)
    
    
    def predict(self, data):
        return self.model.predict(data)[0]