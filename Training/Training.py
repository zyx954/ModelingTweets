
import pickle


pkl_file = open('./tweetsFeatureData.pkl', 'r')

data = pickle.load(pkl_file)
target = pickle.load(pkl_file)


try:
    print len(data)
    print len(target)



finally:
    pkl_file.close()

