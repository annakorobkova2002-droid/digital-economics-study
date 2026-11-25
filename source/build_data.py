import json, importlib
topics=[]
for m in ["bank1","bank2","bank3","bank4"]:
    topics += importlib.import_module(m).T
from assign import A
ids=[t["id"] for t in topics]; assert len(ids)==len(set(ids))
for a in A:
    for t in a["topics"]: assert t in ids, t
n=dict(mcq=0,tf=0,cards=0)
for t in topics:
    for k in n: n[k]+=len(t[k])
    for q in t["mcq"]: assert len(q["o"])==4 and len(set(q["o"]))==4, q["q"]
print(len(topics),"topics",n,len(A),"assignments")
json.dump({"topics":topics,"assignments":A},open("bank.json","w"),ensure_ascii=False)
