import GettingInstanceFromTweets
import GettingInstanceOfUser
import unittest
import GettingInfoFromDB
import Connect2Db as Connect2Db



class TestMethods(unittest.TestCase):
    hashtags_c ='TEAMFOLLOWBACK,TFBJP'


    def test_GettingInstanceFromTweets(self):
        hashtags_c = 'TEAMFOLLOWBACK,TFBJP'
        self.assertTrue(GettingInstanceFromTweets.containsSpammy_hashtag(
        hashtags_c))

    def test_containsNegative_words(self):

        self.assertFalse(GettingInstanceFromTweets.containsNegative_words(
            'good ',0))
        self.assertTrue(GettingInstanceFromTweets.containsNegative_words(
            'rumours  rumor fastidious',0))
        self.assertTrue(GettingInstanceFromTweets.containsNegative_words(
            'good rumor',0))

    def test_ThePercentageOfuppercaseInText(self):
        thePercentageOfuppercaseInText=GettingInstanceFromTweets\
            .textIsUpperCaseCharacters

        self.assertFalse(thePercentageOfuppercaseInText('good'))
        self.assertFalse(thePercentageOfuppercaseInText('gooD'))
        self.assertTrue(thePercentageOfuppercaseInText('goOD'))


    def test_containsCapitalized_hashtag(self):
        containsCapitalized_hashtag=GettingInstanceFromTweets\
            .containsCapitalized_hashtag

        hashtags_c_False=['android,androidgames,gameinsight']
        hashtags_c_True = ['ANDROID,androidgames,gameinsight']
        for i in hashtags_c_True:
            self.assertTrue(containsCapitalized_hashtag(i))
            # containsCapitalized_hashtag(i)

        for i in hashtags_c_False:
            self.assertFalse(containsCapitalized_hashtag(i))

    def test_GettingInstanceOfUser(self):
        sampleUserID= ['21799546','21799430','21799409','21798878',\
                        '21798805','21798372','21798200','21798118']
        gettingInstanceOfUser=GettingInstanceOfUser.gettingInstanceOfUser
        try:
            gettingAllValueOfFollowerAndFollowee = GettingInfoFromDB.gettingAllValueOfFollowerAndFollowee

            db, cursor = Connect2Db.connect_db()
            followers_count_list, percentile5_OnFollower, percentile5_OnFollowee = gettingAllValueOfFollowerAndFollowee(
                db, cursor)
            for s in sampleUserID:
                gettingInstanceOfUser(s,db, cursor,followers_count_list, percentile5_OnFollower, percentile5_OnFollowee)
                pass

        finally:
            db.close()


            # test_GettingInstanceOfUser(s,)

    def test_gettingAllValueOfFollowerAndFollowee(self):
        gettingAllValueOfFollowerAndFollowee=GettingInfoFromDB.gettingAllValueOfFollowerAndFollowee
        gettingInfoFromUser=GettingInfoFromDB.gettingInfoFromUser
        try:
            db, cursor = Connect2Db.connect_db()
            gettingAllValueOfFollowerAndFollowee(db, cursor)
            gettingInfoFromUser('14497663',db, cursor)

        finally:
            db.close()
    def test_GettingAllRelatedVarsFromDBTweets(self):

        GettingAllRelatedVarsFromDBTweets = GettingInfoFromDB.GettingAllRelatedVarsFromDBTweets
        try:
            db, cursor = Connect2Db.connect_db()
            GettingAllRelatedVarsFromDBTweets(db,cursor,1)

        finally:
            db.close()


if __name__ == '__main__':
    unittest.main()