import datetime
import InjectTweet2Mysql


#edit the reference variable on variablesSql and valuesSql ==> suit for
# insert statement.
#this method only can manipulate the variable which its type is bool , int , unicode and none
def jointInsertTweetVarAndValue(tweet,variable,sqlVariables,sqlValues):
    sqlVariablesStr = ''
    sqlValuesStr = ''


    if variable in tweet:
        tpye_ = type(tweet[variable])
        value = tweet[variable]
        if (tpye_ == bool):
            if (value == True):
                sqlValuesStr='\'1\''
                sqlValues.append(sqlValuesStr)
            else:
                sqlValuesStr = '\'0\''
                sqlValues.append(sqlValuesStr)
        elif (tpye_ == int):
            sqlValuesStr = '\''+ str(value)+'\''
            sqlValues.append(sqlValuesStr)
        elif (tpye_ == unicode):
            utf8string_value = value.encode("utf-8")
            # replease the possible single quotes to \'
            utf8string_value = utf8string_value.replace("'", "\\\'")
            sqlValuesStr='\'' + utf8string_value + '\''
            sqlValues.append(sqlValuesStr)
        elif (str(tpye_) == '<type \'NoneType\'>'):
            sqlValuesStr = '\' None\''
            sqlValues.append(sqlValuesStr)
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : " + str(
                tpye_)
        sqlVariablesStr = '`' + variable + '`'
        sqlVariables.append(sqlVariablesStr)
    else:
        pass


# 1. append created_at(if exist) to sqlVariables and append its value to
# sqlValues
def appendCreated_at(tweet, sqlVariables, sqlValues):
    if('created_at' in tweet):
        # print tweet['created_at']
        created_atUnicode = tweet['created_at']
        created_at = datetime.datetime.strptime(created_atUnicode,
                                                "%a %b %d %H:%M:%S +0000 %Y").isoformat()
        utf8string_created_at = created_at.encode("utf-8")
        sqlVariablesStr = '`created_at`'
        sqlValuesStr = '\'' + utf8string_created_at + '\''
        sqlValues.append(sqlValuesStr)
        sqlVariables.append(sqlVariablesStr)

def appendHashtagRelated(tweet, sqlVariables, sqlValues):
    if('hashtags' in tweet['entities']):
        hashtags = tweet['entities']['hashtags']
        # print type(tweet['entities'])
        numberOfHashtags_c= len(hashtags)
        # print "hashtags is :"
        hashtags_list= []
        for hashtag in hashtags:
            hashtag = hashtag['text']
            utf8string_hashtag = hashtag.encode("utf-8")
            hashtags_list.append(utf8string_hashtag)
            # print hashtag
            # print type(hashtag)
        hashtags_c = ','.join(hashtags_list)

        # print hashtags_c
        # print type(hashtags_c)
        # print numberOfHashtags_c
        # sqlVariablesStr = '`hashtags_c`'
        # sqlValuesStr = '\'' + hashtags_c + '\''
        # sqlValues.append(sqlValuesStr)
        # sqlVariables.append(sqlVariablesStr)
        # sqlVariablesStr = '`numberOfHashtags_c`'
        # sqlValuesStr = '\'' + str(numberOfHashtags_c) + '\''
        # sqlValues.append(sqlValuesStr)
        # sqlVariables.append(sqlVariablesStr)
        appendValuseAndVariablse('`hashtags_c`',hashtags_c,sqlVariables, sqlValues)
        appendValuseAndVariablse('`numberOfHashtags_c`',numberOfHashtags_c,sqlVariables, sqlValues)


