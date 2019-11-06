import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction import FeatureHasher
import numpy as np

df = pd.read_csv('Adult_train.tab', sep='\t', skiprows=[1,2])
# print(df.head())
print(df.columns)
# print(df.describe)
# print(df.dtypes)
# print(df.count())
# print(df.isna().sum())
# print(df.isnull().sum())

y_train = df['y']
# print(y_train)
x_train = df.drop(columns=['y', 'education'])
# x_train = x_train.drop(['education'], axis=1)
# print(x_train.columns)

# print(x_train['workclass'].value_counts())
# print(x_train['relationship'].value_counts())
# print(x_train['race'].value_counts())
# print(x_train['native-country'].value_counts())
# print(x_train.columns)

# def get_one_hot_repr(data, colname):
#     ohe = OneHotEncoder()
#     result = ohe.fit_transform(data[colname].values.reshape(-1, 1)).toarray()
#     result = pd.DataFrame(result, columns=[colname + str(ohe.categories_[0][i]) for i in range(len(ohe.categories_[0]))])
#     return result
#
#
# def substitute_with_one_hot(data, colnames):
#     for colname in colnames:
#         one_hot_column = get_one_hot_repr(data, colname)
#         one_hot_column.fillna(0)
#         data = pd.concat([data, one_hot_column], axis=1)
#         del data[colname]
#     return data


columns = [ 'workclass',  'marital-status', 'occupation', 'relationship', 'race', 'sex',  'native-country']
columns_prefix = [ 'workclass_px',  'marital-status_px', 'occupation_px', 'relationship_px', 'race_px', 'sex_px',  'native-country_px']

# columns_other = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']

x_train_onehot = pd.get_dummies(x_train, prefix=columns_prefix, columns=columns)
# print(x_train.head())
print(x_train.shape)

fh = FeatureHasher(n_features=8, input_type='string')
sp = fh.fit_transform(x_train['native-country'])
df1 = pd.DataFrame(sp.toarray(), columns=['country_1', 'country_2','country_3','country_4','country_5','country_16', 'country_7','country_8'])
x_train_hashed = pd.concat([df1, x_train.drop(columns=['native-country'])], axis=1)


print('x_train\n', x_train.columns)
print('x_train_hashed\n', x_train_hashed.columns)
# print('x_train_onehot\n', x_train_onehot.columns)




from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(x_train_onehot, y_train, test_size=0.20, random_state=10 )


from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

svc_model = LinearSVC(random_state=0, max_iter=1000)
pred_test = svc_model.fit(data_train, target_train).predict(data_test)
pred_train = svc_model.fit(data_train, target_train).predict(data_train)
print("LinearSVC accuracy_score: \n", accuracy_score(target_test, pred_test, normalize=True))
print("LinearSVC confusion_matrix: \n", confusion_matrix(target_test, pred_test))
print("LinearSVC classification_report: \n", classification_report(target_test, pred_test))


from sklearn.neighbors import KNeighborsClassifier

knn_model = KNeighborsClassifier(n_neighbors=5, weights='distance')
pred_test = knn_model.fit(data_train, target_train).predict(data_test)
print("KNN accuracy_score: \n", accuracy_score(target_test, pred_test, normalize=True))
print("KNN confusion_matrix: \n", confusion_matrix(target_test, pred_test))
print("KNN classification_report: \n", classification_report(target_test, pred_test))


from sklearn.tree import DecisionTreeClassifier


dTClf_model = DecisionTreeClassifier()
pred_test = dTClf_model.fit(data_train, target_train).predict(data_test)
print("Decision Tree clf accuracy_score: \n", accuracy_score(target_test, pred_test, normalize=True))
print("Decision Tree clf confusion_matrix: \n", confusion_matrix(target_test, pred_test))
print("Decision Tree clf classification_report: \n", classification_report(target_test, pred_test))


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, KFold

# rFClf_model = RandomForestClassifier(n_estimators=100)
random_forest_param = {
    'n_estimators': [30, 50, 100],
    'max_depth':  [7,8,9,10,20]
}
rFClf_model = GridSearchCV(RandomForestClassifier(), random_forest_param, cv=5)
pred_test = rFClf_model.fit(data_train, target_train).predict(data_test)
print("Random Fores clf accuracy_score: \n", accuracy_score(target_test, pred_test, normalize=True))
print("Random Fores clf  confusion_matrix: \n", confusion_matrix(target_test, pred_test))
print("Random Fores clf  classification_report: \n", classification_report(target_test, pred_test))
print(rFClf_model.best_params_)


from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV, KFold
from sklearn import model_selection

# tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4], 'C': [1, 10, 100, 1000]},
#                     {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
svc_params = {
    'C': [0.01, 0.05, 0.1],
}

clf = GridSearchCV(LinearSVC(max_iter=10000), svc_params, cv=5, verbose=3, n_jobs=-1)
# clf.fit(x_train, y_train)
clf.fit(data_train, target_train)
print(clf.best_params_)
# y_train_pred = clf.predict(x_train)
pred_test = clf.predict(data_test)
# print(classification_report(y_train, y_train_pred))
print(" classification_report: \n", classification_report(target_test, pred_test))




model = DecisionTreeClassifier()
kfold = model_selection.KFold(n_splits=10, random_state=7)
cv_results = model_selection.cross_val_score(model, data_train, target_train, cv=kfold, scoring='accuracy')
print(cv_results)
print(cv_results.mean())




# kfold.get_n_splits(data_train)
# for train_index, test_index in kfold.split(data_train):
#     print("TRAIN:", train_index, "TEST:", test_index)
#     data_train, data_test = X[train_index], X[test_index]
#     target_train, target_test = y[train_index], y[test_index]














# test -> wybór argumentów
# train + cv -> wybór hiper parametrów
# trening -> trenowanie modelu przy wybranych algorytmach i wybranych chiper parametrach