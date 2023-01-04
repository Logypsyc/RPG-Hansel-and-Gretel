from Colors import colors as c
from Colors import color, pause

class Player():
  def __init__(self, name):
    self.name = name
    self.stamina = 30
    self.alive = True
  
  def move(self):
    while True:
      answer = input(color("What direction do you move?\n(North/West/South/East)> ",c.HEADER)).title()
      if answer in ("North", "West", "East", "South"):
        break
      else:
        print(color("Please only type 'North', 'West', 'East', or 'South'", c.FAIL) + pause)
        input()
    return answer

  def display(self):
    print(color(
f"{self.name} Stamina: {self.stamina}", c.OKBLUE))