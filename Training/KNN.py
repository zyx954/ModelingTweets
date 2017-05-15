import pickle
from sklearn import neighbors
from sklearn.metrics import confusion_matrix

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



#variables for classifiers from differnt parameters/models and its score
classifiers = []
parameters = []
scores = []

#build kNN classifiers
# for  n in range(1,1000,100):
for n in range(1, 100, 10):
# for n in range (1,21,1):
    for weights in ['uniform', 'distance']:
        # we create an instance of Neighbours Classifier and fit the data.
        clf = neighbors.KNeighborsClassifier(n, weights=weights)
        clf.fit(train_data, train_target)
        # pdf = clf.predict(validation_data)
        score = clf.score(validation_data,validation_target);
        parameter = "the number of neighbors" + str(n) + "; weights : " + str(weights)
        classifiers.append(clf)
        parameters.append(parameter)
        scores.append(score)

        print parameter + "===>score is: ",score


#evaluation
#<choose the best parameter --> test on the test_data and test_target>
max_score_index = scores.index(max(scores))
clf = classifiers[max_score_index]
paremeter = parameters[max_score_index]
score = clf.score(test_data, test_target)
print "Last evaluation on the best score from validation"
print paremeter,"score: -->",score


#print confusing matrix
clf_pred= clf.predict(test_data)
print
print "confusion matrix: "
print confusion_matrix(test_target, clf_pred,labels=[-1,0,1])
