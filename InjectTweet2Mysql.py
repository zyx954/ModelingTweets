import InsertUserStatement
import InsertTweetsStatement
import UpdateUserStatement
import traceback


#inject one particulat tweet based on informaton betweetn DB and tweet
def injectTweet2Mysql(tweet,db, cursor):

    try:

        # tweet['id']
        InsertUserSQLStr = InsertUserStatement.InsertUserSQLStr
        InsertTweetsSQLStr = InsertTweetsStatement.InsertTweetsSQLStr
        UpdateUserSQLStr = UpdateUserStatement.UpdateUserSQLStr
        #initialize containsTweets &containsUser
        containsTweets=False
        containsUser = False
        if(cursor.execute("SELECT id FROM Tweets where id = '"+ str(tweet['id'])
                        +"'; ")!=0):
            # print "SELECT id FROM User where id = '"+ str(tweet['id']) +"'; "
            containsTweets=True
        if (cursor.execute("SELECT id FROM User where id = '" + str(
                tweet['user']['id']) + "'; ") != 0):
            containsUser = True

        # print ContainsTweets
        if(not containsTweets):
            # assert (1 == 0)
            #this tweet is not in DB
            if(containsUser):
                # User Info already in DB
                # todo Start
                tweetTimeStamp = tweet.createdTime
                useInfoUpdataTimeInDB = cursor.execute("SELECT updatetime FROM Users where id = userIdFromTweets ;")
                if(tweetTimeStamp < useInfoUpdataTimeInDB):
                    # the user info in tweets is lastest info-->need to update user Info in DB
                    UpdateUserSQL = UpdateUserSQLStr(tweet);
                    # cursor.execute(UpdateUserSQL)
                # todo End
                else:
                    #the user info in tweets is old info--> not need to update user info in DB
                    pass
            else:
                #User not in the DB--> uodate  user
                InsertUserSQL = InsertUserSQLStr(tweet);
                # cursor.execute(InsertUserSQL)
            #tweets not in DB -->uodate tweets
            InsertTweetsSQL = InsertTweetsSQLStr(tweet);
            # cursor.execute(InsertTweetsSQL)

        else:
            # this tweet already in DB-->  it means this time we get this tweets frmo retweets body or the tweets in DB is updated in retweetstweet id is unique,  -- >do nothing ->next iteration.
            pass
    except:
    #     print args
    #     print "$$$this is RuntimeError"
    # pass error
        traceback.print_exc()

    finally:
        # print  "this is finally "
        pass

        # ContainsTweets = tweet.id
