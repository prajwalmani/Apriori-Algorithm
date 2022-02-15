
# sample transcation dataset from https://www.geeksforgeeks.org/apriori-algorithm/


from itertools import combinations,product

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
    if flag>=2:
        support={}
        values=[]
        for i in trimmed_support:
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

# trim_support=trim_support(generate_support(transcations,1,{}))

def combination(trim_support,combination_flag):
    if combination_flag<=2:
        combination_list=list(combinations((trim_support.keys()),combination_flag))
        return combination_list
    if combination_flag==3:
        keys=[]
        for comb_key in trim_support:
            keys.append(list(comb_key))
        print(list(product(*keys)))
    else:
        keys=[]
        for comb_key in trim_support:
            keys.append(list(comb_key))
        combination_list=list(combinations(keys,combination_flag))
        # combination_list=[','.join(map(str,combi)) for combi in combinations(keys,combination_flag)]
        return combination_list  


ts=combination(trim_support(generate_support(transcations=transcations,flag=1,trimmed_support=0)),combination_flag=2)
ts1=combination(trim_support(generate_support(transcations=transcations,flag=2,trimmed_support=ts)),combination_flag=3)
# ts1=trim_support(generate_support(transcations=transcations,flag=2,trimmed_support=ts))
# print(ts1)


  
