import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
data = pd.read_csv("Importance of understanding factors contributing to depression among students(10+2). (Responses) - Form Responses 1.csv")
ages = list(data.Age)
ages.sort()

# TC: O(n^2) & SC: O(n)
# uAge= []
# for i in ages:
#     if(i not in uAge):
#         uAge.append(i)

# TC:O(n) & SC: O(1)
i=0
for j in range(1,len(ages)):
    if(ages[i]!=ages[j]):
        ages[i+1]=ages[j]
        i+=1
# deleting all the numbers after the ith Index (i.e. the duplicates)
del ages[i+1:]


dataByAges ={}
# sorted the data by groups
for i in ages:
    dataByAges[i]=data[data.Age == i]

# as the colum names are our questions thus we are storing the qs from the columns method
qs = data.columns

# SECTION 1
def sec1(datadic, age):
    dataSet = np.array(datadic[age])
    chkpoints = []
    for i in dataSet:
        curr = []
        for j in range(4, 9):
            curr.append(i[j])
        chkpoints.append(curr)
    print(chkpoints)
    x1 = [0, 0]
    x2 = [0, 0]
    x3 = [0, 0, 0, 0]
    x4 = [0, 0, 0, 0, 0]
    x5 = [0, 0, 0, 0]
    for i in chkpoints:
        for j in range(len(i)):
            # first qs
            if (j == 0):
                if i[j] == "YES":
                    x1[0] += 1
                else:
                    x1[1] += 1
            # second qs
            elif (j == 1):
                if i[j] == "YES":
                    x2[0] += 1
                else:
                    x2[1] += 1
            # third qs
            elif (j == 2):
                if i[j] == "FREQUENTLY":
                    x3[0] += 1
                elif i[j] == "NOT SO FREQUENTLY":
                    x3[1] += 1
                elif i[j] == "ONE TIME":
                    x3[2] += 1
                else:
                    x3[3] += 1
            # fourth qs
            elif (j == 3):
                if i[j] == 1.0:
                    x4[0] += 1
                elif i[j] == 2.0:
                    x4[1] += 1
                elif i[j] == 3.0:
                    x4[2] += 1
                elif i[j] == 4.0:
                    x4[3] += 1
                else:
                    x4[4] += 1
            # fifth qs
            elif (j == 4):
                if i[j] == "NOT COMFORTABLE AT ALL":
                    x5[0] += 1
                elif i[j] == "SOMEWHAT COMFORTABLE":
                    x5[1] += 1
                elif i[j] == "COMFORTABLE":
                    x5[2] += 1
                else:
                    x5[3] += 1
    print("x1:", x1)
    print("x2:", x2)
    print("x3:", x3)
    print("x4:", x4)
    print("x5:", x5)

    # ploting of graphs
    plt.subplot(2, 3, 1)
    plt.pie(x1, radius=1, autopct="%0.1f%%")
    plt.title(qs[4],fontsize=7)
    plt.legend(["yes", "no"], loc='upper left', fontsize=8)
    plt.subplot(2, 3, 2)
    plt.pie(x2, radius=1, autopct="%0.1f%%")
    plt.title(qs[5],fontsize=7)
    plt.legend(["yes", "no"], loc='upper left', fontsize=7)
    plt.subplot(2, 3, 3)
    plt.pie(x3, radius=1, autopct="%0.1f%%")
    plt.title(qs[6],fontsize=7)
    plt.legend(["ferquently", "not so frequently", "one time", "never"], loc='upper left', fontsize=7)
    plt.subplot(2, 3, 4)
    plt.pie(x4, radius=1, autopct="%0.1f%%")
    plt.title(qs[7],fontsize=5)
    plt.legend([1, 2, 3, 4, 5], loc='upper left', fontsize=7)
    plt.subplot(2, 3, 5)
    plt.pie(x5, radius=1, autopct="%0.1f%%")
    plt.title(qs[8],fontsize=5)
    plt.legend(["not comfortable at all", "somewhat comfortable", "comfortable", "very much comfortable"],
               loc='upper left', fontsize=7)
    plt.show()

