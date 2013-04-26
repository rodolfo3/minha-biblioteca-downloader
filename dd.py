from urllib2 import Request, urlopen

id_livro = '9788577808427'
paginas = 717
session = 'BAh7DzoPc29ydF9vcmRlciIKdGl0bGU6HGxhc3RfYWN0aXZpdHlfdGltZXN0YW1wSXU6CVRpbWUNU08cgK3Gl2sGOh9AbWFyc2hhbF93aXRoX3V0Y19jb2VyY2lvbkY6DHVzZXJfaWRpA79XGzoIc3NvVDoXc2tpcF9kZXNrdG9wX2NoZWNrVDoeY2FwdHVyZWRfZXVsYV9kZXN0aW5hdGlvbiItL2Jvb2tzLzk3ODg1Nzc4MDg0MjcvY29udGVudC9pbWFnZS8wLmpwZzoKZW1haWwiEjExMzE4MkB1Y3MuYnI6CGZvbyIIYmFyOg9zZXNzaW9uX2lkIiUzMjI2ZDJjZDZhNmQyMDFjNDlhNzczMzE4ZTExMjIzZToPc29ydF9xdWVyeSIUYm9va3MudGl0bGUgQVND--d279bb616eab14a21976b8abab3eeccd8251dbc8'
c = {
    'Accept-Language': 'en-us,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:23.0) Gecko/20130424 Firefox/23.0',
    'DNT': '1',
    'Host': 'online.minhabiblioteca.com.br',
    'Cookie': '_quasimodan_session=' + session
}


for pagina in xrange(paginas):
    rq = Request("http://online.minhabiblioteca.com.br/books/" + str(id_livro) + "/content/image/" + str(pagina) + ".jpg?width=800", headers=c)
    rr = urlopen(rq)
    assert rr.code == 200

    content = rr.readlines()
    rr.close()

    ff = file('%0.9i.jpg' % pagina, 'w')
    ff.write(''.join(content))
    ff.close()

