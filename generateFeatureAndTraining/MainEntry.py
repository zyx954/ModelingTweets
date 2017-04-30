
import pickle,pprint
import json
import Connect2Db as Connect2Db
import traceback
import  GettingInfoFromDB
import GettingInstanceFromTweets
import GenerateInstance, GettingInstanceOfUser,GettingNegativeWords
from numpy import array
import time



#aim
#--> extra features from DB<--based on the feature in paper.


GettingAllRelatedVarsFromDBTweets=GettingInfoFromDB.GettingAllRelatedVarsFromDBTweets
gettingAllValueOfFollowerAndFollowee=GettingInfoFromDB.gettingAllValueOfFollowerAndFollowee
GettingInstanceFromTweets=GettingInstanceFromTweets.GettingInstanceFromTweets
GenerateInstance=GenerateInstance.GenerateInstance
GettingInstanceOfUser=GettingInstanceOfUser.gettingInstanceOfUser
gettingNegativeWords=GettingNegativeWords.gettingNegativeWords
try:
    # print json.dumps(data3[100], indent=1)
    data=[]
    target=[]
    db, cursor = Connect2Db.connect_db()
    metadataFromTweets,targetMetadat = GettingAllRelatedVarsFromDBTweets(db,
                                                                      cursor,0)
    followers_count_list, percentile5_OnFollower, percentile5_OnFollowee = \
        gettingAllValueOfFollowerAndFollowee(db, cursor,0)

    counter = 0
    print 'the length of metadataFromTweets is : ' + str(len(metadataFromTweets))

    NEGATIVE_opinion_words= gettingNegativeWords()
    start = time.time()


    for i in metadataFromTweets:
        instanceOfTweets= GettingInstanceFromTweets(i,NEGATIVE_opinion_words,0)
        if instanceOfTweets:
            userId = i[3]

            instanceOfUser= GettingInstanceOfUser(userId,db, cursor,
                                                  followers_count_list,
                                                  percentile5_OnFollower,percentile5_OnFollowee,0)
            # if instanceOfUser:
            oneInstance = instanceOfTweets+instanceOfUser
            data.append(oneInstance)
            target.append(targetMetadat[counter])
            counter=counter+1
            if counter == 100:
                print "this is the first time to reach 100000 , the time is : "
                end = time.time()
                print(end - start)
                data = array(data)
                target = array(target)
                file = open('tweetsFeatureData.pkl', 'w')
                pickle.dump(data, file)
                pickle.dump(target, file)

    data = array(data)
    target=array(target)
    file = open('tweetsFeatureData.pkl','w')
    pickle.dump(data,file)
    pickle.dump(target,file)

    print "success"



except:
    traceback.print_exc()
finally:
    db.close()
    file.close()

    print "pkl_file & db closed"




