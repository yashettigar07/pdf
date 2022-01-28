import os
import PyPDF2
import tkinter
import datetime
import shutil
import csv
import sqlite3
import smtplib
import glob
from datetime import datetime
from datetime import timedelta
from tkinter import filedialog
root = tkinter.Tk()
root.withdraw()


class assign:
    # def time(self):
    #     current_time=datetime.now()
    # # print(current_time)
    # # print(type(current_time))
    #     Modified_time=current_time.replace(microsecond=0)
    # # print(Modified_time)
    #     added_current_time=Modified_time + timedelta(minutes=330)
    # # print(added_current_time)
    #     my_time_format = "%Y_%m_%d_%H_%M_%S"
    #     converted_format_time = datetime.strftime(added_current_time, my_time_format)
    # # print(type(converted_format_time))
    #     print(converted_format_time)

    # print()

    def pdf(self):
        pdf_folder = r"C:\Users\DELL\PycharmProjects\assignment\pdf"
        for x,y,z in os.walk(pdf_folder):
             print(x)
             print(y)
             print(z)

    def user_pass(self):
        pdf_folder = r"C:\Users\DELL\PycharmProjects\assignment\pdf"
        file_name=filedialog.askopenfilename()
        print(file_name)
     # file_name=os.path()
        pdf_in_file=open(file_name,'rb')
     #pdf_in_file=open("simple.pdf",'rb')
     #pdf_in_file=open("gre.pdf",'rb')
        inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
        pages_no = inputpdf.numPages
        output = PyPDF2.PdfFileWriter()
        try:
            for i in range(pages_no):
                inputpdf=PyPDF2.PdfFileReader(pdf_in_file)
                output.addPage(inputpdf.getPage(i))
                output.encrypt('admin@123')
        except Exception as ex:
            print(ex)

     # with open("gre_password_protected.pdf", "wb") as outputStream:
        with open("new1.pdf","wb")as outputStream:
            output.write(outputStream)
        current_time = datetime.now()
        # print(current_time)
        # print(type(current_time))
        Modified_time = current_time.replace(microsecond=0)
        # print(Modified_time)
        added_current_time = Modified_time + timedelta(minutes=0)
        print(added_current_time)
        my_time_format = "%Y_%m_%d_%H_%M_%S"
        converted_format_time = datetime.strftime(added_current_time, my_time_format)
        # print(type(converted_format_time))
        # print(converted_format_time)
        old_name = r"C:\Users\DELL\PycharmProjects\assignment\new1.pdf"
        new_name = r"C:\Users\DELL\PycharmProjects\assignment\ "+converted_format_time+".pdf"
        os.rename(old_name, new_name)
        source = r'C:\Users\DELL\PycharmProjects\assignment'
        dest = r'C:\Users\DELL\PycharmProjects\assignment\Protected'

        for fname in os.listdir(source):
            if fname.lower().endswith('.pdf'):
                shutil.move(os.path.join(source, fname), dest)

        # old_name = r"C:\Users\DELL\PycharmProjects\assignment\pdf\new1.pdf"
        # new_name = r"C:\Users\DELL\PycharmProjects\assignment\pdf\." + converted_format_time + ".pdf"
    # def move(self):

# connection=sqlite3.connect("assign.db")
# query="""CREATE TABLE files("file_name" text,"file_size" text,"time" datetime,"enpwd" text)"""
# # query="""INSERT INTO  training("t_name" ,"t_version" ) VALUES("java",8.1)"""
# query="""SELECT * FROM training"""
# execution=connection.execute(query)
# connection.commit()
# connection.close()

        f = open(r"C:\Users\DELL\PycharmProjects\assignment\file.txt", 'r+')
        w = csv.writer(f)
        for path, dirs, files in os.walk(r"C:\Users\DELL\PycharmProjects\assignment\Protected"):

            for filename in files:
                w.writerow(filename)
            file_size = os.path.getsize(r"C:\Users\DELL\PycharmProjects\assignment\Protected")
            with open("file1.csv", "w") as file_obj:
                csv_file_obj = csv.writer(file_obj)
                csv_file_obj.writerow(["filename", "file_size"])
                csv_file_obj.writerows([[filename, file_size]])
            con = sqlite3.connect("new.db")
            cur = con.cursor()
            with open('file1.csv', 'r') as fin:
                dr = csv.DictReader(fin)
                to_db = [(i['filename'], i['file_size']) for i in dr]

            cur.executemany("INSERT INTO files (file_name, file_size) VALUES (?, ?);", to_db)
            con.commit()
            con.close()


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("newyahoo172@gmail.com", "newyahoo7821")
message = "hi the pdf file is password protected plase use admin@123 as your password"
s.sendmail("newyahoo172@gmail.com", "y.shettigar72@gmail.com", message)
s.quit()
my_obj=assign()
# my_obj.time()
my_obj.pdf()
my_obj.user_pass()
# my_obj.move()








