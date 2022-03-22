#!C:\Users\antep\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe
import cgi
params = cgi.FieldStorage()
print ('''
    <!DOCTYPE html>
    <html>
    <body>
    <form action="up.py" method="post">
    Napomena:<textarea id="napomena" name="napomena" rows="4" cols="50">
    </textarea><br><br>
    ''')
print ('<input type="hidden" name="smjer" value="' + params.getvalue("smjer") + '">')
print ('<input type="hidden" name="firstname" value="' + params.getvalue("firstname") + '">' )
print ('<input type="hidden" name="mail" value="' + params.getvalue("mail") + '">')
print ('<input type="hidden" name="studij" value="' + params.getvalue("studij") + '">' )
print ('<input type="hidden" name="zavrsni" value="' + params.getvalue("zavrsni") + '">')
print('''    
    <input type="submit" value="submit">
    </form>
    </body>
    </html>''')