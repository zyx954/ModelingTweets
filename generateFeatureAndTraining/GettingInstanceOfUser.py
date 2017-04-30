#!/usr/bin/env python # -*- coding: utf8 -*-

import GettingInfoFromDB as GettingInfoFromDB
from scipy import stats

def gettingInstanceOfUser(userId,db, cursor,followers_count_list,percentile5_OnFollower,percentile5_OnFollowee,verbose=1):
    # print userId
    #get based on userId get the followers_count  friends_count  description   url
    gettingInfoFromUser=GettingInfoFromDB.gettingInfoFromUser
    followers_count,friends_count,description_from_db,url =gettingInfoFromUser(
        userId,db, cursor,0)

    #initial the value
    Followers_followees_ratio = 0
    description = 0
    url_in_user = 0
    followers_Less_5_percentile = 0
    followees_Less_5_percentile = 0
    Percentile_of_followers = 0

    if(friends_count!=0):
        Followers_followees_ratio = followers_count/float(friends_count)
    if(description_from_db):
        description=1
    if(url):
        url_in_user=1

    Percentile_of_followers = stats.percentileofscore(followers_count_list, followers_count)

    if(followers_count<percentile5_OnFollower):
        followers_Less_5_percentile=1
    if(friends_count<percentile5_OnFollowee):
        followees_Less_5_percentile=1



    instanceOfUser=[Followers_followees_ratio,description,url_in_user,followers_Less_5_percentile,followees_Less_5_percentile,Percentile_of_followers]


    if verbose:
        print "####"
        print followers_count
        print percentile5_OnFollower
        print percentile5_OnFollowee
        print Percentile_of_followers
        print instanceOfUser

    return instanceOfUser
