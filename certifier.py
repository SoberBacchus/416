
d = open("debug.txt", "r")
o = open("output.txt", "r")
oline = ""
dline = ""

oLines = o.readlines()
o.close()
dLines = d.readlines()
d.close()
dDict = {}


for dline in dLines:
    dDict[line.split("\t")[0].strip(" ")] = dline.strip("\n")

oDict = {}

for oline in oLines:
    oDict[line.split("\t")[0].strip(" ")] = oline.strip("\n")

TP = 0
TN = 0
FN = 0
FP = 0

pos1 = -1
pos2 = -1

for i in oDict.keys():
    #i is the
    if(i in dDict.keys()):
        dline = dDict[i]
        oline = dDict[i]
        pos1 = int(oline[i].split("\t")[0].strip(" "))
        pos2 = int(oline[i].split("\t")[1].strip(" "))
        posactual1 = int(dline[i].split("\t")[0].strip(" ") )#actual
        posactual2 = int(dline[i].split("\t")[1].strip(" "))

        if(abs(pos1-posactual1)<10 and (abs(actualpos2-pos2) < 9)):
            TP+=1
        elif (pos1 == (1 or -5)):
            FN+=1
    else:
        #testing if negatives is right
        oline = oDict[i]
        if(int(oline.split("\t")[1].strip(" ")) == (1 or -5)):
            TN+=1
        else:
            FP+=1

#accuracy
print(TP/1./(TP+FN))
#precision
print(TN/1./(TN + FP))
