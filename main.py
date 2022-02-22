from itertools import combinations,permutations
import sqlite3
import time


confidence_values=[]
supports=[]

def generate_support(transcations,flag,trimmed_support):
    """
    This function generates support values for the transactions by taking in three parameters transactions 
    the actual database, flag is like buffer variable which is used to create condition-based code and support generation,
    trimmed_support is the support from the previous iteration and returns a dict type with all the supports.
    """
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

def trim_support(support,min_support_value):
    """
    This function trimes or delete all the supports which is less than the threshold. 
    It has two parameters support that has the all support values from the previous iteration and min_support_value 
    which is the user input and the threshold for the support.
    """
    trim_support={}
    for key,value in support.items():
        if support[key]  >= min_support_value:
            trim_support[key]=value
    return trim_support


def combination(trim_support,combination_flag):
    """
    This function is used to combines the various items from the support value which passes the threshold 
    and combination flag is the number of items should be combined.
    """
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

def singlesupport(supportitem,transcations):
        """
        This function is similar to the generate_support but this is used only to 
        generate support for one item and the rest of the parameters are the same.
        """
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
        

def confidence(trimmed_support,min_confidence_value,transcations,conifdence_flag):
    """
     This function is used to give the confidence of each rule and trim the rules which doesnt 
     pass the min_confidence_value It use permutations concept.
    """
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
                unionupport=float((singlesupport(j,transcations)))
                RHSsupport=float((singlesupport(j_duplicate,transcations)))
                confidence_value=(unionupport/RHSsupport)*100
                if(conifdence_flag==1):
                    if confidence_value>=min_confidence_value:
                        supports.append(j_duplicate+j[k:])
                        confid[str(j_duplicate)]=str(j[k:])
                        confidence_values.append(confidence_value)
                else:
                    supports.append(j_duplicate+j[k:])
                    confid[str(j_duplicate)]=str(j[k:])
                    confidence_values.append(confidence_value)
    return confid

def getuniqeueelementslength(transcations):
    """
    This function's main role is to get the unique elements in the 
    entire database transaction and return the total length of it.
    """
    unique=[]
    for inkey,invalue in transcations.items():
        for items in invalue:
            if items not in unique:
                unique.append(items)
    return len(unique)

def apriori_functions(transcations,min_support_value,min_confidence_value):
    """
    This function calls all other functions in the recursive main which acts as replication 
    of the apriori algorithm and prints the association rules 
    """
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
            ),min_support_value)
            
            comb=combination(trimmed,combination_flag=i+2)
            combination_list.append(comb)
        else:
            trimmed=trim_support(generate_support(
                transcations=transcations,
                flag=i,
                trimmed_support=combination_list[0]
            ),min_support_value)
            comb=combination(trimmed,combination_flag=i+2)
            combination_list.clear()
            combination_list.append(comb)
            confidences=confidence(trimmed,min_confidence_value,transcations,conifdence_flag=1)
            if bool(confidences)==False:
                print("-----------------------------------------------------------")
                print("There is no more frequent item set/assocation rules which is above the \nminumum supoort and confidence threshold")
                print("-----------------------------------------------------------")
                break
            print("\nAssocation rules:")
            values_support.clear()
            for items in supports:
                values_support.append(singlesupport(items,transcations)*100)
            for key,value in confidences.items():
                index=list(confidences.keys()).index(key)
                print("{}=>{}:[Support:{}%, Confidence:{}%]".format(key,value,round(values_support[index],2),round(confidence_values[index],2)))
        count+=1


def database(database_number):
    """
    This is function is used to connect to the sqllite3 and access the database then the database 
    is formatted in such an way that is similar to the datatypes used in python and easy to access  
    """
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
    """
    This function just prints the support values with the itemset.
    """
    print("-----------------------------------------------------------")
    print("Itemset {}".format(buff+1))
    print("-----------------------------------------------------------")
    print("Support:")
    for key,value in support.items():
        print("{}:{}%".format(key,round((value/lentranscations)*100),2))
        

def apriori():
    """
    This function loops around all the databases and applies the apriori algorithm.
    """
    print("Apriori Algorthim method:")
    min_support_value=(int(input("Enter the minimum support in percentage:")))
    min_confidence_value=int(input("Enter the minimum support confidence in percentage:"))
    for i in range(1,6):
        transcations=database(str(i))
        min_support_value=(min_support_value/100)*len(transcations)
        apriori_functions(transcations,min_support_value,min_confidence_value) 

def rules_bruteforce(trimmed_support):
    """
    This function uses permutations concepts and prints rules
    """
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
                    print("{}=>{}".format(j_duplicate,j[k:]))
    

def bruteforce():
    """
    This function calls other functions to replicate the Bruteforce.
    """
    print("Bruteforce Method")
    for i in range(1,6):
        transcation=database(str(i))
        count=0 
        combination_list=[]
        values_support=[]
        for j in range(getuniqeueelementslength(transcation)):
            if count==0:
                trimmed=generate_support(
                    transcations=transcation,
                    flag=j,
                    trimmed_support=0
                )
                comb=combination(trimmed,combination_flag=j+2)
                combination_list.append(comb)
            else:
                trimmed=generate_support(
                transcations=transcation,
                flag=j,
                trimmed_support=combination_list[0])
                comb=combination(trimmed,combination_flag=j+2)
                combination_list.clear()
                combination_list.append(comb)
                print("\nAssocation rules:")
                rules_bruteforce(trimmed_support=trimmed)
            count+=1

while(True):
    print("Database list:")
    print("1.Games\n2.Manga\n3.necessities\n4.Vegetables\n5.Fruits\n")
    print("Which method do you want to apply on the databases")
    print("1.Aprori Algorthim Method\n2 Bruteforce Method")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        start_time = time.time()
        apriori()
        end_time =  time.time()
        print("Aprori Algorthim method took {} seconds".format(round(end_time-start_time,2)))
    if choice==2:
        start_time = time.time()
        bruteforce() 
        end_time =  time.time()
        print("Bruteforce method took {} seconds".format(round(end_time-start_time,2)))
    print("1.Repeat the above steps\n2.Exit")
    exit=int(input("Enter your choice:"))
    if exit==2:
        break
