#!/usr/bin/python
print("Content-Type: text/html")
print("")

#Team "The Brownies" 
#IntroCS pd1
#FP -- Incremental Game
#2019-06-13

import random

###stores titles for the html page that are chosen randomly (flavor text!)
title = [
    "score! rats!", "watch number go up", "waiting simulator",
    "4k HDR ray-traced numbers", "16x Anisotropic Filtering!", "checksanity",
    "buildings (soon) now!", "now with HTML!", "action packed!",
    "possibly fun!", "demo.py", "not capitalism",
    "definitely imperialism", "now with a story!", "an enduring issue",
    "anthromorphic rats", "f5", "insert title text here",
    "E1M1 - At Rats' Gate", "All your base belong to rat", "Nyan Rat",
    "Wolfenstein: The New Rat", "alt+f4 for max rats", "it's over 9000 (rats)",
    "cookie clicker is better", "h", "Is this just fanta C?",
    "now in 3D!", "Knee-Deep in the Rats", "The Shores of Rats",
    "9/10 Telvanni Mages Approve", "skeevers!", "rodents of unusual size!",
    "play minecraft!", "Half-Rat 2: Episode 3", "the elder rats VI"
    ]

html_str = "<!DOCTYPE html>\n"
html_str += "<html>\n"
html_str += "<head>\n"
html_str += "<title>\n"
html_str += random.choice(title)
html_str += "</title>\n"
html_str += "</head>\n"
html_str += "<body>\n"

html_str += """<style>
body {
   color: blue
}
        h1 {
   font-size: 0px;
         }
         </style>"""

