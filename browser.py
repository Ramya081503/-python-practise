import webbrowser
import os

print()
f = open('helloworld.html', 'w')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

# Change path to reflect file location
filename = 'file:///' + os.getcwd() + '/' + 'host1.py'
webbrowser.open_new_tab(filename)
