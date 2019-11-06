import pandas
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy as np


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_iris = sns.load_dataset("iris")
# print(df_iris)
# print(df_iris.size)
# print(df_iris.shape)
print(df_iris.melt())