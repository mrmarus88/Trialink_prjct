import cgi
import html

form = cgi.FieldStorage()
packet = form.getfirst("packet", "0")
Subscribers = form.getfirst("Subscribers", "0")
enodeball = form.getfirst("enodeball", "0")
nontelradenodeb = form.getfirst("nontelradenodeb", "0")
bts = form.getfirst("bts", "0")
bts_d = form.getfirst("bts_d", "0")
terminals = form.getfirst("terminals", "0")

packet = html.escape(packet)
Subscribers = html.escape(Subscribers)
enodeball = html.escape(enodeball)
nontelradenodeb = html.escape(nontelradenodeb)
bts = html.escape(bts)
bts_d = html.escape(bts_d)
terminals = html.escape(terminals)


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>packet: {}</p>".format(packet))
print("<p>Subscribers: {}</p>".format(Subscribers))

print("""</body>
        </html>""")