# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

# ---------------------Aufgabe 1 ------------------------------------
def compute_r2d2_population(steps: int, r2_young: int = 10, r2_adult: int = 10, r2_old: int = 10) -> tuple[int, int, int]:
  """
      Computes the r2d2 population for the given step amount:
        First, they reproduce, then they age.
      - every 2nd young r2d2's becomes adult (rest dies)
      - every adult creates 4 young ones
      - every senior creates 2 young ones
      - every 3rd adult becomes senior (rest dies)
      - seniors die

  :param steps: amount of steps to compute the population (e.g.: 5)
  :param r2_young: start amount of young r2d2, default: 10
  :param r2_adult: start amount of adult r2d2, default: 10
  :param r2_old: start amount of old r2d2, default: 10

  :return: tuple of childs, adults and old r2d2
  """

  for _ in range(steps):
    r2_newborns = math.floor(r2_adult * 4 + r2_old * 2)  # newborns don't age in the same step
    r2_old = r2_adult // 3
    r2_adult = r2_young // 2
    r2_young = r2_newborns

  return r2_young, r2_adult, r2_old

# ---------------------Aufgabe 2 Streichholz------------------------------
def nim_game(matches: int = 31, max_per_turn: int = 6):
  """
  Play a game with a configurable max amount of turns
  Taking more then `max_per_turn` is not allowed.

  :param matches: amount of matches, default: 31
  :param max_per_turn: amount of matches allowed to be taken each turn, default: 6

  :return: the winner's name
  """

  turn = 0
  last_take = 0

  while matches > 0:
    if turn % 2:  # Player's turn
      # Not less than 1, not more than `max_per_turn`, not more than available
      last_take = max(1, min(max_per_turn, matches, int(input(f'Nenne eine Zahl zwischen 1 und {min(max_per_turn, matches)}: '))))
      print(f'Du ziehst {last_take}.')
    elif turn:  # Computer's turn
      last_take = max_per_turn + 1 - last_take
      print(f'Der Computer zieht {last_take}.')
    else:  # Computer's first turn
      last_take = 2
      print('Der Computer zieht 2.')

    matches -= last_take
    turn += 1
    print(f'Es liegen noch {matches} Hölzer.')

  return 'player' if turn % 2 else 'computer'


# ---------------------Aufgabe 3 Heron ------------------------------------
def heron_verfahren(area: float, threshold: float) -> float:
  """
      computes the square root using the heron method
  :param area: size of the area e.g.25
  :param threshold: threshold for the heron method e.g. 0.01
  :return:the square root of the given area according to the heron method
  """

  a = area
  b = 1

  mittelwert = (a + b) / 2
  abweichung = a - b

  while abweichung**2 >= threshold:
    a = mittelwert
    b = area / a
    abweichung = a - b
    mittelwert = (a + b) / 2

  return mittelwert


# ---------------------Aufgabe 4 Quersumme------------------------------
# IMPLEMENT, IF NECESSARY, EXERCISE 4 HERE BUT USE A FUNCTION!
def sqrt(a: int) -> float:
  """SQRT"""
  return math.sqrt(a)

# ---------------MANAGEMENT----------------------
# -------------COMMENT/UNCOMMENT lines to launch the different exercises
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  print("You need to adjust this code to run your implementation")

  # Aufgabe 1
  print(f"""
      # R2D2 Population after 5 steps is:
      # Young: {compute_r2d2_population(5)[0]}
      # Adults: {compute_r2d2_population(5)[1]}
      # Old: {compute_r2d2_population(5)[2]}""")
  # print (compute_r2d2_population(5))

  # Aufgabe 2
  # TO BE IMPLEMENTED
  print(f'Der Gewinner ist {nim_game()}, denn der andere musste das letzte Hölzchen nehmen!')

  # Aufgabe 3
  print(
      f"Die Wurzel für die Fläche 25 und Grenze 0.01 nach Heron ist: {heron_verfahren(25, 0.01)}"
  )

  # Aufgabe 4
  # TO BE IMPLEMENTED

  # Use a breakpoint in the code line below to debug your script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
