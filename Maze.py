from random import random

class Maze:
  def __init__(self, size = 9):
    self.size = size
    self.map = []
    self.player_pos = [int(size/2), int(size/2)]
    self.randomize()

  def randomize(self):
    enemy_num = 8
    tree_num = 5
    boulder_num = 5
    bush_num = 20
    self.map = []
    for y in range(self.size):
      self.map.append([])
      for x in range(self.size):
        seed = random()
        if seed < enemy_num / self.size ** 2:
          self.map[-1].append("e")
        elif seed < (enemy_num + tree_num) / self.size ** 2:
          self.map[-1].append("t")
        elif seed < (enemy_num + tree_num + boulder_num) / self.size ** 2:
          self.map[-1].append("r")
        elif seed < (enemy_num + tree_num + boulder_num + bush_num) / self.size ** 2:
          self.map[-1].append("b")
        else:
          self.map[-1].append("*")
    self.player_pos = [int(self.size/2), int(self.size/2)]
    self.map[self.player_pos[0]][self.player_pos[1]] = "o"    
    target = ((self.size - 3)  * round(random()) + 1, (self.size - 3) * round(random()) + 1)
    self.map[target[0]][target[1]] = "x"
    self.map[target[0]][target[1] + 1] = "*"
    self.map[target[0]][target[1] - 1] = "*"
    self.map[target[0] + 1][target[1]] = "*"
    #self.map[target[0] + 1][target[1] + 1] = "*"
    #self.map[target[0] + 1][target[1] - 1] = "*"
    self.map[target[0] - 1][target[1]] = "*"
    #self.map[target[0] - 1][target[1] + 1] = "*"
    #self.map[target[0] - 1][target[1] - 1] = "*"
  
  def move(self, direction):
    if direction == "North":
      return self.checkPlayer((self.player_pos[0] - 1, self.player_pos[1])), (self.player_pos[0] - 1, self.player_pos[1])
    elif direction == "West":
      return self.checkPlayer((self.player_pos[0], self.player_pos[1] - 1)), (self.player_pos[0], self.player_pos[1] - 1)
    elif direction == "East":
      return self.checkPlayer((self.player_pos[0], self.player_pos[1] + 1)), (self.player_pos[0], self.player_pos[1] + 1)
    elif direction == "South":
      return self.checkPlayer((self.player_pos[0] + 1, self.player_pos[1])), (self.player_pos[0] + 1, self.player_pos[1])
    

  def checkPlayer(self, pos):
    if pos[0] > self.size or pos[0] < 0 or pos[1] > self.size or pos[1] < 0:
      return "out"
    else:
      target = self.map[pos[0]][pos[1]]
      if target == "e":
        return "died"
      elif target == "t":
        return "tree"
      elif target == "r":
        return "rock"
      elif target == "b":
        return "bush"
      elif target == "x":
        return "win"
      else: 
        return "ok"

  def phase3(self):
    self.map[int(self.size/2)][int(self.size/2)] = "x"
  def updatePlayer(self, pos):
    self.map[pos[0]][pos[1]] = "o"
    self.map[self.player_pos[0]][self.player_pos[1]] = "*"
    self.player_pos = pos
    
  def legend(self):
    print("""🗺️
Legend:
  ⬜ = Border
  😈 = Enemy
  🌳 = Tree
  ⛰️ = Boulder
  🌿 = Bush
  ⬛ = Empty
  ❌ = Target
  🧒 = Player

Compass:
    North
West <*> East
    South
""")

  def display(self):
    print((self.size + 2)* "⬜ ")
    for y in self.map:
      print("⬜", end=" ")
      for x in y:
        if x == "e":
          print("😈", end=" ")
        elif x == "t":
          print("🌳", end=" ")
        elif x == "r":
          print("⛰️", end="  ")
        elif x == "b":
          print("🌿", end=" ")
        elif x == "*":
          print("⬛", end=" ")
        elif x == "x":
          print("❌", end=" ")
        elif x == "o":
          print("🧒", end=" ")
      print("⬜")
    print((self.size + 2)* "⬜ ")

