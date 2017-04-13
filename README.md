# project
Project folder on data injection part.
The basic algorithms:

<MainEntry>
For tweet in tweets:
    <insertTweets&UserDB>



<insertTweets&UserDB>
    if (tweets.id NOT IN db.tweets):
        if(tweets.user.id IN db.User):
            if(db.user.updatetime IS old):
                <UpdateUserInfo>
            else:
                Pass
        else:
            <InsertUserInfo>
        <InsertTweets>
    else:
        Pass


<UpdateUserInfo>/<UpdateUserInfo>
	collect all the related variables 
	cast to corresponding DB variables type.
	build Insert query and execute 




<UpdateTweets>
	collect all the related variables 
		if(tweet.retweets NOT Null):
			<insertTweets&UserDB>
	cast to corresponding DB variables type.
	build Insert query and execute 
  
  
  
Ongoing changes...
