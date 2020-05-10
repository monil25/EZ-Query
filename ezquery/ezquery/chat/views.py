from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer
from rasa.nlu import config
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import re
from rasa.nlu.model import Metadata,Interpreter
import mysql.connector
from collections import defaultdict
import pandas as pd
from sqlalchemy import create_engine




'''
NLP Imports
'''

from django.shortcuts import render
import speech_recognition as sr
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.

checkIfRecording = -1

## Fetch Metadata
META_QUERY = "select TABLE_NAME,COLUMN_NAME,DATA_TYPE from information_schema.columns where table_schema = '{}';".format("ez")

'''
This is for adding new table names to the NLU training model
'''

def txt_new_table(tableName):
    file = open("data/table.txt","a")
    file.write(tableName+" \n")
    file.close()
    

'''
This is for adding new column names to the NLU training model
'''
    
    
def txt_new_columns(tableColumns):
    file = open("data/column.txt","a")
    
    for col in tableColumns:
        file.write(col+" \n")
    file.close()

'''
This is for extracting table schema from a SQL Dump
'''
def extract_details_from_SQLDUMP(fileLocation):
    with open(fileLocation,"r") as file:
        data = file.read().replace("\n","")
        req = re.findall("(?<=CREATE TABLE)(.*)(?=ENGINE)",data)
        data = re.findall(r"`(.*?)`", req[0]) 
        
        table = data[0]
        columns = data[1:]
        
        print(table)
        print(columns)
        
        return table,column



'''
This for converting a csv file to a SQL database
'''
def csv_to_SQL_path(csvFilePath,tableName):
    df = pd.read_csv(csvFilePath)
    engine = create_engine('mysql+mysqldb://saumitra:dada9946@localhost:3306/ez', echo = False)
    df.to_sql(name = tableName, con = engine, if_exists = 'append', index = False)
    
'''
def csv_to_SQL(df,tableName):
    engine = create_engine('mysql+mysqldb://saumitra:dada9946@localhost:3306/ez', echo = False)
    df.to_sql(name = tableName, con = engine, if_exists = 'append', index = False)
'''    

'''
This is for fetching all the tables
'''


def fetch_data(QUERY,columns):    
    try:
        connection = connect_to_database()
        sql_select_Query = QUERY
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("All tables", cursor.rowcount)
        data = []

        rlen = 0 
        if records != None:
            rlen = len(records[0])

        if rlen == 0:
            return list()
        
        headers = dict()
        i = 0
        for col in columns:
            headers[i] = col
            i += 1
        data.append(headers)
                
        for row in records:
            rdata = dict()
            dtype = ""
            
            for i in range(rlen):
                rdata[i] = row[i]
            
            data.append(rdata)

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
            
    return data




def fetch_metadata(QUERY_TABLE):
    tables = defaultdict(dict)
    
    try:
        connection = connect_to_database()
        sql_select_Query = QUERY_TABLE
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("All tables", cursor.rowcount)
        
        for row in records:
            dtype = ""
            if row[2] == "text" or row[2] == "varchar":
                dtype = "string"
            elif row[2] == "int" or row[2] == "bigint":
                dtype = "int"
            tables[row[0]][row[1]] = dtype

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
            
    return tables


'''
SQL Table to database
'''
def get_table_from_sql(table):
    df = pd.read_sql_table(table, 'mysql+mysqldb://saumitra:dada9946@localhost:3306/ez')
    return df


## Load config.yml
trainer = Trainer(config.load("../config.yml"))

## model_directory
model_directory = trainer.persist('../models/')

## load interpreter
interpreter = Interpreter.load(model_dir='../models/nlu-4/nlu') 

'''
This is for connecting to the database
'''
def connect_to_database():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="dada9946",
      database = "ez"
    )

    return mydb

def execute(SQLQuery):
    DB = connect_to_database()
    mycursor = DB.cursor(buffered=True)
    mycursor.execute(SQLQuery)
    DB.commit()
    print(mycursor.rowcount, "Transaction Successful")
    mycursor.close()
    return "Successful"

## Query preprocessing
def convertSQLStrings(lofs):
    nlofs = []
    for s in lofs:
        if s.isnumeric() == False:
            ns = "'{}'".format(s)
            nlofs.append(ns)
        else:
            nlofs.append(s)
            
    return nlofs