###stores situation text that progresses depending on expansion
story = [
    "not enough rats! check your population to see if you have enough!",
    '''
    You have just created a machine that spews out an infinite source of food. Instead of solving world hunger, you have decided, as an avid rat<br>
    enthusiast, to use your machine to use your machine to recruit and feed an army of rats instead. By leaving some cheese in your basement, <br>
    rats start to take up residence in your house. You have become a <b>patron</b> of some rats.
    ''',
    '''
    The rats, being grateful for their infinite supply of food, now follow your commands. You have allocated rats to building and expanding their nest.<br>
    They have expanded to your garage. You have also learned that you can allocate rats recruitment duty, leaving the nest to find and bring back more<br>
    rats. You have become the <b>alpha</b> of the rats.
    ''',
    '''
    As your nest increases, your rat population increases, giving you more works to allocate to new tasks. The rats obey your commands, knowing that you'll<br>
    provide and care of them for generations. You have become the <b>master</b> of the rats.
    ''',
    '''
    Your neighbors have started to notice the rat infestation taking up your property. Some have started to move out, giving you more space for your rats.<br>
    Some have tried to complain or threaten you to get rid of your rats, but are unwilling to take action. You have become the <b>chief</b> of the rats.
    ''',
    '''
    Your area seems to be deserted, since all your neighbors moved out. The rats have started to branch out of your house, creating new colonies in the<br>
    abandoned homes surrounding your property. The town government has politely asked for you to buy exterminators to clear your property of rats, scared that<br>
    the increasing rat population will lower property values. You have become the <b>khan</b> of the rats.
    ''',
    '''
    The town government has sent exterminators to deal with your rats. At the start, some rats fell, surprised by the sudden attack. As your army regrouped, they<br>
    began to gnaw holes in the exterminators' clothing, growing inside their clothes and biting them. The exterminators began to flee, resulting in a victory for<br>
    you and your rats. The First Battle of Ratsburgh has concluded. You have become the <b>mayor</b> or the rats.
    ''',
    '''
    Your rats have scared the population of your small town away, leaving a enormous amount of land for your rats to colonize. The previous mayor has fled the town.<br>
    You refurnish the town hall as a command headquarters for your army. You have become the <b>lord</b> of the rats.
    ''',
    '''
    Because of better nutrition provided from your food, your rats have become stronger. A small group can easily take on a human. The increase in nutritional quality<br>
    has also led to an increase of intelligence from your rats. They start to resemble a civilization, with social hierarchies and specialization of labor. Your rats are<br>
    more compotent, and have begun to colonize neighboring towns as well. You have become the <b>count</b> of the rats.
    ''',
    '''
    Your increasing rat population has become a national issue. News reports are spreading word about your army, and the president of the United States (the country you are<br>
    in) has said that your rats will be dealt with if they continue to spread. Curious researchers have come to your colony, surprised by how docile your rats are. Since<br>
    they aren't a threat, you have allowed them to live in your town, researching your rats. You hope that you can gain their sympathy and employ them to work for you.<br>
    You have become the <b>duke</b> of the rats.
    ''',
    '''
    The scientists in your colony have found a compound that, when introduced to your rats via food, makes them more intelligent and cooperative with humans. The rats have begun to develop culture,<br>
    scratching intricate artwork on walls with their teeth, developing a writing system, and creating a religion based on you, the savior and patron of the rats. The scientists are also included within<br>
    their pantheon as your disciples. With this advanced society, more people around the country have gained sympathy for your rat society, and humans have started to move back into your colonized towns.<br>
    They support your cause and sympathize with the rats, whom they enjoy the company of. You have become the <b>governor</b> of the rats.
    ''',
    '''
    The U.S. government has warned that imminent action will be taken on your rats to "return the stolen land to its rightful owners." Many in the country support your rat society, but many also support the<br>
    human government as well. Your rats have spread across multiple U.S. states, providing protection and bringing food (from your machine) to the natives in the areas that they are colonizing, in exchange for land.<br>
    Many more people are sympathizing with your rats. Your rats have learned to use some human technology and you are equipping your army against a potential attack from the U.S. government. You have become the <b>imperator</b>
    of the rats.
    ''',
    '''
    The U.S. launches an small-scale invasion of the areas inhabited by your rats. Because of the utilization of weapons technology by your army and because of support from human militias supporting<br>
    your rats, the invasionhas been repelled. Any escalation of a war against rats is also becoming unpopular as more and more people from around the country are sympathizing and welcoming the<br>
    rat society as they continue to colonize and expand. They are no longer pests, and have become symbols of prosperity and peace. You have become the <b>general</b> of the rats.
    ''',
    '''
    The U.S. president remains firmly opposed to the existence of your rat society. After gaining nationwide support for your rats, a coup is performed against the<br>
    government from armed rat supporters. The president is overthrown, and an election is held. You win the election with overwhelming support from your rats (who have<br>
    the rights and intelligence to vote) and from your subjects in the rat country. You have become the <b>president</b> of the rats.
    ''',
    '''
    Your rats have grown in size, strength, and intelligence due to continued optimizations to their diet. One rat has the physical and mental capabilities of one human.<br>
    Your country of super-intelligent rats continues to expand, taking territory from neighboring countries. Some countries welcome the expansion and the cooperate<br>
    with your government. Some countries try to fight the invasion, but are swiftly crushed. Your rats, greater in number than they have ever been, guarantee that every<br>
    future election will result in your victory. They name you king of the Holy Rat Kingdom. You have become the <b>king</b> of the rats.
    ''',
    '''
    Your rats, having colonized the Americas, have spread to all habitable continents. Expansive colonies have been established in Europe, Asia, Africa, and Australia.<br>
    Humanity now coexists with your rats. Rats bring food to native humans in their colonizies, gaining their support and cooperation. Conflict has mostly ceased. With your
    machine and your army of rats, you have assumed leadership of Earth. You have become the <b>emperor</b> of the rats and humans.
    ''',
    '''
    Running out of land on Earth to colonize, your rats develop a space program and begin colonies on the moon. Colonies on Mars, Phobos, Io, Europa, Ganymede,<br>
    Callisto, and Saturn's Moons have been established. Using newfound resources available from the colonized celestial bodies, expansive space stations, near lightspeed travel,<br>
    and complex nanotechnology has been developed. You have gained eternal life through nanotechnology created by rat scientists. Development of an FTL engine is nearly<br>
    complete. You have become the <b>supreme galactic ruler</b> of the rats and humans.
    ''',
    '''
    An FTL engine is developed, allowing your rat civilization to expand to other solar systems around the galaxy. Blueprints of your original infinite food machine<br>
    have finally been completed. Rat scientists have also figured out how to modify your machine to create any resource they want, providing your civilization with an<br>
    infinite supply of any resource they could ever want. Wormhole travel, dark matter reactors, spacetime manipulation, and galaxy creationtechnologies have been <br>
    developed by rat scientists. The rats continue to worship you, conquering galaxy clusters to expand your empire. You have become <b>god</b> of the universe.    ''',
    ]

