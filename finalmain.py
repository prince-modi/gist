import sqlite3
import smri
import sub_gen


def fileformat():
    file = open('smry.txt', "r")
    filedata = file.readlines()
    article = filedata[0].split(". ")
    demo = ""
    for line in article:
        demo = demo + line
    return demo


conn = sqlite3.connect('example.db')
video = input("Enter Video Name:")
id = sub_gen.sub_g(video)
#id = 'QqsLTNkzvaY'
ch_qry = """select NAME from Sumry where NAME = ?"""
cursor = conn.cursor()
cursor.execute(ch_qry, (id,))
if cursor.fetchone():
    suc_qry = """select * from Sumry where NAME = ?"""
    cursor.execute(suc_qry, (id,))
    result = cursor.fetchone()
    print(result)
else:
    smri.generate_summary("sfile.txt", 5)
    in_qry = """insert into Sumry (NAME, SMRY) VALUES (?,?)"""
    demo = fileformat()
    cursor.execute(in_qry, (id, demo))
    print(demo)

conn.commit()
conn.close()
