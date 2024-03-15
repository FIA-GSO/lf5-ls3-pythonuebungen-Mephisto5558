from random import choice

ARUKONE_GAMES: list[list[list[int | None]]] = [
    [[]],
    [[[1]]],
    [[
        [1, 2],
        [2, 1]
    ],
        [
        [2, 1],
        [1, 2]
    ]],
    [[], []],
    [[], []],
    [[], []]
]

def wundertuete(w: int, k: int, g: int, amount: int) -> list[list[int]]:
  """
  - Gleiche Gesamtzahl an Spielen (nach Möglichkeit)
    - Maximalunterschied 1
  - Jede Spielsorte möglichst gleichmäßig verteilt
    - Maximalunterschied 1
  - Es darf nichts übrig bleiben.
  """

  wundertueten = [[w // amount, k // amount, g // amount] for _ in range(amount)]

  for i, e in enumerate([w, k, g]):
    while e % amount:
      choice([*filter(lambda sub_e: sub_e[i] <= e // amount, wundertueten)])[i] += 1
      e -= 1

  return wundertueten

def st_egano():
  """
  Fürs erste geskippt wegen dateiauslesung
  """

def arukone(n: int):
  """
  :param n >= 4
  Gittergröße n*n
  Mindestzahlanzahl n/2

  Darf sich nicht kreuzen
  muss immer 2 von jede zahl haben
  """

  game = [[] for _ in range(n)]

  for i in range(n / 2):
    """algo hier"""


if __name__ == '__main__':
  print(wundertuete(3, 4, 2, 3))