# get 3 variable(country & city & longtitude_latitude) append them into
# sqlvalues
def appendPlaceRelated(tweet, sqlVariables, sqlValues):

    # four pairs of [longitude, latitude] which form a please box.
    longtitude_latitude = ''
    country=''
    city=''
    # print tweet['user']['id']
    if ('place' in tweet):
        if(str(type(tweet['place']))!='<type \'NoneType\'>'):
            # print tweet['place']
            # print type(tweet['place'])
            # print "courntry Name:"
            if('country' in tweet['place']):
                country= tweet['place']['country']
                appendValuseAndVariablse('`country`',
                                         country,
                                     sqlVariables, sqlValues)
            # print type(tweet['place']['country'])
            if('full_name' in tweet['place']):
                city=tweet['place']['full_name']
                # print city
                utf8string_city = city.encode("utf-8")
                # print utf8string_city
                appendValuseAndVariablse('`city`',utf8string_city,sqlVariables, sqlValues)
                # print sqlValues
            # print type(tweet['place']['full_name'])
            if('bounding_box' in tweet['place']):
                if (str(type(tweet['place']['bounding_box'])) != '<type \'NoneType\'>'):
                    if('coordinates'in tweet['place']['bounding_box']):
                        longitudeAndLatitude = tweet['place']['bounding_box'][
                            'coordinates']
                        #this tweets contains 4 pairs of number in list
                        firstTime = True
                        for firstLayer in longitudeAndLatitude:
                            for secondLayer in firstLayer:
                                # print type(secondLayer)
                                for lastLayer in secondLayer:
                                    if (firstTime):
                                        longtitude_latitude = longtitude_latitude + str(
                                            lastLayer)
                                        firstTime = False
                                    else:
                                        longtitude_latitude = longtitude_latitude + ',' + str(
                                            lastLayer)
                        # str = ''.join(longitudeAndLatitude)
                    # sqlVariablesStr = '`longtitude_latitude`'
                    # sqlValuesStr = '\'' + str(longtitude_latitude) + '\''
                    # sqlValues.append(sqlValuesStr)
                    # sqlVariables.append(sqlVariablesStr)
                    appendValuseAndVariablse('`longtitude_latitude`',
                                             longtitude_latitude,
                                             sqlVariables,sqlValues)


        else:
            pass
            # print "place is none "

def appendUser (tweet, sqlVariables, sqlValues):
    if('user' in tweet):
        user =tweet['user']['id']
        appendValuseAndVariablse('`user`',user,sqlVariables, sqlValues)

# append maliciousMark and annotationMethod
def appendAnontationMark(tweet, sqlVariables, sqlValues):
    #using .rstrip()<--cause the origianl data contains \n
    if hasattr(tweet, 'annotationMethod'):
        annotationMethod =tweet.annotationMethod.rstrip()
        maliciousMark=tweet.maliciousResult
        appendValuseAndVariablse('`annotationMethod`', annotationMethod, sqlVariables, sqlValues)
        appendValuseAndVariablse('`maliciousMark`', maliciousMark, sqlVariables, sqlValues)

def appendRetweetedAndQutedStatus(tweet, sqlVariables, sqlValues,db,cursor):
    injectTweet2Mysql = InjectTweet2Mysql.injectTweet2Mysql
    if('quoted_status' in tweet):
        if (str(type(tweet['quoted_status'])) != '<type \'NoneType\'>'):
            sqlValuesStr = 1
            appendValuseAndVariablse('`quoted_status`', sqlValuesStr,sqlVariables, sqlValues)
            injectTweet2Mysql(tweet['quoted_status'],db,cursor)


    if('retweeted_status' in tweet):
        if (str(type(tweet['retweeted_status'])) != '<type \'NoneType\'>'):
            sqlValuesStr = 1
            appendValuseAndVariablse('`retweeted_status`', sqlValuesStr,sqlVariables, sqlValues)
            injectTweet2Mysql(tweet['retweeted_status'], db, cursor)



def appendValuseAndVariablse(variable,value,sqlVariables, sqlValues):
    sqlVariablesStr = variable
    # print value
    # print str(value)
    sqlValuesStr = '\'' + str(value) + '\''
    sqlValues.append(sqlValuesStr)
    sqlVariables.append(sqlVariablesStr)

def InsertTweetsSQLStr(tweet,db,cursor):

    variablses = ['id','text','favorite_count','favorited',
                  'retweet_count','retweeted','possibly_sensitive',
                  'withheld_copyright']
    variablesSql = []
    valuesSql = []
    for variable in variablses:
        #get the variablesql and valusesql which suit this function
        jointInsertTweetVarAndValue(tweet,variable,variablesSql,valuesSql)

    # append creat_at
    appendCreated_at(tweet, variablesSql, valuesSql);

    #append hashtag and place related variables
    appendHashtagRelated(tweet, variablesSql, valuesSql)
    appendPlaceRelated(tweet, variablesSql, valuesSql)
    appendUser(tweet, variablesSql, valuesSql)
    appendAnontationMark(tweet, variablesSql, valuesSql)
    appendRetweetedAndQutedStatus(tweet, variablesSql, valuesSql,db,cursor)


    # for x in valuesSql:
    #     print x





    # print variablesSql
    # print
    # print valuesSql

    variablesSqlStr = ','.join(variablesSql)
    valuesSqlStr=','.join(valuesSql)
    finalsql = "INSERT INTO`Tweets`(" + variablesSqlStr + ")  VALUES("  + valuesSqlStr + ");"
    # print finalsql
    return finalsql