#!/usr/bin/env python # -*- coding: utf8 -*-

import MySQLdb
import traceback
import pickle,pprint
from scipy import stats




def GettingAllRelatedVarsFromDBTweets(db, cursor, verbos=1):
    try:
        cursor.execute("select  numberOfHashtags_c,text,hashtags_c, user  ,"
                       "maliciousMark,id  from Tweets where maliciousMark IS "
                       "NOT null  ;")
        metadataFromTweets = list(cursor.fetchall())
        #  numberOfHashtags_c, text, hashtags_c, user, maliciousMark
        # output = open('data.pkl', 'wb')
        # pickle.dump(test, output)
        # print cursor.fetchone()
        if(verbos):
            print len(metadataFromTweets)

        # with in the list , each instance is a tuple contains
        # [0] numberOfHashtags_c,
        # [1]text,
        # [2]hashtags_c,
        # [3]user,
        # [4]maliciousMark

        # print metadataFromTweets[0]
        # get all the target value


        # print targetMetadat[0]
        if(verbos):
            print "len of metadataFromTweets is " + str(len(metadataFromTweets))
        return metadataFromTweets
        # print "success"
    except:
        traceback.print_exc()
        print "not successful"

    finally:
        # db.close()
        # output.close()
        pass

        # print "db  closed "

def gettingAllValueOfFollowerAndFollowee(db, cursor,verbos=1):
    #followers_count friends_count
    followers_count_list=[]
    friends_count_list=[]

    try:
        cursor.execute("SELECT followers_count,friends_count  FROM TweetsDB.User;")
        result = list(cursor.fetchall())

        firstTime = True
        for r in result:
            # if firstTime:
            #     print r[0]
            #     firstTime= False
            followers_count_list.append(r[0])
            friends_count_list.append(r[1])

        if(verbos):
            print len(result)
            print "len of followers_count_list is "  + str(len(followers_count_list))
            print "len of friends_count_list is " + str(len(friends_count_list))
            print followers_count_list[0]
            print followers_count_list[1]

        percentile5_OnFollower = stats.scoreatpercentile(followers_count_list,
                                                         5)
        percentile5_OnFollowee = stats.scoreatpercentile(friends_count_list, 5)
        return followers_count_list,percentile5_OnFollower,percentile5_OnFollowee
        # print "success"
    except:
        traceback.print_exc()
        print "not successful"




def gettingInfoFromUser(userId,db, cursor,verbos=1):


    try:
        cursor.execute("SELECT followers_count,friends_count,description,"
                       "url FROM TweetsDB.User where id = " +str(userId)+";")
        result = list(cursor.fetchall())
        if(result):
            followers_count = result[0][0]
            friends_count = result[0][1]
            description = result[0][2]
            url = result[0][3]
            if (verbos):
                print len(result)
                print followers_count, friends_count, description, url

            return followers_count, friends_count, description, url
        else:
            return None,None,None,None



        # print "success"
    except:
        traceback.print_exc()
        print result ,userId
        print "not successful"
