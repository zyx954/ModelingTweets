from sklearn import svm
import pickle
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
#

#variables for classifiers from differnt parameters/models and its score
classifiers = []
parameters = []
scores = []


#build SVM classifiers via different parameters


# for kernel in [ 'linear','rbf','poly','sigmoid']:
#     for degree in [3,4, 6,9]:
#         for class_weight in ['balanced',None]:
#             clf = svm.SVC(kernel=kernel,degree=degree,class_weight=class_weight,cache_size=2000)
#             clf.fit(train_data, train_target)
#             parameter = "kernel: " + str(kernel) + " degree for poly: ", str(degree) + " class_weight: ", +str(class_weight)
#             score = clf.score(validation_data,validation_target)
#             classifiers.append(clf)
#             parameters.append(parameter)
#             scores.append(score)
#             print parameter + "---->score: " + str(score)


for loss in [ 'squared_hinge','hinge']:
    for class_weight in ['balanced',None]:
        clf = svm.LinearSVC(loss=loss,class_weight=class_weight)
        clf.fit(train_data, train_target)
        #store classifier with particular paramters and its score into sperately list
        parameter = "loss: " +str(loss) + "; class_weight: " + str(class_weight)
        score = clf.score(validation_data,validation_target)
        classifiers.append(clf)
        parameters.append(parameter)
        scores.append(score)
        print parameter + "---->score: " + str(score)


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
