
import pickle,pprint
import json
import Connect2Db as Connect2Db
import traceback
import  GettingInfoFromDB

from numpy import array
import time
import numpy as np

import cProfile


def mainEntry():
    import GettingInstanceFromTweets
    import GettingInstanceOfUser, GettingNegativeWords
    #aim
    #--> extra features from DB<--based on the feature in paper.


    GettingAllRelatedVarsFromDBTweets=GettingInfoFromDB.GettingAllRelatedVarsFromDBTweets
    gettingAllValueOfFollowerAndFollowee=GettingInfoFromDB.gettingAllValueOfFollowerAndFollowee
    GettingInstanceFromTweets=GettingInstanceFromTweets.GettingInstanceFromTweets
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

        followers_count_list_sort = np.sort(followers_count_list)
        a_afterInitial, n = initial(followers_count_list)
        a_len_else = a_len_else_function(a_afterInitial)

        spamHashtags_set = (
            ['TEAMFOLLOWBACK', 'TFBJP', 'gameinsight', 'androidgames',
             'OPENFOLLOW',
             'androidgames', 'FF', 'RETWEET', 'IPADGAMES', 'RT', 'SougoFollow',
             'ipad', 'FOLLOWBACK', 'THF', 'FOLLOWNGAIN', '500aday',
             'AUTOFOLLOW',
             'MUSTFOLLOW', 'TEAMHITFOLLOW', 'HITFOLLOWSTEAM'])
        spamHashtags_set_l = set([x.lower() for x in spamHashtags_set])


        print "a_len_else"
        print a_len_else
        print "start loop"

        start = time.time()

        # i=1
        for i in metadataFromTweets:
            instanceOfTweets= GettingInstanceFromTweets(i,
                                                        NEGATIVE_opinion_words,spamHashtags_set_l,0)
            userId = i[3]

            instanceOfUser= GettingInstanceOfUser(userId,db, cursor,
                                                  followers_count_list_sort,n,a_len_else,
                                                  percentile5_OnFollower,percentile5_OnFollowee,0)
            if(instanceOfUser):
                oneInstance = instanceOfTweets+instanceOfUser
                data.append(oneInstance)
                target.append(targetMetadat[counter])
                counter=counter+1
                # if counter == 100000:
                #     print "this is the first time to reach 100 , the time is : "
                #     end = time.time()
                #     print "the time is "
                #     print (end - start)
                #     data = array(data)
                #     target = array(target)
                #     file = open('tweetsFeatureData.pkl', 'w')
                #     pickle.dump(data, file)
                #     pickle.dump(target, file)
                #     break
            pass
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


#these two functions are abstract from percentileofscore -->For the
# performace purpose
def initial(a):
    a_afterInitial = np.array(a)
    n = len(a)
    return a_afterInitial,n

def a_len_else_function(a_AfterInitial):
    a_len_else = np.array(list(range(len(a_AfterInitial)))) + 1.0
    return a_len_else


if __name__ == "__main__":
   import profile

   mainEntry()
   # profile.run("mainEntry()")

