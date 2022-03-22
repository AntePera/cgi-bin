#!C:\Users\antep\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe
import cgi
import os
import cgitb
cgitb.enable(display=0, logdir="")

print  ("""
<!DOCTYPE html>
<html>
<body>
<h2>Unesite podatke:</h2>
<form action="s2.py" method="post">
  Ime:<br>
  <input type="text" name="firstname" value="" required>
  <br>
  Password:<br>
  <input type="password" name="password" value="">
  <br>
  Re-enter password:<br>
  <input type="password" name="password2" value="">
  <br><br>
  <input type="submit" value="Submit">
</form> 


</body>
</html>
""")
params = cgi.FieldStorage() 
