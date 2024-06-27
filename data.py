import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
data = pd.read_csv("Importance of understanding factors contributing to depression among students(10+2). (Responses) - Form Responses 1 (1).csv")
ages = data.Age
uAge= []
for i in ages:
    if(i not in uAge):
        uAge.append(i)
uAge.sort()
ages = uAge
print(ages)
dataByAges ={}
# sorted the data by groups
for i in ages:
    dataByAges[i]=data[data.Age == i]
# print(dataByAges)
qs = data.columns
#print(dataByAges[17])
# print(qs)
def sec1(datadic, age):
    data17 = np.array(datadic[age])
    chkpoints = {1: []}
    for i in data17:
        curr = {1: []}
        for j in range(4, 9):
            curr[1].append(i[j])
        for k in curr:
            chkpoints[k].append(curr[k])
    print(chkpoints)

    x1 = [0, 0]
    x2 = [0, 0]
    x3 = [0, 0, 0, 0]
    x4 = [0, 0, 0, 0, 0]
    x5 = [0, 0, 0, 0]
    for i in chkpoints[1]:
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

def sec2(datadic, age):
    data17 = np.array(datadic[age])

    chkpoints = { 2: []}
    for i in data17:
        curr = {2: []}
        for j in range(4, len(qs)):
            if (j >= 9 and j <= 16):
                curr[2].append(i[j])
        for k in curr:
            chkpoints[k].append(curr[k])

    print(chkpoints)

    x1 = [0, 0,0,0,0]
    x2 = [0, 0]
    x3 = [0, 0, 0, 0]
    x4 = [0, 0]
    x5 = [0, 0]
    x6 = [0,0]
    x7 = [0,0,0,0,0]
    x8 =[0,0,0,0]
    for i in chkpoints[2]:
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
    chkpoints = { 3: []}
    for i in data17:
        curr = { 3: []}
        for j in range(4, len(qs)):
            if (j >= 17 and j <= 20):
                curr[3].append(i[j])
        for k in curr:
            chkpoints[k].append(curr[k])

    print(chkpoints)
    x1 = [0, 0,0]
    x2 = [0, 0]
    x3 = [0, 0, 0, 0,0]
    x4 = [0, 0, 0]
    for i in chkpoints[3]:
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


def sec4(datadic, age):
    data17 = np.array(datadic[age])
    chkpoints = {4: []}
    for i in data17:
        curr = {4: []}
        for j in range(21, 30):
            curr[4].append(i[j])
        for k in curr:
            chkpoints[k].append(curr[k])

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

    for i in chkpoints[4]:
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

#SECTION 6
def sec6(datadic, age):
    data17 = np.array(datadic[age])
    chkpoints = { 6: [] }
    for i in data17:
        curr = {6: []}
        for j in range(4, len(qs)):
            if (j >= 35 and j <= 38):
                curr[6].append(i[j])
        for k in curr:
            chkpoints[k].append(curr[k])

    print(chkpoints)

    x1 = [0, 0]
    x2 = [0, 0]
    x3 = [0, 0, 0, 0,0]
    x4 = [0, 0]

    for i in chkpoints[6]:
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


for i in ages:
    print("AGE: ",i)
    print("Section: 1")
    sec1(dataByAges,i)
for i in ages:
    print("AGE: ", i)
    print("Section: 2")
    sec2(dataByAges,i)
for i in ages:
    print("AGE: ", i)
    print("Section: 3")
    sec3(dataByAges,i)
for i in ages:
    print("AGE: ", i)
    print("Section: 4")
    sec4(dataByAges,i)
for i in ages:
    print("AGE: ", i)
    print("Section: 6")
    sec6(dataByAges,i)
