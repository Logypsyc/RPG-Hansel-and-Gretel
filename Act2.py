import replit 
from Colors import pause, colors, color

def Hansel_Act2():
  result1 = ''
  finger = ''
  with open("textArt/15.txt") as file:
        print(file.read())
  print("After much wandering, you and your sister come across an impossible sight. A colorful house with reflective, striped walls and a rich, brown roof alongside somewhat clear windows tinted with an artificial color of sorts formed this strange sight. It was candy in the shape of walls, chocolate in the shape of a roof, and solidified sugar in the form of windows. The whole house was made of delicacies. You, upon seeing this sight, tell your sister to join you in eating this house. After all, not only were you and Gretel starving, the both of you had not eaten candy in such a long time. Thus, the both of you began to feast on the house. Suddenly, a voice called out." + pause)
  input()
  while True:
    replit.clear()
    with open("textArt/16.txt") as file:
        print(file.read())
    print("The voice is that of a female, an old and kind one. The old lady asks you and Gretel what the both of you were doing.\n" + color(" - Choice 1: You lie, saying you and your sister were doing nothing.\n - Choice 2: You lie, saying the wind was eating the house\n - Choice 3: You tell the truth, saying that you and your sister were eating the house.",colors.HEADER))
    choice1 = input("(1-3)> ")
    if(choice1 in ("1", "2", "3")):
      if(choice1 == "3"):
        result1 = "Despite your honesty, she will eat you and your sister regardless."
      else:
        result1 = "Because of your dishonesty, she will eat you and your sister."
      break
    else:
      print(color("Please only type 1, 2, or 3", colors.FAIL) + pause)
      input()
      
  print("The old lady eventually steps out of the candy house and tells the both of you to come inside. She also says that she means no harm to either one of you. Seeing as you had no choice, considering yours and Gretel’s hunger at the moment, you hold your sister’s hand and walk inside the house. Suddenly, you have a bad premonition." + pause)
  input()
  replit.clear()
  with open("textArt/18.txt") as file:
        print(file.read())
  print(f"Once you and your sister walk inside the candy house, the old woman’s disposition changes immediately. She seizes you by your shirt collar and throws you into a metal cage. She leaves you in the cage, but the witch pushes Gretel into the kitchen and forces her to cook food for you. Despite the little girl’s incessant weeping, the old bag still forces her to work. Finally, the witch comes back to you and taunts you. She tells you that {result1} You grit your teeth and clench your fists. Is this the way that you and your sister will go out? No, you refuse to give in. Suddenly, a plan comes to your mind." + pause)
  input()
  while True:
    replit.clear()
    with open("textArt/19.txt") as file:
        print(file.read())
    print("When Gretel finishes making the food, the crone takes the food away from her and gives it all to you to eat. Considering that you didn’t have much to do, you ate what you were given. After about a week of Gretel making food and the witch forcing you to eat it, something new happens. The witch commands you to stick out a finger. In response to her command, you:\n" + color(' - Choice 1: Take a chicken bone and stick it out in place of your finger.\n - Choice 2: Stick out your finger.', colors.HEADER))
    choice2 = input("(1/2)>")
    if (choice2 not in ("1","2")):
      print(color("Please only enter '1' or '2'.", colors.FAIL) + pause)
      input()
    else:
      if (choice2 == '1'):
        finger = "'finger'"
      else:
        finger = "finger"
      break
  
  print(f"The witch then fumbles around, trying to grab your {finger}{pause}")
  input()
  print(f"Finally, she grabs your {finger} and inspects it.{pause}")
  input()
  if(choice2 == '1'):
    print("She then complains about how you aren’t fat enough. The hag yells at your sister to keep on making food for you. Suddenly, the witch walks away." + pause)
    input()
    replit.clear()
  else:  
    print("""She then licks her lips and tells you that you are ripe for picking. She sticks her hand in the cage and drags you out. After dragging you out, she holds you by your collar and heads to the kitchen. In the kitchen, the oven is blazing hot with smoke and fire, with Gretel crying on the side. She pleads with the witch for her to not kill you, but the old bag cackles and tells your sister to shut up. The demon then pulls her arm back and then heaves you into the oven. "She then closes the door on you, and the last thing you hear is your sister crying her eyes out.""" + pause)
    input()
    replit.clear()
    return "Bad"
  with open("textArt/20.txt") as file:
        print(file.read())
  print("Another week, exactly like the last, came and went. The crone came back to check on you and asked you to stick out your finger once again. You deceive her yet again. She then pulls you out of the cage and goes to her kitchen with you in hand. The oven in the kitchen isn’t on at the moment, so she turns it on." + pause)
  input()
  print("After some time, the hag tells your sister to get inside the oven to see if it is warm enough. Gretel asks the old bag to get in instead, because she, your sister, didn’t know how to do so. The witch rolls her eyes, but complies and gets in the oven after putting you down. Gretel then slams the oven door shut." + pause)
  input()
  print("The last thing you hear of the witch is her death wails and her curses against you and your sister." + pause)
  input()
  print("After running away a good distance from the house, your sister asks for a break. The both of you then sit down and relax. Neither you nor your sister knew how the both of you were going to get home. Out of nowhere, you hear a flapping of wings reverberate. Suddenly, you see a goose." + pause)
  input()
  replit.clear()

