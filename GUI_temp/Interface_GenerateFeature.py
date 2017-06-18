
from Tkinter import *
# Python 2.7, ttk provides Combobox
from ttk import *
import GetTweetsIDFromPickle



def comboBox_DB( values):
    print values

def comboBox_TweetsID(values):
    global featureInfo,tweetsID_feature_target_Dic,tweetsInfo,userInfo,tweetsID_tweets_Dic, tweetsID_user_Dic
    print values
    value_int= int(values)
    featureValue = tweetsID_feature_target_Dic[value_int]
    tweetValue = tweetsID_tweets_Dic[value_int]
    userValue  = tweetsID_user_Dic [ value_int]
    tweetsInfo.set(tweetValue )
    userInfo.set(userValue )
    featureInfo.set(featureValue )



#Global constrants
T, F = True, False
board_height = 600 # height of the board window
board_width = 600 # width of the board window
getTweetsIDFromPickle = GetTweetsIDFromPickle.getTweetsIDFromPickle;

tweetsIDlist, tweetsID_feature_target_Dic, tweetsID_tweets_Dic, tweetsID_user_Dic = getTweetsIDFromPickle()




parent = Tk()

parent = parent  # a Tk GUI
# cave = cave  # the cave, i.e., the environment
# robot = robot  # the agent
# WIDTH = cave.WIDTH  # number of columns in the cave
# HEIGHT = cave.HEIGHT  # number of rows in the cave

## Size of the environment which is a square
canvas_height = board_height
canvas_width = board_width
# length_of_side = 600 / (
# max(WIDTH, HEIGHT) + 2)  # length of each room
#
# ###Read all the pictures and resize them to fit the environment
# img = Image.open("IFN680_AIMA/images/gold.gif")
# image_gold = img.resize((length_of_side, length_of_side))
# gold_img = ImageTk.PhotoImage(image_gold)
# img = Image.open("IFN680_AIMA/images/visited.gif")
# image_visited = img.resize((length_of_side, length_of_side))
# visited_img = ImageTk.PhotoImage(image_visited)
# img = Image.open("IFN680_AIMA/images/blank.gif")
# image_blank = img.resize((length_of_side, length_of_side))
# blank_img = ImageTk.PhotoImage(image_blank)
# img = Image.open("IFN680_AIMA/images/wall.gif")
# image_wall = img.resize((length_of_side, length_of_side))
# wall_img = ImageTk.PhotoImage(image_wall)
# img = Image.open("IFN680_AIMA/images/robot.gif")
# image_robot = img.resize((length_of_side, length_of_side))
# robot_img = ImageTk.PhotoImage(image_robot)
# img = Image.open("IFN680_AIMA/images/wumpus.gif")
# image_wumpus = img.resize((length_of_side, length_of_side))
# wumpus_img = ImageTk.PhotoImage(image_wumpus)
# img = Image.open("IFN680_AIMA/images/pit.gif")
# image_pit = img.resize((length_of_side, length_of_side))
# pit_img = ImageTk.PhotoImage(image_pit)

########## Left Widgets ##########
# Create  setting Frame
settingFrame = Frame(parent, borderwidth=2, relief=RIDGE)
settingFrame.grid(row=0, column=0)
# setting frame title
Label(settingFrame, text="Generate Features", font=('Arial', 14, 'bold')). \
    grid(row=0, column=0, columnspan=2, padx=5, pady=5)




# Let user choose the db scheme
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

generateFeature_Button = Button(settingFrame,text = "GetFeature")
generateFeature_Button.grid(row=1, column=2, sticky=W, padx=5, pady=5)

DbTableName.bind('<<ComboboxSelected>>', lambda x : comboBox_DB(
    DbTableName.get()))


#set Tweets ID comboBox
Label(settingFrame,
      text="choose an tweets ID to check the result:",
      font=('Arial', 10)) \
    .grid(row=2, column=0, padx=5, pady=5)

tweetsID=Combobox(settingFrame, text="tweetsID", \
                  state='readonly', font=('Courier', 10),
                  justify=LEFT)
tweetsID.grid(row=2, column=1, sticky=W, padx=5, pady=5)
# Add the tweets values
tweetsID['values'] = tuple(tweetsIDlist)
# Set the current position
tweetsID.current(0)

# Add it to the setting panel
tweetsID.bind('<<ComboboxSelected>>', lambda x: comboBox_TweetsID(
    tweetsID.get()))


########## Right Widgets ##########
##Create the environment board
rightFrame = Frame(parent, width=canvas_width,
                     height=canvas_height)
# createGrid()
rightFrame.grid(row=1, column=0, rowspan=2)
tweetsInfo = Label(rightFrame,
      text="choose an tweets ID to check the result:",
      font=('Arial', 10)) \
    .grid(row=0, column=0, padx=5, pady=5)




##tweets info
tweetsInfo = StringVar()  # single run result

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
userInfo = StringVar()  # single run result

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
featureInfo = StringVar()  # single run result

correspondingFeatureInfo = Label(rightFrame,text="   ", textvariable=featureInfo,
      font=('Arial', 13)) \
    .grid(row=5, column=0, padx=5, pady=5)
# test = Label(rightFrame,text="   ", textvariable=featureInfo,font = ('Arial',
#                                                                      10), width = 10)
featureInfo.set('-------------------')

parent.title("generate Features From DB")

parent.mainloop()




