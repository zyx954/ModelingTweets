from sklearn import svm
import pickle
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold



def svm_training(kernal, loss, class_weight,pickleFileName,flolderValue):
    # pickleFileName='tweetsFeatureData'
    try:
        print "####enter dataPrecess before f "
        # f = open('./tweetsFeatureData.pkl', 'rb')
        f = open('./' + pickleFileName + '.pkl', 'rb')
        print "enter dataPrecess"

        data = pickle.load(f)
        target = pickle.load(f)
        IDs = pickle.load(f)

        i = 0
        for id in IDs:
            if (id == 329850889856761856):
                print "this is target *****" + str(i)
                print str(data[i])
                print IDs[i]
                print "********end ****"
            i = i + 1



    finally:

        f.close()
        print "all files closed "

    # SVM parameter setting  and set classifiers
    clf = svm.LinearSVC(loss=loss,class_weight=class_weight)

    ###build N folder ###
    kf = KFold(n_splits=int(flolderValue))
    percisions = []
    recalls = []
    for train_index, test_index in kf.split(data):
        train_data = data[train_index]
        test_data = data[test_index]
        test_ID = IDs[train_index]
        train_target = target[train_index]
        test_target = target[test_index]
        print train_data[1]
        print test_ID[1]

        # build classifiers
        classifier = clf.fit(train_data, train_target)

        # get confusing matrix from test dataset
        clf_pred = classifier.predict(test_data)
        DTconfusion_matrix = confusion_matrix(test_target, clf_pred,
                                              labels=[
                                                  -1, 0, 1])
        print DTconfusion_matrix
        percision, recall = calculatePercisionAndRecall(DTconfusion_matrix)
        percisions.append(percision)
        recalls.append(recall)
        print "percision is :  " + str(percision)
        print "recall is : " + str(recall)

    averagePercision = reduce(lambda x, y: x + y, percisions) / len(percisions)
    averageRecall = reduce(lambda x, y: x + y, recalls) / len(recalls)
    return percisions, recalls, averagePercision, averageRecall


def calculatePercisionAndRecall(DTconfusion_matrix):
    print DTconfusion_matrix[0][2]
    percision = float(DTconfusion_matrix[2][2]) / (DTconfusion_matrix[0][
                                                       2] +
                                                   DTconfusion_matrix[1][
                                                       2] +
                                                   DTconfusion_matrix[2][2])
    recall = float(DTconfusion_matrix[2][2]) / (DTconfusion_matrix[2][
                                                    0] + DTconfusion_matrix[2][
                                                    1] + DTconfusion_matrix[2][
                                                    2])
    return percision, recall
