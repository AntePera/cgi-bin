#!C:\Users\antep\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe
import cgi
import os
import base
from http import cookies
import subjects

params = cgi.FieldStorage()

def decide_year(year):
    cookies_string = os.environ.get('HTTP_COOKIE', '')
    all_cookies_object = cookies.SimpleCookie(cookies_string)
    if year is not None:
        cookie = cookies.SimpleCookie()
        cookie['god'] = year
        print (cookie.output())
    elif all_cookies_object.get('year'):
        year = all_cookies_object.get('year').value
    else:
        year = 1
    return year

cookie = cookies.SimpleCookie()

def save_data(params):
    cookies_string = os.environ.get('HTTP_COOKIE', '')
    all_cookies_object = cookies.SimpleCookie(cookies_string)
    for k in params:
        cookie[k] = params.getvalue(k)
        print(cookie) 

    
years = decide_year(params.getvalue('year'))

checked=""

# def readFromCookes():
#     for k in cookie:
       

def print_subjects(params):
    year=params.getvalue('year')
    print('''
    ''')
    if year=="1st Year":
        for k,v in subjects.subjects.items():
            if (v.get('year')==1):
                print("")
                print(''' ''')    
    elif year=="2nd Year":
        for k,v in subjects.subjects.items():
            if (v.get('year')==2):
                print("")
                print(''' ''')
    elif year=="3rd Year":
        for k,v in subjects.subjects.items():
            if (v.get('year')==3):
                print("")
                print(''' ''')
    elif year==None:
        for k,v in subjects.subjects.items():
            print("")
            print(v.get('year'))
            print(v.get('name'))
            for s,val in subjects.status_names.items():
                print(''' ''' +val+ '''  ''')
    elif year=='Lista svih predmeta':
        for k,v in subjects.subjects.items():
            print("")
            print(v.get('year'))
            print(v.get('name'))
            for s,val in subjects.status_names.items():
                print(''' ''' +val+ '''  ''')
    print('''
    
        ''' + year + '''
        Ects
        status
    ''' +v.get('name')+ '''''')
    for s,val in subjects.status_names.items():
        print(''' ''' +val+ ''' ''')
    print('''''' +v.get('name')+ '''''')
    for s,val in subjects.status_names.items():
        print(''' ''' +val+ '''  ''')
    print('''''' +v.get('name')+ '''''')
    for s,val in subjects.status_names.items():
        print(''' ''' +val+ '''  ''')
    print('''''')

year=params.getvalue('year')

save_data(params)
base.start_html()

print_subjects(params)

#subjects.print_subjects(year)
#translate.display_year()
print('''
    
''')

base.end_html()
print("""""")
print(years)
print("""""")
#params.getvalue('1')
print("""""")
print(params)