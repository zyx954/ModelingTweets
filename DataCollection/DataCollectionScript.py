#import tweepy
import time
import twitter
import json
import pickle,pprint
from itertools import cycle

import sys
import time
from urllib2 import URLError
from httplib import BadStatusLine


#usign tweepy
def oauth_login():
    # XXX: Go to http://twitter.com/apps/new to create an app and get values
    # for these credentials that you'll need to provide in place of these
    # empty string values that are defined as placeholders.
    # See https://dev.twitter.com/docs/auth/oauth for more information
    # on Twitter's OAuth implementation.

    # use your own key
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth,retry=True)
    return twitter_api


# Sample usage
twitter_api = oauth_login()

# everytime this script will collect 7 files & when it's over, I just need to
#  uncommit another fileNames -->split into 7 for checking purpose which
# means I need to do a update every 7-8 days
fileNames = ['xbf', 'xbg', 'xbh', 'xbi', 'xbj']
# fileNames = ['xbk','xbl','xbm','xbn','xbo','xbp','xbq']
# fileNames = ['xbr','xbs','xbt','xbu','xbv','xbw','xbx']
# fileNames = ['xby','xbz','xca','xcb','xcc','xcd','xce']
# fileNames = ['xcf','xcg','xch','xci','xcj','xck','xcl']
# fileNames = ['xcm','xcn','xco','xcp','xcq','xcr','xcs']
# fileNames = ['xct','xcu','xcv','xcw','xcx','xcy','xcz']
# fileNames = ['xda','xdb','xdc','xdd','xde','xdf','xdg']
# fileNames = ['xdh','xdi','xdj','xdk','xdl','xdm','xdn']
# fileNames = ['xdo','xdp','xdq','xdr','xds','xdt','xdu']
# fileNames = ['xdv','xdw','xdx','xdy','xdz','xea','xeb']
# fileNames = ['xec','xed','xee','xef','xeg','xeh','xei']
# fileNames = ['xej','xek','xel','xem','xen','xeo','xep']
# fileNames = ['xeq','xer','xes','xet','xeu','xev','xew']
# fileNames = ['xex','xey','xez','xfa','xfb','xfc','xfd']
# fileNames = ['xfe','xff','xfg','xfh','xfi','xfj','xfk']
# fileNames = ['xfl','xfm','xfn','xfo','xfp','xfq','xfr']
# fileNames = ['xfs','xft','xfu','xfv','xfw','xfx','xfy']
for filename in fileNames:
    # the filename formate is  'xbe'  'xbf'
    #======get data from file to ListDict

    #manipulate  filename into  the formate as "./SplitAs90000/xbe"
    fileName4Read = './SplitAs90000/' + filename
    file = open(fileName4Read,"r")
    try:
        lines = file.readlines()
        # print lines[0]
        # print lines[1]N
        # print lines[2]

        ListItems = []

        for s in lines:
            # print lines[s]
            items = s.split(",")
            # ListItems[3]=4
            ListItems.append({'tweetsID':items[0],'maliciousResult':items[1],'annotationMethod':items[2]})
    finally:
        file.close()



    print "get " +str(len(ListItems)) + "  lines data list[ dict {} ]"
    # print  ListItems[1999]["tweetsID"]
    #



    # #==========
    List4TweetsResponse = []
    running = True
    ListDicts = cycle(ListItems)
    stopIterationCounter = len(ListItems)
    counter = 0
    errorCounter=0
    #     # print tweetsID

    while running:
        if(counter ==stopIterationCounter):
            break
        DataDict = ListDicts.next()
        try:
            tweetsResonse = twitter_api.statuses.show(_id=DataDict["tweetsID"])
            tweetsResonse.maliciousResult = DataDict["maliciousResult"]
            tweetsResonse.annotationMethod = DataDict["annotationMethod"]
            List4TweetsResponse.append(tweetsResonse)
        # except tweepy.RateLimitError:
        #     time.sleep(60 * 15)
        #     # here sleep 15mins and drop the previouse id. No matter the id is valide or not. kind of bug
        #     print "rete limited , wait 15mins "
        #     continue

            # print json.dumps(List4TweetsResponse[0], indent=1)
            # print d["tweetsID"]
            # g=9+3
            # r=g/0
            # print List4TweetsResponse[0]
        except:
            print "catch error for " + DataDict["tweetsID"]
            errorCounter= errorCounter+1
        counter=counter+1
        # print DataDict
    try:
        print "the number of data withinfile " + str(len(List4TweetsResponse))
        print "the number of invalid data  " + str(errorCounter)
        print "total number of data" + str(len(List4TweetsResponse)+errorCounter)
    except:
        pass



    try:
        # manipulate  filename  into  the formate as "'xbeData.pkl'"
        fileName4Load = filename + 'Data.pkl'
        output = open(fileName4Load, 'w')

        # Pickle dictionary using protocol 0.
        print List4TweetsResponse[0].annotationMethod
        pickle.dump(List4TweetsResponse, output)
    finally:
        output.close()

#==============finish writing data to file======



#ListItems is list contains dic which can is the three values in dataset

# print ListItems[0]["tweetsID"]
# print twitter_api.statuses.show(_id=ListItems[0]["tweetsID"])


#
# s = twitter_api.statuses.show(_id=838727227256745984)
# print s
