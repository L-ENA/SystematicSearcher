import pandas as pd
from tqdm import tqdm
import re

path=r'C:\Users\lena.schmidt\Documents\SR automation review\Update_2\FinalExtraction.xlsx'
tabs = pd.ExcelFile(path).sheet_names
print(tabs)

df = pd.read_excel(path,
                   sheet_name = "Question 11",
                   skiprows = 1)


df=df[df["Answers"]=='"Yes, include the reference"']

includes=df["ActiveScreener Id"]
#print(len(includes))

new_df=pd.read_csv(r'C:\Users\lena.schmidt\Documents\SR automation review\Update_2\all_screened_2023.csv')
collist=[]
coldict={}
for i, id in enumerate(includes):
    print(i)
    cols={k: "" for k in new_df.columns}
    cols["ID"]=int(id)
    collist.append(cols)
    print(collist[i]["ID"])
    coldict[int(id)]=i

print(collist[1]["ID"])
print(collist[10]["ID"])
print(collist[20]["ID"])
#
# print(collist)
# print(coldict)
#
for t in tabs:

    df = pd.read_excel(path,sheet_name=t, skiprows=1)
    desc=df["Question"][0]
    print("-------TAB:", desc)
    cands=set()
    for c in new_df.columns:
        if c in desc:
            cands.add(c)
    if len(cands)>0:
        # print(cands)
        ca= max(cands, key=len)
    else:
        try:
            ca=cands[0]
        except:
            ca=False
    print(ca)
    if ca:
        print(ca)
        for i, row in df.iterrows():
            #print(type(row["ActiveScreener Id"]))
            if row["ActiveScreener Id"] in coldict.keys():
                collist[coldict[row["ActiveScreener Id"]]][ca]=row["Answers"].replace("|", ',').replace("\n", " ").replace("\"", "")
                #print(row["Answers"].replace("|", ',').replace("\n", " "))
            if ca== 'q5':
                collist[coldict[row["ActiveScreener Id"]]]['Xauthors'] = row["Authors"]
                collist[coldict[row["ActiveScreener Id"]]]['title'] = row["Title"]
                print(row["Title"])
                #collist[coldict[row["ActiveScreener Id"]]]['abstract'] = row["Answers"]
                collist[coldict[row["ActiveScreener Id"]]]['initial_decision'] = "Include"
                collist[coldict[row["ActiveScreener Id"]]]['expert_decision'] = "Include"
                collist[coldict[row["ActiveScreener Id"]]]['extraction_date'] = "10/10/2024"

#
new_df=new_df.append(collist, ignore_index=True, sort=False)
new_df.to_csv(r'C:\Users\lena.schmidt\Documents\SR automation review\Update_2\merged2024.csv', index=False)






#print(cols)