def Gretel_Act2():
  with open("textArt/15.txt") as file:
        print(file.read())
  print("After a long time, my brother and I finally see something different from all the trees, bushes and mountains. We saw something that was impossible! It was a candy house! The walls were made of candy canes, the roof was made of chocolate, and the windows were made of sugar! My brother said that we could eat the house, but I was going to do that anyway. I was starving! We then ate parts of the house really quickly. But then, someone said something." + pause)
  input()
  with open("textArt/16.txt") as file:
        print(file.read())
  print("The voice sounded like it came from an old, kind lady. She asked us what we were doing. Brother said that the wind was eating at the house. I couldn’t understand why Hansel said that, but before I could, the lady came out of her house. She then told us that she meant us no harm, and that if we came inside, she would help us. I wish that my brother and I knew better than to accept her offer, but we were hungry and tired. We needed somewhere to rest. So we went inside the house with her. But then, the old woman changed." + pause)
  input()
  while True:
    replit.clear()
    with open("textArt/21.txt") as file:
        print(file.read())
    print("When we walked inside, the old woman changed immediately! She grabbed my brother by his shirt collar and threw him into a metal cage! The woman then pushed me into the kitchen and forced me to make food for Hansel. When I told her that I didn’t want to make food, she hit me and yelled at me. She told me to start making food even if I didn’t want to. I started to cry, but then the witch started to get ready to hit me again. I had no choice but to make food for my brother.\n" + color(" - Choice 1: Cook Chicken\n - Choice 2: Cook Steak\n - Choice 3: Cook Venison", colors.HEADER))
    choice3 = input("(1-3)>")
    if (choice3 in ('1','2','3')):
      if(choice3 == '1'):
        with open("textArt/23.txt") as file:
          print(file.read())
        print("When I made the chicken, the witch fed my brother with it, but didn’t leave me anything to eat. I was forced to eat the scraps that I could find in the kitchen. I wished that my life could change. But then, after a week, things changed." + pause)
        input()
        print("After a week, the witch went to the iron cage that held Hansel. She commanded Hansel to stick out a finger. Instead of his actual finger, he stuck out a chicken bone. The witch, none the wiser, touched and felt the chicken bone. I was quite scared, as I was worried that Hansel would be found out. Thankfully, she didn’t have any problem aside from the fact that Hansel was still “skinny.” She yelled at me for not making Hansel fat enough and went away." + pause)
        input()
        print("\nAnother week, just like the last. The witch forces me to make food for my brother, with which she only feeds my brother. Just like last week, the witch asks Hansel to stick out his finger, but, just like last week, he sticks out a chicken bone in place of his finger. The witch feels it, but this time, she grabs Hansel out of the cage and drags him to the kitchen." + pause)
        input()
        print("She then yells at me to turn on the oven in the kitchen. I do exactly as she says, because she could’ve killed me if I didn’t. After some time, the witch tells me to get in the oven to test the heat. I didn’t believe that, so I pretended that I didn’t know how to get into the oven." + pause)
        input()
        print("I asked her to get in to show me how. I don’t know why, but the witch believed me, and got in the oven. Hehe, I got her good! I slammed the oven door on her, and she started yelling because the oven was very hot and was still heating up." + pause)
        input()
        print("I took my brother's hand, who was standing around in shock because of what just happened, and ran away from the house. After some time, we finally stopped to sit down and took a break. We didn’t know how we were going to go home, but we were going to try our best! But then, fortunately, we saw a goose!" + pause)
        input()
        break
        
      if (choice3 == '2'):
        with open("textArt/25.txt") as file:
          print(file.read())
        print("When I made the steak, the witch fed my brother with it, but didn’t leave me anything to eat. I was forced to eat the scraps that I could find in the kitchen. I wished that my life could change. But then, after a week, things changed." + pause)
        input()
        print("After a week, the witch went to the iron cage that held Hansel. She commanded Hansel to stick out a finger, and he complied." + pause)
        input() 
        print("She felt his finger and smiled. She then dragged Hansel out of the metal cage and takes him to the kitchen. The whole while, I was crying because I knew what was going to happen to my brother, and I knew I couldn’t do anything about it." + pause)
        input()
        print("The wicked witch then threw my brother into the oven. When I saw her do that, I ran away from the house. I ran and I ran and I ran." + pause)
        input()
        replit.clear()
        return "Neutral"
        
      if (choice3 == '3'):
        with open("textArt/25.txt") as file:
          print(file.read())
        print("When I made the venison, the witch fed my brother with it, but didn’t leave me anything to eat. I was forced to eat the scraps that I could find in the kitchen. I wished that my life could change. But then, after a week, things changed." + pause)
        input()
        print("After a week, the witch went to the iron cage that held Hansel. She commanded Hansel to stick out a finger, and he complied." + pause)
        input() 
        print("She felt his finger and smiled. She then dragged Hansel out of the metal cage and takes him to the kitchen. The whole while, I was crying because I knew what was going to happen to my brother, and I knew I couldn’t do anything about it." + pause)
        input()
        print("The wicked witch then threw my brother into the oven. When I saw her do that, I ran away from the house. I ran and I ran and I ran." + pause)
        input()
        replit.clear()
        return "Neutral"
        
    else:
      print(color("Please enter only  '1', '2', or '3'.", colors.FAIL) + pause)
      input()
      continue