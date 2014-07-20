#!/usr/bin/python
#
import cgi

formulaire = cgi.FieldStorage()
print 'Content-type: text/html'
print '''
<html>
    <head>
        <title>Page de test</title>
    </head>
    <body>
        <p>Contenu</p>'''
print formulaire["number"][0].value
print formulaire["number"][1].value
print formulaire["number"][2].value
print '''
    </body>
</html>
'''
