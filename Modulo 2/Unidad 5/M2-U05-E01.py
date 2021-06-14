#Ejemplo 1
import re

html = '''<html>
<head>
   <title>Basic Examples</title>
</head>
<body>
    <h1>Python IDEs</h1>
    <p>
        The most used <span style="color:#ff0000;">Python</span> IDEs are the following:
    </p>
        <a href="https://www.spyder-ide.org" target="_blank" rel="noopener">Spyder</a>
        <a href="https://www.jetbrains.com/pycharm/" target="_blank" rel="noopener">PyCharm</a>
        <a href="https://jupyter.org" target="_blank" rel="noopener">Jupyter Notebook</a>
    <p>
        &iexcl;Download the one you liked the most!
    </p>
</body>
</html>
'''

# Tags (No Parenthesis)
pattern = r'<\w+>'
matches = re.findall(pattern, html)
print("Pattern: ", pattern)
print(matches)

# Tags 
pattern = r'<(\w+)>'
matches = re.findall(pattern, html)
print("Pattern: ", pattern)
print(matches)

# Tags with attributes
pattern = r'<(\w+)\s'
matches = re.findall(pattern, html)
print("Pattern: ", pattern)
print(matches)

# All tags with attributes
pattern = r'<(\w+)\s?'
matches = re.findall(pattern, html)
print("Pattern: ", pattern)
print(matches)

# Attributes (only first one)
pattern = r'<\w+\s+(.*?)='
matches = re.findall(pattern, html)
print("Pattern: ", pattern)
print(matches)

# Attributes
pattern = r'(\w+)='
matches = re.findall(pattern, html)
print("Pattern: ", pattern)
print(matches)

# Attribute Values
pattern = r'=\"([\w\S]+)\"'
matches = re.findall(pattern, html)
print("Pattern: ", pattern)
print(matches)

# Text Content
pattern = r'\>(.*)\<'
matches = re.findall(pattern, html)
print("Pattern: ", pattern)
print(matches)