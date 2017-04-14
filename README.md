# project
This is part of project on data injection from Pickle file(tweets collected from Twitter) to Mysql Database.

The file introduction:

MainEntry.py :  loop all the instance within pickle file(50,000 each)

insertTweets2DB.py : condition statement on tweets and user table. This method will update user information if user update their profile.


InsertUserStatement.py: conver all the related variables from tweets standard into Mysql standard;  Return corresponding insert SQL for user table.

UpdateUserInfo.py  : generate update sql language


& InsertTweets.py  ongoing... 

