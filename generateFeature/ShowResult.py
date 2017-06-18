
import pickle
def showResult():
    # get the data and target from generated pickle file.

    try:
        dataFile  =  open ("tweetsFeatureData.pkl",'r')
        data = pickle.load(dataFile)
        target  =  pickle.load(dataFile)
        for i in range(10):
            # print type(data)
            print data[i]
    finally:
        dataFile.close()


    pass


if __name__ == '__main__':
    showResult()