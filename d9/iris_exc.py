import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_iris = sns.load_dataset("iris")
print(df_iris)
print(df_iris.size)
print(df_iris.shape)
print(df_iris.melt())

# print(df_iris.head())
# # plt.scatter(df_iris.petal_length, df_iris.petal_width)
# # # plt.show()
#
print(df_iris.dtypes)
# rows from 1:10, columns 3, 4
print(df_iris.iloc[1:10, [3, 4]])
print(pd.Categorical(df_iris.iloc[:, 4]))
print(pd.Categorical(df_iris.loc[:, "species"]))

s = pd.Series(pd.Categorical(df_iris.loc[:, "species"]))
print(s)

tips = sns.load_dataset('tips')
print(tips.head())
tips_ratio = round((tips['tip'] / tips['total_bill'])*100).astype(int)
tips['tips_ratio'] = tips_ratio
print(tips)
print(tips['tips_ratio'].mean())
print(tips.dtypes)

tip_time = tips.groupby('time').mean()['tip']


colors = np.array(["#f442bf", "#6e41f4", "#f4dc41"])[s.cat.codes]
plt.scatter(df_iris.petal_length, df_iris.petal_width, c=colors)
plt.show()
print(s)





# przetrenowac trzy modele z sales.py dla danych iris
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
classes = le.fit_transform(s)
print(classes)

# labels= classes
target = classes
data = df_iris.drop(columns='species')
print(data)


from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split( data, target, test_size=0.20, random_state=10 )

print(data_train, '\n', data_test, '\n', target_train, '\n', target_test )

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

gnb = GaussianNB()
pred = gnb.fit(data_train, target_train).predict(data_test)
print("Naive-Bayes accuracy : ", accuracy_score(target_test, pred, normalize=True))


from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


svc_model = LinearSVC(random_state=0)
pred = svc_model.fit(data_train, target_train).predict(data_test)
print("LinearSVC accuracy : ", accuracy_score(target_test, pred, normalize=True))


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


neigh = KNeighborsClassifier(n_neighbors=3, weights='distance')
neigh.fit(data_train, target_train)
pred = neigh.predict(data_test)
print("KNeighbors accuracy score : ", accuracy_score(target_test, pred))

