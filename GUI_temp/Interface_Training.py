
from Tkinter import *
import tkMessageBox
# Python 2.7, ttk provides Combobox
from ttk import *
# todo Now can not run this in pycham.
import DataPreprocess,SVM_training,DT
# import GetTweetsIDFromPickle


dataPreprocess  = DataPreprocess.dataProcess
# confusion_matrix,percision, recall
# getfile = GetTweetsIDFromPickle.getFile
def partitioningData():
    # get value from snipBox; validate value ; call
    global w1,w2,w3,trainingDataLengthForSpinBox, validationDataLengthForSpinBox, testingDataLengthForSpinBox
    trainingPercentage=  int(w1.get())
    validationPercentage=  int(w2.get())

    testingPercentage=  int(w3.get())
    # print type(testingPercentage)
    totalPercentage  = trainingPercentage+validationPercentage+testingPercentage
    if(totalPercentage!= 100):

        tkMessageBox.showinfo("Wrong setting!",
                          "the sum of all the persentage should be 100")
    else:
    # pass three numbers
        trainingDataLength, validationDataLength, \
        testingDataLength=    dataPreprocess(trainingPercentage,
                       validationPercentage,testingPercentage)
        trainingDataLengthForSpinBox.set('trainingDataLength is ' + str(trainingDataLength))
        validationDataLengthForSpinBox.set(
            'validationDataLength is ' + str(validationDataLength))
        testingDataLengthForSpinBox.set(
            'testingDataLength is ' + str(testingDataLength))


def TrainingOnDT():
    global DTClass_weight,DTMax_features,DTCriterion,unknowRow,hamRow,spamRow,PercisionRow,recallRow

    print  DTClass_weight.get()
    DTconfusion_matrix, percision, recall = DT.DT(DTCriterion.get(),DTMax_features.get(),
                     DTClass_weight.get())
    print DTconfusion_matrix,percision, recall
    strOnUnknowRow = "unknown:            " +  "            ".join( str(x)
                                                                    for x in \
            DTconfusion_matrix[0])
    strOnHamRow= "Ham:           " + "         ".join(str(x) for x in \
                                                DTconfusion_matrix[1])
    strOnSpamRow = "Spam:           " + "          ".join(str(x) for x in \
                                                DTconfusion_matrix[2])
    strOnPercisionRow = "precision On spam is : " + str(percision)
    strOnRecallRow = "Recall on spam is : " + str(recall)
    unknowRow.set(strOnUnknowRow)
    hamRow.set(strOnHamRow)
    spamRow.set(strOnSpamRow)
    PercisionRow.set(strOnPercisionRow)
    recallRow.set(strOnRecallRow)



    print strOnUnknowRow


def TrainingOnSVM():
    global SVMLoss,SVMClass_weight,SVMKernel,unknowRow,hamRow,spamRow,PercisionRow,recallRow
    # here for presentation all use liner kernel
    SVMconfusion_matrix, percision, recall = SVM_training.svm_training(SVMKernel.get(), SVMLoss.get(),
                                          SVMClass_weight.get())
    print SVMconfusion_matrix, percision, recall
    strOnUnknowRow = "unknown:            " + "            ".join(str(x) for x
                                                                in \
                                                    SVMconfusion_matrix[0])
    strOnHamRow = "Ham:           " + "         ".join(str(x) for x in \
                                             SVMconfusion_matrix[1])
    strOnSpamRow = "Spam:           " + "          ".join(str(x) for x in \
                                               SVMconfusion_matrix[2])
    strOnPercisionRow = "precision On spam is : " + str(percision)
    strOnRecallRow = "Recall on spam is : " + str(recall)
    unknowRow.set(strOnUnknowRow)
    hamRow.set(strOnHamRow)
    spamRow.set(strOnSpamRow)
    PercisionRow.set(strOnPercisionRow)
    recallRow.set(strOnRecallRow)

    pass
#Global constrants
T, F = True, False
board_height = 600 # height of the board window
board_width = 600 # width of the board window

# if __name__ == "__main__" :


# if __name__ == '__main__'and __package__ is None:
    # __package__ = "DataInjection.Training.DataPreprocess"
    # Create the GUI interface for the game
main_GUI = Tk()

# Create board setting frame
setting_up = Frame(main_GUI, width=100, borderwidth=2, relief=RIDGE)
setting_up.grid(row=0, column=0)

Label(setting_up, text="Data Partitioning", font=('Arial', 14, 'bold')). \
    grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# ##Let user choose the number of rows in the cave environment
rows = Label(setting_up, text="Please choose percentage of training "
                              "data:") \
    .grid(row=1, column=0, padx=5, pady=5)
w1 = Spinbox(setting_up, from_=1, to=100)
w1.grid(row=1, column=1, padx=5, pady=5)

