from ion import *
from kandinsky import *
from random import *
from time import *

for i in range(4):
  fill_rect(85, 35 + i * 50, 150, 2, (0, 0, 0))
  fill_rect(85 + i * 50, 35, 2, 150, (0, 0, 0))

tour = "x"
plateau = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
fin = False


def checkEnd():
  global plateau
  for forme in ["o", "x"]:
    for y in range(3):
      if plateau[y] == [forme] * 3:
        return forme
    for x in range(3):
      if [plateau[y][x] for y in range(3)] == [forme] * 3:
        return forme
    if [plateau[x][x] for x in range(3)] == [forme] * 3:
      return forme
    if [plateau[2 - x][x] for x in range(3)] == [forme] * 3:
      return forme
  return "."

while not fin:
  if tour == "o":
    x = 3
    for forme in ["o", "x"]:
      patterns = [[forme, forme, "."], [forme, ".", forme], [".", forme, forme]]
      for a in range(3):
        for b in range(3):
          if plateau[a] == patterns[b]:
            cases = [[2, a], [1, a], [0, a]]
            x, y = cases[b]
          elif [plateau[x][a] for x in range(3)] == patterns[b]:
            cases = [[a, 2], [a, 1], [a, 0]]
            x, y = cases[b]
      for b in range(3):
        if [plateau[x][x] for x in range(3)] == patterns[b]:
          cases = [[2, 2], [1, 1], [0, 0]]
          x, y = cases[b]
        elif [plateau[2 - x][x] for x in range(3)] == patterns[b]:
          cases = [[2, 0], [1, 1], [0, 2]]
          x, y = cases[b]
    if x == 3:
      x, y = randrange(0, 2), randrange(0, 2)
      while plateau[y][x] != ".":
        x, y = randrange(0, 2), randrange(0, 2)
  else:
    while True:
      x = 3
      touches = [30, 31, 32, 36, 37, 38, 42, 43, 44]
      xValeurs, yValeurs = [0, 1, 2] * 3, [0, 0, 0, 1, 1, 1, 2, 2, 2]
      for i in range(9):
        if keydown(touches[i]):
          x, y = xValeurs[i], yValeurs[i]
      if x != 3:
        break
  if plateau[y][x] != ".":
    continue
  elif tour == "x":
    plateau[y][x] = "x"
    fill_rect(105 + x * 50, 45 + y * 50, 10, 30, (0, 0, 0))
    fill_rect(95 + x * 50, 55 + y * 50, 30, 10, (0, 0, 0))
  else:
    plateau[y][x] = "o"
    fill_rect(95 + x * 50, 45 + y * 50, 30, 30, (0, 0, 0))
    fill_rect(105 + x * 50, 55 + y * 50, 10, 10, (255, 255, 255))
  if tour == "x":
    tour = "o"
  else:
    tour = "x"
  sleep(0.4)
  if checkEnd() == "o":
    draw_string("Vous avez perdu !", 80, 200)
    fin = True
  elif checkEnd() == "x":
    draw_string("Vous avez gagne !", 80, 200)
    fin = True
  rempli = True
  for ligne in plateau:
    if "." in ligne:
      rempli = False
  if rempli:
    draw_string("Egalite !", 115, 200)
    fin = True