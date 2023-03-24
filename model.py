import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv('titanic.csv', index_col=0)

# selecting the features we need
df = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Survived']]

# encoding the column to a numberic value
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# converting the Age column to numberic type
df['Age'] = pd.to_numeric(df.Age)

# filling the null values
df['Age'] = df.Age.fillna(np.mean(df.Age))

# creating additional features from Embarked columns after converting to dummy variables
dummies = pd.get_dummies(df.Embarked)
df = pd.concat([df, dummies], axis=1)
df.drop(['Embarked'], axis=1, inplace=True)

X = df.drop(['Survived'], axis=1)
y = df['Survived']

# scaling the features
scaler = MinMaxScaler(feature_range=(0,1))
X_scaled = scaler.fit_transform(X)

model = LogisticRegression(C=1)
model.fit(X_scaled, y)

# saving model as a pickle
pickle.dump(model, open('titanic.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))