#feature Info
trainingDataLengthForSpinBox = StringVar()  # single run result

trainingPercentageLabel = Label(setting_up, text="   ",
                                textvariable=trainingDataLengthForSpinBox,
                                font=('Arial', 12)) \
    .grid(row=1, column=2, padx=5, pady=5)
# trainingPercentageFromSpinBox.set(444444)



# Let user choose the number of columns in the cave environment
columns = Label(setting_up, text="Please choose percentage of validation "
                                 "data:")
columns.grid(row=2, column=0, padx=5, pady=5)
w2 = Spinbox(setting_up, from_=1, to=100)
w2.grid(row=2, column=1, padx=5, pady=5)
#feature Info
validationDataLengthForSpinBox = StringVar()  # single run result

validationPercentageLabel = Label(setting_up, text="   ",
                                  textvariable=validationDataLengthForSpinBox,
                                  font=('Arial', 12)) \
    .grid(row=2, column=2, padx=5, pady=5)


# Let user choose the number of pits in the cave environment
pits = Label(setting_up, text="Please choose percentage of testing data")
pits.grid(row=3, column=0, padx=5, pady=5)
w3 = Spinbox(setting_up, from_=1, to=100)
w3.grid(row=3, column=1, padx=5, pady=5)


#feature Info
testingDataLengthForSpinBox = StringVar()  # single run result

testingPercentageLabel = Label(setting_up, text="   ",
                               textvariable=testingDataLengthForSpinBox,
                               font=('Arial', 12)) \
    .grid(row=3, column=2, padx=5, pady=5)


# Let user to choose: random or fixed board
# b = IntVar()
# fixed = Radiobutton(setting_up, text="Fixed Board", variable=b, value=1)
# fixed.grid(row=4, column=0)

partitioningDataButton = Button(setting_up, text="Partitioning DataSet")
partitioningDataButton.grid(row=4, column=1, padx=5, pady=5)
partitioningDataButton.config(command = partitioningData)
# b.set(2)  # initially, Random is chosen



# Fixed board setting
fixed_board = Canvas(setting_up, borderwidth=2, relief=RIDGE)
fixed_board.grid(row=5, column=0, columnspan=2)

