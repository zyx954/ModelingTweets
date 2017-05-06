
import pickle,pprint

import json

pkl_file = open('./tweetsFeatureData.pkl', 'r')

data = pickle.load(pkl_file)
# pprint.pprint(data3[1])


# print data3[100].annotationMethod
try:
    # print json.dumps(data3[100], indent=1)

    print len(data)
    # print data

    # a,b,c=0,0,0;
    # print type(data[100].maliciousResult)
    # for p in data:
    #     if(p.maliciousResult=='0'):
    #         a=a+1;
    #     if (p.maliciousResult == '-1'):
    #         b = b + 1;
    #     if (p.maliciousResult == '1'):
    #         c = c + 1;
    #
    # print a,b,c
    # print type(data[100])
    #
    # data2 = pickle.load(pkl_file)
    # pprint.pprint(data2)
finally:
    pkl_file.close()

