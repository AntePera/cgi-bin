#!C:\ProgramData\Anaconda3\python.exe
import subjects
import cgi
from http import cookies
from webbrowser import get
import time
params = cgi.FieldStorage()
C=cookies.SimpleCookie()
C['lastvisit'] = str(time.time())
def start_html():
    print('''
    <!DOCTYPE html>
    <html>
    <head></head>
    <body>
    <form method="post">
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


start_html()

for k_par,v_par in subjects.subjects.items():
    print("<br>")
    if v_par['year']==1:
        print(v_par['name'])
        print(v_par['ects'])
        for s,val in subjects.status_names.items():
            print('''<input type="radio" name=" '''+k_par+ ''' " value=" '''+s+''' "> ''' +val+ '''  ''')
    # for k,v in subjects.year_names.items():
    #     if params.getvalue('botun')==v.get('1st Year') :
    #         print("ahahaha")


print("<br>")
print(params.getvalue('botun'))
end_html()
