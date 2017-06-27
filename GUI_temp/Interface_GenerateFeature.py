
from Tkinter import *
# Python 2.7, ttk provides Combobox
from ttk import *
import GetTweetsIDFromPickle
import GetTweetsFeatureFiles
import Interface_Training as  Interface_Training
import Interface_Training_NFolder as Interface_Training_NFolder





#Global constrants
T, F = True, False
board_height = 600 # height of the board window
board_width = 600 # width of the board window
getTweetsIDFromPickle = GetTweetsIDFromPickle.getTweetsIDFromPickle;
pickleFileName=''

tweetsIDlist, tweetsID_feature_target_Dic, tweetsID_tweets_Dic, tweetsID_user_Dic = getTweetsIDFromPickle(
    pickleFileName)

parent = Tk()

parent = parent  # a Tk GUI
# cave = cave  # the cave, i.e., the environment
# robot = robot  # the agent
# WIDTH = cave.WIDTH  # number of columns in the cave
# HEIGHT = cave.HEIGHT  # number of rows in the cave

## Size of the environment which is a square
canvas_height = board_height
canvas_width = board_width




########## Generate Features pannel ##########

## Create  setting Frame
settingFrame = Frame(parent, borderwidth=2, relief=RIDGE)
settingFrame.grid(row=0, column=0)
# setting frame title
Label(settingFrame, text="Generate Features", font=('Arial', 14, 'bold')). \
    grid(row=0, column=0, columnspan=2, padx=5, pady=5)




####### Combobox1 DB : Let user choose the db scheme
Label(settingFrame, text='Choose DB Scheme: ', font=('Arial', 10)). \
    grid(row=1, column=0, sticky='E', padx=5, pady=5)
DbTableName = Combobox(settingFrame, text="DbTableName", \
                       state='readonly', font=('Courier', 10),
                       justify=LEFT)
# Add the db scheme  names
DbTableName['values'] = ('TweetsDB', 'otherDBs')
# Set the current position
DbTableName.current(0)
# Add it to the setting panel
DbTableName.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# TODO: generateFeature_Button needs links to getFeature function.
generateFeature_Button = Button(settingFrame,text = "GetFeature")
generateFeature_Button.grid(row=1, column=2, sticky=W, padx=5, pady=5)


##### Redirect to TrainingGUI Button ####
def RedirectToTrainingGUI():
    pass
    print "new Training GUI"
    Interface_Training.Training_main()

TrainingGUI =Button(settingFrame,text = "TrainingGUI")
TrainingGUI.grid(row=1, column=3, sticky=W, padx=5, pady=5)
TrainingGUI.config(command = (lambda: RedirectToTrainingGUI()))



##### Redirect to TrainingGUI_NFolder  Button ####
def RedirectToTrainingGUI_NFloder():
    pass
    Interface_Training_NFolder.Training_main()

TrainingGUI_NFolder =Button(settingFrame,text = "TrainingGUI_NFolder")
TrainingGUI_NFolder.grid(row=2, column=3, sticky=W, padx=5, pady=5)
TrainingGUI_NFolder.config(command = (lambda: RedirectToTrainingGUI_NFloder()))


# select Pickle files
DbTableName.bind('<<ComboboxSelected>>', lambda x : comboBox_DB(
    DbTableName.get()))

#TODO  get DB scheme value from comboBox DB
def comboBox_DB( values):
    print values




#########Combobox2 pickleFile:  select pickle file from comboBox if exist
Label(settingFrame,
      text="Choose the features from existed pickle files :",
      font=('Arial', 10)) \
    .grid(row=2, column=0, padx=5, pady=5)

pickleFile=Combobox(settingFrame, text="pickleFile", \
                  state='readonly', font=('Courier', 10),
                  justify=LEFT)
pickleFile.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# get tweetsFeature*.pickle file name
pickleFilelist = GetTweetsFeatureFiles.getTweetsFeatureFiles()

# Add the tweets values
pickleFile['values'] = tuple(pickleFilelist)

# Set the current position
# pickleFile.current(0)

# bind a funciton when slect a differnt value
pickleFile.bind('<<ComboboxSelected>>', lambda x: comboBox_pickleFile(
    pickleFile.get()))


