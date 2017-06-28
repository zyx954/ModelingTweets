
from Tkinter import *
import tkMessageBox
# Python 2.7, ttk provides Combobox
from ttk import *
# todo Now can not run this in pycham.
import DataPreprocess,SVM_training,DT
import GetTweetsFeatureFiles
from tkFileDialog import askopenfilename
# import GetTweetsIDFromPickle


dataPreprocess  = DataPreprocess.dataProcess
# confusion_matrix,percision, recall
# getfile = GetTweetsIDFromPickle.getFile




def Training_main():

    #####################################Start of GUI ##########################

    #Global constrants
    T, F = True, False
    board_height = 600 # height of the board window
    board_width = 600 # width of the board window
    pickleFileName = ''
    # filename=''

    main_GUI = Tk()

    # Create board setting frame
    setting_up = Frame(main_GUI, width=100, borderwidth=2, relief=RIDGE)
    setting_up.grid(row=0, column=0)

    Label(setting_up, text="Data Partitioning", font=('Arial', 14, 'bold')). \
        grid(row=0, column=0, columnspan=2, padx=5, pady=5)



    ####################### start of data Partitioning ###################

    #########Combobox2 pickleFile:  select pickle file from comboBox if exist
    Label(setting_up,
          text="Choose the features from existed pickle files :",
          font=('Arial', 12)) \
        .grid(row=1, column=0, padx=5, pady=5)

    pickleFile=Combobox(setting_up, text="pickleFile", \
                      state='readonly', font=('Arial', 12),
                      justify=LEFT)
    pickleFile.grid(row=1, column=1, sticky=W, padx=5, pady=5)

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


    # ######Choose percentage of Traning data######
    rows = Label(setting_up, text="Please choose percentage of training "
                                  "data:") \
        .grid(row=2, column=0, padx=5, pady=5)
    w1 = Spinbox(setting_up, from_=1, to=100)
    w1.grid(row=2, column=1, padx=5, pady=5)

    #set length of Training Data
    trainingDataLengthForSpinBox = StringVar()

    trainingPercentageLabel = Label(setting_up, text="   ",
                                    textvariable=trainingDataLengthForSpinBox,
                                    font=('Arial', 12)) \
        .grid(row=2, column=2, padx=5, pady=5)
    # trainingPercentageFromSpinBox.set(444444)


    #


    # ######Choose percentage of Testing   data#######
    pits = Label(setting_up, text="Please choose percentage of testing data")
    pits.grid(row=3, column=0, padx=5, pady=5)
    w3 = Spinbox(setting_up, from_=1, to=100)
    w3.grid(row=3, column=1, padx=5, pady=5)

    #set length of testing Data
    testingDataLengthForSpinBox = StringVar()

    testingPercentageLabel = Label(setting_up, text="   ",
                                   textvariable=testingDataLengthForSpinBox,
                                   font=('Arial', 12)) \
        .grid(row=3, column=2, padx=5, pady=5)



    # Grab the data from snipbox and do the data partitioning

    def partitioningData():
        # get value from snipBox; validate value ; call
        global w1,w2,w3,trainingDataLengthForSpinBox, \
            validationDataLengthForSpinBox, testingDataLengthForSpinBox,pickleFileName
        trainingPercentage=  int(w1.get())
        # validationPercentage=  int(w2.get())
        validationPercentage=0
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
                           validationPercentage,testingPercentage,pickleFileName)
            trainingDataLengthForSpinBox.set('trainingDataLength is ' + str(trainingDataLength))
            # validationDataLengthForSpinBox.set(
            #     'validationDataLength is ' + str(validationDataLength))
            testingDataLengthForSpinBox.set(
                'testingDataLength is ' + str(testingDataLength))


    partitioningDataButton = Button(setting_up, text="Partitioning DataSet")
    partitioningDataButton.grid(row=4, column=1, padx=5, pady=5)
    partitioningDataButton.config(command=partitioningData)

    ###############



    ################  start of Traing setting ################

    fixed_board = Canvas(setting_up, borderwidth=2, relief=RIDGE)
    fixed_board.grid(row=5, column=0, columnspan=2)

    Label(fixed_board, text="Traing Setting", font=('Arial', 12, 'bold')). \
        grid(row=0, column=0, columnspan=4, padx=5, pady=5)



    # #########seeting  for DT ############
    Label(fixed_board, text="DT parameters ") \
        .grid(row=1, column=0, padx=5, pady=5, sticky='E')

    Label(fixed_board, text="criterion:  ") \
        .grid(row=2, column=0, padx=5, pady=5, sticky='E')

    DTCriterion = Combobox(fixed_board, text="DTCriterion", \
                           state='readonly', font=('Courier', 10),
                           justify=LEFT)
    DTCriterion['values'] = ('gini', 'entropy')
    DTCriterion.current(0)
    DTCriterion.grid(row=2, column=1, padx=5, pady=5, sticky=W)


    Label(fixed_board, text="max_features:   ") \
        .grid(row=3, column=0, padx=5, pady=5, sticky='E')
    DTMax_features = Combobox(fixed_board, text="DTMax_features", \
                              state='readonly', font=('Courier', 10),
                              justify=LEFT)
    DTMax_features['values'] = ('sqrt','log2', 'auto')
    DTMax_features.current(0)
    DTMax_features.grid(row=3, column=1, padx=5, pady=5, sticky=W)


    Label(fixed_board, text="class_weight:  ") \
        .grid(row=4, column=0, padx=5, pady=5, sticky='E')
    DTClass_weight = Combobox(fixed_board, text="DTClass_weight", \
                              state='readonly', font=('Courier', 10),
                              justify=LEFT)
    DTClass_weight['values'] = ('balanced','None')
    DTClass_weight.current(0)
    DTClass_weight.grid(row=4, column=1, padx=5, pady=5, sticky=W)


    # ##########setting for SVM  ######
    Label(fixed_board, text="kernel:  ") \
        .grid(row=2, column=2, padx=5, pady=5, sticky=W)
    # w_row = Spinbox(fixed_board, from_=1, to=3)
    # w_row.grid(row=2, column=3, padx=5, pady=5, sticky=W)
    SVMKernel = Combobox(fixed_board, text="SVMKernel", \
                         state='readonly', font=('Courier', 10),
                         justify=LEFT)
    SVMKernel['values'] = ('linear')
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
    SVMClass_weight['values'] = ('balanced')
    SVMClass_weight.current(0)
    SVMClass_weight.grid(row=4, column=3, padx=5, pady=5, sticky=W)


    Label(fixed_board, text="SVM parameters ") \
        .grid(row=1, column=2, padx=5, pady=5, sticky='E')

    ################  end of Traing setting ################




    ############set PathForTrainingResult########
    def FilePathForResult():
        global filepathForTrainingResult,filenameForTrainingResult
        filenameForTrainingResult = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        filepathForTrainingResult.set(filenameForTrainingResult)

    Button(setting_up, text="PathForTrainingResult", command =
    FilePathForResult).grid(row=6,column=0,)
    filepathForTrainingResult = StringVar()
    filenameForTrainingResult=''
    Label(setting_up, text="   ", textvariable=filepathForTrainingResult,).grid(row=6,column=1,)


    ############set Path for actualt and predicted result ########
    def FilePathForResult():
        global filepathForPredictedResult,filenameForPredictedResult
        filenameForPredictedResult = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        filepathForPredictedResult.set(filenameForPredictedResult)

    Button(setting_up, text="PathForPredictedResult", command =
    FilePathForResult).grid(row=7,column=0,)
    filepathForPredictedResult = StringVar()
    filenameForPredictedResult=''
    Label(setting_up, text="   ", textvariable=filepathForPredictedResult,
                        ).grid(row=7, column=1,  )



    #

    ########Training On DT button ##########
    def TrainingOnDT():
        global filenameForTrainingResult,filenameForPredictedResult,\
            DTClass_weight,DTMax_features,\
            DTCriterion,unknowRow,hamRow,spamRow,PercisionRow,recallRow

        print  DTClass_weight.get()
        DTconfusion_matrix, percision, recall,combinedResultOnActualAndPred = DT.DT(DTCriterion.get(),
                                                       DTMax_features.get(),
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



        # ####write Condussion result into file
        print filenameForTrainingResult

        if (filenameForTrainingResult == ''):
            pass
        else:
            fileOnTrainingResult = open(filenameForTrainingResult, 'w')
            try:
                fileOnTrainingResult.write("The result of confusion matrix")
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write("             predicted           ")
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write("                     unknown    ham    spam")
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write(strOnUnknowRow)
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write(strOnHamRow)
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write(strOnSpamRow)
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write(strOnPercisionRow)
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write(strOnRecallRow)
            finally:
                fileOnTrainingResult.close()


        # ###Write ID --Actual result --Predicted resutl into file
        print filenameForPredictedResult
        if(filenameForPredictedResult==''):
            pass
        else:
            fileOnIndividualResult = open(filenameForPredictedResult, 'w')
            fileOnIndividualResult.write("     ID           "
                                         "\tActual\tPredicted\r\n")
            try:
                for i in combinedResultOnActualAndPred:
                    fileOnIndividualResult.write(i)
                # fileOnIndividualResult.write('\r\n')

            finally:
                fileOnIndividualResult.close()


        print strOnUnknowRow

    buttonOnDT = Button(setting_up, text="Training On DT", command =
    TrainingOnDT).grid(row=8,
                                                                      column=0,
                                                                      )


    ######TrainingOnSVM Button#####
    def TrainingOnSVM():
        global filenameForTrainingResult,filenameForPredictedResult,SVMLoss,SVMClass_weight,SVMKernel,unknowRow,hamRow,spamRow,PercisionRow,recallRow
        # here for presentation all use liner kernel
        SVMconfusion_matrix, percision, recall,combinedResultOnActualAndPred = SVM_training.svm_training(
            SVMKernel.get(), SVMLoss.get(),
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



        # ####write Condussion result into file
        print filenameForTrainingResult

        if (filenameForTrainingResult == ''):
            pass
        else:
            fileOnTrainingResult = open(filenameForTrainingResult, 'w')
            try:
                fileOnTrainingResult.write("The result of confusion matrix")
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write("             predicted           ")
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write("                     unknown    ham    spam")
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write(strOnUnknowRow)
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write(strOnHamRow)
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write(strOnSpamRow)
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write(strOnPercisionRow)
                fileOnTrainingResult.write('\r\n')
                fileOnTrainingResult.write(strOnRecallRow)
            finally:
                fileOnTrainingResult.close()


        # ###Write ID --Actual result --Predicted resutl into file
        print filenameForPredictedResult
        if(filenameForPredictedResult==''):
            pass
        else:
            fileOnIndividualResult = open(filenameForPredictedResult, 'w')
            fileOnIndividualResult.write("   SVM  \r\n")
            fileOnIndividualResult.write("     ID           "
                                         "\tActual\tPredicted\r\n")
            try:
                for i in combinedResultOnActualAndPred:
                    fileOnIndividualResult.write(i)
                # fileOnIndividualResult.write('\r\n')

            finally:
                fileOnIndividualResult.close()




        pass


    buttonOnSVM = Button(setting_up, text="Training On SVM", command =
    TrainingOnSVM).grid(row=8,
                                                                      column=1,
                                                                      )





    ############# Result Borad ###########
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
    unknowRow = StringVar()
    Label(resultBoard,text="   ", textvariable=unknowRow,
          font=('Arial', 12)) \
        .grid(row=3, column=1, padx=5, pady=5,sticky=E)


    ##hamRow
    hamRow = StringVar()
    Label(resultBoard,text="   ", textvariable=hamRow,
          font=('Arial', 12)) \
        .grid(row=4, column=1, padx=5, pady=5,sticky=E)


    ##spamRow
    spamRow = StringVar()
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
