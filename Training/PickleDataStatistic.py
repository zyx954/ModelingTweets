
import pickle,pprint

import json

pkl_file = open('../generateFeature/tweetsFeatureData.pkl', 'r')

data = pickle.load(pkl_file)
target = pickle.load(pkl_file)

variablesName= ['hashtags_more_two','exclamation_sign','url_in_tweets','suffix_hashtag','spammy_hashtag','negative_words','upper_case_characters','capitalized_hashtag','Followers_followees_ratio','description','url_in_user','followers_Less_5_percentile','followees_Less_5_percentile','Percentile_of_followers']
variables=[0]*14
index = range(0,14)
print variables

counter=0
target_counter=0
# this method will print the number of 0 for all the variables within data.
try:

    print len(data)
    print len(target)
    for instance in data:
        for i in index:
            if(instance[i]==0):
                variables[i]=variables[i]+1
    for target_instane in target:
        if(target_instane==0):
            target_counter=target_counter+1



    print "total number of data is " + str( len(data))
    print "the number of 0 in Target is " + str(target_counter )
    for name in variablesName:
        print " the number of 0 in "+ name + " is : "+ str(variables[counter])
        counter = counter+1



finally:
    pkl_file.close()

