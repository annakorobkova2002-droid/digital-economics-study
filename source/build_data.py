import json, importlib
topics=[]
for m in ["bank1","bank2","bank3","bank4"]:
    topics += importlib.import_module(m).T
from assign import A
ORDER=["foundations","revolutions","google","domains","platforms","consumer","buyer","experimentation","data","constraints","disruption","valueprop","approaches","ai1","ai2","green","antifragile","physical"]
HB={"foundations":"02","revolutions":"03","google":"04","domains":"05","platforms":"05 & 07","consumer":"06","buyer":"08","experimentation":"09","data":"10","constraints":"11","disruption":"12","valueprop":"13","approaches":"14","ai1":"15","ai2":"16","green":"17 & 20","antifragile":"18 & 21","physical":"19"}
topics=sorted(topics,key=lambda t:ORDER.index(t["id"]))
for i,t in enumerate(topics,1): t["n"]=i; t["hb"]=HB[t["id"]]
ids=[t["id"] for t in topics]; assert len(ids)==len(set(ids))
for a in A:
    for t in a["topics"]: assert t in ids, t
n=dict(mcq=0,tf=0,cards=0)
for t in topics:
    for k in n: n[k]+=len(t[k])
    for q in t["mcq"]: assert len(q["o"])==4 and len(set(q["o"]))==4, q["q"]
print(len(topics),"topics",n,len(A),"assignments")
json.dump({"topics":topics,"assignments":A},open("bank.json","w"),ensure_ascii=False)
