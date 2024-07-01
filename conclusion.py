import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("Importance of understanding factors contributing to depression among students(10+2). (Responses) - Form Responses 1 (1).csv")
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

# # CONCLUSION DATAS

con={}
for i in ages:
    con[i]={"car": 0,
           "aca": 0,
           "Not": 0,
           'fam': 0,
           'per': 0,
            'j':0,
           'soc': 0}

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
        elif (i==18):
            if res[i].upper() in["YES",'NO']:
                chklst[0][1]=1
        elif(i==19):
            if res[i] in[1,2,3,4]:
                chklst[0][2]=1
        elif(i==20):
            if res[i].upper() in['SELF CHOICE','PRESSURED BY SOME INDIVIDUAL','PEER']:
                chklst[0][3]=1
    for i in range(30,34):
        if(i==30):
            if res[i] in [3,4,5]:
                chklst[1][0]=1
        elif(i==31):
            if res[i].upper() in["YES",'NO']:
                chklst[1][1]=1
        elif(i==32):
            if res[i].upper() in["ACADEMIC","STUDIES","STUDY","EXAMS","EDUCATION","EXAM","ACADEMICS","STUDYING","RESOURCES","FORCED","SYLLABUS","MARKS","WORKLOAD","WORK PRESSURE","TEACHERS","DAILY"]:
                chklst[1][2]=1
        else:
            if res[i].upper() in['YES','NO']:
                chklst[1][3]=1
        for i in chklst:
            for  j in i:
                if j==0:
                    return False
                else:
                    return True
def family(res):
    chklst=[0,0]
    if res[28] in [1,2,3]:
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
    if res[30] in [3, 4, 5]:
        return True
    return False

def social(res):
    chklst=[[0,0,0,0,0,0,0,0,0],[0]]
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
    CAREER=["WORK","FUTURE","CAREER","GOAL",'DAILY']
    ACADEMIC=["ACADEMIC","STUDIES","STUDY","EXAMS","EDUCATION","EXAM","ACADEMICS","STUDYING","RESOURCES","FORCED","SYLLABUS","MARKS","WORKLOAD","WORK PRESSURE","TEACHERS","DAILY"]
    NOT= ["OK","||","DON'T HAVE","NOTHING","NAN","NO",'.']
    FAMILY=["FAMILY","PARENTAL","PARENTS","MONETARY","MONEY","DAILY","FINANCIAL"]
    PERSONAL=["PERSONAL","OWN",'SOLITUDE','FEAR','CLOSED ONES','LIFE','MOBILE','MOBILITY','PORCRASTINATION','PROCRASTINATION','LONLINESS','LONELY','RELATIONSHIP','OVERTHINKING','THINKING','THING','ATTACHMENT','DAILY','SINGLE','PHOBIA','MONOTONOUS','TENSION']
    SOCIAL=['SOCIAL','JUDGEMENTAL','FRIENDS','DAILY']
    ALL=["DON'T KNOW","DK","NOT TO SAY","YES","IDEA","EVERYTHING","MANY","NOT ANT PARTICULAR THING","PARTICULAR"]
    JOB=["OFFICE","JOB","DAILY"]
    primarySource = indiRes[32]
    lst=words(primarySource)
    CheckOption = []
    x=False
    if ((career(indiRes))):
        con[age]["car"] = 1
        x=True
        CheckOption.append("Career")
    if ((academic(indiRes))):
        con[age]["aca"] = 1
        x = True
        CheckOption.append("Academic")
    if ((family(indiRes))):
        con[age]["fam"] = 1
        x = True
        CheckOption.append("Family")
    if ((personal(indiRes))):
        con[age]["per"] = 1
        x = True
        CheckOption.append("Personal")
    if ((social(indiRes))):
        con[age]["soc"] = 1
        x = True
        CheckOption.append("Social")
    if not x :
        con[age]["Not"]=1
    for i in lst:
        if (i != "" or i !=","):
            if("Career" not in CheckOption):
                if(i.upper() in CAREER):
                    if career(indiRes):
                        con[age]['car']+=1
                        CheckOption.append("Career")
            if ("Academic" not in CheckOption):
                if(i.upper() in ACADEMIC):
                    if academic(indiRes):
                        con[age]['aca']+=1
                        CheckOption.append("Academic")
            if("Job" not in CheckOption):
                if(i.upper() in JOB):
                    print("RESPONSE: ", i)
                    if job(indiRes):
                        con[age]['j']+=1
                        CheckOption.append("Job")
            if ("Family" not in CheckOption):
                if(i.upper() in FAMILY):
                    if family(indiRes):
                        con[age]['fam']+=1
                        CheckOption.append("Family")
            if ("Personal" not in CheckOption):
                if(i.upper() in PERSONAL):
                    if personal(indiRes):
                        con[age]['per']+=1
                        CheckOption.append("Personal")
            if ("Career" not in CheckOption):
                if(i.upper() in SOCIAL):
                    if social(indiRes):
                        con[age]['soc']+=1
                        CheckOption.append("Career")
            if(i.upper() in ALL):
                chk=False
                if career(indiRes):
                    con[age]['car']+=1
                    chk=True
                if academic(indiRes):
                    con[age]['aca']+=1
                    chk = True
                # if job(indiRes):
                #     con[age]['j']+=1
                #     chk = True
                if family(indiRes):
                    con[age]['fam'] += 1
                    chk = True
                if personal(indiRes):
                    con[age]['per']+=1
                    chk = True
                if social(indiRes):
                    con[age]['soc']+=1
                    chk = True
                if(not chk):
                    con[age]['Not']+=1
            if (i.upper() in NOT):
                con[age]['Not'] += 1

    # return con


def conclusion(age):
    df = np.array(dataByAges[age])
    qs = data.columns
    # RESPONSES FOR MENTAL STABILITY = NOT WELL
    res1 = [[1, 2, 3, 4], ["YES"], ["SOMETIMES", "OFTEN", "ALWAYS"], ['YES', 'NO'], ['YES'], ['YES', 'NO'],
            ['POOR', 'FAIR', 'GOOD'], ['SEVERAL DAYS', 'MORE THAN HALF THE DAY', 'NEARLY EVERYDAY']]
    for i in df:
        chk = [0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(9, 17):
            if (i[j] in res1[j - 9]):
                chk[j - 9] = 1
        for k in chk:
            if (k == 0):
                con[age]['Not']+=1
                break
        else:
            forward(i,age)
for i in ages:
    conclusion(i)
print(con)
