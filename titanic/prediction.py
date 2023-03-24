import pickle

def getPrediction(pclass, sex, age, sibsp, parch, fare, C, Q, S):
    model = pickle.load(open('titanic.pkl', 'rb'))
    scaled = pickle.load(open('scaler.pkl', 'rb'))
    transform = scaled.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]])
    prediction = model.predict(transform)

    return 'Not Survived' if prediction == 0 else 'Survived' if prediction == 1 else 'error'

