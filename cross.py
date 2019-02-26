import re
import random
import math
class spam:
    def __init__(self):
        "do "

    def readFile(self):

        n = 57
        spamCount = 0
        nonSpamCount = 0
        spam = [0 for k in range(n)]
        nonspam = [0 for k in range(n)]
        total = [0 for k in range(n)]
        with open("spambase.data") as file:
            for line in file:
                # x=line.split(",")

                x = re.split(",|\n", line)
                dataset.append(x)
                l = x.__len__()
                clas = x[l - 2]
                if int(clas) == 1:
                    spamCount += 1
                else:
                    nonSpamCount += 1
                i = 0
                while i < l - 2:
                    total[i] += float(x[i])
                    if int(clas) == 1:
                        spam[i] += float(x[i])

                    else:
                        nonspam[i] += float(x[i])

                    i += 1

        print(total)
        print("spam")
        print(spamCount)
        print("nonspam")
        print(nonSpamCount)
        self.checkspam(total, spam, nonspam)

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
        print(probablity_spam)
        print(probablity_nonspam)



        '''probablity_spam=[0 for k in range (57)]
        probablity_nonspam=[0 for k in range (57)]

        for i in range (total.__len__()):
            probablity_spam[i]=(spam[i]/total[i])
            probablity_nonspam[i]=(nonspam[i]/total[i])
        print(probablity_spam)
        print(probablity_nonspam)
        '''

        self.spamMessage(probablity_spam,probablity_nonspam)


    def spamMessage(self, probablity_spam,probablity_nonspam):
        given = input("please enter your email")
        temp=re.split(",|\n", given)
        print(temp)
        spam=1
        nonspam=1
        l=temp.__len__()
        i=0
        while i<l-2:
            if float(temp[i])>0:
                if probablity_spam[i]>0:
                    spam*=float(probablity_spam[i])
                if probablity_nonspam[i]>0:
                    nonspam*=float(probablity_nonspam[i])
            i+=1

        print(spam)
        print(nonspam)

        if spam> nonspam:
            print("Your message is spam")
        else:
            print("Your message is non-spam")


dataset=list()
spam().readFile()
