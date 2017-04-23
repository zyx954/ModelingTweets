import datetime

def InsertUserSQLStr(tweet):
    # pass
    # print "this is user "
    # print tweet

    # print tweet['user']['protected']

    # get the templet from mysql workingbanch and the corresponding variable
        #for all varibale
        #for some variable.

    sqlValues=''
    sqlVariables=''

    #needs to varify if contains this varibale
    #  if can cast from int , bool , unicode,  str/int/datatime
        #for bool type in tweets-->cast to int 0/1

    #if both not work need to change

    if 'id' in tweet['user']:
        idTpye=type(tweet['user']['id'])
        id = tweet['user']['id']
        if (idTpye==bool):
            if (id==True):
                sqlValues=sqlValues+'\'1\''
            else:
                sqlValues = sqlValues + '\'0\''
        elif(idTpye==int):
            sqlValues = sqlValues + '\''+str(id)+'\''
        elif(idTpye==unicode):
            utf8string_id = id.encode("utf-8")
            sqlValues = sqlValues + '\'' + utf8string_id + '\''
        elif(str(idTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + '\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                idTpye)
        sqlVariables=sqlVariables+'`id`'
    else:
        pass
    if 'followers_count' in tweet['user']:
        followers_countTpye=type(tweet['user']['followers_count'])
        followers_count = tweet['user']['followers_count']
        if (followers_countTpye==bool):
            if (followers_count==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(followers_countTpye==int):
            sqlValues = sqlValues + ',\''+str(followers_count)+'\''
        elif(followers_countTpye==unicode):
            utf8string_followers_count = followers_count.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_followers_count + '\''
        elif(str(followers_countTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                followers_countTpye)
        sqlVariables=sqlVariables+',`followers_count`'
    else:
        pass
    if 'friends_count' in tweet['user']:
        friends_countTpye=type(tweet['user']['friends_count'])
        friends_count = tweet['user']['friends_count']
        if (friends_countTpye==bool):
            if (friends_count==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(friends_countTpye==int):
            sqlValues = sqlValues + ',\''+str(friends_count)+'\''
        elif(friends_countTpye==unicode):
            utf8string_friends_count = friends_count.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_friends_count + '\''
        elif(str(friends_countTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                friends_countTpye)
        sqlVariables=sqlVariables+',`friends_count`'
    else:
        pass
    if 'description' in tweet['user']:
        descriptionTpye=type(tweet['user']['description'])
        description = tweet['user']['description']
        if (descriptionTpye==bool):
            if (description==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(descriptionTpye==int):
            sqlValues = sqlValues + ',\''+str(description)+'\''
        elif(descriptionTpye==unicode):
            utf8string_description = description.encode("utf-8")
            # print utf8string_description
            utf8string_description=utf8string_description.replace("'","\\\'")
            # utf8string_description = utf8string_description.replace("\"",
            #                                                         "\\\\")
            # utf8string_description = utf8string_description.replace("\\",
            #                                                         "\\\\")
            # sqlValues = sqlValues + ',\'' + utf8string_description + '\''
            # sqlValues = sqlValues +  ','+'%s'
        elif(str(descriptionTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                descriptionTpye)
        sqlVariables=sqlVariables+',`description`'
    else:
        pass
    if 'url' in tweet['user']:
        urlTpye=type(tweet['user']['url'])
        url = tweet['user']['url']
        if (urlTpye==bool):
            if (url==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(urlTpye==int):
            sqlValues = sqlValues + ',\''+str(url)+'\''
        elif(urlTpye==unicode):
            utf8string_url = url.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_url + '\''
        elif(str(urlTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                urlTpye)
        sqlVariables=sqlVariables+',`url`'
    else:
        pass
    if 'contributors_enabled' in tweet['user']:
        contributors_enabledTpye=type(tweet['user']['contributors_enabled'])
        contributors_enabled = tweet['user']['contributors_enabled']
        if (contributors_enabledTpye==bool):
            if (contributors_enabled==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(contributors_enabledTpye==int):
            sqlValues = sqlValues + ',\''+str(contributors_enabled)+'\''
        elif(contributors_enabledTpye==unicode):
            utf8string_contributors_enabled = contributors_enabled.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_contributors_enabled + '\''
        elif(str(contributors_enabledTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                contributors_enabledTpye)
        sqlVariables=sqlVariables+',`contributors_enabled`'
    else:
        pass
    if 'created_at' in tweet['user']:
        created_atTpye=type(tweet['user']['created_at'])
        created_at_Unicode = tweet['user']['created_at']
        created_at = datetime.datetime.strptime(created_at_Unicode,
                                                "%a %b %d %H:%M:%S +0000 %Y").isoformat()
        if (created_atTpye==bool):
            if (created_at==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(created_atTpye==int):
            sqlValues = sqlValues + ',\''+str(created_at)+'\''
        elif(created_atTpye==unicode):
            utf8string_created_at = created_at.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_created_at + '\''
        elif(str(created_atTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                created_atTpye)
        sqlVariables=sqlVariables+',`created_at`'
    else:
        pass
    if 'default_profile' in tweet['user']:
        default_profileTpye=type(tweet['user']['default_profile'])
        default_profile = tweet['user']['default_profile']
        if (default_profileTpye==bool):
            if (default_profile==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(default_profileTpye==int):
            sqlValues = sqlValues + ',\''+str(default_profile)+'\''
        elif(default_profileTpye==unicode):
            utf8string_default_profile = default_profile.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_default_profile + '\''
        elif(str(default_profileTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                default_profileTpye)
        sqlVariables=sqlVariables+',`default_profile`'
    else:
        pass
    if 'default_profile_image' in tweet['user']:
        default_profile_imageTpye=type(tweet['user']['default_profile_image'])
        default_profile_image = tweet['user']['default_profile_image']
        if (default_profile_imageTpye==bool):
            if (default_profile_image==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(default_profile_imageTpye==int):
            sqlValues = sqlValues + ',\''+str(default_profile_image)+'\''
        elif(default_profile_imageTpye==unicode):
            utf8string_default_profile_image = default_profile_image.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_default_profile_image + '\''
        elif(str(default_profile_imageTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                default_profile_imageTpye)
        sqlVariables=sqlVariables+',`default_profile_image`'
    else:
        pass
    if 'favourites_count' in tweet['user']:
        favourites_countTpye=type(tweet['user']['favourites_count'])
        favourites_count = tweet['user']['favourites_count']
        if (favourites_countTpye==bool):
            if (favourites_count==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(favourites_countTpye==int):
            sqlValues = sqlValues + ',\''+str(favourites_count)+'\''
        elif(favourites_countTpye==unicode):
            utf8string_favourites_count = favourites_count.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_favourites_count + '\''
        elif(str(favourites_countTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                favourites_countTpye)
        sqlVariables=sqlVariables+',`favourites_count`'
    else:
        pass
    if 'is_translator' in tweet['user']:
        is_translatorTpye=type(tweet['user']['is_translator'])
        is_translator = tweet['user']['is_translator']
        if (is_translatorTpye==bool):
            if (is_translator==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(is_translatorTpye==int):
            sqlValues = sqlValues + ',\''+str(is_translator)+'\''
        elif(is_translatorTpye==unicode):
            utf8string_is_translator = is_translator.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_is_translator + '\''
        elif(str(is_translatorTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                is_translatorTpye)
        sqlVariables=sqlVariables+',`is_translator`'
    else:
        pass
    if 'listed_count' in tweet['user']:
        listed_countTpye=type(tweet['user']['listed_count'])
        listed_count = tweet['user']['listed_count']
        if (listed_countTpye==bool):
            if (listed_count==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(listed_countTpye==int):
            sqlValues = sqlValues + ',\''+str(listed_count)+'\''
        elif(listed_countTpye==unicode):
            utf8string_listed_count = listed_count.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_listed_count + '\''
        elif(str(listed_countTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                listed_countTpye)
        sqlVariables=sqlVariables+',`listed_count`'
    else:
        pass
    if 'name' in tweet['user']:
        nameTpye=type(tweet['user']['name'])
        name = tweet['user']['name']
        if (nameTpye==bool):
            if (name==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(nameTpye==int):
            sqlValues = sqlValues + ',\''+str(name)+'\''
        elif(nameTpye==unicode):
            utf8string_name = name.encode("utf-8")
            utf8string_name = utf8string_name.replace("'","\\\'")
            sqlValues = sqlValues + ',\'' + utf8string_name + '\''
        elif(str(nameTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                nameTpye)
        sqlVariables=sqlVariables+',`name`'
    else:
        pass
    if 'notifications' in tweet['user']:
        notificationsTpye=type(tweet['user']['notifications'])
        notifications = tweet['user']['notifications']
        if (notificationsTpye==bool):
            if (notifications==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(notificationsTpye==int):
            sqlValues = sqlValues + ',\''+str(notifications)+'\''
        elif(notificationsTpye==unicode):
            utf8string_notifications = notifications.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_notifications + '\''
        elif(str(notificationsTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                notificationsTpye)
        sqlVariables=sqlVariables+',`notifications`'
    else:
        pass
    if 'protected' in tweet['user']:
        protectedTpye=type(tweet['user']['protected'])
        protected = tweet['user']['protected']
        if (protectedTpye==bool):
            if (protected==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(protectedTpye==int):
            sqlValues = sqlValues + ',\''+str(protected)+'\''
        elif(protectedTpye==unicode):
            utf8string_protected = protected.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_protected + '\''
        elif(str(protectedTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                protectedTpye)
        sqlVariables=sqlVariables+',`protected`'
    else:
        pass
    if 'screen_name' in tweet['user']:
        screen_nameTpye=type(tweet['user']['screen_name'])
        screen_name = tweet['user']['screen_name']
        if (screen_nameTpye==bool):
            if (screen_name==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(screen_nameTpye==int):
            sqlValues = sqlValues + ',\''+str(screen_name)+'\''
        elif(screen_nameTpye==unicode):
            utf8string_screen_name = screen_name.encode("utf-8")
            utf8string_screen_name=utf8string_screen_name.replace("'","\\\'")
            sqlValues = sqlValues + ',\'' + utf8string_screen_name + '\''
        elif(str(screen_nameTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                screen_nameTpye)
        sqlVariables=sqlVariables+',`screen_name`'
    else:
        pass
    if 'statuses_count' in tweet['user']:
        statuses_countTpye=type(tweet['user']['statuses_count'])
        statuses_count = tweet['user']['statuses_count']
        if (statuses_countTpye==bool):
            if (statuses_count==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(statuses_countTpye==int):
            sqlValues = sqlValues + ',\''+str(statuses_count)+'\''
        elif(statuses_countTpye==unicode):
            utf8string_statuses_count = statuses_count.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_statuses_count + '\''
        elif(str(statuses_countTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                statuses_countTpye)
        sqlVariables=sqlVariables+',`statuses_count`'
    else:
        pass
    if 'verified' in tweet['user']:
        verifiedTpye=type(tweet['user']['verified'])
        verified = tweet['user']['verified']
        if (verifiedTpye==bool):
            if (verified==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(verifiedTpye==int):
            sqlValues = sqlValues + ',\''+str(verified)+'\''
        elif(verifiedTpye==unicode):
            utf8string_verified = verified.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_verified + '\''
        elif(str(verifiedTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                verifiedTpye)
        sqlVariables=sqlVariables+',`verified`'
    else:
        pass
    if 'follow_request_sent' in tweet['user']:
        follow_request_sentTpye=type(tweet['user']['follow_request_sent'])
        follow_request_sent = tweet['user']['follow_request_sent']
        if (follow_request_sentTpye==bool):
            if (follow_request_sent==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(follow_request_sentTpye==int):
            sqlValues = sqlValues + ',\''+str(follow_request_sent)+'\''
        elif(follow_request_sentTpye==unicode):
            utf8string_follow_request_sent = follow_request_sent.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_follow_request_sent + '\''
        elif(str(follow_request_sentTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                follow_request_sentTpye)
        sqlVariables=sqlVariables+',`follow_request_sent`'
    else:
        pass
    if 'following' in tweet['user']:
        followingTpye=type(tweet['user']['following'])
        following = tweet['user']['following']
        if (followingTpye==bool):
            if (following==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(followingTpye==int):
            sqlValues = sqlValues + ',\''+str(following)+'\''
        elif(followingTpye==unicode):
            utf8string_following = following.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_following + '\''
        elif(str(followingTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                followingTpye)
        sqlVariables=sqlVariables+',`following`'
    else:
        pass
    if 'location' in tweet['user']:
        locationTpye=type(tweet['user']['location'])
        location = tweet['user']['location']
        if (locationTpye==bool):
            if (location==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(locationTpye==int):
            sqlValues = sqlValues + ',\''+str(location)+'\''
        elif(locationTpye==unicode):
            utf8string_location = location.encode("utf-8")
            utf8string_location=utf8string_location.replace("'","\\\'")
            sqlValues = sqlValues + ',\'' + utf8string_location + '\''
        elif(str(locationTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                locationTpye)
        sqlVariables=sqlVariables+',`location`'
    else:
        pass

    #this created_at is direct to time in tweets rather than in user
    # created_at variable
    if 'created_at' in tweet:
        updateTimeTpye=type(tweet['created_at'])
        updateTimeUnicode = tweet['created_at']
        updateTime = datetime.datetime.strptime(updateTimeUnicode,
                                       "%a %b %d %H:%M:%S +0000 %Y").isoformat()
        if (updateTimeTpye==bool):
            if (updateTime==True):
                sqlValues=sqlValues+',\'1\''
            else:
                sqlValues = sqlValues + ',\'0\''
        elif(updateTimeTpye==int):
            sqlValues = sqlValues + ',\''+str(updateTime)+'\''
        elif(updateTimeTpye==unicode):
            utf8string_updateTime = updateTime.encode("utf-8")
            sqlValues = sqlValues + ',\'' + utf8string_updateTime + '\''
        elif(str(updateTimeTpye)=='<type \'NoneType\'>'):
            sqlValues = sqlValues + ',\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                updateTimeTpye)
        sqlVariables=sqlVariables+',`updateTime`'
    else:
        pass


    # assert(tweet['user']['id']
    # print test

    # if(tweet['user']['id'] != null):
    #     sqlValues=sqlVariables+str(tweet['user']['id'])
    #     sqlVariables = sqlVariables+'\'id\''
    # if()
    # print sqlVariables
    # print sqlValues

    # finalSql =
    finalSql = 'INSERT INTO `User` ' + '(' + sqlVariables + ')' + ' VALUES ' + \
          '(' + sqlValues + ')'
    # print finalSql
    return finalSql
