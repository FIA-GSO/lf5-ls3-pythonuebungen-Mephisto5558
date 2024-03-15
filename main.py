# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# ---------------------Aufgabe 1 ------------------------------------
def compute_r2d2_population(steps: int) -> tuple[int, int, int]:
  """
      Computes the r2d2 population for the given step amount
  :param steps: amount of steps to compute the population (e.g.: 5)
  :return: tuple of childs adults and old r2d2
  """

  r2_young = 10
  r2_adult = 10
  r2_old = 10

  for _ in range(steps):
    r2_newborns = int(r2_adult * 4 + r2_old * 2)
    r2_old = int(r2_adult / 3)
    r2_adult = int(r2_young / 2)
    r2_young = r2_newborns

  return (r2_young, r2_adult, r2_old)

# ---------------------Aufgabe 2 Streichholz------------------------------
# IMPLEMENT YOUR SOLUTION FOR THE STEICHHOLZSPIEL HERE
def nim_game():
  """Streichholzsspiel"""

  computer = 0
  player = 0
  turn = 0

  player_last_take = 0

  while computer + player < 31:
    if turn % 2 == 0:
      if turn == 0:
        print('Der Computer zieht 2.')
        computer += 2
      else:
        num = 7 - player_last_take % 7
        print(f'Der Computer zieht {num}.')
        computer += num
    else:
      num = max(1, min(31 - computer - player, 6, int(input(f'Nenne eine Zahl zwischen 1 und {min(6, 31 - computer - player)}: '))))
      print(f'Du ziehst {num}.')
      player_last_take = num
      player += num

    turn += 1
    print(f'Es liegen noch {31 - player - computer} Hölzer.')

  return 'computer' if turn % 2 else 'player'


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

  import math
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
  print(f'Der Gewinner ist {nim_game()}!')

  # Aufgabe 3
  print(
      f"Die Wurzel für die Fläche 25 und Grenze 0.01 nach Heron ist: {heron_verfahren(25, 0.01)}"
  )

  # Aufgabe 4
  # TO BE IMPLEMENTED

  # Use a breakpoint in the code line below to debug your script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
