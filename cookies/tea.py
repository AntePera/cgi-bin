#!C:\Users\antep\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe

import ss
import base
import os
import cgi
from http import cookies

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)

params = cgi.FieldStorage()


dicti = ss.get_cookies(all_cookies_object)

def print_navigation():
    ss.display_year()
    if params.getvalue("button") is not None:
            if(params.getvalue("button") != "Upisni List"):
                 year = ss.year_ids[params.getvalue("button")]
            else:
                year = params.getvalue("button")
    else:
        year = 1
    ss.display_subject_on_year(year, dicti)


ss.make_cookies(params)

base.start_html()
print_navigation()

base.end_html()
