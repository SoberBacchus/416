def get_firstx_reads(num, file):
     #ONLY USE THIS CODE ONEC
    reader = open(file, 'r')
    seq = []
    first = reader.readline()
    line = first
    idsOI = []
    for currIdRead in range(num):
        idsOI.append("S0R" + str(currIdRead) + "/2")
    count =0
    w = open("debug.txt", "w")
    while(len(seq) < num and (line != "")):

        line = reader.readline()
        currId = line.split("\t")[0].strip(" ")
        if(not currId.find("/1") > 0):
            try:
                if int(currId[currId.find("R")+1:currId.find("/")]) < num+1:
                    w.write(line)

            except ValueError:
                print("Err in Paradise!")
    w.close()
    file = open("debug.txt", "r")
    lines = file.readlines()
    file.close()
    line = ""
    first = {}
    second = {} #stores
    sort_lst = []
    integer = 0


    file = open("debug.txt", "w")
    for line in lines:
        st = ""
        st = line.split("\t")[0].strip(" ")
        integer = int(st[st.find("R")+1:st.find("/")])
        first[integer] = line
        sort_lst.append(integer)
    sort_lst.sort()
    for integer in sort_lst:

        line = first[integer]
        file.write(line)
    file.close()
def certify():
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
        dDict[dline.split("\t")[0].strip(" ")] = dline.strip("\n")

    oDict = {}

    for oline in oLines:
        oDict[oline.split("\t")[0].strip(" ")] = oline.strip("\n")

    TP = 0
    TN = 0
    FN = 0
    FP = 0

    pos1 = -1
    pos2 = -1

    bestMatches = 0
    missedMatches = 0
    badMatches = 0
    correctMismatches = 0

    for seq in dDict.keys():
        if seq in oDict.keys():
            pos1 = int(oDict[seq].split("\t")[1].strip(" "))
            pos2 = int(oDict[seq].split("\t")[2].strip(" "))

            posactual1 = int(dDict[seq].split("\t")[1].strip(" ") )#actual
            posactual2 = int(dDict[seq].split("\t")[2].strip(" "))

            if(abs(pos1-posactual1)<9 and (abs(posactual2-pos2) < 10)):
                bestMatches+=1
            else:
                print(seq)
                badMatches+=1
        else:
            missedMatches+=1
    for seq in oDict.keys():
        if seq not in dDict.keys() and int(oDict[seq].split("\t")[1]) == (-1):
            correctMismatches+=1
    print("secondary accuracies")
    TP = bestMatches
    TN = correctMismatches
    FP = badMatches
    FN = missedMatches
    print(bestMatches, correctMismatches, badMatches, missedMatches)

    print("primary accuracies")
    print(TP, TN, FP,FN)
    return(TP*1./(TP+FN), TN/1./(TN + FP))
    #
    print()
    #
    print()
