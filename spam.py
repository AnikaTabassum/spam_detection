import re
class spam:
    def __init__(self):
        "do "


    def readFile(self):
        dataItem = set()
        transact=list()
        n=57
        spamCount=0
        nonSpamCount=0
        spam=[0 for k in range(n)] 
        nonspam=[0 for k in range(n)] 
        total=[0 for k in range(n)] 
        with open("spambase.data") as file:
            for line in file:
                # x=line.split(",")
                
                x = re.split(",|\n", line)
                l=x.__len__()
                clas=x[l-2]
                if int(clas)==1:
                    spamCount+=1
                else:
                    nonSpamCount+=1
                i=0
                while i < l-2:
                    total[i]+=float(x[i])
                    if int(clas)==1:
                        spam[i]+=float(x[i])
                        
                    else:
                        nonspam[i]+=float(x[i])
                        
                    i+=1

        print(total)
        print("spam")
        print(spamCount)
        print("nonspam")
        print(nonSpamCount)
        self.checkspam(total,spam,nonspam,spamCount, nonSpamCount)

    def checkspam(self,total,spam,nonspam,spamCount, nonSpamCount):
        probablity_spamWord=[0 for k in range (57)]
        probablity_nonspamWord=[0 for k in range (57)]
        probablity_spam=[0 for k in range (57)]
        probablity_nonspam=[0 for k in range (57)]
        for i in range (spam.__len__()):
            probablity_spamWord[i]=(spam[i]/spamCount)
            probablity_nonspamWord[i]=(nonspam[i]/nonSpamCount)
            totalSum=probablity_spamWord[i]+probablity_nonspamWord[i]
            probablity_spam[i]=probablity_spamWord[i]/totalSum
            probablity_nonspam[i]=probablity_nonspamWord[i]/totalSum
        print(probablity_spam)
        print(probablity_nonspam)

        spam=1
        nonspam=1
        for value in probablity_spam:
            if value>0:
                spam*=value
        
        for value in probablity_nonspam:
            if value>0:
                nonspam*=value

        print("spam "+str(spam))
        print("nonspam "+str(nonspam))        



        '''probablity_spam=[0 for k in range (57)]
        probablity_nonspam=[0 for k in range (57)]
        
        for i in range (total.__len__()):
            probablity_spam[i]=(spam[i]/total[i])
            probablity_nonspam[i]=(nonspam[i]/total[i])
        print(probablity_spam)
        print(probablity_nonspam)
        spam=1
        nonspam=1
        for value in probablity_spam:
            if value>0:
                spam*=value
        
        for value in probablity_nonspam:
            if value>0:
                nonspam*=value

        print("spam "+str(spam))
        print("nonspam "+str(nonspam))'''
                
spam().readFile()