# SECTION 2
def sec2(datadic, age):
    dataSet = np.array(datadic[age])
    chkpoints = []
    for i in dataSet:
        curr = []
        for j in range(9, 17):
            curr.append(i[j])
        chkpoints.append(curr)
    print(chkpoints)
    x1 = [0, 0,0,0,0]
    x2 = [0, 0]
    x3 = [0, 0, 0, 0]
    x4 = [0, 0]
    x5 = [0, 0]
    x6 = [0,0]
    x7 = [0,0,0,0,0]
    x8 =[0,0,0,0]
    for i in chkpoints:
        for j in range(len(i)):
            # first qs
            if (j == 0):
                if i[j] == 1.0:
                    x1[0] += 1
                elif i[j] == 2.0:
                    x1[1] += 1
                elif i[j] == 3.0:
                    x1[2] += 1
                elif i[j] == 4.0:
                    x1[3] += 1
                else:
                    x1[4]+=1
            # second qs
            elif (j == 1):
                if i[j] == "YES":
                    x2[0] += 1
                else:
                    x2[1] += 1
            # third qs
            elif (j == 2):
                if i[j] == "RARELY":
                    x3[0] += 1
                elif i[j] == "SOMETIMES":
                    x3[1] += 1
                elif i[j] == "OFTEN":
                    x3[2] += 1
                else:
                    x3[3] += 1
            # fourth qs
            elif (j == 3):
                if i[j] == "YES":
                    x4[0] += 1
                else:
                    x4[1] += 1
            # fifth qs
            elif (j == 4):
                if i[j] == "YES":
                    x5[0] += 1
                else:
                    x5[1] += 1
            #SIXTH QS
            elif (j==5):
                if i[j] == "YES":
                    x6[0] += 1
                else:
                    x6[1] += 1
            #seventh qs
            elif(j==6):
                if i[j] == "POOR":
                    x7[0] += 1
                elif i[j] == "FAIR":
                    x7[1] += 1
                elif i[j] == "GOOD":
                    x7[2] += 1
                elif i[j] == "VERY GOOD":
                    x7[3] += 1
                else:
                    x7[4] += 1
            #EIGHTH QS
            elif (j == 7):
                if i[j] == "NOT AT ALL":
                    x8[0] += 1
                elif i[j] == "SEVERAL DAYS":
                    x8[1] += 1
                elif i[j] == "MORE THAN HALF THE DAY":
                    x8[2] += 1
                else:
                    x8[3] += 1
    print("x1:", x1)
    print("x2:", x2)
    print("x3:", x3)
    print("x4:", x4)
    print("x5:", x5)
    print("x6:", x6)
    print("x7:", x7)
    print("x8:", x8)

    # ploting of graphs
    plt.subplot(4, 2, 1)
    plt.pie(x1, radius=1, autopct="%0.1f%%")
    plt.title(qs[9],fontsize=7)
    plt.legend([1,2,3,4,5], loc='upper left', fontsize=8)
    plt.subplot(4, 2, 2)
    plt.pie(x2, radius=1, autopct="%0.1f%%")
    plt.title(qs[10],fontsize=7)
    plt.legend(["yes", "no"], loc='upper left', fontsize=7)
    plt.subplot(4, 2, 3)
    plt.pie(x3, radius=1, autopct="%0.1f%%")
    plt.title(qs[11],fontsize=7)
    plt.legend(["RARELY", "SOMETIMES", "OFTEN", "ALWAYS"], loc='upper left', fontsize=7)
    plt.subplot(4, 2, 4)
    plt.pie(x4, radius=1, autopct="%0.1f%%")
    plt.title(qs[12],fontsize=5)
    plt.legend(["YES","NO"], loc='upper left', fontsize=7)
    plt.subplot(4,2, 5)
    plt.pie(x5, radius=1,autopct="%0.1f%%")
    plt.title(qs[13],fontsize=5)
    plt.legend(["YES", "NO"],
               loc='upper left', fontsize=7)
    plt.subplot(4, 2, 6)
    plt.pie(x5, radius=1, autopct="%0.1f%%")
    plt.title(qs[14], fontsize=5)
    plt.legend(["YES", "NO"],
               loc='upper left', fontsize=7)
    plt.subplot(4,2,7)
    plt.pie(x5, radius=1, autopct="%0.1f%%")
    plt.title(qs[15],fontsize=5)
    plt.legend(["POOR", "FAIR", "GOOD", "VERY GOOD","EXCELLENT"],
               loc='upper left', fontsize=7)
    plt.subplot(4,2,8)
    plt.pie(x5, radius=1, autopct="%0.1f%%")
    plt.title(qs[16], fontsize=5)
    plt.legend(["NOT AT ALL", "SEVERAL DAYS", "MORE THAN HALF THE DAYS", "NEARLY EVERYDAY"],
               loc='upper left', fontsize=7)
    plt.show()

