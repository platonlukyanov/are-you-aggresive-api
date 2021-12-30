from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import joblib


def prepare_data():
    df = joblib.load("pickles/df.pkl")
    dataset = df.values
    corpus = [text for text, intent in dataset]
    y = [1 if intent == 'агрессия' else 0 for text, intent in dataset]
    vectoriser = TfidfVectorizer(analyzer='char_wb', ngram_range=(3, 4), use_idf=False)
    X = vectoriser.fit_transform(corpus)
    return X, y, vectoriser


def prepare_clf(X, y):
    clf = LinearSVC()
    clf.fit(X, y)
    return clf


def get_cross_score(clf, X, y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    cross_score = cross_val_score(clf, X_train, Y_train, cv=5).mean()
    return cross_score


X, y, _ = prepare_data()
clf = prepare_clf(X, y)
get_cross_score(clf, X, y)
