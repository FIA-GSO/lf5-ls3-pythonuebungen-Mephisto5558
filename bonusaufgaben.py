from random import choice
from PIL import Image  # pip install Pillow

ARUKONE_GAMES: list[list[list[list[int | None]]]] = [
    [[
        []
    ]],
    [[
        []
    ]],
    [[
        [1, None],
        [None, 1]
    ], [
        [None, 1],
        [1, None]
    ]],
    [[
        [1, None, 2],
        [None, 2, None],
        [1, None, None]
    ], [
        [None, 1, None],
        [2, None, None],
        [None, 2, 1]
    ]],
    [[
        [1, 3, None, 2],
        [None, 3, None, None],
        [None, 2, None, 1],
        [None, None, None, None]
    ], [
        [None, 2, None, None],
        [1, None, None, 3],
        [None, 1, None, None],
        [2, None, None, 3]
    ]]
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

def st_egano(filepath: str):
  """
  Fürs erste geskipped wegen dateiauslesung
  start pixel oben links -> (r, g b)
  r=ascii des 1. Zeichen der msg
  g=pixel nach rechts für nächsten Buchstaben
  b=pixel nach unten für nächsten Buchstaben
  wenn bei rechtsbewegung am rechten bildrand, in der selben Zeile von vorn beginnen, ebenso bei unten
  zielpixel: g=0, b=0
  """

  image = Image.open(filepath, mode='r')
  pixels = image.load()

  x = 0
  y = 0
  text = ''

  while True:  # Exits when g and b are 0
    r, g, b, *_ = pixels[x, y]  # rgb(a)
    text += chr(r)

    if g == 0 and b == 0: break

    x = (x + g) % image.width
    y = (y + b) % image.height

  return text

def arukone(n: int):
  """
  :param n >= 4
  Gittergröße n*n
  Mindestzahlanzahl n/2

  Darf sich nicht kreuzen
  muss immer 2 von jede zahl haben
  """

  game = choice(ARUKONE_GAMES[n])


if __name__ == '__main__':
  # print(wundertuete(3, 4, 2, 3))

  for i in range(1, 7):
    for e in ('png', 'ppm', 'tiff'):
      print(f'bild0{i}.{e}: ', st_egano(f'./St. Egano/bild0{i}.{e}'), '\n')
