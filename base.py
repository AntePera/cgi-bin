#!C:\Users\antep\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe

def start_html():
    print("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    table, th, td {
    border:1px solid black;
    }
    </style>
    </head>
    <body>
    <form action='pera.py' method='post'>
     """)

def end_html():
    print("""
    </form>
    </body>
    </html>
    """)