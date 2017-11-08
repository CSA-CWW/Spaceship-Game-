esc = 0
def game():
    global speed
    global planet
    global planetgo
    global loadend
    planet = "Earth"
    planetgo = "Earth"
    def planets():
        if planetgo == planet:
            print ("")
            print ("You are already on " +str(planet)+ "!")
            print ("")
        for something in range(10000):
            if planetgo != planet:
                if planetgo == "Earth":
                    break
                if planetgo == "Jupiter":
                    break
                if planetgo == "Mars":
                    break
                if planetgo == "Venus":
                    break
                if planetgo == "Mercury":
                    break
                if planetgo == "Saturn":
                    break
                if planetgo == "Uranus":
                    break
                if planetgo == "Neptune":
                    break
                if planetgo == "Pluto":
                    break
                else:
                    print ("")
                    print ("" +str(planetgo)+ " is not a valid planet!")
                    print ("")
                    
        for somethingggg in range(10000):
            if planet != planetgo:
                if planet == "Earth":
                    esc = 11.186
                    break
                if planet == "Jupiter":
                    esc = 11.186
                    break
                if planet == "Mars":
                    esc = 11.186
                    break
                if planet == "Venus":
                    esc = 11.186
                    break
                if planet == "Mercury":
                    esc = 11.186
                    break
                if planet == "Saturn":
                    esc = 11.186
                    break
                if planet == "Uranus":
                    esc = 11.186
                    break
                if planet == "Neptune":
                    esc = 11.186
                    break
                if planet == "Pluto":
                    esc = 11.186
                    break
                else:
                    print ("")
                    print ("" +str(planet)+ " is not a valid planet!")
                    print ("")
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
                print ("Insert planet name")
                planet = input("")
                planet = planet
                planets()
            else:
                print ("")
                print ("" +str(menu)+ " is not a valid option!")
                print ("")
            planet = planet

            
    


    def escape():
        global esc
        global speed
        global break_
        global planetgo
        global planet
        for stufff in range(100000):
            if break_ == 0:
                for stuffthings in range(100000):
                    print ("What planet would you like to go to? (q) if you want to quit")
                    print ("")
                    planetgo = input("")
                    planetgo = planetgo
                    planets()
                    
                    
                print ("")       
                print ("How much do you weigh?")
                weight = input("")
                print ("")
                print ("How fast [km/s] do you wanna go? ")
                speed = input("")
                speed = +float(speed)

                
                if speed >= esc:
                    if speed > (esc * 1.15):
                        print ("")
                        print ("You crashed!, as you were going [" +str(abs(speed - esc))+ "] km/s too fast!")
                        print ("")
                        print ("Try again!")
                        print ("")
                    else:
                        print ("")
                        print ("You make it off of " +str(planet)+ ", and on to " +str(planetgo)+ "!")
                        planet = planetgo
                        planetgo = planet
                        print ("")
                if speed < esc:
                    print ("")
                    print ("You were [" +str(abs(speed - esc))+ "] too slow, and crashed back to the surface!")
                    print ("")
                    print ("Try again!")
                    print ("")



    opening()
    menu()
    escape()
game()

#Cameron Watts#
#Comp Prog#
#10 16 17#