## Query creation
def construct_insert_query(rasa):
    TABLE = ""
    COLUMN = []
    VALUE = []
    CONDITION = []
    SHOW_COL = []
    for ent in rasa["entities"]:
        if ent["entity"] == "table":
            TABLE = ent["value"]
        elif ent["entity"] == "column" and TABLE != "":
            COLUMN.append(ent["value"])
        elif ent["entity"] == "value" and TABLE != "":
            VALUE.append(ent["value"])
        else:
            if TABLE == "" and ent["entity"] == "column":
                SHOW_COL.append(ent["value"])
                
    
    VALUE = convertSQLStrings(VALUE)
    
    mapped = set(zip(COLUMN,VALUE))
    print(mapped)
    
    table_col = ["name","age","standard","marks"]
    print(COLUMN)
    for col in table_col:
        if col not in COLUMN:
            print("Specify value for {} ignore to insert NULL".format(col))
    
    QUERY = "INSERT INTO {} ({}) VALUES({})".format(TABLE,','.join(COLUMN),','.join(VALUE))
    print(QUERY)
    return QUERY,[],"I"


'''
Fetch All Column Names
'''

def fetch_allcol(table):    
    try:
        connection = connect_to_database()
        QUERY = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='ez' AND `TABLE_NAME`='{}';".format(table)
        sql_select_Query = QUERY
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("All tables", cursor.rowcount)
        data = []

        for row in records:
            data.append(row.lstrip("(").rstrip(",)"))

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
            
    return data



def construct_select_query(rasa):
    TABLE = ""
    COLUMN = []
    VALUE = []
    CONDITION = []
    SHOW_COL = []
    SORT = ""
    SORT_COUNT = "100"
    curr_col = ""
    curr_cond = ""
    conditions = "1=1"
    ORDER = ""
    
    for ent in rasa["entities"]:
        if ent["entity"] == "table":
            TABLE = ent["value"]
        elif ent["entity"] == "column" and TABLE != "":
            COLUMN.append(ent["value"])
            curr_cond = ""
        elif ent["entity"] == "value" and TABLE != "":
            if curr_cond == "":
                CONDITION.append("equal")
            VALUE.append(ent["value"])
        elif ent["entity"] == "condition" and TABLE != "":
            CONDITION.append(ent["value"])
            curr_cond = ent["value"]
        elif ent["entity"] == "sort" and TABLE == "":
            SORT = ent["value"]
        elif ent["entity"] == "sort_count" and TABLE == "":
            SORT_COUNT = ent["value"]
        else:
            if TABLE == "" and ent["entity"] == "column":
                SHOW_COL.append(ent["value"])
                
    
    VALUE = convertSQLStrings(VALUE)
    if COLUMN != []:
        ORDER = COLUMN.pop()
    else:
        ORDER = "NULL"

    MODIFIED_COND = []
    
    if SORT.lower() == "top":
        SORT = "ASC"
    elif SORT.lower() in ["bottom","last"]:
        SORT = "DESC"
    else:
        SORT = ""
    
    for c in CONDITION:
        if c.lower() == "greater":
            MODIFIED_COND.append(">")
        if c.lower() in ["lesser","less"]:
            MODIFIED_COND.append("<")
        if c.lower() in ["equal"]:
            MODIFIED_COND.append("=")
            
    if SHOW_COL == list():
        SELECT = "*"
        SHOW_COL = fetch_allcol(TABLE)
    else:
        SELECT = ",".join(SHOW_COL)
        
    if len(COLUMN) != 0:
        conditions = handle_conditions(COLUMN,MODIFIED_COND,VALUE)
    
    QUERY = "SELECT {} FROM {} WHERE {} ORDER BY {} {} LIMIT {}".format(SELECT,TABLE,conditions,ORDER,SORT,SORT_COUNT)
    print(QUERY)
    return QUERY,SHOW_COL,"S" 
    
    
    
    
