
from Tkinter import *
import tkMessageBox
# Python 2.7, ttk provides Combobox
from ttk import *
# todo Now can not run this in pycham.
from ..Training import DataPreprocess
import GetTweetsIDFromPickle


dataPreprocess  = DataPreprocess.dataProcess
getfile = GetTweetsIDFromPickle.getFile
def partitioningData():
    # get value from snipBox; validate value ; call
    global w1,w2,w3
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
    #     todo , here should no pass f
        f = getfile()
        dataPreprocess(trainingPercentage,
                       validationPercentage,f)
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

# Let user choose the number of rows in the cave environment
rows = Label(setting_up, text="Please choose percentage of training "
                              "data:") \
    .grid(row=1, column=0, padx=5, pady=5)
w1 = Spinbox(setting_up, from_=1, to=100)
w1.grid(row=1, column=1, padx=5, pady=5)

# Let user choose the number of columns in the cave environment
columns = Label(setting_up, text="Please choose percentage of validation "
                                 "data:")
columns.grid(row=2, column=0, padx=5, pady=5)
w2 = Spinbox(setting_up, from_=1, to=100)
w2.grid(row=2, column=1, padx=5, pady=5)

# Let user choose the number of pits in the cave environment
pits = Label(setting_up, text="Please choose percentage of testing data")
pits.grid(row=3, column=0, padx=5, pady=5)
w3 = Spinbox(setting_up, from_=1, to=100)
w3.grid(row=3, column=1, padx=5, pady=5)

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
Label(fixed_board, text="Fixed Board Setting", font=('Arial', 12, 'bold')). \
    grid(row=0, column=0, columnspan=4, padx=5, pady=5)

Label(fixed_board, text='Please Note: The board will be 3x3 and only one pit is allowed. \
Please choose a room for the wumpus,\n a room for one pit, and a room for the gold. The wumpus \
and the pit cannot be in rooms (1,3),(1,2), (2,3),\n the gold cannot be in room (1,3), and the \
three must occupy different rooms.', \
      font=('Arial', 10)).grid(row=1, column=0, columnspan=4, padx=5,
                               pady=5)

# Choose a position for the wumpus
Label(fixed_board, text="A room for the wumpus.   Column: ") \
    .grid(row=2, column=0, padx=5, pady=5, sticky='E')
w_column = Spinbox(fixed_board, from_=1, to=3)
w_column.grid(row=2, column=1, padx=5, pady=5, sticky=W)

Label(fixed_board, text="Row: ") \
    .grid(row=2, column=2, padx=5, pady=5, sticky=W)
w_row = Spinbox(fixed_board, from_=1, to=3)
w_row.grid(row=2, column=3, padx=5, pady=5, sticky=W)

# Choose a position for one pit
Label(fixed_board, text="A room for one pit.   Column: ") \
    .grid(row=3, column=0, padx=5, pady=5, sticky='E')
p_column = Spinbox(fixed_board, from_=1, to=3)
p_column.grid(row=3, column=1, padx=5, pady=5, sticky=W)

Label(fixed_board, text="Row :") \
    .grid(row=3, column=2, padx=5, pady=5, sticky=W)
p_row = Spinbox(fixed_board, from_=1, to=3)
p_row.grid(row=3, column=3, padx=5, pady=5, sticky=W)

# Choose a position for the gold
Label(fixed_board, text="A room for the gold.   Column: ") \
    .grid(row=4, column=0, padx=5, pady=5, sticky='E')
g_column = Spinbox(fixed_board, from_=1, to=3)
g_column.grid(row=4, column=1, padx=5, pady=5, sticky=W)

Label(fixed_board, text="Row: ") \
    .grid(row=4, column=2, padx=5, pady=5, sticky=W)
g_row = Spinbox(fixed_board, from_=1, to=3)
g_row.grid(row=4, column=3, padx=5, pady=5, sticky=W)

# A button to get the setting
# button = Button(setting_up, text="Set Up", command=getInfor).grid(row=6,
#                                                                   column=0,
#                                                                   columnspan=2)
button = Button(setting_up, text="Set Up", ).grid(row=6,
                                                                  column=0,
                                                                  columnspan=2)

## Set up the environment board, here it is an empty area, just a place holder
board = Canvas(main_GUI, width=board_width, height=board_height,
               highlightbackground='black')
board.grid(row=0, column=1, rowspan=2)
main_GUI.title("The Wumpus World")
main_GUI.mainloop()
