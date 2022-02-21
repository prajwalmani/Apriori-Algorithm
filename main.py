from itertools import combinations,permutations
import sqlite3

confidence_values=[]
supports=[]

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
    printsupportvalue(support,flag,len(transcations))
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
    supports.clear()
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
                    supports.append(j_duplicate+j[k:])
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
    values_support=[]
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
                print("-----------------------------------------------------------")
                print("There is no more frequent item set/assocation rules which is above the \nminumum supoort and confidence threshold")
                print("-----------------------------------------------------------")
                break
            print("\nAssocation rules:")
            values_support.clear()
            for items in supports:
                values_support.append(singlesupport(items)*100)
            for key,value in confidences.items():
                index=list(confidences.keys()).index(key)
                print("{}=>{}:[Support:{}%, Confidence:{}%]".format(key,value,round(values_support[index],2),round(confidence_values[index],2)))
        count+=1


def database(database_number):
    transcation={}
    databasename="transcations"+database_number+".db"
    con = sqlite3.connect(databasename)
    cur=con.cursor()
    res=cur.execute(
    '''
    select * from store;
    '''
    )
    print("-----------------------------------------------------------")
    print("Database items")
    print("-----------------------------------------------------------")
    for row in res:
        print("{},{}".format(row[0],row[1]))
        values_list=list(row[1].split(','))
        values_list=[x.strip(' ') for x in values_list]
        transcation[row[0]]=values_list
    print("-----------------------------------------------------------")
    con.commit()
    con.close()

    return transcation

def printsupportvalue(support,buff,lentranscations):
    print("-----------------------------------------------------------")
    print("Itemset {}".format(buff+1))
    print("-----------------------------------------------------------")
    print("Support:")
    for key,value in support.items():
        print("{}:{}%".format(key,round((value/lentranscations)*100),2))
        


print("Apriori Algorthim")
print("Databases List")
print("1.Games\n2.Mangas\n3.Basic necessities\n4.Vegetables\n5.Fruits\n")
database_number=int(input("Enter your selection:"))
if database_number<=0 or database_number>5:
    print("Please enter the proper number associated to the database list")
    database_number=int(input("Enter your selection:"))

transcations=database(str(database_number))
min_support_value=((int(input("Enter the minimum support in percentage:")))/100)*len(transcations)
min_confidence_value=int(input("Enter the minimum support confidence in percentage:"))


call_functions(transcations) 
