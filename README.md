# project

dataInjectionFromPickle2DB Folder:
    This is part of project on data injection from Pickle file(tweets collected from Twitter) to Mysql Database.

    Basic introduction:

        1.MainEntry.py :  loop all the instance within pickle file(50,000 each)

        2.insertTweets2DB.py : condition statement on tweets and user table. This method will update user information if user update their profile.

        3.InsertUserStatement.py: conver all the related variables from tweets standard into Mysql standard;  Return corresponding insert SQL for user table.
        4.UpdateUserInfo.py  : generate update statement

        5.InsertTweets.py : generate insert tweets statement

    Note:
    Current veision Problems: Insert statement did not handle all the errors in
    tweets(text & description value). Around 60 out of 60,000 errors occurs.
    --> Further improvement: refactoring InsertUserStatement & change sql
    statement into parameter style / handle all the possible errors(eg: " & \ in
    value)


generateFeatureAndTraining Folder
    Task: generature from tweet in DB to two npArrays(data and target)
    status: Finshed
    Problems: performance needs to be improvemented. Now (35s per 100 instances)



