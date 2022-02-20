# database.py in this file we just create databases and insert values to the tables 

import sqlite3

con = sqlite3.connect('transcations5.db')

cur=con.cursor()

cur.execute(
    '''
    CREATE TABLE store (tno text,items text)
    '''
)

cur.execute("INSERT into store values('t1','apple, orange, mango, grapes')")
cur.execute("INSERT into store values('t2','mango, banana')")
cur.execute("INSERT into store values('t3','orange, mango')")
cur.execute("INSERT into store values('t4','apple, banana')")
cur.execute("INSERT into store values('t5','grapes, banana, apple')")
cur.execute("INSERT into store values('t6','mango, orange, grapes')")
cur.execute("INSERT into store values('t7','mango, grapes, banana')")
cur.execute("INSERT into store values('t8','banana, grapes')")
cur.execute("INSERT into store values('t9','banana, orange, mango')")
cur.execute("INSERT into store values('t10','grapes, apple')")
cur.execute("INSERT into store values('t11','grapes, orange, apple')")
cur.execute("INSERT into store values('t12','banana, orange, grapes')")
cur.execute("INSERT into store values('t13','mango')")
cur.execute("INSERT into store values('t14','banana, mango, grapes, orange')")
cur.execute("INSERT into store values('t15','apple, banana, mango')")
cur.execute("INSERT into store values('t16','grapes, apple')")
cur.execute("INSERT into store values('t17','mango, apple, banana')")
cur.execute("INSERT into store values('t18','orange, mango, banana, apple')")
cur.execute("INSERT into store values('t19','mango')")
cur.execute("INSERT into store values('t20','orange, mango')")

con.commit()
con.close()

con = sqlite3.connect('transcations3.db')

cur=con.cursor()

cur.execute(
    '''
    CREATE TABLE store (tno text,items text)
    '''
)

cur.execute("INSERT into store values('t1','hairgel, chips')")
cur.execute("INSERT into store values('t2','bodywash, hairgel')")
cur.execute("INSERT into store values('t3','cookies, chips')")
cur.execute("INSERT into store values('t4','hairgel, bodywash, toothpaste')")
cur.execute("INSERT into store values('t5','hairgel, cookies, toothpaste')")
cur.execute("INSERT into store values('t6','toothpaste, bodywash, cookies')")
cur.execute("INSERT into store values('t7','chips')")
cur.execute("INSERT into store values('t8','bodywash')")
cur.execute("INSERT into store values('t9','toothpaste')")
cur.execute("INSERT into store values('t10','cookies, chips, bodywash')")
cur.execute("INSERT into store values('t11','hairgel')")
cur.execute("INSERT into store values('t12','toothpaste, hairgel, cookies')")
cur.execute("INSERT into store values('t13','cookies')")
cur.execute("INSERT into store values('t14','toothpaste, hairgel, bodywash')")
cur.execute("INSERT into store values('t15','toothpaste, bodywash, chips')")
cur.execute("INSERT into store values('t16','chips, cookies, hairgel, toothpaste')")
cur.execute("INSERT into store values('t17','hairgel, toothpaste, bodywash')")
cur.execute("INSERT into store values('t18','bodywash, cookies')")
cur.execute("INSERT into store values('t19','cookies')")
cur.execute("INSERT into store values('t20','bodywash, chips, hairgel')")

con.commit()
con.close()

con = sqlite3.connect('transcations2.db')

cur=con.cursor()

cur.execute(
    '''
    CREATE TABLE store (tno text,items text)
    '''
)

cur.execute("INSERT into store values('t1','bleach, gintama, pokemon, demonslayer, boruto')")
cur.execute("INSERT into store values('t2','gintama, pokemon, bleach, boruto')")
cur.execute("INSERT into store values('t3','gintama, naruto')")
cur.execute("INSERT into store values('t4','demonslayer, bleach')")
cur.execute("INSERT into store values('t5','naruto, gintama, bleach, pokemon')")
cur.execute("INSERT into store values('t6','pokemon, naruto')")
cur.execute("INSERT into store values('t7','gintama, bleach, boruto')")
cur.execute("INSERT into store values('t8','boruto, gintama, naruto')")
cur.execute("INSERT into store values('t9','pokemon, gintama, naruto')")
cur.execute("INSERT into store values('t10','naruto, bleach, boruto')")
cur.execute("INSERT into store values('t11','gintama, demonslayer, bleach')")
cur.execute("INSERT into store values('t12','pokemon, gintama, demonslayer, naruto')")
cur.execute("INSERT into store values('t13','naruto, boruto, gintama')")
cur.execute("INSERT into store values('t14','gintama, naruto, pokemon, bleach')")
cur.execute("INSERT into store values('t15','demonslayer, gintama, boruto, bleach')")
cur.execute("INSERT into store values('t16','boruto, gintama, demonslayer, pokemon')")
cur.execute("INSERT into store values('t17','bleach, demonslayer, boruto, naruto')")
cur.execute("INSERT into store values('t18','gintama, demonslayer, naruto, boruto')")
cur.execute("INSERT into store values('t19','naruto, demonslayer, pokemon')")
cur.execute("INSERT into store values('t20','demonslayer, gintama, naruto')")

con.commit()
con.close()



con = sqlite3.connect('transcations1.db')

cur=con.cursor()

cur.execute(
    '''
    CREATE TABLE store (tno text,items text)
    '''
)

cur.execute("INSERT into store values('t1','valorant, fortnite, minecraft')")
cur.execute("INSERT into store values('t2','fortnite, csgo, gta')")
cur.execute("INSERT into store values('t3','csgo')")
cur.execute("INSERT into store values('t4','valorant, overwatch')")
cur.execute("INSERT into store values('t5','csgo, valorant, apex, overwatch')")
cur.execute("INSERT into store values('t6','apex')")
cur.execute("INSERT into store values('t7','overwatch')")
cur.execute("INSERT into store values('t8','apex')")
cur.execute("INSERT into store values('t9','fortnite, valorant')")
cur.execute("INSERT into store values('t10','csgo, valorant, minecraft, gta')")
cur.execute("INSERT into store values('t11','apex, csgo, overwatch, minecraft, valorant')")
cur.execute("INSERT into store values('t12','apex, csgo, overwatch')")
cur.execute("INSERT into store values('t13','gta, valorant')")
cur.execute("INSERT into store values('t14','overwatch, apex, valorant')")
cur.execute("INSERT into store values('t15','apex, csgo')")
cur.execute("INSERT into store values('t16','overwatch')")
cur.execute("INSERT into store values('t17','overwatch')")
cur.execute("INSERT into store values('t18','overwatch, apex, gta, valorant')")
cur.execute("INSERT into store values('t19','minecraft, apex, overwatch, csgo')")
cur.execute("INSERT into store values('t20','gta, minecraft, apex, overwatch')")

con.commit()
con.close()




