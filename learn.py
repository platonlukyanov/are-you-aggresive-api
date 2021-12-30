from ml_helpers import prepare_clf, prepare_data
import joblib


if __name__ == '__main__':
    X, y, vectoriser = prepare_data()
    clf = prepare_clf(X, y)
    joblib.dump(clf, "pickles/model.pkl")
    joblib.dump(vectoriser, 'pickles/vectoriser.pkl')

