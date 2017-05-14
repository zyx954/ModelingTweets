import pickle
import numpy as np
from sklearn import preprocessing
import os


#get data and target
try:
    f= open('../generateFeature/tweetsFeatureData.pkl', 'rb')

    data = pickle.load(f)
    target = pickle.load(f)
    # test =  pickle.load(f)

    print(data.shape, data.dtype)
    print(target.shape, target.dtype)
    print data[1:100]
    print target[1:100]
    # print test.shape


    #shufflers(needs to match the data and target)
    r = np.random.permutation(len(target))
    print r
    data = data[r, :]
    target = target[r]
    print  type(data)
    print  type(target)

    print(data.shape, data.dtype)
    print(target.shape, target.dtype)

    print data[1:100]
    print target[1:100]


    #there no missing value


    #
    #normalize data with norm "l2"
    data = preprocessing.normalize(data,norm="l2")


    #creat train_data , validatiaon_data , test_data
    train_data, validation_data, test_data = np.split(data, [int(.7*len(data)),int(.85*len(data))])
    train_target, validation_target, test_target = np.split(target, [int(.7*len(target)),int(.85*len(target))])
    print train_data.shape,validation_data.shape,test_data.shape
    print train_target.shape,validation_target.shape,test_target.shape


    # save data to pickle formate
    data_pickle={"train_data":train_data,"validation_data":validation_data,"test_data":test_data}
    target_pickle={"train_target":train_target,"validation_target":validation_target,"test_target":test_target}


    if(os.path.isfile('data_pickle.pkl')):
        os.remove("data_pickle.pkl")
        print "data_pickle.pkl removed"
    if(os.path.isfile('target_pickle.pkl')):
        os.remove('target_pickle.pkl')
        print "target_pickle.pkl removed"

    output_data = open('data_pickle.pkl', 'wb')
    output_target = open('target_pickle.pkl', 'wb')


    pickle.dump(data_pickle, output_data)

    pickle.dump(target_pickle, output_target)

finally:
    f.close()
    output_data.close()
    output_target.close();
    print "all files closed "

