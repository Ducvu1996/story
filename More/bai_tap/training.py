import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import glob
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle

# path to the data csv file
path = r"DatasetUniqueI.csv"
path2 = r"DatasetUniqueFranceI.csv"

#read csv file and concat 2 databases, dataset is from Vietnamese, and dataset 2 is from France 
dataset=pd.read_csv(path)
dataset2=pd.read_csv(path2)
dataset2.columns=dataset.columns
dataset = pd.concat([dataset,dataset2],axis=0)

y=dataset['CLASS']
X=dataset.iloc[:,0:-1].values
# smotthing filter and derivate function, for the extract of features
X=signal.savgol_filter(X,window_length=17, polyorder=2, deriv=2)

#Encoding dummy Variable, in this case is the name of the fruit
from sklearn.preprocessing import LabelEncoder
labelencoder_Y = LabelEncoder()
y = labelencoder_Y.fit_transform(y)

# Stadard Scaler for the Data
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X = sc.fit_transform(X)


# PCA for choosing the most relevant variable for the prediction
from sklearn.decomposition import PCA
pca=PCA(n_components = 10)
X = pca.fit_transform (X)
explained_variance = pca.explained_variance_ratio_

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)


r"""
from sklearn.decomposition import KernelPCA
kpca=KernelPCA(n_components = 20 , kernel = 'rbf')
X_train = kpca.fit_transform (X_train)
X_test = kpca.transform(X_test)
"""
# Random Forest Algorithm application
from sklearn.ensemble import RandomForestClassifier
Rf = RandomForestClassifier(random_state=0)
Rf_fit=Rf.fit(X_train, y_train)

y_pred = Rf_fit.predict(X_test)

print("Test Result of Random Forest:\n")        
print("accuracy score: {0:.4f}\n".format(accuracy_score(y_test, y_pred)))
print("Classification Report: \n {}\n".format(classification_report(labelencoder_Y.inverse_transform(y_test), labelencoder_Y.inverse_transform(y_pred))))
print("Confusion Matrix: \n {}\n".format(confusion_matrix(y_test,y_pred)))

from sklearn.cross_decomposition import PLSRegression
pls = PLSRegression(n_components=10)
pls.fit(X_train, y_train)
y_pred=pls.predict(X_test)

#print("Test Result of Random Forest:\n")        
#print("accuracy score: {0:.4f}\n".format(accuracy_score(y_test, y_pred)))
#print("Classification Report: \n {}\n".format(classification_report(y_test, y_pred)))
#print("Confusion Matrix: \n {}\n".format(confusion_matrix(y_test,y_pred)))


# KNN Algorithm
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors  = 1,metric='minkowski',p=2)
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)

print("Test Result of KNN:\n")        
print("accuracy score: {0:.4f}\n".format(accuracy_score(y_test, y_pred)))
print("Classification Report: \n {}\n".format(classification_report(y_test, y_pred)))
print("Confusion Matrix: \n {}\n".format(confusion_matrix(y_test,y_pred)))

#SVC Algorithm
from sklearn.svm import SVC
classifierSVC=SVC(kernel='rbf', random_state = 0)
classifierSVC.fit(X_train, y_train)
y_pred=classifierSVC.predict(X_test)

print("Test Result of SVC:\n")        
print("accuracy score: {0:.4f}\n".format(accuracy_score(y_test, y_pred)))
print("Classification Report: \n {}\n".format(classification_report(y_test, y_pred)))
print("Confusion Matrix: \n {}\n".format(confusion_matrix(y_test,y_pred)))

#Bayes Algorithm
from sklearn.naive_bayes import GaussianNB
classifierNB=GaussianNB(var_smoothing=1e-8)
classifierNB.fit(X_train,y_train) 
y_pred=classifierNB.predict(X_test)

print("Test Result of naive bayes:\n")        
print("accuracy score: {0:.4f}\n".format(accuracy_score(y_test, y_pred)))
print("Classification Report: \n {}\n".format(classification_report(y_test, y_pred)))
print("Confusion Matrix: \n {}\n".format(confusion_matrix(y_test,y_pred)))

#DecisionTree Algorithm
from sklearn.tree import DecisionTreeClassifier
classifierDT = DecisionTreeClassifier(criterion="entropy",random_state=8)
classifierDT.fit(X_train,y_train)
y_pred=classifierDT.predict(X_test)
print("Test Result of Decision Tree:\n")        
print("accuracy score: {0:.4f}\n".format(accuracy_score(y_test, y_pred)))
print("Classification Report: \n {}\n".format(classification_report(y_test, y_pred)))
print("Confusion Matrix: \n {}\n".format(confusion_matrix(y_test,y_pred)))

print (labelencoder_Y.inverse_transform(y_pred))
print (labelencoder_Y.inverse_transform(y_test))

#Cross validation matrix, which mean we will take many of test set in order to have the best performance
from sklearn.model_selection import cross_val_score
accuracies1=cross_val_score(estimator=classifierNB,X=X_train,y=y_train,cv=10)
accuracies2=cross_val_score(estimator=classifierDT,X=X_train,y=y_train,cv=10)
accuracies3=cross_val_score(estimator=classifierSVC,X=X_train,y=y_train,cv=10)
accuracies4=cross_val_score(estimator=classifier,X=X_train,y=y_train,cv=10)
accuracies5=cross_val_score(estimator=Rf_fit,X=X_train,y=y_train,cv=10)




#dump the binnary file for the server application
pickle.dump(classifier,open("modelKNN.pkl","wb"))
pickle.dump(Rf_fit,open("modelRf_fit.pkl","wb"))
pickle.dump(classifierDT,open("modelDT.pkl","wb"))
pickle.dump(classifierSVC,open("modelSVC.pkl","wb"))
pickle.dump(classifierNB,open("modelNB.pkl","wb"))
pickle.dump(labelencoder_Y,open("labelEncoder.pkl","wb"))
pickle.dump(sc,open("Scaler.pkl","wb"))
pickle.dump(pca,open("Pca.pkl","wb"))
