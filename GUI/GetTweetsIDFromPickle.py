

import pickle
import Connect2Db

def getFile():
    f = open('../generateFeature/tweetsFeatureData.pkl', 'rb')
    return f

def getTweetsIDFromPickle():
    #get 10 tweets id and return a id  list and a dic (id:feature str ) and
    # a dic ( id: tweets) and anoher dic (id : user)
    try:
        f = open('../generateFeature/tweetsFeatureData.pkl', 'rb')
        db,cursor = Connect2Db.connect_db()

        data = pickle.load(f)
        target = pickle.load(f)
        tweetsID =  pickle.load(f)
        print tweetsID[0]
        tweetsIDlist=[]
        tweetsID_feature_target_Dic={}
        tweetsID_tweets_Dic = {}
        tweetsID_user_Dic= {}
        # print range()
        for i in range(1,500,50):
            # if(target[i]!=0):
            tweetsIDlist.append(tweetsID[i])
            tweetsID_feature_target_Dic[tweetsID[i]] = str(data[i]) +"  " \
                                                                     "target:  " \
                                                                     ""+ str(target[i])
            cursor.execute("select  numberOfHashtags_c,"
                                               "text,hashtags_c, "
                            "user  ,"
                       "maliciousMark,id  from Tweets where id = " + str(
                tweetsID[i]) + ";")

            Result=cursor.fetchall()
            tweetsTableResult =  Result[0]
            # print tweetsTableResult
            userId = tweetsTableResult[3]
            # print userId
            tweetStr = ",   ".join(str(x) for x in tweetsTableResult)
            tweetsID_tweets_Dic[tweetsID[i]] = tweetStr


            cursor.execute("SELECT followers_count,friends_count,"
                                  "description,"
                           "url FROM TweetsDB.User where id = " + str(
                userId) + ";")
            Result = cursor.fetchall()

            userTableResult = Result[0]
            userStr = ",   ".join(str(x) for x in userTableResult)
            tweetsID_user_Dic[tweetsID[i]] = userStr
            # print userTableResult




            # print target[i]
    finally:
        f.close()
        db.close()
    pass
    # print tweetsIDlist
    # print tweetsID_feature_target_Dic[329850905157591040]
    return tweetsIDlist,tweetsID_feature_target_Dic,tweetsID_tweets_Dic,tweetsID_user_Dic


tweetsIDlist, tweetsID_feature_target_Dic, tweetsID_tweets_Dic, tweetsID_user_Dic = getTweetsIDFromPickle()

print tuple(tweetsIDlist)
print tweetsID_feature_target_Dic[tweetsIDlist[0]]
print tweetsID_user_Dic