def construct_delete_query(rasa):
    TABLE = ""
    INI_COL = []
    INI_VAL = []
    
    
    
    for ent in rasa["entities"]:
        if ent["entity"] == "table":
            TABLE = ent["value"]
            
        if ent["entity"] == "column" and TABLE != "":
            INI_COL.append(ent["value"])
        elif ent["entity"] == "value" and TABLE != "":
            INI_VAL.append(ent["value"])
        
         
    print(INI_VAL)    
     
    INI_VAL = convertSQLStrings(INI_VAL) 
    
    
    where = ""
    for i in range(len(INI_COL)):
        where += INI_COL[i]
        where += " = "
        where += INI_VAL[i] + ","
        
    where = where.rstrip(",")
    
    
    QUERY = "DELETE FROM {} WHERE {}".format(TABLE,where)
    print(QUERY)   
    return QUERY,[],"D"
        


def create_table_query(rasa):
    TABLE = ""
    COLUMN = []
    DOMAIN = []
    
    for ent in rasa["entities"]:
        if ent["entity"] == "table":
            TABLE = ent["value"]
        elif ent["entity"] == "column" and TABLE != "":
            COLUMN.append(ent["value"])
        elif ent["entity"] == "domain" and TABLE != "":
            DOMAIN.append(ent["value"])
        
    
    columns = []
    
    for i in range(len(COLUMN)):
        domain = DOMAIN[i]
        if DOMAIN[i] == "string":
            domain = "VARCHAR(25)"
        statement = " ".join([COLUMN[i],domain])
        columns.append(statement)
        
    columns = ",".join(columns)
            
    
    
    QUERY = "CREATE TABLE {} ({});".format(TABLE,columns)
    print(QUERY)
    return QUERY,[],"C"


def construct_update_query(rasa):
    TABLE = ""
    INI_COL = []
    INI_VAL = []
    UPDATE_COL = []
    UPDATE_VAL = []
    
    change = resp["text"].find("new")
    
    
    for ent in rasa["entities"]:
        if ent["entity"] == "table":
            TABLE = ent["value"]
            
        if ent['start'] < change:
            if ent["entity"] == "column" and TABLE != "":
                INI_COL.append(ent["value"])
            elif ent["entity"] == "value" and TABLE != "":
                INI_VAL.append(ent["value"])
        else:
            if ent["entity"] == "column" and TABLE != "":
                UPDATE_COL.append(ent["value"])
            elif ent["entity"] == "value" and TABLE != "":
                UPDATE_VAL.append(ent["value"]) 
        
         
    print(INI_VAL)
    print(UPDATE_VAL)
    
     
    INI_VAL = convertSQLStrings(INI_VAL) 
    UPDATE_VAL = convertSQLStrings(UPDATE_VAL)
    
    print(INI_VAL)
    print(UPDATE_VAL)
    

    update = ""
    for i in range(len(UPDATE_COL)):
        update += UPDATE_COL[i]
        update += " = "
        update += UPDATE_VAL[i] + ","
    
    update = update.rstrip(",")
    
    where = ""
    for i in range(len(INI_COL)):
        where += INI_COL[i]
        where += " = "
        where += INI_VAL[i] + ","
        
    where = where.rstrip(",")
    
    
    QUERY = "UPDATE {} SET {} WHERE {}".format(TABLE,update,where)
    print(QUERY)
    return QUERY,[],"U"   
        


## Intent identifier
def identify_intent(resp):
    QUERY = ""
    QT = ""
    if resp["intent"]["name"] == "insert_query":
        QUERY,LIST,QT = construct_insert_query(resp)
    elif resp["intent"]["name"] == "update_query":
        QUERY,LIST,QT = construct_update_query(resp)
    elif resp["intent"]["name"] == "select_query":
        QUERY,LIST,QT = construct_select_query(resp)
    elif resp["intent"]["name"] == "delete_query":
        QUERY,LIST,QT = construct_delete_query(resp)
    elif resp["intent"]["name"] == "create_table":
        QUERY,LIST,QT = create_table_query(resp)
    else:
        return "Bad Request"
    
    return QUERY,LIST,QT


## Fetch Metadata
MetaTables = fetch_metadata(META_QUERY)
print(MetaTables)


def chatbot(request):
    return render(request, 'chat/chat.html')


