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

# Find URLs
pattern = r'href=\"([\w\S]+)\"'
matches = re.findall(pattern, html)
print("Pattern: ", pattern)
print(matches)