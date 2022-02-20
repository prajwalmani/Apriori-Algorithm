
# sample transcation dataset from https://www.geeksforgeeks.org/apriori-algorithm/


from ast import Break
from itertools import combinations,permutations
from msilib.schema import DuplicateFile

transcations={
    't1':['i1','i2','i5'],
    't2':['i2','i4'],
    't3':['i2','i3'],
    't4':['i1','i2','i4'],
    't5':['i1','i3'],
    't6':['i2','i3'],
    't7':['i1','i3'],
    't8':['i1','i2','i3','i5'],
    't9':['i1','i2','i3']
}

min_support_value=2
min_confidence_value=50
confidence_values=[]

def generate_support(transcations,flag,trimmed_support):
    support={}
    values=[]
    for key,value in transcations.items():
        for i in value:
            if i not in values:
                if i not in support:
                    support[i]=0
                    temp_item_support=support[i]
                else:
                    temp_item_support=support[i]
                for inkey,invalue in transcations.items():
                        if i in invalue:
                                temp_item_support+=1
                                support[i]=temp_item_support
                values.append(i)
    if flag>=1:
        support={}
        for i in trimmed_support:
                if not isinstance(i, tuple):
                    i=tuple(map(str, i.split(',')))
                if i not in support:
                    support[i]=0
                    temp_item_support=support[i]
                else:
                    temp_item_support=support[i]
                for inkey,invalue in transcations.items():
                        if set(i).issubset(set(invalue)):
                                temp_item_support+=1
                                support[i]=temp_item_support
    return support

def trim_support(support):
    trim_support={}
    for key,value in support.items():
        if support[key]  >= min_support_value:
            trim_support[key]=value
    return trim_support


def combination(trim_support,combination_flag):
    if combination_flag<=2:
        combination_list=list(combinations((trim_support.keys()),combination_flag))
        return combination_list
    else:
        keys=[]
        for comb_key in trim_support:
            for i in comb_key:
                if i not in keys:
                    keys.append(i)
        combination_list=[",".join(map(str, comb)) for comb in combinations(keys, combination_flag)]
        return (combination_list)

def singlesupport(supportitem):
        support={}
        if not isinstance(supportitem, tuple):
            supportitem=tuple(supportitem)
        if supportitem not in support:
            support[supportitem]=0
            temp_item_support=support[supportitem]
        else:
            temp_item_support=support[supportitem]
        for inkey,invalue in transcations.items():
            if set(supportitem).issubset(set(invalue)):
                temp_item_support+=1
                support[supportitem]=temp_item_support
        singlesupports=support[supportitem]/len(transcations)      

        return singlesupports
        

def confidence(trimmed_support):
    confid={}
    confidence_values.clear()
    for i in trimmed_support.keys():
        i=list(i)
        perm=list(permutations(i))
        for j in list(perm):
            len_j=len(j)
            for k in range(1,len_j):
                j=list(j)
                j_duplicate=list(j)
                j_remove=j[k:]
                for l in j_remove:
                    j_duplicate.remove(l)
                unionupport=float((singlesupport(j)))
                RHSsupport=float((singlesupport(j_duplicate)))
                confidence_value=(unionupport/RHSsupport)*100
                if confidence_value>=min_confidence_value:
                    confid[str(j_duplicate)]=str(j[k:])
                    confidence_values.append(confidence_value)
    return confid

def getuniqeueelementslength(transcations):
    unique=[]
    for inkey,invalue in transcations.items():
        for items in invalue:
            if items not in unique:
                unique.append(items)
    return len(unique)

def call_functions(transcations):
    count=0 
    combination_list=[]
    confidences={}
    uniqueelements=getuniqeueelementslength(transcations)
    for i in range(uniqueelements):
        if count==0:
            trimmed=trim_support(generate_support(
                transcations=transcations,
                flag=i,
                trimmed_support=0
            ))
            comb=combination(trimmed,combination_flag=i+2)
            combination_list.append(comb)
        else:
            trimmed=trim_support(generate_support(
                transcations=transcations,
                flag=i,
                trimmed_support=combination_list[0]
            ))
            comb=combination(trimmed,combination_flag=i+2)
            combination_list.clear()
            combination_list.append(comb)
            confidences=confidence(trimmed)
            if bool(confidences)==False:
                print("Thats all the transcations")
                break
            for key,value in confidences.items():
                index=list(confidences.keys()).index(key)
                print("{}->{}:{}%".format(key,value,round(confidence_values[index],2)))
        count+=1

call_functions(transcations)

# ts=combination(trim_support(generate_support(transcations=transcations,flag=0,trimmed_support=0)),combination_flag=2)
# ts1=combination(trim_support(generate_support(transcations=transcations,flag=2,trimmed_support=ts)),combination_flag=3)
# ts2=combination(trim_support(generate_support(transcations=transcations,flag=3,trimmed_support=ts1)),combination_flag=4)
# ts3=combination(trim_support(generate_support(transcations=transcations,flag=3,trimmed_support=ts2)),combination_flag=4)
# # ts1=trim_support(generate_support(transcations=transcations,flag=2,trimmed_support=ts))
# # conf=confidence(generate_support(transcations=transcations,flag=2,trimmed_support=ts))
# confidence(trim_support(generate_support(transcations=transcations,flag=2,trimmed_support=ts1)))
# print(generate_support(transcations=transcations,flag=1,trimmed_support=0))
# print(ts)


  
