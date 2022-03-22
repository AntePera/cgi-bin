#!C:\Users\antep\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe
import subjects

def start_html():
    print("""
    <!DOCTYPE html>
    <html>
    <head></head>
    <body>
     """)
def body():
    print('''<form action="s2.py" method="get">
  <button>1st year</button> <br><br>''')
    for k_par,v_par in subjects.subjects.items():
        if v_par.get('year')==1:
            print(v_par)
            print('''<input type="radio" name="not" value="Not Selected"> Not Selected
  <input type="radio" name="enr" value="Enrolled"> Enrolled
 <input type="radio" name="pass" value="Passed"> Passed <br><br>''')
            print('''<br><br>''')
    print('''
</form>''')
    print('''<form action="s2.py" method="get">
  <button>2nd year</button><br><br>''')
    for k_par,v_par in subjects.subjects.items():
        if v_par.get('year')==2:
            print(v_par)
            print('''<input type="radio" name="not" value="Not Selected"> Not Selected
  <input type="radio" name="enr" value="Enrolled"> Enrolled
 <input type="radio" name="pass" value="Passed"> Passed <br><br>''')
            print('''<br><br>''')
    print('''
</form>''')
    print('''<form action="s2.py" method="get">
  <button>3rd year</button><br><br>''')
  
    for k_par,v_par in subjects.subjects.items():
        if v_par.get('year')==3:
            print(v_par)
            print('''<input type="radio" name="not" value="Not Selected"> Not Selected
  <input type="radio" name="enr" value="Enrolled"> Enrolled
 <input type="radio" name="pass" value="Passed"> Passed <br><br>''')
            print('''<br><br>''')
    print('''
</form>''')
    print('''<form action="s2.py" method="get">
  <button>Upisni list</button> 
</form>''')        
def end_html():
    print("""</body>
    </html>
    """)  
start_html()
body()
end_html()