import re
import random
import math
from math import ceil
class spam:

    def __init__(self):
        "do "

    def readFile(self):

        global n
        spamCount = 0
        nonSpamCount = 0
        cnt=0
        with open("spambase.data") as file:
            for line in file:
                # x=line.split(",")

                x = re.split(",|\n", line)
                n=x.__len__()-2

                cnt+=1
                dataSet.append(x)

        self.testSet(cnt)

        print((accuracy/cnt)*100)


    def checkspam(self, total, spam, nonspam):
        n=total.__len__()
        probablity_spamWord = [0 for k in range(n)]
        probablity_nonspamWord = [0 for k in range(n)]
        probablity_spam = [0 for k in range(n)]
        probablity_nonspam = [0 for k in range(n)]
        for i in range(spam.__len__()):
            probablity_spamWord[i] = (spam[i] / total[i])
            probablity_nonspamWord[i] = (nonspam[i] / total[i])
            totalSum = probablity_spamWord[i] + probablity_nonspamWord[i]
            probablity_spam[i] = probablity_spamWord[i] / totalSum
            probablity_nonspam[i] = probablity_nonspamWord[i] / totalSum
        #print(probablity_spam)
        #print(probablity_nonspam)



        '''probablity_spam=[0 for k in range (57)]
        probablity_nonspam=[0 for k in range (57)]

        for i in range (total.__len__()):
            probablity_spam[i]=(spam[i]/total[i])
            probablity_nonspam[i]=(nonspam[i]/total[i])
        print(probablity_spam)
        print(probablity_nonspam)
        '''

        accur=(self.spamMessage(probablity_spam,probablity_nonspam))
        return accur


    def spamMessage(self, probablity_spam,probablity_nonspam):


        for i in range (testData.__len__()):
            temp=testData[i]
            #print(temp.__len__)
            acr=0
            spam=0
            nonspam=0
            l=temp.__len__()
            i=0
            while i<l-2:
                if float(temp[i])>0:
                    if probablity_spam[i]>0:
                        spam+=math.log10(float(probablity_spam[i])+1)
                    if probablity_nonspam[i]>0:
                        nonspam+=math.log10(float(probablity_nonspam[i])+1)
                i+=1

            if spam> nonspam:
                acr+=(self.accuracy(1,temp[temp.__len__()-2]))
            else:
                acr+=(self.accuracy(0, temp[temp.__len__() - 2]))
        return acr
    def testSet(self,cnt):

        testset = ceil(cnt / 10.0)
        random.Random(10).shuffle(dataSet)
        k = 0
        tempData = list()
        while k < 10:
            tempData.extend(testData)
            testData.clear()
            i = 0
            idx = k * testset

            while i < testset:
                if i + idx >= cnt:
                    break
                testData.insert(i, dataSet[idx + i])
                i = i + 1
            index = (i * k) + testData.__len__()
            i = 0
            j = 0
            trainData.clear()
            while index + i < cnt:
                trainData.insert(j, dataSet[index + i])
                i = i + 1
                j = j + 1
            trainData.extend(tempData)

            self.calculate()
            k = k + 1
    def calculate(self):
        global n
        count=0
        spam = [0 for k in range(n)]
        nonspam = [0 for k in range(n)]
        total = [0 for k in range(n)]
        for i in range(trainData.__len__()):
            l = trainData[i].__len__()
            x=trainData[i]
            clas = x[l - 2]

            i = 0
            while i < l - 2:
                total[i] += float(x[i])
                if int(clas) == 1:
                    spam[i] += float(x[i])

                else:
                    nonspam[i] += float(x[i])

                i += 1

        #print(spam)
        count=(self.checkspam(total,spam,nonspam))
        #print(count)

    def accuracy(self, predicted, expected):

        global accuracy
        if int(predicted)== int(expected):
            accuracy+=1
        return accuracy

n=0
dataSet = list()
trainData = list()
testData=list()
accuracy=0
spam().readFile()