###score limits based on expansion status
lim = [
    15, #patron
    50, #alpha
    100, #master
    500, #chief
    1000, #khan
    5000, #mayor
    10000, #lord
    50000, #count
    100000, #duke
    500000, #governor
    1000000, #imperator
    5000000, #general
    10000000, #president
    1000000000, #king
    100000000000, #emperor
    10000000000000, #supreme galactic ruler
    -1 #god
    ]

import cgitb
cgitb.enable()

#-------------------------------------------------------------------------------#####encryption

##generates a key for encrypting new written data
def key():
    import random
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    outstr = ""

    outstr = outstr + random.choice(base64) #base64 rotation alpha start
    outstr = outstr + str(random.randrange(1, 7)) #base64 rotation alpha augmentation interval
    outstr = outstr + str(random.randrange(10)) #encrypted output rotation

    return outstr

encryptkey = key()

##encrypts a, returns a string, using a key
def encrypt(num, key):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    outstr = ""

    alpha = base64[base64.find(key[0])::int(key[1])] + base64[:base64.find(key[0]):int(key[1])] #make enc alpha from key pair
    for x in str(num): #for each num in outstr 1, find the character in alpha with an index that corr. with num
        outstr = outstr + alpha[int(x)]

    rot = int(key[2]) % len(str(num))
    outstr = outstr[rot:] + outstr[:rot]

    return outstr

#print(encrypt(23456, encryptkey) + "     this is what the data looks like after being encrypted")
#encstr = encrypt(23456, encryptkey)

##decrypts a string, returns a int
def decrypt(string, key):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    outstr = ""

    counterrot = len(string) - (int(key[2]) % len(string))
    string = string[counterrot:] + string[:counterrot]

    alpha = base64[base64.find(key[0])::int(key[1])] + base64[:base64.find(key[0]):int(key[1])]
    for x in string:
        outstr =  outstr + str(alpha.find(x))

    return int(outstr)

#print(str(decrypt(encstr, encryptkey)) + "     this is what the data looks like after being decrypted")

#-------------------------------------------------------------------------------###turns a num (like 1234567) into a number with commas (like 1,234,567) for readability
def commanum(numstr):
    ctr = len(numstr) - 1
    while ctr - 3 >= 0:
        ctr = ctr - 3
        numstr = numstr[:ctr + 1] + "," + numstr[ctr + 1:]
    return numstr

#-------------------------------------------------------------------------------
import cgi
cgidict = cgi.FieldStorage()
querydict = {}
#print(cgidict)
for x in cgidict:
    querydict[x] = cgidict[x].value

###
###NOTE: the url stores the PREVIOUS score and timestamp. it uses this previous score and timestamp to calculate the new ones, which are printed
###and stored locally in the html.
###

import time

#-------INITIALIZE QUERY STRING IF NOT INITIALIZED-------------------------------------------------------------------------

