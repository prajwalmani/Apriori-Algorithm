
# sample transcation dataset from https://www.geeksforgeeks.org/apriori-algorithm/


from itertools import combinations
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

def generate_support(transcations):
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
    return support

def trim_support(support):
    trim_support={}
    for key,value in support.items():
        if value  >= min_support_value:
            trim_support[key]=value
    return trim_support

trim_support=trim_support(generate_support(transcations))

def combination(trim_support):
    x=list(combinations((trim_support.keys()),2))
    # print(x)
combination(trim_support)

trim_support=trim_support(generate_support(trim_support))
print(trim_support)