#get tweets ID value from comboBox TweetsID
def comboBox_pickleFile(values):
    global pickleFileName
    print values
    pickleFileName = values


    #########Dynamicly Create Combobox3 tweetsID:  set Tweets ID comboBox
    tweetsIDlist, tweetsID_feature_target_Dic, tweetsID_tweets_Dic, tweetsID_user_Dic = getTweetsIDFromPickle(
        pickleFileName)

    # create label
    Label(settingFrame,
          text="choose an tweets ID to check the result:",
          font=('Arial', 10)) \
        .grid(row=3, column=0, padx=5, pady=5)

    # create combobox for tweetsID
    tweetsID=Combobox(settingFrame, text="tweetsID", \
                      state='readonly', font=('Courier', 10),
                      justify=LEFT)
    tweetsID.grid(row=3, column=1, sticky=W, padx=5, pady=5)

    # Add the tweets values
    tweetsID['values'] = tuple(tweetsIDlist)
    # if tweetsIDlist != []:
    #     # Set the current position
    # tweetsID.current(0)


    # bind functions to tweetsID combolist
    tweetsID.bind('<<ComboboxSelected>>', lambda x: comboBox_TweetsID(
        tweetsID.get()))

    #get tweets ID value from comboBox TweetsID
    def comboBox_TweetsID(values):
        if(values is not None):
            # featureInfo,tweetsID_feature_target_Dic,tweetsInfo,userInfo,tweetsID_tweets_Dic, tweetsID_user_Dic
            print values
            # Add the tweets values
            tweetsID['values'] = tuple(tweetsIDlist)
            if tweetsIDlist != []:
                # Set the current position
                tweetsID.set(values)
        value_int= int(values)
        tweetsVariableNames = ["numberOfHashtags_c","text","hashtags_c","user",
                               "maliciousMark","id"]
        userVariableNames = ["followers_count","friends_count","description","url"]
        featureVariableNames = ["hashtags_more_two ","exclamation_sign ",
                                "url_in_tweets ","suffix_hashtag ",
                                "spammy_hashtag ","negative_words ",
                                "upper_case_characters ","capitalized_hashtag ","Followers_followees_ratio","description","url_in_user","followers_Less_5_percentile","followees_Less_5_percentile","Percentile_of_followers","Target"]

        # joint featureValue
        featureValue = tweetsID_feature_target_Dic[value_int]
        featureValue=addNamesForEachValue(featureValue,featureVariableNames)
        print "+++++"
        print type(featureValue)
        print featureValue

        # joint tweetValue
        tweetValue = tweetsID_tweets_Dic[value_int]
        tweetValue = addNamesForEachValue(tweetValue, tweetsVariableNames)
        # joint userValue
        userValue  = tweetsID_user_Dic [ value_int]
        userValue = addNamesForEachValue(userValue, userVariableNames)


        tweetsInfo.set(tweetValue )
        userInfo.set(userValue )
        featureInfo.set(featureValue )

    def addNamesForEachValue(valueString,variableNames):
        valuesList = valueString.split(',*,')

        print "*****"
        print valueString
        print variableNames
        if len(valuesList)<10:
            spliter = '\n'
        else:
            spliter = '\n'
        i=0
        finalValue=''
        print valuesList
        for val in valuesList:
            finalValue=finalValue+spliter+variableNames[i]+' : '+str(val)
            # print finalValue
            i=i+1
            # firstTime = False
        print finalValue

        return finalValue











########## show Features pannel ##########
##Create the environment board
rightFrame = Frame(parent, width=canvas_width,
                     height=canvas_height)
# createGrid()
rightFrame.grid(row=1, column=0, rowspan=2)
# tweetsInfo = Label(rightFrame,
#       text="choose an tweets ID to check the result:",
#       font=('Arial', 10)) \
#     .grid(row=0, column=0, padx=5, pady=5)
#



##tweets info
tweetsInfo = StringVar()

correspondingTweetsInfoInfo = Label(rightFrame,text="   ",
                                    textvariable=tweetsInfo,
      font=('Arial', 13)) \
    .grid(row=1, column=0, padx=5, pady=5)
# test = Label(rightFrame,text="   ", textvariable=featureInfo,font = ('Arial',
#                                                                      10), width = 10)
tweetsInfo.set('-------------------')

Label(rightFrame,text="-----------------------",
      font=('Arial', 13)) \
    .grid(row=2, column=0, padx=5, pady=5)

######user info
userInfo = StringVar()

correspondingUserInfo = Label(rightFrame,text="   ", textvariable=userInfo,
      font=('Arial', 13)) \
    .grid(row=3, column=0, padx=5, pady=5)
# test = Label(rightFrame,text="   ", textvariable=featureInfo,font = ('Arial',
#                                                                      10), width = 10)
userInfo.set('-------------------')


Label(rightFrame,text="-----------------------",
      font=('Arial', 13)) \
    .grid(row=4, column=0, padx=5, pady=5)


####feature Info
featureInfo = StringVar()

correspondingFeatureInfo = Label(rightFrame,text="   ", textvariable=featureInfo,
      font=('Arial', 13)) \
    .grid(row=5, column=0, padx=5, pady=5)
# test = Label(rightFrame,text="   ", textvariable=featureInfo,font = ('Arial',
#                                                                      10), width = 10)
featureInfo.set('-------------------')

parent.title("generate Features From DB")

parent.mainloop()




