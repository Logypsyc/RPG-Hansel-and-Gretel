from Maze import Maze
from Player import Player
from Colors import color, pause
from Colors import colors as c
from random import randint
from Act1 import Hansel_POV_Background, Gretel_POV_Background
from Act2 import Hansel_Act2, Gretel_Act2
from Act3 import Hansel_Act3, Gretel_Act3_Good, Gretel_Act3_Neutral
import replit

musics = []


def badEnd(num=1):
    global musics
    with open("textArt/13.txt") as file:
        print(file.read())
    try:
        for music in musics:
            music.set_paused(True)
        musics.append(replit.audio.play_file("music/badendingmusic.mp3"))
    except:
        print("Audio Disabled")
    print(
        color(
            "The lights fade away from your view and you succumb to the darkness",
            c.FAIL) + pause)
    input()
    input("YOU DIED" + pause)
    input("Next time, try not to die" + pause)


def neutralEnd():
    global musics
    with open("textArt/14.txt") as file:
        print(file.read())
    try:
        for music in musics:
            music.set_paused(True)
        musics.append(replit.audio.play_file("music/neutralendingmusic.mp3"))
    except:
        print("Audio Disabled")
    print(color("You survived, but your brother has died.", c.FAIL) + pause)
    input()
    input("Hansel died" + pause)
    # input("<cutscene here>" + pause)
    input("Next time, try to keep Hansel alive" + pause)


def trueEnd():
    global musics
    with open("textArt/7.txt") as file:
        print(file.read())
    try:
        for music in musics:
            music.set_paused(True)
        musics.append(replit.audio.play_file("music/goodendingmusic.mp3"))
    except:
        print("Audio Disabled")
    print("True Ending Reached")
    #add stuff here


def phase1():
    global player, maze

    run = True
    replit.clear()
    maze.legend()
    while run:
        player.display()
        maze.display()
        while True:
            x, y = maze.move(player.move())
            if player.stamina <= 0:
                replit.clear()
                print(
                    color(
                        "You collapse to the ground, weighted down by exhaustion",
                        c.FAIL) + pause)
                input()
                player.alive = False
                run = False
                return
            elif x == "died":
                replit.clear()
                print(
                    color(
                        "You freeze, hearing a feral howl dangerously close to you",
                        c.FAIL) + pause)
                input()
                print(
                    color(
                        "There is a faint rustle in the tall foliage to your right",
                        c.FAIL) + pause)
                input()
                print(
                    color(
                        "You see a glint of light shining off of a pair of claws, and before you can shout in warning, you are slashed alive.",
                        c.FAIL) + pause)
                input()
                player.alive = False
                run = False
                return
            elif x == "out":
                input(
                    color("Invalid move! You can't leave the map.", c.FAIL) +
                    pause)
            elif x == "invalid":
                input(
                    color(
                        "Invalid move! Try to move into a square without any obstacles.",
                        c.FAIL) + pause)
            elif x == "bush":
                cost = randint(1, 10)
                input(
                    f"You cut through the bush, draining {color(f'{cost} stamina', c.OKBLUE)}"
                    + pause)
                player.stamina -= cost
                maze.updatePlayer(y)
                break
            elif x == "tree":
                print(
                    color("You try to punch your way through a tree",
                          c.OKBLUE))
                input()
                print(color("Maybe try something smarter?", c.WARNING))
                input()
                break
            elif x == "rock":
                print(
                    color("You try slapping your way through a boulder",
                          c.OKBLUE))
                input()
                print(color("Maybe try something smarter?", c.WARNING))
                input()
                break
            elif x == "win":
                maze.updatePlayer(y)
                run = False
                break
            else:
                maze.updatePlayer(y)
                break
        cost = randint(1, 3)
        print(f"You walk, draining {color(f'{cost} stamina', c.OKBLUE)}" +
              pause)
        input()
        player.stamina -= cost
        replit.clear()


def phase3():
    print("Get home." + pause)
    input()
    global player, maze
    maze.phase3()
    phase1()


if __name__ == "__main__":
    while True:
        musics.clear()
        try:
            musics.append(
                replit.audio.play_file("music/background.mp3",
                                       does_loop=True,
                                       loop_count=-1))
        except:
            print("music disabled")
        while True:
            replit.clear()
            print(
                'Welcome to the RPG retelling of the tale of Hansel and Gretel\n'
            )
            with open("textArt/titlePic.txt") as file:
                print(file.read())
            choose_char = input(
                color(
                    "\nDo you want to play as Hansel or Gretel? \n(Hansel/Gretel)> ",
                    c.HEADER)).title()
            if choose_char in ("Hansel", "Gretel"):
                break
            elif choose_char == "Kenny":
                print(
                    "\nHey! It seems that you are a cool kid. Here's a special gift, just for you: \n\nhttps://sites.google.com/ahschool.com/hanselandgretelvideogame/gallery/music/unused-songs\n"
                )
                input(
                    color("Please type in only 'Hansel' or 'Gretel'", c.FAIL) +
                    pause)
            else:
                input(
                    color("Please type in only 'Hansel' or 'Gretel'", c.FAIL) +
                    pause)

        player = Player(choose_char)
        maze = Maze()
        replit.clear()
        if (choose_char == "Hansel"):
            Hansel_POV_Background()
        else:
            Gretel_POV_Background()
        print("Stuck in the forest, you see a faint light in the shadows" +
              pause)
        input()
        phase1()
        if player.alive:
            if (choose_char == "Hansel"):
                result1 = Hansel_Act2()
                # result2 = Gretel_Act2()
                if (result1 == "Bad"):
                    player.alive = False
                    badEnd()
            else:
                result2 = Gretel_Act2()
                # if (result2 == "Neutral"):
                #   player.alive = False
                #   neutralEnd()
        else:
            player.alive = False
            badEnd()
        if player.alive:
            player.stamina += 30
            phase3()
        if player.alive:
            if (choose_char == "Hansel"):
                Hansel_Act3()
                trueEnd()
            if (choose_char == "Gretel"):
                if (result2 == "Good"):
                    Gretel_Act3_Good()
                    trueEnd()
                else:
                    Gretel_Act3_Neutral()
                    neutralEnd()

        input("Press enter to restart the game" + pause)