###if the query vars are not present, create them
if len(querydict) < 1:
    ###this comment stores the previous initialization method which used a hyperlink to lisa with the correct query vars
    #html_str += '<a href="https://lisa.stuy.edu/~eshieh10/fp/rats.py?s=0&timestamp=' + str(int(time.time())) + '&score=0&stage=0&one=0&two=0&three=0&four=0&key=010">initialize</a>'

    ###this stores the current initialization method which uses hidden inputs and a initialization submit button
    html_str += '<form method="GET" action="rats.py">'
    html_str += '<input type="submit" name="s" value="initialize">' #submit to initialize
    html_str += '<input type="hidden" name="timestamp" value="' + encrypt(int(time.time()), encryptkey) + '">' #stores current timestamp
    html_str += '<input type="hidden" name="score" value="' + encrypt(0, encryptkey) + '">' #stores starting score
    html_str += '<input type="hidden" name="stage" value="' + encrypt(0, encryptkey) + '">' #stores starting stage
    html_str += '<input type="hidden" name="one" value="' + encrypt(0, encryptkey) + '">' #stores starting one
    html_str += '<input type="hidden" name="two" value="' + encrypt(0, encryptkey) + '">' #stores starting two
    html_str += '<input type="hidden" name="three" value="' + encrypt(0, encryptkey) + '">' #stores starting three
    html_str += '<input type="hidden" name="four" value="' + encrypt(0, encryptkey) + '">' #stores starting four
    html_str += '<input type="hidden" name="five" value="' + encrypt(0, encryptkey) + '">' #stores starting five
    html_str += '<input type="hidden" name="key" value="' + encryptkey + '">' #stores starting key