@csrf_exempt
def record_audio_start(request):
    global checkIfRecording
    if checkIfRecording == -1:
        checkIfRecording = 1
    main_text = ""
    # obtain audio from the microphone
    while(checkIfRecording == 1):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source)
            # audio = r.listen(source)
            audio = r.record(source=source, duration=10)
            print("Audio recorded")
        # recognize speech using Google Speech Recognition
        try:
            message = r.recognize_google(audio)
            message = message.lower()
            print(message)
    
            message = interpreter.parse(message)
            print(message)
            print(type(message))
            QUERY,Columns,QT = identify_intent(message)
            print(QUERY,Columns,QT)
            TABLE = []
            RESPONSE = ""
            if QT == "S":
                TABLE = fetch_data(QUERY,Columns)
            else:
                if QT == "I":
                    RESPONSE = execute(QUERY) + "INSERT"
                elif QT == "D":
                    RESPONSE = execute(QUERY) + "DELETE"
                elif QT == "C":
                    RESPONSE = execute(QUERY) + "CREATE"
                elif QT == "U":
                    RESPONSE = execute(QUERY)+"UPDATE"

            print(TABLE)
            context = {"message": "echo"+RESPONSE}
            return JsonResponse(context)

            # main_text = main_text + "\n" + new_text
            # print("Google Speech Recognition thinks you said " + new_text)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        print(main_text)
    return JsonResponse({"text": main_text})


@csrf_exempt
def record_audio_stop(request):
    global checkIfRecording
    checkIfRecording = -1
    return JsonResponse({"text": "Recording stopped"})


@csrf_exempt
def nlp_process(request):
    message = request.POST.get('message', '')
    print(message)
    message = message.lower()
    '''
    Message is recieved from post
    '''
    
    message = interpreter.parse(message)

    '''
    Message is interpreted
    '''
    print(message)
    print(type(message))

    '''
    Identify INTENT RETURNS


    QUERY - SQL Query
    LIST - LIST of COLUMNS Required during SQL query
    QT - Query Type

    '''

    QUERY,Columns,QT = identify_intent(message)
    print(QUERY,Columns,QT)
    TABLE = []
    RESPONSE = ""
    if QT == "S":
        TABLE = fetch_data(QUERY,Columns)
    else:
        if QT == "I":
            RESPONSE = execute(QUERY) + "INSERT"
        elif QT == "D":
            RESPONSE = execute(QUERY) + "DELETE"
        elif QT == "C":
            RESPONSE = execute(QUERY) + "CREATE"
        elif QT == "U":
            RESPONSE = execute(QUERY)+"UPDATE"

    '''
    RESPONSE : Transaction is executed succesfully
    '''

    '''
    Very Important TABLE format:

    [{0: 'name', 1: 'age', 2: 'marks',3: 'standard'},
    {0: 'Rick', 1: 65, 2: 100, 3: 10},
    {0: 'Morty', 1: 12, 2: 10, 3: 5},
    {0: 'Summer', 1: 14, 2: 12, 3: 10},
    {0: 'Jerry', 1: 40, 2: 50, 3: 10},
    {0: 'Meesik', 1: 100, 2: 100, 3: 10},
    {0: 'Ed', 1: 12, 2: 75, 3: 10}, 
    {0: 'saumi', 1: 19, 2: None, 3: None}, 
    {0: 'donald', 1: 12, 2: 20, 3: 10}]

    '''
    '''
    details=[{0: 'name', 1: 'age', 2: 'marks',3: 'standard'},
    {0: 'Rick', 1: 65, 2: 100, 3: 10},
    {0: 'Morty', 1: 12, 2: 10, 3: 5},
    {0: 'Summer', 1: 14, 2: 12, 3: 10},
    {0: 'Jerry', 1: 40, 2: 50, 3: 10},
    {0: 'Meesik', 1: 100, 2: 100, 3: 10},
    {0: 'Ed', 1: 12, 2: 75, 3: 10}, 
    {0: 'saumi', 1: 19, 2: None, 3: None}, 
    {0: 'donald', 1: 12, 2: 20, 3: 10}]

    # for select
    context = {"type": "select","information":details}
    #for update/delete example below
    context = {"type": "update","message":Information updated}
    '''


    print(TABLE)
    context = {"message": "echo"+RESPONSE}
    return JsonResponse(context)
