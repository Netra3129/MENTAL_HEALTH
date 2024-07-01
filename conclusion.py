import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("Importance of understanding factors contributing to depression among students(10+2). (Responses) - Form Responses 1.csv")
ages = data.Age
uAge= []
for i in ages:
    if(i not in uAge):
        uAge.append(i)
uAge.sort()
ages = uAge
# print(ages)
dataByAges ={}
# sorted the data by groups
for i in ages:
    dataByAges[i]=data[data.Age == i]
df = np.array(dataByAges[19])
qs =  data.columns

#CONCLUSION DATAS
NO=0
ACADEMICS=0
CAREER=0
familyPressure=0
socialLife=0
Personal=0

def words(sentence):
    wordslst = []
    s = 0
    for i in range(1, len(sentence)):
        if ((sentence[i] == " " and sentence[i - 1] != " ") or sentence[i]==',' ):
            wordslst.append(sentence[s:i])
            s = i + 1
        elif (i == len(sentence) - 1):
            wordslst.append(sentence[s:i + 1])
    return wordslst

def career(res):
    if res[30] in [3, 4, 5]:
        return True
    return False
def academic(res):
    chklst=[[0,0,0,0],[0,0,0,0]]
    for i in range(17,21):
        if i==17:
            if res[i].upper() in ["MODERATE",'HEAVY']:
                chklst[0][0]=1
        elif
        elif res[i].upper() in["YES",'NO']:
            chklst[0][1]=1
        elif res[i].upper() in[1,2,3]:
            chklst[0][2]=1
        elif res[i].upper() in['SELF CHOICE','PRESSURED BY SOME INDIVIDUAL','PEER']:
            chklst[0][3]=1
    for i in range(30,34):
        if res[i].upper() in [3,4,5]:
            chklst[1][0]=1
        elif res[i].upper() in["YES",'NO']:
            chklst[1][1]=1
        elif res[i].upper() in["ACADEMIC","STUDIES","STUDY","EXAMS","EDUCATION","EXAM","ACADEMICS","STUDYING","RESOURCES","FORCED","SYLLABUS","MARKS","WORKLOAD","WORK PRESSURE","TEACHERS","DAILY"]:

            chklst[1][2]=1
        elif res[i].upper() in['YES','NO']:
            chklst[1][3]=1
        for i in chklst:
            for  j in i:
                if j==0:
                    return False
                else:
                    return True
def family(res):
    chklst=[0,0]
    if res[28].upper() in [1,2,3]:
        chklst[0]=1
    if res[30] in [3,4,5]:
        chklst[1]=1
    for i in chklst:
         if i==0:
             return False
    else:
        return True

def personal(res):
    chklst=[[0],[0,0,0]]
    if res[30] in [3,4,5]:
        chklst[0][0]=1
    for i in range(36,39):
        if(i==36):
            if res[i].upper() in ["YES"]:
                chklst[1][0]=1
        elif(i==37):
            if(res[i] in [3,4,5]):
                chklst[1][1]=1
        else:
            if(res[i].upper() == "YES"):
                chklst[1][2]=1
    for i in chklst:
        for j in i:
            if j==0:
                return False
    else:
        return True


def job(res):
    if res[30].upper() in [3, 4, 5]:
        return True
    return False

def social(res):
    chklst=[[0,0,0,0,0,0,0,0],[0]]
    for i in range(21,30):
        if i==21:
            if res[i] in [1,2,3,4,5]:
                chklst[0][0]=1
        elif i==22:
            if res[i].upper() in ['YES','NO']:
                chklst[0][1]=1
        elif i==23:
            if res[i] in [1,2,3,4,5]:
                chklst[0][2]=1
        elif i==24:
            if res[i].upper() == "YES":
                chklst[0][3]=1
        elif i==25:
            if res[i] in[1,2,3,4,5]:
                chklst[0][4]=1
        elif i==26:
            if res[i].upper() in ["YES",'NO']:
                chklst[0][5]=1
        elif i==27:
            if res[i] in [3,4,5]:
                chklst[0][7]=1
        elif i==29:
            if res[i] in ['NOT AT ALL','SEVERAL DAYS','MORE THAN HALF THE DAYS','ALWAYS']:
                chklst[0][8]=1
    if res[30] in [3,4,5]:
        chklst[1][0]=1
    for i in chklst:
        for j in i:
            if j == 0:
                return False
    else:
        return True


