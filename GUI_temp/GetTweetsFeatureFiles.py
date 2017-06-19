
from os import listdir
from os.path import isfile, join,dirname,realpath
import re



def getTweetsFeatureFiles():
    # get current direction
    dir_path = dirname(realpath(__file__))

    # get all files from current direction
    onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

    print onlyfiles

    # filter unrelated file name
    tweetsFeatureFiles = []
    for item in onlyfiles:
        matchObj = re.match( r'tweetsFeature.*', item)
        if matchObj:
            item=item.strip('.pkl')
            tweetsFeatureFiles.append(item)

    print tweetsFeatureFiles
    return tweetsFeatureFiles