###if the query vars are present
else:
###try making a new page. if there is an error (most likely with decryption from user tampering) it prints an error page instead of a blank one
#-------INITIALIZE VARIABLES AND DO SCORE MATH-----------------------------------------------------------------------------

    ###initialize form data
    html_str += '<form method="GET" action="rats.py">'

    ###initialize vars
    now = int(time.time())
    key = querydict['key'] #read key
    stage = decrypt(querydict['stage'], key) #int stage level
    txt = story[stage + 1] #stores the situation text that will be written (assuming this var is not overwritten)

    one = decrypt(querydict['one'], key) #int building one
    two = decrypt(querydict['two'], key) #int building two
    three = decrypt(querydict['three'], key) #int building three
    four = decrypt(querydict['four'], key) #int building four
    five = decrypt(querydict['five'], key) #int building five

    score = decrypt(querydict['score'], key) #int starting score
    elapsed = int(now // 1) - decrypt(querydict['timestamp'], key) #int elapsed time for scorecalc

    ###score increase + score increase for buildings + score limit
    ##stage double multiplier increase
    doubles = 2 ** (stage // 2)

    ##increase score for each building
    score = score + elapsed #default 1 rate
    score = score + (elapsed * (one * 1 * doubles)) #multiplies score based on building one
    score = score + (elapsed * (two * 10 * doubles)) #multiplies score based on building two
    score = score + (elapsed * (three * 100 * doubles)) #multiplies score based on building three
    score = score + (elapsed * (four * 1000 * doubles)) #multiplies score based on building four
    score = score + (elapsed * (five * 10000 * doubles)) #multiplies score based on building five
    if lim[stage] == -1: #if at inf, don't touch score
        score = score
    elif score >= lim[stage]: #if over limit, limit score
        score = lim[stage]

#-------PURCHASE CHECK-----------------------------------------------------------------------------------------------------

    ##stage upgrade purchase
    if not lim[stage] == -1: #if not at max, score can be increased
        stagepr = lim[stage] - 5
        if querydict['s'] == "Expand Colony": #if the building is asked to be bought
            if score > stagepr: #if the building can be bought
                score = score - int(stagepr)
                html_str += '<input type="hidden" name="stage" value="' + encrypt(stage + 1, encryptkey) + '">'
                stage += 1
                txt = story[stage + 1]
            else: #if the building is not bought (too expensive)
                html_str += '<input type="hidden" name="stage" value="' + encrypt(stage, encryptkey) + '">'
                txt = story[0]
        else: #if the building is not bought
            html_str += '<input type="hidden" name="stage" value="' + encrypt(stage, encryptkey) + '">'
    else: #score at max
        html_str += '<input type="hidden" name="stage" value="' + encrypt(stage, encryptkey) + '">'


    ##building 1 upgrade increase
    onepr = int(round(10 * (1.3 ** one))) #build 1 cost
    if querydict['s'] == "Rat Platoon": #if the building is asked to be bought
        if score >= onepr: #if the building can be bought
            score = score - int(onepr)
            html_str += '<input type="hidden" name="one" value="' + encrypt(one + 1, encryptkey) + '">'
            one += 1
        else: #if the building is not bought (too expensive)
            html_str += '<input type="hidden" name="one" value="' + encrypt(one, encryptkey) + '">'
            txt = story[0]
    else: #if the building is not bought
        html_str += '<input type="hidden" name="one" value="' + encrypt(one, encryptkey) + '">'

    ##building 2 upgrade increase
    twopr = int(round(500 * (1.3 ** two))) #build 2 cost
    if querydict['s'] == "Rat Battalion": #if the building is asked to be bought
        if score >= twopr: #if the building can be bought
            score = score - int(twopr)
            html_str += '<input type="hidden" name="two" value="' + encrypt(two + 1, encryptkey) + '">'
            two += 1
        else: #if the building is not bought (too expensive)
            html_str += '<input type="hidden" name="two" value="' + encrypt(two, encryptkey) + '">'
            txt = story[0]
    else: #if the building is not bought
        html_str += '<input type="hidden" name="two" value="' + encrypt(two, encryptkey) + '">'

    ##building 3 upgrade increase
    threepr = int(round(10000 * (1.3 ** three))) #build 3 cost
    if querydict['s'] == "Rat Legion": #if the building is asked to be bought
        if score >= threepr: #if the building can be bought
            score = score - int(threepr)
            html_str += '<input type="hidden" name="three" value="' + encrypt(three + 1, encryptkey) + '">'
            three += 1
        else: #if the building is not bought (too expensive)
            html_str += '<input type="hidden" name="three" value="' + encrypt(three, encryptkey) + '">'
            txt = story[0]
    else: #if the building is not bought
        html_str += '<input type="hidden" name="three" value="' + encrypt(three, encryptkey) + '">'

    ##building 4 upgrade increase
    fourpr = int(round(250000 * (1.3 ** four))) #build 4 cost
    if querydict['s'] == "Rat Army": #if the building is asked to be bought
        if score >= fourpr: #if the building can be bought
            score = score - int(fourpr)
            html_str += '<input type="hidden" name="four" value="' + encrypt(four + 1, encryptkey) + '">'
            four += 1
        else: #if the building is not bought (too expensive)
            html_str += '<input type="hidden" name="four" value="' + encrypt(four, encryptkey) + '">'
            txt = story[0]
    else: #if the building is not bought
        html_str += '<input type="hidden" name="four" value="' + encrypt(four, encryptkey) + '">'

    ##building 5 upgrade increase
    fivepr = int(round(1500000 * (1.3 ** five))) #build 5 cost
    if querydict['s'] == "Rat Front": #if the building is asked to be bought
        if score >= fivepr: #if the building can be bought
            score = score - int(fivepr)
            html_str += '<input type="hidden" name="five" value="' + encrypt(five + 1, encryptkey) + '">'
            five += 1
        else: #if the building is not bought (too expensive)
            html_str += '<input type="hidden" name="five" value="' + encrypt(five, encryptkey) + '">'
            txt = story[0]
    else: #if the building is not bought
        html_str += '<input type="hidden" name="five" value="' + encrypt(five, encryptkey) + '">'

#-------HTML PAGE GENERATION-----------------------------------------------------------------------------------------------

    ###calculates and prints score
    scoreincrease = 1 + (one * 1 * doubles) + (two * 10 * doubles) + (three * 100 * doubles) + (four * 1000 * doubles) + (five * 1000 * doubles)
    html_str += "<u>Population</u><br>"
    html_str += "Population: " + commanum(str(score)) + "     / " + commanum(str(lim[stage])) + "<br>" #prints new calculated score
    html_str += "Your population is increasing by<b> " + commanum(str(scoreincrease)) + " </b>rats per second<br>"
    html_str += "Your current maximum population is <b>" + commanum(str(lim[stage])) + "</b> rats<br><br>"

    ###create building purchase buttons so new prices are accurate
    onepr = int(round(10 * (1.3 ** one))) #update prices
    twopr = int(round(500 * (1.3 ** two))) #update prices
    threepr = int(round(10000 * (1.3 ** three))) #update prices
    fourpr = int(round(250000 * (1.3 ** four))) #update prices
    fivepr = int(round(1500000 * (1.3 ** five))) #update prices
    stagepr = lim[stage] - 5 #update prices
    html_str += '<input type="submit" name="s" value="Check Population"><br><br><br>' #checkscore button

    html_str += "<u>Recruitment</u><br>"

    #button + info for building 1
    doubles = 2 ** (stage // 2) #update doubles so that the info presented is accurate

    html_str += "Amount: <b>" + str(one) + '</b><br><input type="submit" name="s" value="Rat Platoon">          ' + "Price: <b>" + commanum(str(onepr)) + '</b><br>'
    html_str += 'increases your rate by <b>' + commanum(str(1 * 1 * doubles)) + ' </b>rats per second<br><br>'

    if one > 0:
        #button + info for building 2
        html_str += "Amount: <b>" + str(two) + '</b><br><input type="submit" name="s" value="Rat Battalion">          ' + "Price: <b>" + commanum(str(twopr)) + '</b><br>'
        html_str += 'increases your rate by <b>' + commanum(str(10 * 1 * doubles)) + ' </b>rats per second<br><br>'

    if two > 0:
        #button + info for building 3
        html_str += "Amount: <b>" + str(three) + '</b><br><input type="submit" name="s" value="Rat Legion">          ' + "Price: <b>" + commanum(str(threepr)) + '</b><br>'
        html_str += 'increases your rate by <b>' + commanum(str(100 * 1 * doubles)) + ' </b>rats per second<br><br>'

    if three > 0:
        #button + info for building 4
        html_str += "Amount: <b>" + str(four) + '</b><br><input type="submit" name="s" value="Rat Army">          ' + "Price: <b>" + commanum(str(fourpr)) + '</b><br>'
        html_str += 'increases your rate by <b>' + commanum(str(1000 * 1 * doubles)) + ' </b>rats per second<br><br>'

    if four > 0:
        #button + info for building 5
        html_str += "Amount: <b>" + str(five) + '</b><br><input type="submit" name="s" value="Rat Front">          ' + "Price: <b>" + commanum(str(fivepr)) + '</b><br>'
        html_str += 'increases your rate by <b>' + commanum(str(10000 * 1 * doubles)) + ' </b>rats per second<br><br>'

    html_str += "<br><u>Expansion</u><br>"

    ###buy next stage
    if not lim[stage] == -1: #if there are more score
        html_str += '<input type="submit" name="s" value="Expand Colony">          ' + "Price: <b>" + commanum(str(stagepr)) + '</b><br>'
        html_str += 'increases your maximum population of rats<br>every 3 stages, all group rate increases will double<br><br><br>'
    else:
        stagepr = 0
        html_str += '<input type="submit" name="s" value="Expand Colony">          ' + str(stagepr) + '<br><br><br>'


    ###score and timestamp and stage data storage
    html_str += '<input type="hidden" name="score" value="' + encrypt(score, encryptkey) + '">' #score storage
    html_str += '<input type="hidden" name="timestamp" value="' + encrypt(now, encryptkey) + '">' #current time storage
    html_str += '<input type="hidden" name="key" value="' + encryptkey + '">' #write key storage


    html_str += '</form>'

    ###text stuff
    html_str += "<u>Situation</u><br>"
    html_str += txt

    html_str += "</body>\n"
    html_str += "</html>"
    #except:
    #    html_str += '''<h1>:(</h1><br>It looks like the game has run into an unexpected issue. This could be because of a bug or because
    #                of tampering done to the encrypted gamedata. Please go back to the previous page.'''

###all hail the mighty print function
print(html_str)
