import joblib

clf = joblib.load('pickles/model.pkl')
vectoriser = joblib.load('pickles/vectoriser.pkl')


def get_ml_prediction(text: str) -> str:
    return clf.predict(vectoriser.transform([text]))[0]
