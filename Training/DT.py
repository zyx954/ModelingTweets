from sklearn.tree import DecisionTreeClassifier
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

#variables for classifiers from differnt parameters/models and its score
classifiers = []
parameters = []
scores = []


#build DT classifiers <--via different parameters
# for criterion in ['gini', 'entropy']:
#     for max_features in ['sqrt','log2', 'auto',None]:
#         for class_weight in ['balanced',None]:
criterion = 'gini'
max_features= 'log2'
class_weight=None
clf = DecisionTreeClassifier(criterion=criterion,max_features=max_features,class_weight=class_weight)
# Train data based on the parameters
clf.fit(train_data, train_target)

#validation
score = clf.score(validation_data,validation_target)
paremeter = "criterion: " +str(criterion)+ "; max_features: "+str(max_features) + "; class_weight: " + str(class_weight)
print paremeter,"score: -->",score
classifiers.append(clf)
parameters.append(paremeter+"score: -->")
scores.append(score)

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