# section 3
def sec3(datadic, age):
    data17 = np.array(datadic[age])
    chkpoints = []
    for i in data17:
        curr = []
        for j in range(17, 21):
            curr.append(i[j])
        chkpoints.append(curr)
    print(chkpoints)
    x1 = [0, 0,0]
    x2 = [0, 0]
    x3 = [0, 0, 0, 0,0]
    x4 = [0, 0, 0]
    for i in chkpoints:
        for j in range(len(i)):
            # first qs
            if (j == 0):
                if i[j] == "LIGHT":
                    x1[0] += 1
                elif(i[j]=="MODERATE"):
                    x1[1] += 1
                else:
                    x1[2]+=1
            # second qs
            elif (j == 1):
                if i[j] == "YES":
                    x2[0] += 1
                else:
                    x2[1] += 1
            # third qs
            elif (j == 2):
                if i[j] == 1.0:
                    x3[0] += 1
                elif i[j] == 2.0:
                    x3[1] += 1
                elif i[j] == 3.0:
                    x3[2] += 1
                elif i[j] == 4.0:
                    x3[3] += 1
                else:
                    x3[4] += 1
            # fourth qs
            elif (j == 3):
                if i[j] == "SELF CHOICE":
                    x4[0] += 1
                elif i[j] == "PRESSURIZED BY SOME INDIVIDUAL":
                    x4[1] += 1
                else:
                    x4[2] += 1
    print("x1:", x1)
    print("x2:", x2)
    print("x3:", x3)
    print("x4:", x4)
    plt.subplot(2, 2, 1)
    plt.pie(x1, radius=1, autopct="%0.1f%%")
    plt.title(qs[17],fontsize=7)
    plt.legend(["light","moderate","heavy"], loc='upper left', fontsize=8)
    plt.subplot(2, 2, 2)
    plt.pie(x2, radius=1, autopct="%0.1f%%")
    plt.title(qs[18],fontsize=7)
    plt.legend(["yes", "no"], loc='upper left', fontsize=7)
    plt.subplot(2, 2, 3)
    plt.pie(x3, radius=1, autopct="%0.1f%%")
    plt.title(qs[19],fontsize=5)
    plt.legend([1,2,3,4,5], loc='upper left', fontsize=7)
    plt.subplot(2, 2, 4)
    plt.pie(x4, radius=1, autopct="%0.1f%%")
    plt.title(qs[20],fontsize=5)
    plt.legend(["self choice","pressurized by some individual","peer pressure"], loc='upper left', fontsize=7)
    plt.show()

