#!C:\Users\antep\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe
import cgi
data=cgi.FieldStorage()
print('''
<!DOCTYPE html>
    <html>
    <body>

    <h2>Uneseni podaci</h2>
 ''') 
print('''Ime:''')
print(data.getvalue("firstname"))
print('''<br><br>''')
print('''E-mail:''')
print(data.getvalue("mail"))
print('''<br><br>''')
print('''Status:''')
print(data.getvalue("studij"))
print('''<br><br>''')
print('''Smjer:''')
print(data.getvalue("smjer"))
print('''<br><br>''')
print('''Zavrsni rad:''')
print(data.getvalue("zavrsni"))
print('''<br><br>''')
print('''Napomena:''')
print(data.getvalue("napomena"))
print('''
    <br><br>
    <a href= s1.py>Na pocetak</a >
    </body>
    </html>
''')