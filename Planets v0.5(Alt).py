import random
break_ = 0
esc = 0
score = 0
fail = 0
yes = 0
pscore = 0
randm = 0
highscore = 0
meteor = random.randrange(1,21)
def game():
    global break_
    global speed
    global planet
    global planetgo
    global planetgoo
    global loadend
    global score
    global fail
    global yes
    global pscore
    global meteor
    global highscore
    planet = "Earth"
    planetgo = "NoNoNoTest"
    def planets():
        global planet
        global pscore
        global break_
        for diddlydo in range(1000):
            if planetgo == planet:
                print ("")
                print ("You are already on " +str(planet)+ "!")
                print ("")
                break_ = 1
                break
            else:
                break
        for something in range(10000):
            if planet != planetgo:
                global pscore
                if planetgo == "Earth":
                    pscore = -3
                    break_ = 10
                    break
                if planetgo == "Jupiter":
                    pscore = -5
                    break_ = 10
                    break
                if planetgo == "Mars":
                    pscore = -3.75
                    break_ = 10
                    break
                if planetgo == "Venus":
                    pscore = -3
                    break_ = 10
                    break
                if planetgo == "Mercury":
                    pscore = -3
                    break_ = 10
                    break
                if planetgo == "Saturn":
                    pscore = -4.9
                    break_ = 10
                    break
                if planetgo == "Uranus":
                    pscore = -5.7
                    break_ = 10
                    break
                if planetgo == "Neptune":
                    pscore = -6
                    break_ = 10
                    break
                if planetgo == "Pluto":
                    pscore = -6
                    break_ = 10
                    break
                if planetgo == "NoNoNoTest":
                    break_ = 10
                    break
                if planetgo == "q":
                    quit()
                if planetgo == "l":
                    print ("")
                    print ("List of planets:")
                    print ("----------------")
                    print ("Mercury")
                    print ("Venus")
                    print ("Earth")
                    print ("Mars")
                    print ("Jupiter")
                    print ("Saturn")
                    print ("Uranus")
                    print ("Neptune")
                    print ("Pluto")
                    print ("")
                    break_ = 999999999999
                    break
                else:
                    pscore = 0
                    print ("")
                    print ("" +str(planetgo)+ " is not a valid planet!")
                    print ("")
                    break_ = 1
                    break
                    
        for somethingggg in range(10000):
            global esc
            if planet != planetgo:
                if planet == "Earth":
                    esc = 11.186
                    break
                if planet == "Jupiter":
                    esc = 60.20
                    break
                if planet == "Mars":
                    esc = 5.03
                    break
                if planet == "Venus":
                    esc = 10.36
                    break
                if planet == "Mercury":
                    esc = 4.25
                    break
                if planet == "Saturn":
                    esc = 36.09
                    break
                if planet == "Uranus":
                    esc = 21.38
                    break
                if planet == "Neptune":
                    esc = 23.56
                    break
                if planet == "Pluto":
                    esc = 1.23
                    break
                else:
                    esc = 0
                    print ("")
                    print ("" +str(planet)+ " is not a valid planet!")
                    print ("")
                    planet = "Earth"
                    break
    global break_


    
    def opening():
        print ("Cpu> Hello and welcome to SpaceShip game, and in this game you will be traveling across from planet to planet on your spaceship")
        print ("")
        global name
        print ("Cpu> But first, what is your name?")
        name = input("")
        print ("")
        print ("Cpu> " +str(name)+ "? Ahhh that's a fine name!")
        print ("")


    def menu():
        global planet
        for something in range(10000):
            global break_
            print ("Cpu> So " +str(name)+ " , would you like to start the game? (y / n)\nOr would you like to load a planet? (l)")
            menu = input ("")
            if menu == "y":
                break_ = 0
                print ("")
                break
            if menu == "n":
                planet = planet
                print ("")
                print ("Cpu> Ok then I'll just shutdown instead.")
                break_ = 1
                break
            if menu == "l":
                print ("")
                print ("List of planets:")
                print ("----------------")
                print ("Mercury")
                print ("Venus")
                print ("Earth")
                print ("Mars")
                print ("Jupiter")
                print ("Saturn")
                print ("Uranus")
                print ("Neptune")
                print ("Pluto")
                print ("")
                print ("Insert planet name")
                planet = input("")
                planet = planet
                planets()
                if esc != 0:
                    print ("")
                    print ('Loaded planet "' +str(planet)+ '"')
                    print ("")
            else:
                print ("")
                print ("" +str(menu)+ " is not a valid option!")
                print ("")
            planet = planet

            
    


    def escape():
        global pscore
        global break_
        global esc
        global speed
        global break_
        global planetgo
        global planet
        global score
        global yes
        global fail
        global randm
        global highscore
        global meteor
        for stufff in range(100000):
            if break_ == 0:
                for stuffthings in range(100000):
                    print ("What planet would you like to go to? (q) to quit, (l) for planet list")
                    planetgo = input("")
                    meteor = random.randrange(1,21)
                    planetgo = planetgo
                    planets()
                   
                

                    if break_ == 10:   
                        print ("")       
                        print ("How much do you weigh?")
                        weight = input("")
                        print ("")
                        print ("How fast [km/s] do you wanna go? ")
                        speed = input("")
                        speed = +float(speed)

                        
                        if speed >= esc:
                            if speed > (esc * 1.4):
                                print ("")
                                print ("You were atleast " +str(+int(esc - speed)* -1)+ " km/s too fast, and crashed back to the surface!")
                                print ("")
                                print ("Try again!")
                                print ("")
                                score = 0
                                score = score
                                if score >= highscore:
                                    highscore = score
                                print ("Score -> [" +str(score)+ "]")
                                print ("Highscore -> [" +str(highscore)+ "]")
                                print ("")
                                
                            else:
                                if meteor == 20:
                                    print ("")
                                    print ("You crashed, as you were hit by a meteor!")
                                    print ("")
                                    score = score - 5
                                    score = score
                                    if score >= highscore:
                                        highscore = score
                                    print ("Score -> [" +str(score)+ "]")
                                    print ("Highscore -> [" +str(highscore)+ "]")
                                    print ("")

                                    
                                if meteor == 19:
                                    print ("")
                                    print ("You were hit by a meteor, but luckily you still made it!")
                                    randm = random.randrange(1,3)
                                    randm = random.randrange(1269, 1314)
                                    score = (+int(((score - ((((abs(esc / speed)))* pscore) * (randm / 845))))))
                                    score = score
                                    if score >= highscore:
                                        highscore = score
                                    planet = planetgo
                                    planetgo = planet
                                    print ("")
                                    print ("Score -> [" +str(score)+ "]")
                                    print ("Highscore -> [" +str(highscore)+ "]")
                                    print ("")
                                    
                                else:
                                    randm = random.randrange(1,3)
                                    randm = random.randrange(1269, 1314)
                                    score = (+int(((score - ((((abs(esc / speed)))* pscore) * (randm / 845))))))
                                    score = score
                                    print ("")
                                    print ("You make it off of " +str(planet)+ ", and on to " +str(planetgo)+ "!")
                                    if score >= highscore:
                                        highscore = score
                                    planet = planetgo
                                    planetgo = planet
                                    print ("")
                                    print ("Score -> [" +str(score)+ "]")
                                    print ("Highscore -> [" +str(highscore)+ "]")
                                    print ("")
                                    
                        if speed < esc:
                            print ("")
                            print ("You were atleast " +str(+int(speed - esc)* -1)+ " km/s too slow, and crashed back to the surface!")
                            print ("")
                            print ("Try again!")
                            print ("")
                            if score >= highscore:
                                highscore = score
                            score = 0
                            score = score
                            print ("Score -> [" +str(score)+ "]")
                            print ("Highscore -> [" +str(highscore)+ "]")
                            print ("")
                            break_ = 0


    opening()
    menu()
    for anything in range(1000):
        escape()
game()

#Cameron Watts#
#Comp Prog#
#10 27 17#