# SECTION 4
def sec4(datadic, age):
    dataSet = np.array(datadic[age])
    chkpoints = []
    for i in dataSet:
        curr = []
        for j in range(21, 30):
            curr.append(i[j])
        chkpoints.append(curr)
    print("Checkpoints:", chkpoints)
    x1 = [0, 0, 0, 0, 0]
    x2 = [0, 0]
    x3 = [0, 0, 0, 0, 0]
    x4 = [0, 0]
    x5 = [0, 0, 0, 0, 0]
    x6 = [0, 0]
    x7 = [0, 0, 0, 0, 0]
    x8 = [0, 0, 0, 0, 0]
    x9 = [0, 0, 0, 0]
    for i in chkpoints:
        for j in range(len(i)):
            if j == 0:
                if i[j] == 1.0:
                    x1[0] += 1
                elif i[j] == 2.0:
                    x1[1] += 1
                elif i[j] == 3.0:
                    x1[2] += 1
                elif i[j] == 4.0:
                    x1[3] += 1
                elif i[j] == 5.0:
                    x1[4] += 1
            elif j == 1:
                if i[j] == "YES":
                    x2[0] += 1
                else:
                    x2[1] += 1
            elif j == 2:
                if i[j] == 1.0:
                    x3[0] += 1
                elif i[j] == 2.0:
                    x3[1] += 1
                elif i[j] == 3.0:
                    x3[2] += 1
                elif i[j] == 4.0:
                    x3[3] += 1
                elif i[j] == 5.0:
                    x3[4] += 1
            elif j == 3:
                if i[j] == "YES":
                    x4[0] += 1
                else:
                    x4[1] += 1
            elif j == 4:
                if i[j] == 1.0:
                    x5[0] += 1
                elif i[j] == 2.0:
                    x5[1] += 1
                elif i[j] == 3.0:
                    x5[2] += 1
                elif i[j] == 4.0:
                    x5[3] += 1
                elif i[j] == 5.0:
                    x5[4] += 1
            elif j == 5:
                if i[j] == "YES":
                    x6[0] += 1
                else:
                    x6[1] += 1
            elif j == 6:
                if i[j] == 1.0:
                    x7[0] += 1
                elif i[j] == 2.0:
                    x7[1] += 1
                elif i[j] == 3.0:
                    x7[2] += 1
                elif i[j] == 4.0:
                    x7[3] += 1
                elif i[j] == 5.0:
                    x7[4] += 1
            elif j == 7:
                if i[j] == 1.0:
                    x8[0] += 1
                elif i[j] == 2.0:
                    x8[1] += 1
                elif i[j] == 3.0:
                    x8[2] += 1
                elif i[j] == 4.0:
                    x8[3] += 1
                elif i[j] == 5.0:
                    x8[4] += 1
            else:
                if i[j] == "NOT AT ALL":
                    x9[0] += 1
                elif i[j] == "SEVERAL DAYS":
                    x9[1] += 1
                elif i[j] == "MORE THAN HALF THE DAYS":
                    x9[2] += 1
                elif i[j] == "ALWAYS":
                    x9[3] += 1

    # Debugging output for the lists
    print("x1:", x1)
    print("x2:", x2)
    print("x3:", x3)
    print("x4:", x4)
    print("x5:", x5)
    print("x6:", x6)
    print("x7:", x7)
    print("x8:", x8)
    print("x9:", x9)

    # ploting of graphs
    plt.subplot(4, 5, 1)
    plt.pie(x1, radius=1, autopct="%0.1f%%")
    plt.title(qs[21], fontsize=7)
    plt.legend([1, 2, 3, 4, 5], loc='upper left', fontsize=8)
    plt.subplot(4, 5, 2)
    plt.pie(x2, radius=1, autopct="%0.1f%%")
    plt.title(qs[22], fontsize=7)
    plt.legend(["YES", "NO"], loc='upper left', fontsize=7)
    plt.subplot(4, 5, 3)
    plt.pie(x3, radius=1, autopct="%0.1f%%")
    plt.title(qs[23], fontsize=7)
    plt.legend([1, 2, 3, 4, 5], loc='upper left', fontsize=7)
    plt.subplot(4, 5, 4)
    plt.pie(x4, radius=1, autopct="%0.1f%%")
    plt.title(qs[24], fontsize=5)
    plt.legend(["YES", "NO"], loc='upper left', fontsize=7)
    plt.subplot(4, 5, 5)
    plt.pie(x5, radius=1, autopct="%0.1f%%")
    plt.title(qs[25], fontsize=5)
    plt.legend([1, 2, 3, 4, 5], loc='upper left', fontsize=7)
    plt.subplot(4, 5, 6)
    plt.pie(x6, radius=1, autopct="%0.1f%%")
    plt.title(qs[26], fontsize=5)
    plt.legend(["YES", "NO"], loc='upper left', fontsize=7)
    plt.subplot(4, 5, 7)
    plt.pie(x7, radius=1, autopct="%0.1f%%")
    plt.title(qs[27], fontsize=5)
    plt.legend([1, 2, 3, 4, 5], loc='upper left', fontsize=7)
    plt.subplot(4, 5, 8)
    plt.pie(x8, radius=1, autopct="%0.1f%%")
    plt.title(qs[28], fontsize=5)
    plt.legend([1, 2, 3, 4, 5], loc='upper left', fontsize=7)
    plt.subplot(4, 5, 9)
    plt.pie(x9, radius=1, autopct="%0.1f%%")
    plt.title(qs[29], fontsize=5)
    plt.legend(["NOT AT ALL", "SEVERAL DAYS", "MORE THAN HALF THE DAYS", "ALWAYS"], loc='upper left', fontsize=7)
    plt.show()