def forward(indiRes,age):
    print(indiRes)
    CAREER=["WORK","FUTURE","CAREER","GOAL",'DAILY']
    ACADEMIC=["ACADEMIC","STUDIES","STUDY","EXAMS","EDUCATION","EXAM","ACADEMICS","STUDYING","RESOURCES","FORCED","SYLLABUS","MARKS","WORKLOAD","WORK PRESSURE","TEACHERS","DAILY"]
    NOT= ["OK","||","DON'T HAVE","NOTHING","NAN","NO",'.']
    FAMILY=["FAMILY","PARENTAL","PARENTS","MONETARY","MONEY","DAILY","FINANCIAL"]
    PERSONAL=["PERSONAL","OWN",'SOLITUDE','FEAR','CLOSED ONES','LIFE','LONELINESS','MOBILE',"SELF-CONFIDENCE","GUIDANCE","HYPERTENSION",'MOBILITY','PORCRASTINATION','PROCRASTINATION','LONELY','RELATIONSHIP','OVERTHINKING','THINKING','THING','ATTACHMENT','DAILY','SINGLE','PHOBIA','MONOTONOUS','TENSION']
    SOCIAL=['SOCIAL','JUDGEMENTAL','FRIENDS','DAILY']
    ALL=["DON'T KNOW","DK","NOT TO SAY","YES","IDEA","EVERYTHING","MANY","NOT ANT PARTICULAR THING","PARTICULAR"]
    JOB=["OFFICE","JOB","DAILY"]
    car=0
    aca=0
    Not=0
    fam=0
    per=0
    soc=0
    j=0
    primarySource = indiRes[32]
    lst=words(primarySource)
    for i in lst:
        # print("I: ",i)
        if (i != "" or i !=","):
            if(i.upper() in CAREER):
                if career(indiRes):
                    car+=1
            if(i.upper() in ACADEMIC):
                if academic(indiRes):
                    aca+=1
            if(i.upper() in JOB):
                if job(indiRes):
                    j+=1
            if(i.upper() in FAMILY):
                if family(indiRes):
                    fam+=1
            if(i.upper() in PERSONAL):
                if personal(indiRes):
                    per+=1
            if(i.upper() in SOCIAL):
                if social(indiRes):
                    soc+=1
            if(i.upper() in ALL):
                chk=False
                if career(indiRes):
                    car+=1
                    chk=True
                if academic(indiRes):
                    aca+=1
                    chk = True
                if job(indiRes):
                    j+=1
                    chk = True
                if family(indiRes):
                    fam+=1
                    chk = True
                if personal(indiRes):
                    per+=1
                    chk = True
                if social(indiRes):
                    soc+=1
                    chk = True
                if(not chk):
                    Not+=1
                    print("not")
            if (i.upper() in NOT):
                Not+=1
                print("Not")


# RESPONSES FOR MENTAL STABILITY = NOT WELL
res1 = [[1,2,3,4],["YES"],["SOMETIMES","OFTEN","ALWAYS"],['YES','NO'],['YES'],['YES','NO'],['POOR','FAIR','GOOD'],['SEVERAL DAYS','MORE THAN HALF THE DAY','NEARLY EVERYDAY']]

for i in df:
    chk=[0,0,0,0,0,0,0,0]
    for j in range(9,17):
        if(i[j] in res1[j-9]):
            chk[j-9]=1
    for k in chk:
        if(k==0):
            NO+=1
            # print("NO")
            break
    else:
        # print(i)
        # move further
        forward(i,19)
        # career()
        # academics()
        # personal()
        # social()
        # family()
