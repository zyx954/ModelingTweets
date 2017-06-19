
import pickle
import numpy as np

def showResult():
    # get the data and target from generated pickle file.

    try:
        dataFile  =  open ("tweetsFeatureData.pkl",'r')
        data = pickle.load(dataFile)
        target  =  pickle.load(dataFile)
        id =  pickle.load(dataFile)
        for i in range(10):
            print type(data)
            print type(target)
            print type(id)
            print data[i]
            print target[i]
            print id[i]
    finally:
        dataFile.close()


    pass

# generate another feature file by shuffle data
def getSecondFeatureFile():
    try:
        dataFile  =  open ("tweetsFeatureData.pkl",'r')
        data = pickle.load(dataFile)
        target  =  pickle.load(dataFile)
        id =  pickle.load(dataFile)
        p = np.random.permutation(len(data))
        data=data[p]
        target= target[p]
        id = id[p]

        file = open('tweetsFeatureData2.pkl', 'w')
        pickle.dump(data, file)
        pickle.dump(target, file)
        pickle.dump(id, file)


    finally:
        dataFile.close()
        file.close()

if __name__ == '__main__':
    # showResult()
    getSecondFeatureFile()