# SECTION 5
def optionSep(Alloptions):
    options=[]
    s=0
    for i in range(len(Alloptions)):
        if(Alloptions[i]==','):
            options.append(Alloptions[s:i])
            s=i+2
    return options

def sec5(datadic, age):
    print("AGE: ",age)
    dataForSection5 = np.array(datadic[age])

    # for the 3rd qs
    PrimarySourceOfStess = {}
    # for the 5th qs
    copeUp={}
    # response according to option of 1st qs
    res1=[0,0,0,0,0]
    # response according to option of 2nd qs
    res2=[0,0]
    # response according to option of 4th qs
    res4=[0,0]
    # responses for storing the choices of 5th qs
    res5=[]
    # here we will calculate the frequency for each option
    freqFor5={}
    responses = []
    for i in dataForSection5:
        curr=[]
        for j in range(30, 35):
            curr.append(i[j])
        responses.append(curr)
    # print(responses)
    # [[3, 'NO', 'Fear of not doing anything', 'YES','EXERCISE, LISTENING MUSIC, SPENDING SOME TIME WITH YOUR FRIENDS, SPENDING SOME TIME WITH YOURSELF, Sports'],[]]
    for i in responses:
        for j in range(len(i)):
            # first qs
            if j==0:
                if(i[j]==1.0):
                    res1[0]+=1
                elif (i[j] == 2.0):
                    res1[1] += 1
                elif (i[j] == 3.0):
                    res1[2] += 1
                elif (i[j] == 4.0):
                    res1[3] += 1
                else:
                    res1[4]+=1
            # second qs
            elif j==1:
                if(i[j]=="YES"):
                    res2[0]+=1
                else:
                    res2[1]+=1
            # third qs
            elif j==2:
                if(str(i[j]).upper() not in PrimarySourceOfStess.keys()):
                    # print(i[j],": ",words(str(i[j])))
                    # print(i[j], ": ", str(i[j]).split(","))
                    PrimarySourceOfStess[str(i[j]).upper()]=1
                else:
                    PrimarySourceOfStess[str(i[j]).upper()]+=1

            # fourth qs
            elif j==3:
                if (i[j] == "YES"):
                    res4[0] += 1
                else:
                    res4[1] += 1
            else:
                individualResponse=optionSep(str(i[j]))
                res5.append(individualResponse)

    # finding the frequency for each option
    for i in res5:
        for j in i:
            if j not in freqFor5:
                freqFor5[j]=1
            else:
                freqFor5[j]+=1
    print("Response for qs 1: ",res1)
    print("Response for qs 2: ",res2)
    print("Primary sources of stress(Qs 3) : ", PrimarySourceOfStess)
    print("Response for qs 4: ",res4)
    print("Response for qs 5:",res5)
    print("Frequency for qs 5:",freqFor5)
    x=["EXERCISE",'LISTENING MUSIC','SLEEPING','SPENDING SOME TIME WITH YOUR FRIENDS','SPENDING SOME TIME WITH YOUR FAMILY','SPENDING SOME TIME WITH YOUR PARTNER','SPENDING SOME TIME WITH YOURSELF','LISTENING AUDIOBOOKS','READING STORY BOOKS/ARTICLES','DANCE','MUSIC','DRAWING']
    xres=[]
    for i in x:
        if i in freqFor5:
            xres.append(freqFor5[i])
        else:
            xres.append(0)
    plt.subplot(2, 2, 1)
    plt.pie(res1, radius=1, autopct="%0.1f%%")
    plt.title(qs[30], fontsize=7)
    plt.legend([1,2,3,4,5], loc='upper left', fontsize=8)
    plt.subplot(2, 2, 2)
    plt.pie(res2, radius=1, autopct="%0.1f%%")
    plt.title(qs[31], fontsize=7)
    plt.legend(["YES", "NO"], loc='upper left', fontsize=7)
    plt.subplot(2, 2, 3)
    plt.pie(res4, radius=1, autopct="%0.1f%%")
    plt.title(qs[33], fontsize=5)
    plt.legend(["YES", "NO"], loc='upper left', fontsize=7)
    plt.subplot(2,2,4)
    plt.bar(x,xres,color="b")
    plt.xlabel("Various ways")
    plt.xticks(x,rotation=90,fontsize=5)
    plt.ylabel("count")
    plt.title("Number of students cope up with stress through various ways")
    plt.show()

