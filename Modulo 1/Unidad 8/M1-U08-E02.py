#Ejemplo 2
import re

timeDate='''<time datetime="2020-11-11T17:00:00+00:00"></time>
<time datetime="2020-09-17T14:49:00+00:00"></time>
<time datetime="2020-12-08T11:29:00.000001+00:00"></time>
<time datetime="2021-11-05T15:38:00.000006+00:00"></time>
<time datetime="2021-08-09T11:37:00+00:00"></time>'''

pattern = r'(20\d+)([-]+)(0[1-9]|1[012])([-]+)(0[1-9]|[12][0-9]|3[01])'

for match in re.finditer(pattern, timeDate):
    start = match.start()
    end   = match.end()
    span  = match.span()

    print('Found {} at {}:{}, span: {}'.format(timeDate[start:end], start, end, span))