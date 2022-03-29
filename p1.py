#!C:\Users\antep\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe
import subjects
import cgi
from webbrowser import get
import time
from http import cookies
import os 
params = cgi.FieldStorage()
C=cookies.SimpleCookie()
print ("Set-Cookie:Domain = http://localhost/cgi-bin/p1.py;")
def start_html():
    print('''
    <!DOCTYPE html>
    <html>
    <head></head>
    <body>
    <form action="p1.py" method="post">
    <input type='submit' name='botun' value='1st Year'>
    <input type='submit' name='botun' value='2nd Year'>
    <input type='submit' name='botun' value='3rd Year'>
    ''')

def end_html():
    print('''
    </form>
    </body>
    </html>
   ''' )
def button_val():
    if params.getvalue('botun')==None:
            yr_val(1)       
    for k,v in subjects.year_names.items():
        if params.getvalue('botun')==v:
            yr_val(k)
start_html()
def yr_val(yr):
    for k_par,v_par in subjects.subjects.items():
        print("<br>")
        if v_par['year']==yr:
            print(v_par['name'])
            print(v_par['ects'])
            for s,val in subjects.status_names.items():
                print('''<input type="radio" name=" '''+k_par+ ''' "  value=" '''+s+''' " checked> ''' +val+ '''  ''')
                vals=cookie(s)
                C[k_par]=vals
    # for k,v in subjects.year_names.items():
    #     if params.getvalue('botun')==v.get('1st Year') :
    #         print("ahahaha")
def cookie(b_val):
    if b_val=='not':
        b_val='Not selected'
        return b_val
    if b_val=='enr':
        b_val='Enrolled'
        return b_val
    if b_val=='pass':
        b_val='Passed'
        return b_val
    
button_val()
print (C)
end_html()

