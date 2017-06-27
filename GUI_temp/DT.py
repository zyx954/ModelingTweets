from sklearn.tree import DecisionTreeClassifier
import pickle
from sklearn.metrics import confusion_matrix


def DT(criterion,max_features,class_weight):
    # ###############3get  data(dictionar) from pickle###########
    output_data = open('data_pickle.pkl', 'rb')
    output_target = open('target_pickle.pkl', 'rb')
    output_IDs = open('IDs_pickle.pkl', 'rb')


    data_dic = pickle.load(output_data)
    target_dic = pickle.load(output_target)
    IDs_dic = pickle.load(output_IDs)


    output_data.close()
    output_target.close()
    output_IDs.close()

    #data
    train_data = data_dic["train_data"]
    validation_data = data_dic["validation_data"]
    test_data = data_dic["test_data"]

    #target
    train_target = target_dic["train_target"]
    validation_target = target_dic["validation_target"]
    test_target = target_dic["test_target"]

    # IDs
    train_IDs = IDs_dic["train_IDs"]
    validation_IDs = IDs_dic["validation_IDs"]
    test_IDs = IDs_dic["test_IDs"]

    print test_data[1]
    print "#########"
    print train_data.shape, validation_data.shape, test_data.shape
    print train_target.shape, validation_target.shape, test_target.shape


    # ########### DT Parameters ##########
    #variables for classifiers from differnt parameters/models and its score
    classifiers = []
    parameters = []
    scores = []

    # #######Training based on selected parameters
    # build DT classifiers <--via different parameters
    # for criterion in ['gini', 'entropy']:
    #     for max_features in ['sqrt','log2', 'auto',None]:
    #         for class_weight in ['balanced',None]:
    criterion = criterion
    max_features= max_features
    class_weight=class_weight
    clf = DecisionTreeClassifier(criterion=criterion,max_features=max_features,class_weight=class_weight)
    # Train data based on the parameters
    clf.fit(train_data, train_target)

    # #validation
    # score = clf.score(validation_data,validation_target)
    # paremeter = "criterion: " +str(criterion)+ "; max_features: "+str(max_features) + "; class_weight: " + str(class_weight)
    # print paremeter,"score: -->",score
    # classifiers.append(clf)
    # parameters.append(paremeter+"score: -->")
    # scores.append(score)

    ###### evaluation
    #<choose the best parameter --> test on the test_data and test_target>
    # max_score_index = scores.index(max(scores))
    # clf = classifiers[max_score_index]
    # paremeter = parameters[max_score_index]
    score = clf.score(test_data, test_target)
    print "Last evaluation on the best score from validation"
    print "score: -->",score


    # Get predicted Results & combine with ID& Actual results
    clf_pred = clf.predict(test_data)
    print type(clf_pred), len(clf_pred)
    i=0
    combinedResultOnActualAndPred=[]
    for predictResult in clf_pred:
        combinedResultOnActualAndPred.append( str(
            train_IDs[i] )+"\t"+ str(train_target[i]
                                                                         )+"\t"+ str(predictResult )+"\r\n")
        i=i+1

    #print confusing matrix
    print "confusion matrix: "
    print confusion_matrix(test_target, clf_pred,labels=[-1,0,1])
    DTconfusion_matrix= confusion_matrix(test_target, clf_pred,labels=[-1,0,1])
    percision, recall = calculatePercisionAndRecall(DTconfusion_matrix)
    return DTconfusion_matrix,percision, recall,combinedResultOnActualAndPred

def calculatePercisionAndRecall(DTconfusion_matrix):
    print DTconfusion_matrix[0][2]
    percision = float(DTconfusion_matrix[2][2])/(DTconfusion_matrix[0][
                                              2]+DTconfusion_matrix[1][
        2]+DTconfusion_matrix[2][2])
    recall = float(DTconfusion_matrix[2][2]) / (DTconfusion_matrix[2][
                                                0] + DTconfusion_matrix[2][
                                                1] + DTconfusion_matrix[2][2])
    return percision,recall

