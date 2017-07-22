# Project Name

A software system to Modelling spam tweets


## Related Packages
###Packages
* [Twitter](http://mike.verdone.ca/twitter/#install) 
* [SciPy](https://www.scipy.org/)
* [MysqlDB](http://mysql-python.sourceforge.net/MySQLdb.html)
* [Numpy](http://www.numpy.org/)
* [Sklearn](http://scikit-learn.org/)

### setup working environment 
`pip install -r stable-req.txt`

## Project functions

### Data collection
#### Introduction
Collect tweets by ID via twitter API.
Export collected tweets into files
#### Usage
* Enter personal Twitter keys in DatacollectionScript.py  
* Customize "fileNames" in “DatacollectionScript.py” by choosing different name of Tweets ID files from SplitAs90000 folder
* Corresponding data files will be generated based on Tweets ID file. Such as “xaaData.pkl","xabData.pkl” and " xacData.pkl"


### Data injection to Mysql

#### Introduction
* Read tweets data from tweets data file, such as “xaaData.pkl",  by running MainEntry.py
* Build SQL statements
* Insert Tweets information (InsertTweetsStatement.py)
    * Insert or update user information (InsertUserStatement.py and UpdateUserStatement.py)
    * Execute statement and store tweets into MySQL (InjectTweet2Mysql.py)

#### Usage
* Required [Database Scheme](https://pasteboard.co/GB2k0HD.png) and  [Code](https://github.com/zyx954/project/blob/master/dataInjectionFromPickle2DB/Tweets.sql)
* Customize two variables in dataInjectionFromPickle2DB Folder
    * Change database setting at file Connect2Db.py
    * Customize variable "c” for different collected tweets files at MainEntry.py

### GUI

#### Introduction
There are three interfaces:
* Interface_GenerateFeature:
	* Generate features from chosen database to individual text file
	* Read specified feature file and demonstrate features
* Interface_Training.py:
	* Partition data into two parts training and testing
	* Training model and test by SVM or DT
	* Export confusion matrix result and predicted result into files
* Interface_Training_NFolder.py:
	* Partition data by N-folder.
	* Training model and test by SVM or DT
	* Export confusion matrix result into files

#### Usage

**1. Interface_GenerateFeature:**
* GetFeature Button will call a function to generate feature in generateFeature Folders
	* The features will store into a text file called "tweetsFeatureData.pkl"
* Move "tweetsFeatureData.pkl" file into GUI_temp Folders
* Choose this "tweetsFeatureData.pkl" file at “Interface_GenerateFeature” GUI
* Then, 10 tweets ID will be available in a dropdown list.
* The feature information will be demonstrated after choosing a tweet ID.

**2. Interface_Training.py:**
* Data partitioning
	* Choose a tweet feature file like “tweetsFeatureData.pkl” in drop down list
	* Set Training data and test data ratio.
	* Click the button on “Partitioning DataSet”
	* Partition result will be distributed into three files
	* data_pickle.pkl: training data and testing data
	* target_pickle.pkl: training target and testing target
	* IDs_pickle.pkl: training ID and testing ID
* Model Training
	* Choose parameters on DT or SVM
	* Choose a file path for confusion matrix result
	* Choose a file path for predicted result
	* Click button on DT or SVM
		* The confusion matrix result will be demonstrated in both GUI and exported to the specified file path
		* The Predicted result will be export the specified file path

**3. Interface_Training_NFolder.py:**
* Model Training
	* Choose a tweet feature file like “tweetsFeatureData.pkl” in drop down list
	* Set numbers of folder
	* Choose parameters on DT or SVM
	* Choose a file path for predicted result
	* Click button on DT or SVM
		* The Predicted result will be export the specified file 
