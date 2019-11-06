import pandas as pd
from analyse import Analyzer
import seaborn as sns
import matplotlib.pyplot as plt

from data_operations import drop_unnecessary_columns, parametrize_columns, categorize_columns

df = pd.read_csv('new_students_data.csv')
df = drop_unnecessary_columns(df)
df = parametrize_columns(df)

# Start analysing
analyzer = Analyzer(df)
analyzer.analyse_bool_words_columns()
print(analyzer.bool_words_results)

df = categorize_columns(df)

print(df.dtypes)

features = columns = [
    'Liczba brakujacych przedmiotow',
    'Brakujace ECTS',
    'ECTS uznane w bieżącym semstrze',
    'Suma zdobytych ECTS',
    # 'Liczba prac dyplomowych'
]

labels = df['Status']
data = df[features]

from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split( data, labels, test_size=0.20, random_state=10 )


from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

gnb = GaussianNB()
pred = gnb.fit(data_train, target_train).predict(data_test)
print("Naive-Bayes accuracy : ", accuracy_score(target_test, pred, normalize=True))


# from sklearn.svm import LinearSVC
# from sklearn.metrics import accuracy_score
#
# svc_model = LinearSVC(random_state=0)
# pred = svc_model.fit(data_train, target_train).predict(data_test)
# print("LinearSVC accuracy : ", accuracy_score(target_test, pred, normalize=True))


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


neigh = KNeighborsClassifier(n_neighbors=3, weights='distance')
neigh.fit(data_train, target_train)
pred = neigh.predict(data_test)
print("KNeighbors accuracy score : ", accuracy_score(target_test, pred))


from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(100, 50, 20))
mlp.fit(data_train, target_train)
predictions = mlp.predict(data_test)
print(predictions)


from joblib import dump, load
dump(mlp, 'mlp.joblib')
mlp = load('mlp.joblib')
pred = mlp.predict([[1, 4, 26]])
print(pred)


from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(target_test, predictions))
print(classification_report(target_test,predictions))

from pandas_ml import ConfusionMatrix
cm = ConfusionMatrix(target_test, predictions)
cm.plot()
plt.show()