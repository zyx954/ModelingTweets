
import pickle,pprint
import json
import Connect2Db as Connect2Db
import InjectTweet2Mysql
import traceback

injectTweet2Mysql= InjectTweet2Mysql.injectTweet2Mysql
# injectTweet2Mysql= TestGettingInfo.injectTweet2Mysql

pkl_file = open('../xaaData.pkl', 'r')
tweets_data = pickle.load(pkl_file)

try:
    # print json.dumps(data3[100], indent=1)
    db, cursor = Connect2Db.connect_db()
    print 'lenght of this Tweets ; ' + str(len(tweets_data))

    injectTweet2Mysql(tweets_data[1],db, cursor)
    # for tweet in tweets_data:
    #     # print "test error times, "
    #     injectTweet2Mysql(tweet,db, cursor);


except:
    traceback.print_exc()
finally:
    pkl_file.close()
    db.close()
    print "pkl_file & db closed"





