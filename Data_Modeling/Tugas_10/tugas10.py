import pandas as pd
import numpy as np

df = pd.read_csv('Datartrwdki1317.csv')
print(df)

available_kabkota = df['nama_kabupaten_kota'].unique()
print (available_kabkota)

count_kabkota = df.groupby(['nama_kabupaten_kota']).size().reset_index(name='counts')
print (count_kabkota)

rt=df.groupby(['nama_kabupaten_kota','nama_kecamatan','nama_kelurahan'])['jumlah_rt'].sum().reset_index()
print(rt)

import pandas
import sklearn
import scipy
import numpy
import matplotlib
pandas.__version__, sklearn.__version__,scipy.__version__,numpy.__version__,matplotlib.__version__

import matplotlib.pyplot as plt
import numpy
from pandas.plotting import scatter_matrix
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
from sklearn import datasets

iris = datasets.load_iris()
iris

iris.keys()

print(iris.DESCR)

dataset = pandas.DataFrame(data= numpy.c_[iris['data']],
                          columns= iris['feature_names'])
dataset['class'] = numpy.c_[list(map((lambda x: iris.target_names[x]), iris.target))]

dataset.shape

dataset.head(5)

dataset.describe()

dataset.groupby('class').size()

dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

dataset.hist()
plt.show()

scatter_matrix(dataset)
plt.show()