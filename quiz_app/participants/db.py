import sqlite3
from datetime import datetime

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)

# s = conn.execute('select * from participants_participants')

# class user:
#     def __init__(self):
#         self.phone = 123
        
#         self.conn = sqlite3.connect('db.sqlite3')
    
#     def insert(self,f_name,l_name,email,score):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.datetime = datetime.now()
#         global emails
#         emails = email
#         self.email = email
#         self.score = score
#         self.conn = sqlite3.connect('db.sqlite3')
#         self.conn.execute(f"""insert into participants_participants(f_name,l_name,email,phone,score) values('{f_name}','{l_name}','{email}','{score}',0);""")
        
#     def update(self,score,email):
#         self.score = score
#         self.conn = sqlite3.connect('db.sqlite3')

#         self.conn.execute(f""" update participants_participants set score={self.score} where id =  """)


def call(f_name, l_name, email, score):
    cursor = conn.execute(f"""select * from participants_participants;""")
    date = datetime.now()
    s = str(date)
    s = s[:-7]

    for i in cursor:
        print(i)
        print(i[3])
        if email == i[3]:
            print('inside')
            conn.execute(f"""update participants_participants set score= {score}, date = '{s}'  where email='{email}'; """)
            print('success')
            conn.commit()
            return 


    t = []
    for i in cursor:    
        if i[3] not in t:
            t.append(i[3])
    if email not in t:
         conn.execute(f"""insert into participants_participants(f_name,l_name,email,phone,score,date) values('{f_name}','{l_name}','{email}','344',{score},'{s}');""")


    

    # conn.execute(""" delete from participants_participants where email = 'ramzan@gmail.com' """)
    
    conn.commit()
    # cursor = conn.execute(f"""select * from participants_participants;""")
    # for i in cursor:
    #     if email == i[3]:
    #         print(i[3])

    # print(f_name, l_name, email, score)

# call('ramzan','khan' ,'ramzan@gmail.com',70)
# def fetch(email):
#     cursor  = conn.execute(f"""select * from participants_participants;""")
#     s = []
#     for i in cursor:
#         if i[3] not in s:
#             s.append(i[3])
#     if email not in s:
#         print(s[1])

# # 
# fetch('rf')

# class u2(user):
#     def __init__(self,score):
#         self.score = score
#         self.conn = sqlite3.connect('db.sqlite3')

        
# def insert(f_name,l_name,email,score):
#     s = user(f_name,l_name,email,score)
#     s.insert()
# def updte(score):
#     s = u2(score)
#     s.update(score)

""""


"""
# global e
# e = ''
# def eml(email):
#     e = email
#     return email

# def insert(f_name,l_name,email,score):

#     conn.execute(f"""insert into participants_participants(f_name,l_name,email,phone,score,date) values('{f_name}','{l_name}','{email}',{0},{score},{datetime.now()})""")

# def update(score):
#     conn.execute(f""" update participants_participants set score={score} where email='{e}' """)
