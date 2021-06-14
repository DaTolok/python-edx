# Ejemplo 2
import re


sentence = '''
MIME-Version: 1.0
Date: Thu, 27 May 2021 04:25:52 -0500
Subject: Mensaje Importante
From: Didier G <dg.correo@gmail.com>
To: "Romeo C <rc.correo@gmail.com>
Cc: Jhonatan P <jp.correo@gmail.com>, wv.correo@gmail.com
Content-Type: multipart/alternative; boundary="000000000000b19c9605c34c581a"

--000000000000b19c9605c34c581a
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

Estimado Romeo C,

Env=C3=ADo este mensaje importante.

Saludos cordiales,
Didier G

--000000000000b19c9605c34c581a
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr">Estimado Romeo C,<div><br></div><div>Env=C3=ADo este mensa=
je importante.</div><div><br></div><div>Saludos=C2=A0cordiales,</div><div>D=
idier G</div></div>

--000000000000b19c9605c34c581a--
'''

matches = re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+', sentence)

print(matches)
