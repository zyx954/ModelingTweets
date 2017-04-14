import datetime

def JointUpdateSQL(tweet,variable,ListupdateVariablesAndValues):
    updateVariablesAndValues=''
    if variable in tweet['user']:
        ValueType=type(tweet['user'][variable])
        value = tweet['user'][variable]
        if (ValueType==bool):
            if (value==True):
                updateVariablesAndValues=updateVariablesAndValues+'`'+variable+'`'+' = \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues +'`'+variable+'`'+ '= \'0\''
        elif(ValueType==int):
            updateVariablesAndValues = updateVariablesAndValues + '`'+variable+'`'+'= \''+str(value)+'\''
        elif(ValueType==unicode):
            utf8string_value = value.encode("utf-8")
            utf8string_value = utf8string_value.replace("\'", "\\\'")
            updateVariablesAndValues = updateVariablesAndValues + '`'+variable+'`'+'= \'' + utf8string_value + '\''
        elif(str(ValueType)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + '`'+variable+'`'+'= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                ValueType)
    else:
        pass
    ListupdateVariablesAndValues.append(updateVariablesAndValues)

#just append the data , cause data need unique handle
def appendUpdateTime(tweet,ListupdateVariablesAndValues):
    # update user update time
    updateVariablesAndValues=''

    if 'created_at' in tweet:
        updateTimeTpye = type(tweet['created_at'])
        updateTimeUnicode = tweet['created_at']
        updateTime = datetime.datetime.strptime(updateTimeUnicode,
                                                "%a %b %d %H:%M:%S +0000 %Y").isoformat()
        if (updateTimeTpye == bool):
            if (updateTime == True):
                updateVariablesAndValues = updateVariablesAndValues + '`updateTime`=\'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + '`updateTime`=\'0\''
        elif (updateTimeTpye == int):
            updateVariablesAndValues = updateVariablesAndValues + '`updateTime`=' + '\'' + str(
                updateTime) + '\''
        elif (updateTimeTpye == unicode):
            utf8string_updateTime = updateTime.encode("utf-8")
            updateVariablesAndValues = updateVariablesAndValues +  \
                                                                  '`updateTime`=' + '\'' + utf8string_updateTime + '\''
        elif (str(updateTimeTpye) == '<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + '`updateTime`=\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : " + str(
                updateTimeTpye)
    else:
        pass
    ListupdateVariablesAndValues.append(updateVariablesAndValues)



def UpdateUserSQLStr(tweet):
    variables = ['followers_count','friends_count','description','url',
                 'contributors_enabled','default_profile','default_profile_image','favourites_count','is_translator','listed_count','name','notifications','protected','screen_name','statuses_count','verified','follow_request_sent','following','location'];
    ListupdateVariablesAndValues=[]
    for variable in variables:
        JointUpdateSQL(tweet,variable,ListupdateVariablesAndValues);
        # print ListupdateVariablesAndValues
    appendUpdateTime(tweet,ListupdateVariablesAndValues)
    # print ListupdateVariablesAndValues
    ListupdateVariablesAndValues=filter(None,ListupdateVariablesAndValues)
    updateVariablesAndValues=','.join(ListupdateVariablesAndValues)
    finalSql = 'UPDATE  `User` SET  ' + updateVariablesAndValues + '  WHERE ' '`id`=\'' + str(tweet['user']['id']) + '\';'
    print finalSql
    return finalSql

