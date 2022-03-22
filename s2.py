#!C:\Users\antep\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe
import cgi
from tkinter import*
ws=Tk()
params = cgi.FieldStorage()
if(params.getvalue("password")==params.getvalue("password2")):
    print ('''
    <!DOCTYPE html>
    <html>
    <body>

    <h2>Odaberite smjer:</h2>

    <form action="s3.py" method="post">
    Status: 
    <input type="radio" name="studij" value="izvanredni" checked> izvanredni 
    <input type="radio" name="studij" value="redovni"> redovni 
    <br>
    <br>
    E-mail:<input type="email" name="mail" value="">
    <br>
    <br>
    Predmet:<select name="smjer">
        <option value="programiranje">programiranje</option>
        <option value="baze_podataka">baze podataka</option>
        <option value="mreze">mreze</option>
        <option value="informacijski_sustavi">informacijski sustavi</option>
    </select>
    <br>
    <br>
    <input type="checkbox" name="zavrsni" value="zavrsni">Zavrsni rad
    <br>  
    <br>
    ''')
    print ('<input type="hidden" name="firstname" value="''' + params.getvalue("firstname") + '">')

    print('''<input type="submit" value="submit">
    </form>

    </body>
    </html>''')
else:
    ws.destroy()
    import s1
#print ('<input type="hidden" name="ime" value="' + params.getvalue("firstname") + '">')