# Fixed board setting items
Label(fixed_board, text="Traing Setting", font=('Arial', 12, 'bold')). \
    grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Label(fixed_board, text='Please Note: The board will be 3x3 and only one pit is allowed. \
# Please choose a room for the wumpus,\n a room for one pit, and a room for the gold. The wumpus \
# and the pit cannot be in rooms (1,3),(1,2), (2,3),\n the gold cannot be in room (1,3), and the \
# three must occupy different rooms.', \
#       font=('Arial', 10)).grid(row=1, column=0, columnspan=4, padx=5,
#                                pady=5)

Label(fixed_board, text="DT parameters ") \
    .grid(row=1, column=0, padx=5, pady=5, sticky='E')

# Choose a position for the wumpus
Label(fixed_board, text="criterion:  ") \
    .grid(row=2, column=0, padx=5, pady=5, sticky='E')
# w_column = Spinbox(fixed_board, from_=1, to=3)
# w_column.grid(row=2, column=1, padx=5, pady=5, sticky=W)

DTCriterion = Combobox(fixed_board, text="DTCriterion", \
                       state='readonly', font=('Courier', 10),
                       justify=LEFT)
DTCriterion['values'] = ('gini', 'entropy')
DTCriterion.current(0)
DTCriterion.grid(row=2, column=1, padx=5, pady=5, sticky=W)


# Choose a position for one pit
Label(fixed_board, text="max_features:   ") \
    .grid(row=3, column=0, padx=5, pady=5, sticky='E')
# p_column = Spinbox(fixed_board, from_=1, to=3)
# p_column.grid(row=3, column=1, padx=5, pady=5, sticky=W)
DTMax_features = Combobox(fixed_board, text="DTMax_features", \
                          state='readonly', font=('Courier', 10),
                          justify=LEFT)
DTMax_features['values'] = ('sqrt','log2', 'auto')
DTMax_features.current(0)
DTMax_features.grid(row=3, column=1, padx=5, pady=5, sticky=W)


# Choose a position for the gold
Label(fixed_board, text="class_weight:  ") \
    .grid(row=4, column=0, padx=5, pady=5, sticky='E')
# g_column = Spinbox(fixed_board, from_=1, to=3)
# g_column.grid(row=4, column=1, padx=5, pady=5, sticky=W)
DTClass_weight = Combobox(fixed_board, text="DTClass_weight", \
                          state='readonly', font=('Courier', 10),
                          justify=LEFT)
DTClass_weight['values'] = ('balanced','None')
DTClass_weight.current(0)
DTClass_weight.grid(row=4, column=1, padx=5, pady=5, sticky=W)


Label(fixed_board, text="kernel:  ") \
    .grid(row=2, column=2, padx=5, pady=5, sticky=W)
# w_row = Spinbox(fixed_board, from_=1, to=3)
# w_row.grid(row=2, column=3, padx=5, pady=5, sticky=W)
SVMKernel = Combobox(fixed_board, text="SVMKernel", \
                     state='readonly', font=('Courier', 10),
                     justify=LEFT)
SVMKernel['values'] = ('linear', 'sigmoid')
SVMKernel.current(0)
SVMKernel.grid(row=2, column=3, padx=5, pady=5, sticky=W)

Label(fixed_board, text="loss :") \
    .grid(row=3, column=2, padx=5, pady=5, sticky=W)
# p_row = Spinbox(fixed_board, from_=1, to=3)
# p_row.grid(row=3, column=3, padx=5, pady=5, sticky=W)
SVMLoss = Combobox(fixed_board, text="SVMLoss", \
                   state='readonly', font=('Courier', 10),
                   justify=LEFT)
SVMLoss['values'] = ( 'squared_hinge','hinge')
SVMLoss.current(0)
SVMLoss.grid(row=3, column=3, padx=5, pady=5, sticky=W)
# print SVMLoss.get()



Label(fixed_board, text="class_weight:  ") \
    .grid(row=4, column=2, padx=5, pady=5, sticky=W)
# g_row = Spinbox(fixed_board, from_=1, to=3)
# g_row.grid(row=4, column=3, padx=5, pady=5, sticky=W)
SVMClass_weight = Combobox(fixed_board, text="SVMClass_weight", \
                           state='readonly', font=('Courier', 10),
                           justify=LEFT)
SVMClass_weight['values'] = ('balanced',None)
SVMClass_weight.current(0)
SVMClass_weight.grid(row=4, column=3, padx=5, pady=5, sticky=W)


Label(fixed_board, text="SVM parameters ") \
    .grid(row=1, column=2, padx=5, pady=5, sticky='E')

# A button to get the setting
# button = Button(setting_up, text="Set Up", command=getInfor).grid(row=6,
#                                                                   column=0,
#                                                                   columnspan=2)
buttonOnDT = Button(setting_up, text="Training On DT", command =
TrainingOnDT).grid(row=6,
                                                                  column=0,
                                                                  )
buttonOnSVM = Button(setting_up, text="Training On SVM", command =
TrainingOnSVM).grid(row=6,
                                                                  column=1,
                                                                  )

## Set up the environment board, here it is an empty area, just a place holder
resultBoard = Frame(main_GUI, width=board_width, height=board_height,
                    )
resultBoard.grid(row=0, column=1, rowspan=2)

columns = Label(resultBoard, text="Confusion Matrix Result:")
columns.grid(row=0, column=0, padx=10, pady=10,columnspan=2)



columns = Label(resultBoard, text="             predicted           ")
columns.grid(row=1, column=1, padx=5, pady=5)



columns = Label(resultBoard, text="Actual:")
columns.grid(row=3, column=0, padx=5, pady=5)

columns = Label(resultBoard, text="                     unknown    ham    "
                                  "spam")
columns.grid(row=2, column=1, padx=5, pady=5,sticky=E)


##unknowRow
unknowRow = StringVar()  # single run result
Label(resultBoard,text="   ", textvariable=unknowRow,
      font=('Arial', 12)) \
    .grid(row=3, column=1, padx=5, pady=5,sticky=E)


##hamRow
hamRow = StringVar()  # single run result
Label(resultBoard,text="   ", textvariable=hamRow,
      font=('Arial', 12)) \
    .grid(row=4, column=1, padx=5, pady=5,sticky=E)


##spamRow
spamRow = StringVar()  # single run result
Label(resultBoard,text="   ", textvariable=spamRow,
      font=('Arial', 12)) \
    .grid(row=5, column=1, padx=5, pady=5,sticky=E )

Label(resultBoard,text="   ",
      font=('Arial', 12)) \
    .grid(row=6, column=1, padx=5, pady=5)
Label(resultBoard,text="   ",
      font=('Arial', 12)) \
    .grid(row=7, column=1, padx=5, pady=5)
##PercisionRow
PercisionRow = StringVar()  # single run result
Label(resultBoard,text="   ", textvariable=PercisionRow,
      font=('Arial', 12)) \
    .grid(row=8, column=1, padx=5, pady=5,sticky=W )


##recallRow
recallRow = StringVar()  # single run result
Label(resultBoard,text="   ", textvariable=recallRow,
      font=('Arial', 12)) \
    .grid(row=9, column=1, padx=5, pady=5,sticky=W )








main_GUI.title("Traning")
main_GUI.mainloop()
