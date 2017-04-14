import InsertUserStatement
import InsertTweetsStatement
import UpdateUserStatement
import traceback
import datetime



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
                tweetTimeStamp = tweet['created_at']
                tweetTimeStamp = datetime.datetime.strptime(tweetTimeStamp,"%a %b %d %H:%M:%S +0000 %Y")
                sqlOnUpdatetime = "SELECT updateTime FROM User where id = '"+ str(tweet['user']['id']) + "';"
                cursor.execute(sqlOnUpdatetime)
                useInfoUpdataTimeInDB = cursor.fetchone()
                useInfoUpdataTimeInDB = useInfoUpdataTimeInDB[0]  # dateTime type
                print "useInfoUpdataTimeInDB is "
                print useInfoUpdataTimeInDB
                if(tweetTimeStamp > useInfoUpdataTimeInDB):
                    # the user info in tweets is lastest info-->need to update user Info in DB
                    UpdateUserSQL = UpdateUserSQLStr(tweet);
                    print UpdateUserSQL
                    cursor.execute(UpdateUserSQL)
                    print "****** userinfo in DB  updated *******"
                # else:
                #     #the user info in tweets is old info--> not need to update user info in DB
                    pass
            else:
                #User not in the DB--> uodate  user
                InsertUserSQL = InsertUserSQLStr(tweet);
                result = cursor.execute(InsertUserSQL)
                # if (result == 0):
                #     print result;
                #     print InsertUserSQL;

                # print result;
            #tweets not in DB -->uodate tweets
            # todo start
            # InsertTweetsSQL = InsertTweetsSQLStr(tweet);
            # cursor.execute(InsertTweetsSQL)
            # todo end
            db.commit();

        else:
            # this tweet already in DB-->  it means this time we get this tweets frmo retweets body or the tweets in DB is updated in retweetstweet id is unique,  -- >do nothing ->next iteration.

            pass
    except:
    #     print args
        print "$$$this is RuntimeError"
    # pass error
        db.rollback()
        traceback.print_exc()

    finally:
        # print  "this is finally "
        pass

        # ContainsTweets = tweet.id