#SECTION 6
def sec6(datadic, age):
    dataSet = np.array(datadic[age])
    chkpoints = []
    for i in dataSet:
        curr=[]
        for j in range(35, 39):
            curr.append(i[j])
        chkpoints.append(curr)
    print(chkpoints)
    x1 = [0, 0]
    x2 = [0, 0]
    x3 = [0, 0, 0, 0,0]
    x4 = [0, 0]
    for i in chkpoints:
        for j in range(len(i)):
            # first qs
            if (j == 0):
                if i[j] == "YES":
                    x1[0] += 1
                else:
                    x1[1] += 1
            # second qs
            elif (j == 1):
                if i[j] == "YES":
                    x2[0] += 1
                else:
                    x2[1] += 1
            # third qs
            elif(j == 2):
                if i[j] == 1:
                    x3[0] += 1
                elif i[j] == 2:
                    x3[1] += 1
                elif i[j] == 3:
                    x3[2] += 1
                elif i[j] == 4:
                    x3[3] += 1
                else:
                    x3[4] += 1

            # fourth qs
            else:
                if i[j] == "YES":
                    x4[0] += 1
                else:
                    x4[1] += 1
    print("x1:", x1)
    print("x2:", x2)
    print("x3:", x3)
    print("x4:", x4)

    # ploting of graphs
    plt.subplot(2, 2, 1)
    plt.pie(x1, radius=1, autopct="%0.1f%%")
    plt.title(qs[35],fontsize=7)
    plt.legend(["yes", "no"], loc='upper left', fontsize=8)
    plt.subplot(2, 2, 2)
    plt.pie(x2, radius=1, autopct="%0.1f%%")
    plt.title(qs[36],fontsize=7)
    plt.legend(["yes", "no"], loc='upper left', fontsize=7)
    plt.subplot(2, 2, 3)
    plt.pie(x3, radius=1, autopct="%0.1f%%")
    plt.title(qs[37],fontsize=7)
    plt.legend([1,2,3,4,5], loc='upper left', fontsize=7)
    plt.subplot(2, 2, 4)
    plt.pie(x4, radius=1, autopct="%0.1f%%")
    plt.title(qs[38],fontsize=5)
    plt.legend(["YES","NO"], loc='upper left', fontsize=7)
    plt.show()


# printing the datas
# printing the section 1 for every age
for i in ages:
    print("AGE: ",i)
    print("Section: 1")
    sec1(dataByAges,i)
# printing the section 2 for every age
for i in ages:
    print("AGE: ", i)
    print("Section: 2")
    sec2(dataByAges,i)
# printing the section 3 for every age
for i in ages:
    print("AGE: ", i)
    print("Section: 3")
    sec3(dataByAges,i)
# printing the section 4 for every age
for i in ages:
    print("AGE: ", i)
    print("Section: 4")
    sec4(dataByAges,i)
# printing the section 5 for every age
for i in ages:
    print("AGE: ",i)
    print("Section 5")
    sec5(dataByAges, i)
# # printing the section 6 for every age
for i in ages:
    print("AGE: ", i)
    print("Section: 6")
    sec6(dataByAges,i)

