import datetime

def UpdateUserSQLStr(tweet):

    updateVariablesAndValues=''
    # get
    # if 'followers_count' in tweet['user']:
    #     followers_countTpye=type(tweet['user']['followers_count'])
    #     followers_count = tweet['user']['followers_count']
    #     if (followers_countTpye==bool):
    #         if (followers_count==True):
    #             updateVariablesAndValues=updateVariablesAndValues+',`followers_count`= \'1\''
    #         else:
    #             updateVariablesAndValues = updateVariablesAndValues + ',`followers_count`= \'0\''
    #     elif(followers_countTpye==int):
    #         updateVariablesAndValues = updateVariablesAndValues + ',`followers_count`= \''+str(followers_count)+'\''
    #     elif(followers_countTpye==unicode):
    #         utf8string_followers_count = followers_count.encode("utf-8")
    #         utf8string_followers_count=utf8string_followers_count.replace("\'","\\\'")
    #         updateVariablesAndValues = updateVariablesAndValues + ',`followers_count`= \'' + utf8string_followers_count + '\''
    #     elif(str(followers_countTpye)=='<type \'NoneType\'>'):
    #         updateVariablesAndValues = updateVariablesAndValues + ',`followers_count`= \'none\''
    #     else:
    #         print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
    #             followers_countTpye)
    # else:
    #     pass

    if 'followers_count' in tweet['user']:
        followers_countTpye=type(tweet['user']['followers_count'])
        followers_count = tweet['user']['followers_count']
        if (followers_countTpye==bool):
            if (followers_count==True):
                updateVariablesAndValues=updateVariablesAndValues+'`followers_count`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + '`followers_count`= \'0\''
        elif(followers_countTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + '`followers_count`= \''+str(followers_count)+'\''
        elif(followers_countTpye==unicode):
            utf8string_followers_count = followers_count.encode("utf-8")
            updateVariablesAndValues = updateVariablesAndValues + '`followers_count`= \'' + utf8string_followers_count + '\''
        elif(str(followers_countTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + '`followers_count`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                followers_countTpye)
    else:
        pass


    if 'friends_count' in tweet['user']:
        friends_countTpye=type(tweet['user']['friends_count'])
        friends_count = tweet['user']['friends_count']
        if (friends_countTpye==bool):
            if (friends_count==True):
                updateVariablesAndValues=updateVariablesAndValues+',`friends_count`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`friends_count`= \'0\''
        elif(friends_countTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`friends_count`= \''+str(friends_count)+'\''
        elif(friends_countTpye==unicode):
            utf8string_friends_count = friends_count.encode("utf-8")
            utf8string_friends_count=utf8string_friends_count.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`friends_count`= \'' + utf8string_friends_count + '\''
        elif(str(friends_countTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`friends_count`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                friends_countTpye)
    else:
        pass

    if 'description' in tweet['user']:
        descriptionTpye=type(tweet['user']['description'])
        description = tweet['user']['description']
        if (descriptionTpye==bool):
            if (description==True):
                updateVariablesAndValues=updateVariablesAndValues+',`description`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`description`= \'0\''
        elif(descriptionTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`description`= \''+str(description)+'\''
        elif(descriptionTpye==unicode):
            utf8string_description = description.encode("utf-8")
            utf8string_description=utf8string_description.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`description`= \'' + utf8string_description + '\''
        elif(str(descriptionTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`description`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                descriptionTpye)
    else:
        pass

    if 'url' in tweet['user']:
        urlTpye=type(tweet['user']['url'])
        url = tweet['user']['url']
        if (urlTpye==bool):
            if (url==True):
                updateVariablesAndValues=updateVariablesAndValues+',`url`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`url`= \'0\''
        elif(urlTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`url`= \''+str(url)+'\''
        elif(urlTpye==unicode):
            utf8string_url = url.encode("utf-8")
            utf8string_url=utf8string_url.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`url`= \'' + utf8string_url + '\''
        elif(str(urlTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`url`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                urlTpye)
    else:
        pass

    if 'contributors_enabled' in tweet['user']:
        contributors_enabledTpye=type(tweet['user']['contributors_enabled'])
        contributors_enabled = tweet['user']['contributors_enabled']
        if (contributors_enabledTpye==bool):
            if (contributors_enabled==True):
                updateVariablesAndValues=updateVariablesAndValues+',`contributors_enabled`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`contributors_enabled`= \'0\''
        elif(contributors_enabledTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`contributors_enabled`= \''+str(contributors_enabled)+'\''
        elif(contributors_enabledTpye==unicode):
            utf8string_contributors_enabled = contributors_enabled.encode("utf-8")
            utf8string_contributors_enabled=utf8string_contributors_enabled.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`contributors_enabled`= \'' + utf8string_contributors_enabled + '\''
        elif(str(contributors_enabledTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`contributors_enabled`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                contributors_enabledTpye)
    else:
        pass

    if 'default_profile' in tweet['user']:
        default_profileTpye=type(tweet['user']['default_profile'])
        default_profile = tweet['user']['default_profile']
        if (default_profileTpye==bool):
            if (default_profile==True):
                updateVariablesAndValues=updateVariablesAndValues+',`default_profile`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`default_profile`= \'0\''
        elif(default_profileTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`default_profile`= \''+str(default_profile)+'\''
        elif(default_profileTpye==unicode):
            utf8string_default_profile = default_profile.encode("utf-8")
            utf8string_default_profile=utf8string_default_profile.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`default_profile`= \'' + utf8string_default_profile + '\''
        elif(str(default_profileTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`default_profile`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                default_profileTpye)
    else:
        pass

    if 'default_profile_image' in tweet['user']:
        default_profile_imageTpye=type(tweet['user']['default_profile_image'])
        default_profile_image = tweet['user']['default_profile_image']
        if (default_profile_imageTpye==bool):
            if (default_profile_image==True):
                updateVariablesAndValues=updateVariablesAndValues+',`default_profile_image`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`default_profile_image`= \'0\''
        elif(default_profile_imageTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`default_profile_image`= \''+str(default_profile_image)+'\''
        elif(default_profile_imageTpye==unicode):
            utf8string_default_profile_image = default_profile_image.encode("utf-8")
            utf8string_default_profile_image=utf8string_default_profile_image.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`default_profile_image`= \'' + utf8string_default_profile_image + '\''
        elif(str(default_profile_imageTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`default_profile_image`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                default_profile_imageTpye)
    else:
        pass

    if 'favourites_count' in tweet['user']:
        favourites_countTpye=type(tweet['user']['favourites_count'])
        favourites_count = tweet['user']['favourites_count']
        if (favourites_countTpye==bool):
            if (favourites_count==True):
                updateVariablesAndValues=updateVariablesAndValues+',`favourites_count`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`favourites_count`= \'0\''
        elif(favourites_countTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`favourites_count`= \''+str(favourites_count)+'\''
        elif(favourites_countTpye==unicode):
            utf8string_favourites_count = favourites_count.encode("utf-8")
            utf8string_favourites_count=utf8string_favourites_count.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`favourites_count`= \'' + utf8string_favourites_count + '\''
        elif(str(favourites_countTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`favourites_count`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                favourites_countTpye)
    else:
        pass

    if 'is_translator' in tweet['user']:
        is_translatorTpye=type(tweet['user']['is_translator'])
        is_translator = tweet['user']['is_translator']
        if (is_translatorTpye==bool):
            if (is_translator==True):
                updateVariablesAndValues=updateVariablesAndValues+',`is_translator`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`is_translator`= \'0\''
        elif(is_translatorTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`is_translator`= \''+str(is_translator)+'\''
        elif(is_translatorTpye==unicode):
            utf8string_is_translator = is_translator.encode("utf-8")
            utf8string_is_translator=utf8string_is_translator.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`is_translator`= \'' + utf8string_is_translator + '\''
        elif(str(is_translatorTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`is_translator`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                is_translatorTpye)
    else:
        pass

    if 'listed_count' in tweet['user']:
        listed_countTpye=type(tweet['user']['listed_count'])
        listed_count = tweet['user']['listed_count']
        if (listed_countTpye==bool):
            if (listed_count==True):
                updateVariablesAndValues=updateVariablesAndValues+',`listed_count`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`listed_count`= \'0\''
        elif(listed_countTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`listed_count`= \''+str(listed_count)+'\''
        elif(listed_countTpye==unicode):
            utf8string_listed_count = listed_count.encode("utf-8")
            utf8string_listed_count=utf8string_listed_count.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`listed_count`= \'' + utf8string_listed_count + '\''
        elif(str(listed_countTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`listed_count`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                listed_countTpye)
    else:
        pass

    if 'name' in tweet['user']:
        nameTpye=type(tweet['user']['name'])
        name = tweet['user']['name']
        if (nameTpye==bool):
            if (name==True):
                updateVariablesAndValues=updateVariablesAndValues+',`name`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`name`= \'0\''
        elif(nameTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`name`= \''+str(name)+'\''
        elif(nameTpye==unicode):
            utf8string_name = name.encode("utf-8")
            utf8string_name=utf8string_name.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`name`= \'' + utf8string_name + '\''
        elif(str(nameTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`name`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                nameTpye)
    else:
        pass

    if 'notifications' in tweet['user']:
        notificationsTpye=type(tweet['user']['notifications'])
        notifications = tweet['user']['notifications']
        if (notificationsTpye==bool):
            if (notifications==True):
                updateVariablesAndValues=updateVariablesAndValues+',`notifications`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`notifications`= \'0\''
        elif(notificationsTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`notifications`= \''+str(notifications)+'\''
        elif(notificationsTpye==unicode):
            utf8string_notifications = notifications.encode("utf-8")
            utf8string_notifications=utf8string_notifications.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`notifications`= \'' + utf8string_notifications + '\''
        elif(str(notificationsTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`notifications`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                notificationsTpye)
    else:
        pass

    if 'protected' in tweet['user']:
        protectedTpye=type(tweet['user']['protected'])
        protected = tweet['user']['protected']
        if (protectedTpye==bool):
            if (protected==True):
                updateVariablesAndValues=updateVariablesAndValues+',`protected`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`protected`= \'0\''
        elif(protectedTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`protected`= \''+str(protected)+'\''
        elif(protectedTpye==unicode):
            utf8string_protected = protected.encode("utf-8")
            utf8string_protected=utf8string_protected.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`protected`= \'' + utf8string_protected + '\''
        elif(str(protectedTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`protected`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                protectedTpye)
    else:
        pass

    if 'screen_name' in tweet['user']:
        screen_nameTpye=type(tweet['user']['screen_name'])
        screen_name = tweet['user']['screen_name']
        if (screen_nameTpye==bool):
            if (screen_name==True):
                updateVariablesAndValues=updateVariablesAndValues+',`screen_name`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`screen_name`= \'0\''
        elif(screen_nameTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`screen_name`= \''+str(screen_name)+'\''
        elif(screen_nameTpye==unicode):
            utf8string_screen_name = screen_name.encode("utf-8")
            utf8string_screen_name=utf8string_screen_name.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`screen_name`= \'' + utf8string_screen_name + '\''
        elif(str(screen_nameTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`screen_name`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                screen_nameTpye)
    else:
        pass

    if 'statuses_count' in tweet['user']:
        statuses_countTpye=type(tweet['user']['statuses_count'])
        statuses_count = tweet['user']['statuses_count']
        if (statuses_countTpye==bool):
            if (statuses_count==True):
                updateVariablesAndValues=updateVariablesAndValues+',`statuses_count`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`statuses_count`= \'0\''
        elif(statuses_countTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`statuses_count`= \''+str(statuses_count)+'\''
        elif(statuses_countTpye==unicode):
            utf8string_statuses_count = statuses_count.encode("utf-8")
            utf8string_statuses_count=utf8string_statuses_count.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`statuses_count`= \'' + utf8string_statuses_count + '\''
        elif(str(statuses_countTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`statuses_count`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                statuses_countTpye)
    else:
        pass

    if 'verified' in tweet['user']:
        verifiedTpye=type(tweet['user']['verified'])
        verified = tweet['user']['verified']
        if (verifiedTpye==bool):
            if (verified==True):
                updateVariablesAndValues=updateVariablesAndValues+',`verified`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`verified`= \'0\''
        elif(verifiedTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`verified`= \''+str(verified)+'\''
        elif(verifiedTpye==unicode):
            utf8string_verified = verified.encode("utf-8")
            utf8string_verified=utf8string_verified.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`verified`= \'' + utf8string_verified + '\''
        elif(str(verifiedTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`verified`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                verifiedTpye)
    else:
        pass

    if 'follow_request_sent' in tweet['user']:
        follow_request_sentTpye=type(tweet['user']['follow_request_sent'])
        follow_request_sent = tweet['user']['follow_request_sent']
        if (follow_request_sentTpye==bool):
            if (follow_request_sent==True):
                updateVariablesAndValues=updateVariablesAndValues+',`follow_request_sent`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`follow_request_sent`= \'0\''
        elif(follow_request_sentTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`follow_request_sent`= \''+str(follow_request_sent)+'\''
        elif(follow_request_sentTpye==unicode):
            utf8string_follow_request_sent = follow_request_sent.encode("utf-8")
            utf8string_follow_request_sent=utf8string_follow_request_sent.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`follow_request_sent`= \'' + utf8string_follow_request_sent + '\''
        elif(str(follow_request_sentTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`follow_request_sent`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                follow_request_sentTpye)
    else:
        pass

    if 'following' in tweet['user']:
        followingTpye=type(tweet['user']['following'])
        following = tweet['user']['following']
        if (followingTpye==bool):
            if (following==True):
                updateVariablesAndValues=updateVariablesAndValues+',`following`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`following`= \'0\''
        elif(followingTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`following`= \''+str(following)+'\''
        elif(followingTpye==unicode):
            utf8string_following = following.encode("utf-8")
            utf8string_following=utf8string_following.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`following`= \'' + utf8string_following + '\''
        elif(str(followingTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`following`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                followingTpye)
    else:
        pass

    if 'location' in tweet['user']:
        locationTpye=type(tweet['user']['location'])
        location = tweet['user']['location']
        if (locationTpye==bool):
            if (location==True):
                updateVariablesAndValues=updateVariablesAndValues+',`location`= \'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`location`= \'0\''
        elif(locationTpye==int):
            updateVariablesAndValues = updateVariablesAndValues + ',`location`= \''+str(location)+'\''
        elif(locationTpye==unicode):
            utf8string_location = location.encode("utf-8")
            utf8string_location=utf8string_location.replace("\'","\\\'")
            updateVariablesAndValues = updateVariablesAndValues + ',`location`= \'' + utf8string_location + '\''
        elif(str(locationTpye)=='<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`location`= \'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
                locationTpye)
    else:
        pass

    # if 'updateTime' in tweet['user']:
    #     updateTimeTpye=type(tweet['user']['updateTime'])
    #     updateTime = tweet['user']['updateTime']
    #     if (updateTimeTpye==bool):
    #         if (updateTime==True):
    #             updateVariablesAndValues=updateVariablesAndValues+',`updateTime`= \'1\''
    #         else:
    #             updateVariablesAndValues = updateVariablesAndValues + ',`updateTime`= \'0\''
    #     elif(updateTimeTpye==int):
    #         updateVariablesAndValues = updateVariablesAndValues + ',`updateTime`= \''+str(updateTime)+'\''
    #     elif(updateTimeTpye==unicode):
    #         utf8string_updateTime = updateTime.encode("utf-8")
    #         utf8string_updateTime=utf8string_updateTime.replace("\'","\\\'")
    #         updateVariablesAndValues = updateVariablesAndValues + ',`updateTime`= \'' + utf8string_updateTime + '\''
    #     elif(str(updateTimeTpye)=='<type \'NoneType\'>'):
    #         updateVariablesAndValues = updateVariablesAndValues + ',`updateTime`= \'none\''
    #     else:
    #         print "@@@@@@ ERROR: There one unexpected type exist.it is : "+ str(
    #             updateTimeTpye)
    # else:
    #     pass

    #update user update time
    if 'created_at' in tweet:
        updateTimeTpye = type(tweet['created_at'])
        updateTimeUnicode = tweet['created_at']
        updateTime = datetime.datetime.strptime(updateTimeUnicode,
                                                "%a %b %d %H:%M:%S +0000 %Y").isoformat()
        if (updateTimeTpye == bool):
            if (updateTime == True):
                updateVariablesAndValues = updateVariablesAndValues + ',`updateTime`=\'1\''
            else:
                updateVariablesAndValues = updateVariablesAndValues + ',`updateTime`=\'0\''
        elif (updateTimeTpye == int):
            updateVariablesAndValues = updateVariablesAndValues + ',`updateTime`=' + '\''+str(updateTime) +'\''
        elif (updateTimeTpye == unicode):
            utf8string_updateTime = updateTime.encode("utf-8")
            updateVariablesAndValues = updateVariablesAndValues + ',' \
                                                                  '`updateTime`=' + '\''+utf8string_updateTime + '\''
        elif (str(updateTimeTpye) == '<type \'NoneType\'>'):
            updateVariablesAndValues = updateVariablesAndValues + ',`updateTime`=\'none\''
        else:
            print "@@@@@@ ERROR: There one unexpected type exist.it is : " + str(
                updateTimeTpye)
        # sqlVariables = sqlVariables + ',`updateTime`'
    else:
        pass


    finalSql =  'UPDATE  `User` SET  '+ updateVariablesAndValues + '  WHERE ' \
                                                                '`id`=\''+str(tweet['user']['id'])+'\';'



    print finalSql
    return "finnal update sql "


def