
# import pickle

from string import ascii_uppercase


def GettingInstanceFromTweets(instance,NEGATIVE_opinion_words,
                              spamHashtags_set_l,verbose=1):
    #based on the metadata from data generate corresponding feature valuse
    # from tweets
    # within instance
    # [0] numberOfHashtags_c,
    # [1]text,
    # [2]hashtags_c,
    # [3]user,
    # [4]maliciousMark

    # instanceOfTweets[0] = hashtags_more_two
    # instanceOfTweets[1] = exclamation_sign
    # instanceOfTweets[2] = url_in_tweets
    # instanceOfTweets[3] = suffix_hashtag
    # instanceOfTweets[4] = spammy_hashtag
    # instanceOfTweets[5] = negative_words
    # instanceOfTweets[6] = upper_case_characters
    # instanceOfTweets[7] = capitalized_hashtag

    hashtags_more_two = 0
    exclamation_sign = 0
    url_in_tweets = 0
    suffix_hashtag = 0
    spammy_hashtag = 0
    negative_words = 0
    upper_case_characters = 0
    capitalized_hashtag = 0


    instanceOfTweets = []
    numberOfHashtags_c= instance[0]
    text = instance[1]
    hashtags_c = instance[2]

    # firstTime = True
    # if (firstTime):
    if(verbose):
        print "text is : " + text
        print "hashtags_c is " + hashtags_c
        print "numberOfHashtags_c is " + str(numberOfHashtags_c)
        # verbose=0
        # firstTime=

    if (numberOfHashtags_c>2):
        hashtags_more_two=1
    if ('!' in text):
        exclamation_sign=1
    if('http' in text.lower()):
        url_in_tweets=1
    if ('suffix' in text.lower()):
        suffix_hashtag=1
    if (containsSpammy_hashtag(hashtags_c,spamHashtags_set_l,verbose)):
        spammy_hashtag = 1

    if (containsNegative_words(text,NEGATIVE_opinion_words,verbose)):
        negative_words = 1

    if(textIsUpperCaseCharacters(text,verbose)):
        upper_case_characters=1
    if(containsCapitalized_hashtag(hashtags_c,verbose)):
        capitalized_hashtag=1


    instanceOfTweets.append(hashtags_more_two)
    instanceOfTweets.append(exclamation_sign)
    instanceOfTweets.append(url_in_tweets)
    instanceOfTweets.append(suffix_hashtag)
    instanceOfTweets.append(spammy_hashtag)
    instanceOfTweets.append(negative_words)
    instanceOfTweets.append(upper_case_characters)
    instanceOfTweets.append(capitalized_hashtag)




    return instanceOfTweets
    #eg : [1,0,1,1,1,1,1,1]




    pass

def textIsUpperCaseCharacters(text, verbose = True):
    #if 25% of characters in text is upcase return true
    if text:
        # strs = 'tesTtT  Test hhhhhhhh T'
        length = len(text.replace(' ', ''))
        count = len([letter for letter in text if letter in ascii_uppercase])
        if verbose:
            print  length, count, count / float(length)
        if(count / float(length)>0.25):
            return True
        else:
            return False
        pass
    else:
        #test is empty , so < 25% , return false
        return False

def containsCapitalized_hashtag(hashtags_c,verbose=True):
    # if one hashtag are caputalized return True
    #eg hashtags_c =>  'android,androidgames,gameinsight'
    # print hashtags_c
    result = False
    if hashtags_c:
        #consider if one of hashtag is caputalized or not
        hashtags = hashtags_c.split(',')
        for h in hashtags:
            if(h.isupper()):

                if(verbose):
                    print "this is on upper "
                    print h

                result= True
        pass
        return result

    else:
        #the hashtags_c is empty<--this will consider as false
        return result

def containsSpammy_hashtag(hashtags_c,spamHashtags_set_l,verbose=1):
    #compare hashtags with a list of spammy hashtages in the paper.
    if hashtags_c:
        # read spammy hashtags
        hashtags_List = hashtags_c.split(',')
        hashtags_Set_l = set([x.lower() for x in hashtags_List])
        # extract these calculation to outside
        # spamHashtags_set = (
        # ['TEAMFOLLOWBACK', 'TFBJP', 'gameinsight', 'androidgames', 'OPENFOLLOW',
        #  'androidgames', 'FF', 'RETWEET', 'IPADGAMES', 'RT', 'SougoFollow',
        #  'ipad', 'FOLLOWBACK', 'THF', 'FOLLOWNGAIN', '500aday', 'AUTOFOLLOW',
        #  'MUSTFOLLOW', 'TEAMHITFOLLOW', 'HITFOLLOWSTEAM'])
        # spamHashtags_set_l = set([x.lower() for x in spamHashtags_set])
        overlap = hashtags_Set_l & spamHashtags_set_l


        # print spamHashtags_set_l
        if(overlap):
            # contains spamHashtag
            if verbose:
                print "overlap spamtags is : " + str(overlap)
            return True
        else:
            # not contain
            return False

        pass

    else:
        return False


def containsNegative_words(text,NEGATIVE_opinion_words,verbose = 1):
    if text:
        # transfer text to list , then
        text_list = text.split(' ')
        text_set=set([x.lower() for x in text_list])
        # print text_set

        # transfer nagative opinion words to list
        # try:
        #     file = open("NEGATIVE_opinion_words")
        #     # lines = file.readlines()
        #     lines = file.read().splitlines()
        #     NEGATIVE_opinion_words = set(lines)
        containsNegatie = NEGATIVE_opinion_words & text_set
        if verbose:
            # print lines
            print len(NEGATIVE_opinion_words)
            print containsNegatie
            print NEGATIVE_opinion_words
            print text_set
            # if
            #     # return True
            # print type(lines)

        # finally:
        #     file.close()

        if (containsNegatie):
            # containsNegatie is not empty --> these two set overlap each other
            return True
        else:
            return False
    else:
        return False


#
# def transformString2List(strs):
#     if strs:
#         list = strs.split(' ')
#         pass