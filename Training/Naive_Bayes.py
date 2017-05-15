import numpy as np
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing


# get  data(dictionar) from pickle
output_data = open('data_pickle.pkl', 'rb')
output_target = open('target_pickle.pkl', 'rb')

data_dic = pickle.load(output_data)
target_dic = pickle.load(output_target)

output_data.close()
output_target.close()

#data
train_data = data_dic["train_data"]
validation_data = data_dic["validation_data"]
test_data = data_dic["test_data"]

#target
train_target = target_dic["train_target"]
validation_target = target_dic["validation_target"]
test_target = target_dic["test_target"]

print train_data.shape, validation_data.shape, test_data.shape
print train_target.shape, validation_target.shape, test_target.shape

# normalize data to [0,1]
min_max_scaler = preprocessing.MinMaxScaler()
train_data = min_max_scaler.fit_transform(train_data)
validation_data = min_max_scaler.fit_transform(validation_data)
test_data = min_max_scaler.fit_transform(test_data)

#variables for classifiers from differnt parameters/models and its score
classifiers = []
parameters = []
scores = []

#build naive Bayes Classifiers
gnb = GaussianNB()
mnb = MultinomialNB()
bnb = BernoulliNB()

#train classifiers
clf_gnb = gnb.fit(train_data, train_target)
print train_data.shape,train_target.shape
#build the classifiers with mnb .
clf_mnb = mnb.fit(train_data, train_target) # needs non-negative value
clf_bnb = bnb.fit(train_data, train_target)

#validate different classifiers
gnb_score = clf_gnb.score(validation_data,validation_target)
print("gnb-->score:  %f " %gnb_score)
mnb_score = clf_mnb.score(validation_data,validation_target)
print("mnb-->score:  %f " %mnb_score)
bnb_score = clf_bnb.score(validation_data,validation_target)
print("bnb-->score:  %f " %bnb_score)



#test the final classifiers
#based on the previous test choose mnb classifier as the finial classifier

score_final = clf_mnb.score(test_data,test_target)
print("final test -->score:  %f " %score_final)


#print confusing matrix
clf_mnb_pred = clf_mnb.predict(test_data)
print
print "confusion matrix: "
print confusion_matrix(test_target, clf_mnb_pred,labels=[-1,0,1])


