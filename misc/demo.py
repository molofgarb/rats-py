#!/usr/bin/python
print("Content-Type: text/html")
print("")

###HTML heading stuff
html_str = "<!DOCTYPE html>\n"
html_str += "<html>\n"
html_str += "<head>\n"
html_str += "<title>\n"
html_str += "demo"
html_str += "</title>\n"
html_str += "</head>\n"
html_str += "<body>\n"

import cgitb
#cgitb.enable()

###converts cgi dict into nice dict
import cgi
cgidict = cgi.FieldStorage()
querydict = {}
for x in cgidict:
    querydict[x] = cgidict[x].value

###
###NOTE: the url stores the PREVIOUS score and timestamp. it uses this previous score and timestamp to calculate the new ones, which are printed
###and stored locally in the html.
###

import time

###initializes page if it hasn't been
if len(querydict) < 1:
    html_str += '<a href="https://lisa.stuy.edu/~eshieh10/fp/demo.py?timestamp=' + str(int(time.time())) + '&score=0">initialize</a>'

else:
    ###initializes variables to print
    elapsed = round(time.time()) - int(float(querydict['timestamp'])) #int elapsed time
    score = str(int(querydict['score']) + int(elapsed)) #new score calculated

    html_str += "current score: " + score + "<br><br>" #prints new calculated score

    html_str += '<form method="GET" action="demo.py">'
    ###submit button to ask game to update
    html_str += '<input type="submit" value="checkscore">'

    ###score and timestamp data storage for use in refresh calculation
    html_str += '<input type="hidden" name="score" value="' + score + '">' #score storage
    html_str += '<input type="hidden" name="timestamp" value="' + str(now) + '">' #current time storage
    html_str += '</form>'

html_str += "</body>\n"
html_str += "</html>"

print(html_str)
