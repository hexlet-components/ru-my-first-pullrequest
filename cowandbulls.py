from random import sample

class CowsBulls:
  symbols = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(48, 58)]
  def __init__(self, length=4):
    self.__length = length
    self.__word = sample(self.symbols, self.__length)

  def change_word(self, length=4):
    self.__length = length
    self.__word = sample(self.symbols, length)

  def play(self):
    print(f"Game started\nIf you want to give up, type '!'")
    while 1:
      player_word = input()
      if player_word == '!':
        print(f'Hidden word: {"".join(self.__word)}')
        break
      if len(player_word) != self.__length:
        print(f'Word length should be {self.__length}\n')
        continue
      cows = self.__find_cows(player_word)
      bulls = self.__find_bulls(player_word)
      cows -= bulls
      if bulls == self.__length:
        print(f'Successfully!\nHidden word: {"".join(self.__word)}')
        break
      else:
        print(f'Cows: {cows}\nBulls: {bulls}\n')

  def __find_cows(self, player_word):
    cows = 0
    for c in player_word:
      cows += [0, 1][c in self.__word]
    return cows

  def __find_bulls(self, player_word):
    bulls = 0
    for i in range(self.__length):
      if player_word[i] == self.__word[i]:
        bulls += 1
    return bulls


game = CowsBulls()
game.play()