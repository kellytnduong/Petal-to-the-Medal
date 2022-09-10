import random
from graphics import *
from button import Button
from replit import audio
import time

#Starting Page
def start():
  start = GraphWin("HANGMAN HOME",500,500)
  start.setCoords(-10,-10,10,10)
  menu = Image(Point(0,0),"graphics/menu.png")
  menu.draw(start)
  return (start,menu)

#Information and Rules Page
def infoRules():
  info = GraphWin("HANGMAN HOME",500,500)
  info.setCoords(-10,-10,10,10)
  infoImage = Image(Point(0,0),"graphics/info.png")
  infoImage.draw(info)
  closebutton = Button(info,Point(8.7,8.7),1.4,1.4, "X")
  closebutton.activate() 
  flag = True
  while flag == True:
    userSelect = info.getMouse()
    if closebutton.clicked(userSelect):
      info.close()
      flag = False
      
#Category Selection on the Starting Page
def categorySelect(start, menu):
  pokemonbutton = Button(start,Point(-4,-0.5),5.2,3.2, " ")
  pokemonbutton.activate()
  pokemon = Image(Point(-4,-0.5),"graphics/pokemonbutton.png")
  pokemon.draw(start)
  booksbutton = Button(start,Point(4,-0.5),5.2,3.2, " ")
  booksbutton.activate()
  books = Image(Point(4,-0.5),"graphics/booksbutton.png")
  books.draw(start)
  foodbutton = Button(start,Point(-4,-5.5),5.2, 3.2," ")
  foodbutton.activate()
  food = Image(Point(-4,-5.5),"graphics/foodbutton.png")
  food.draw(start)
  idiomsbutton = Button(start,Point(4,-5.5),5.2,3.2," ")
  idiomsbutton.activate()
  idioms = Image(Point(4,-5.5),"graphics/idiomsbutton.png")
  idioms.draw(start)
  infobutton = Button(start,Point(8.7,8.7),2,2,"X")
  infobutton.activate()
  info = Image(Point(8.7,8.7),"graphics/infobutton.png")
  info.draw(start)
  flag = True
  while flag == True:
    userSelect = start.getMouse()
    if pokemonbutton.clicked(userSelect):
      filename = "categories/pokemon.txt"
      flag = False
    elif booksbutton.clicked(userSelect):
      filename = "categories/books.txt"
      flag = False
    elif foodbutton.clicked(userSelect):
      filename = "categories/food.txt"
      flag = False
    elif idiomsbutton.clicked(userSelect):
      filename = "categories/idioms.txt"
      flag = False
    elif infobutton.clicked(userSelect):
      infoRules()
  pokemonbutton.deactivate()
  booksbutton.deactivate()
  foodbutton.deactivate()
  idiomsbutton.deactivate()
  menu.undraw()
  return(filename)

#Difficulty Selection on the Starting Page
def difficultySelect(start):
  menu2 = Image(Point(0,0),"graphics/menu2.png")
  menu2.draw(start)
  easybutton = Button(start,Point(0,4.2),5,2," ")
  easybutton.activate()
  easy = Image(Point(0,4.2),"graphics/easy.png")
  easy.draw(start)
  mediumbutton = Button(start,Point(0,0),5,2," ")
  mediumbutton.activate()
  medium = Image(Point(0,0),"graphics/medium.png")
  medium.draw(start)
  hardbutton = Button(start,Point(0,-4.2),5,2," ")
  hardbutton.activate()
  hard = Image(Point(0,-4.2),"graphics/hard.png")
  hard.draw(start)
  infobutton = Button(start,Point(8.7,8.7),2,2,"X")
  infobutton.activate()
  info = Image(Point(8.7,8.7),"graphics/infobutton.png")
  info.draw(start)
  flag = True
  while flag == True:
    userSelect = start.getMouse()
    if easybutton.clicked(userSelect):
      difficulty = "easy"
      flag = False
    elif mediumbutton.clicked(userSelect):
      difficulty = "medium"
      flag = False
    elif hardbutton.clicked(userSelect):
      difficulty = "hard"
      flag = False
    elif infobutton.clicked(userSelect):
      infoRules()  
  easybutton.deactivate()
  mediumbutton.deactivate()
  hardbutton.deactivate()
  start.close()
  return(difficulty)

#Hangman Gameplay Page
def play():
  play = GraphWin("HANGMAN PLAY",500,500)
  play.setCoords(-10,-10,10,10)
  play.setBackground("lightcyan2")
  grass = Rectangle(Point(-11,-11),Point(11,-7.7))
  grass.setFill(color_rgb(113,198,113))
  grass.setOutline(color_rgb(113,198,113))
  grass.draw(play)
  hellokitty = Image(Point(5,-5),"graphics/hellokitty.png")
  hellokitty.draw(play)
  return(play)

#Keyboard and Keys using Button Class
def keyboard(play):
  key1 = Button(play,Point(-9,4),1.25,1.25,"A")
  key1.activate()
  key2 = Button(play,Point(-7.5,4),1.25,1.25,"B")
  key2.activate()
  key3 = Button(play,Point(-6, 4),1.25,1.25,"C")
  key3.activate()
  key4 = Button(play,Point(-4.5,4),1.25,1.25,"D")
  key4.activate()
  key5 = Button(play,Point(-3,4),1.25,1.25,"E")
  key5.activate()
  key6 = Button(play,Point(-1.5,4),1.25,1.25,"F")
  key6.activate()
  key7 = Button(play,Point(0,4),1.25,1.25,"G")
  key7.activate()
  key8 = Button(play,Point(1.5,4),1.25,1.25,"H")
  key8.activate()
  key9 = Button(play,Point(3,4),1.25,1.25,"I")
  key9.activate()
  key10 = Button(play,Point(4.5,4),1.25,1.25,"J")
  key10.activate()
  key11 = Button(play,Point(6,4),1.25,1.25,"K")
  key11.activate()
  key12 = Button(play,Point(7.5,4),1.25,1.25,"L")
  key12.activate()
  key13 = Button(play,Point(9,4),1.25,1.25,"M")
  key13.activate()
  key14 = Button(play,Point(-9,2.5),1.25,1.25,"N")
  key14.activate()
  key15 = Button(play,Point(-7.5,2.5),1.25,1.25,"O")
  key15.activate()
  key16 = Button(play,Point(-6,2.5),1.25,1.25,"P")
  key16.activate()
  key17 = Button(play,Point(-4.5,2.5),1.25,1.25,"Q")
  key17.activate()
  key18 = Button(play,Point(-3,2.5),1.25,1.25,"R")
  key18.activate()
  key19 = Button(play,Point(-1.5,2.5),1.25,1.25,"S")
  key19.activate()
  key20 = Button(play,Point(0,2.5),1.25,1.25,"T")
  key20.activate()
  key21 = Button(play,Point(1.5,2.5),1.25,1.25,"U")
  key21.activate()
  key22 = Button(play,Point(3,2.5),1.25,1.25,"V")
  key22.activate()
  key23 = Button(play,Point(4.5,2.5),1.25,1.25,"W")
  key23.activate()
  key24 = Button(play,Point(6,2.5),1.25,1.25,"X")
  key24.activate()
  key25 = Button(play,Point(7.5, 2.5),1.25,1.25,"Y")
  key25.activate()
  key26 = Button(play,Point(9, 2.5),1.25,1.25,"Z")
  key26.activate()
  buttonList = [key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,key11,key12,key13,key14,key15,key16,key17,key18,key19,key20,key21,key22,key23,key24,key25,key26]
  return (buttonList)

#Guess Selection and Graphics using Keyboard
def keySelect(buttonList,play):
  flag = True
  while flag == True:
    userSelect = play.getMouse()
    for i in range(26):
      if buttonList[i].clicked(userSelect):
        userInput = buttonList[i].getLabel()
        buttonList[i].deactivate()
        flag = False
  return (userInput)

#Picks Random Words for the User to Guess
def getWord(filename):
  file = open(filename, "r")
  contents = file.readlines()
  content = random.choices(contents)
  word = content[0]
  file.close()
  return (word)

#Makes a Puzzle of Asterixes the Represent the Mystery Words
def makePuzzle(word):
  alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  puzz = []
  for letter in word:
    if alpha.find(letter) >= 0:
      puzz.append("*")
    else:
      puzz.append(letter)
  puzzle = puzz[:len(puzz) - 1]
  return(puzzle)
#Checks the Validity of a Guess (Whether or not the Guess is Found in the Word(s))
def isIn(guess,word,puzzle):
  bool = False
  for i in range(len(word)):
    if word[i].lower() == guess.lower():
      pos = word[i]
      puzzle[i] = pos
      bool = True
  return(bool)

#Executes the mechanics of the game. Runs the user-specified difficulty by directing to each mode's respective functions and handles the change in display (text, flower graphics, etc.).
def runGame(buttonList,filename,play,difficulty):
  word = getWord(filename)
  puzzle = makePuzzle(word)
  letterList = []
  errors = 0
  puzzleText = ("{0}".format("".join(puzzle)))
  text = Text(Point(0,7), puzzleText)
  text.setSize(13)
  text.setFill(color_rgb(237,73,151))
  text.draw(play)
  if difficulty == "easy":
    limit = 7
    flower = Image(Point(-2,-3.5), "flowers/easy/1.png")
    flower.draw(play)
  elif difficulty == "medium":
    limit = 5
    flower = Image(Point(-2,-3.5), "flowers/medium/1.png")
    flower.draw(play)
  elif difficulty == "hard":
    limit = 3
    flower = Image(Point(-2,-3.5), "flowers/hard/1.png")
    flower.draw(play)
  word = word[:len(word)-1]
  while ("".join(puzzle) != word) and errors <= limit:
    guess = keySelect(buttonList,play)
    letterList.append(guess)

    bool = isIn(guess,word,puzzle)
    if bool == False:
      errors += 1
      if limit == 7:
        petalList = easyFlowers()
        flower.undraw()
        flower = easyErrors(errors,play,puzzle,petalList)
        flower.draw(play)

      elif limit == 5:
        petalList = mediumFlowers()
        flower.undraw()
        flower = mediumErrors(errors,play,puzzle,petalList)
        flower.draw(play)

      elif limit == 3:
        petalList = hardFlowers()
        flower.undraw()
        flower = hardErrors(errors,play,puzzle,petalList)
        flower.draw(play)
    text.setText("".join(puzzle))
  play.close()
  if ("".join(puzzle) == word):
    return (True, word)
  else:
    return (False, word)
    
#The Easy-Mode Flower Petal Animation Files
def easyFlowers():
#petal fall 1
  petal1 = Image(Point(-2, -3.7), "flowers/easy/2.png")
  petal2 = Image(Point(-2, -3.7), "flowers/easy/3.png")
  petal3 = Image(Point(-2, -3.7), "flowers/easy/4.png")
  petal4 = Image(Point(-2, -3.7), "flowers/easy/5.png")
#petal fall 2
  petal5 = Image(Point(-2, -3.7), "flowers/easy/6.png")
  petal6 = Image(Point(-2, -3.7), "flowers/easy/7.png")
  petal7 = Image(Point(-2, -3.7), "flowers/easy/8.png")
  petal8 = Image(Point(-2, -3.7), "flowers/easy/9.png")
#petal fall 3
  petal9 = Image(Point(-2, -3.7), "flowers/easy/10.png")
  petal10 = Image(Point(-2, -3.7), "flowers/easy/11.png")
  petal11 = Image(Point(-2, -3.7), "flowers/easy/12.png")
  petal12 = Image(Point(-2, -3.7), "flowers/easy/13.png")
#petal fall 4
  petal13 = Image(Point(-2, -3.7), "flowers/easy/14.png")
  petal14 = Image(Point(-2, -3.7), "flowers/easy/15.png")
  petal15 = Image(Point(-2, -3.7), "flowers/easy/16.png")
  petal16 = Image(Point(-2, -3.7), "flowers/easy/17.png")
#petal fall 5  
  petal17 = Image(Point(-2, -3.7), "flowers/easy/18.png")
  petal18 = Image(Point(-2, -3.7), "flowers/easy/19.png")
  petal19 = Image(Point(-2, -3.7), "flowers/easy/20.png")
  petal20 = Image(Point(-2, -3.7), "flowers/easy/21.png")
#petal fall 6
  petal21 = Image(Point(-2, -3.7), "flowers/easy/22.png")
  petal22 = Image(Point(-2, -3.7), "flowers/easy/23.png")
  petal23 = Image(Point(-2, -3.7), "flowers/easy/24.png")
  petal24 = Image(Point(-2, -3.7), "flowers/easy/25.png")
#petal fall 7  
  petal25 = Image(Point(-2, -3.7), "flowers/easy/26.png")
  petal26 = Image(Point(-2, -3.7), "flowers/easy/27.png")
  petal27 = Image(Point(-2, -3.7), "flowers/easy/28.png")
  petal28 = Image(Point(-2, -3.7), "flowers/easy/29.png")
  petals = [petal1, petal2, petal3, petal4, petal5, petal6, petal7, petal8, petal9,
        petal10, petal11, petal12, petal13, petal14, petal15, petal16, petal17,
        petal18, petal19, petal20, petal21, petal22, petal23,petal24,petal25,petal26,petal27,petal28]
  return (petals)

#The Easy-Mode Animation of the Flower Petals
def easyErrors(errors, play, puzzle, petalList):
  if errors == 1:
    for i in range(3):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[3]
    
  elif errors == 2:
    for i in range(4, 8):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[7]
    
  elif errors == 3:
    for i in range(8, 11):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[11]
    
  elif errors == 4:
    for i in range(12, 15):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[15]
    
  elif errors == 5:
    for i in range(16, 19):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[19]
    
  elif errors == 6:
    for i in range(20, 23):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[23]
    
  elif errors == 7:
    for i in range(24, 27):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()  
    petal = petalList[27]    
    mess = Image(Point(0, 0), "graphics/mess.png")
    background = Image(Point(0, 0), "graphics/background.png")
    for i in range(2):
      mess.draw(play)
      time.sleep(0.5)
      mess.undraw()
      background.draw(play)
      time.sleep(0.5)
      background.undraw()
      
  else:
    petal = petalList[27]
  return(petal)

#The Medium-Mode Flower Petal Animation Files
def mediumFlowers():
#petal fall 1
  petal1 = Image(Point(-2, -3.43), "flowers/medium/2.png")
  petal2 = Image(Point(-2, -3.43), "flowers/medium/3.png")
  petal3 = Image(Point(-2, -3.53), "flowers/medium/4.png")
  petal4 = Image(Point(-2, -3.43), "flowers/medium/5.png")
#petal fall 2
  petal5 = Image(Point(-2, -3.5), "flowers/medium/6.png")
  petal6 = Image(Point(-2, -3.6), "flowers/medium/7.png")
  petal7 = Image(Point(-2, -3.7), "flowers/medium/8.png")
  petal8 = Image(Point(-2, -3.7), "flowers/medium/9.png")
#petal fall 3
  petal9 = Image(Point(-2, -3.8), "flowers/medium/10.png")
  petal10 = Image(Point(-2, -4.3), "flowers/medium/11.png")
  petal11 = Image(Point(-2, -4.3), "flowers/medium/12.png")
  petal12 = Image(Point(-2, -4.35), "flowers/medium/13.png")
#petal fall 4
  petal13 = Image(Point(-2, -3.8), "flowers/medium/14.png")
  petal14 = Image(Point(-2, -3.8), "flowers/medium/15.png")
  petal15 = Image(Point(-2, -4.4), "flowers/medium/16.png")
  petal16 = Image(Point(-2, -4.4), "flowers/medium/17.png")
  petal17 = Image(Point(-2, -4.4), "flowers/medium/18.png")
#petal fall 5
  petal18 = Image(Point(-2, -4.3), "flowers/medium/19.png")
  petal19 = Image(Point(-2, -4.3), "flowers/medium/20.png")
  petal20 = Image(Point(-2, -4.5), "flowers/medium/21.png")
  petal21 = Image(Point(-2, -4.5), "flowers/medium/22.png")
  petals = [petal1, petal2, petal3, petal4, petal5, petal6, petal7, petal8, petal9, petal10, petal11, petal12, petal13, petal14, petal15, petal16, petal17, petal18, petal19, petal20, petal21]
  return (petals)
  
#The Medium-Mode Animation of the Flower Petals
def mediumErrors(errors, play, puzzle, petalList):
  if errors == 1:
    for i in range(3):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[3]
    
  elif errors == 2:
    for i in range(4, 7):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[7]
    
  elif errors == 3:
    for i in range(8, 11):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[11]
    
  elif errors == 4:
    for i in range(12, 16):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[16]
    
  elif errors == 5:
    for i in range(17, 20):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[20]
    mess = Image(Point(0, 0), "graphics/mess.png")
    background = Image(Point(0, 0), "graphics/background.png")
    for i in range(2):
      mess.draw(play)
      time.sleep(0.5)
      mess.undraw()
      background.draw(play)
      time.sleep(0.5)
      background.undraw()
      
  else:
    petal = petalList[20]
  return(petal)

#The Hard-Mode Flower Petal Animation Files
def hardFlowers():
#petal fall 1
  petal1 = Image(Point(-2, -3.43), "flowers/hard/2.png")
  petal2 = Image(Point(-2, -3.43), "flowers/hard/3.png")
  petal3 = Image(Point(-2, -3.53), "flowers/hard/4.png")
  petal4 = Image(Point(-2, -3.43), "flowers/hard/5.png")
#petal fall 2
  petal5 = Image(Point(-2, -3.5), "flowers/hard/6.png")
  petal6 = Image(Point(-2, -3.6), "flowers/hard/7.png")
  petal7 = Image(Point(-2, -3.7), "flowers/hard/8.png")
  petal8 = Image(Point(-2, -3.7), "flowers/hard/9.png")
#petal fall 3
  petal9 = Image(Point(-2, -3.8), "flowers/hard/10.png")
  petal10 = Image(Point(-2, -4.3), "flowers/hard/11.png")
  petal11 = Image(Point(-2, -4.3), "flowers/hard/12.png")
  petal12 = Image(Point(-2, -4.35), "flowers/hard/13.png")
  petals = [petal1, petal2, petal3, petal4, petal5, petal6, petal7, petal8, petal9, petal10, petal11, petal12]
  return (petals)
  
#The Hard-Mode Animation of the Flower Petals
def hardErrors(errors, play, puzzle, petalList):
  if errors == 1:
    for i in range(3):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[3]
    
  elif errors == 2:
    for i in range(4, 7):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[7]
    
  elif errors == 3:
    for i in range(8, 11):
      petalList[i].draw(play)
      time.sleep(0.1)
      petalList[i].undraw()
    petal = petalList[11]
    mess = Image(Point(0, 0), "graphics/mess.png")
    background = Image(Point(0, 0), "graphics/background.png")
    for i in range(2):
      mess.draw(play)
      time.sleep(0.5)
      mess.undraw()
      background.draw(play)
      time.sleep(0.5)
      background.undraw()
      
  else:
    petal = petalList[11]
  return(petal)

#The Flower Regrowing Animation that Appears on the Losing Page
def flowerGrow(lose, grow1):
  wateringcan = Image(Point(0.6, -6), "graphics/wateringcan.png")
  wateringcan.draw(lose)
  time.sleep(0.5)
  grow1.undraw()
  grow2 = Image(Point(-1, -4.1), "flowers/lose/23.png")
  grow2.draw(lose)
  time.sleep(0.5)
  grow2.undraw()
  grow3 = Image(Point(-1, -3.7), "flowers/lose/24.png")
  grow3.draw(lose)
  time.sleep(0.5)
  grow3.undraw()
  grow4 = Image(Point(-1, -2.6), "flowers/lose/25.png")
  grow4.draw(lose)
  time.sleep(0.5)
  grow4.undraw()
  grow5 = Image(Point(-1, -3.4), "flowers/lose/26.png")
  grow5.draw(lose)
  time.sleep(0.5)
  grow5.undraw()
  grow6 = Image(Point(-1, -3.4), "flowers/lose/27.png")
  grow6.draw(lose)
  time.sleep(0.5)
  grow6.undraw()
  grow7 = Image(Point(-1, -3.5), "flowers/medium/1.png")
  grow7.draw(lose)
  wateringcan.undraw()


#Winning Page
def win(word):
  win = GraphWin("YAY! YOU WIN!", 500, 500)
  win.setCoords(-10, -10, 10, 10)
  winGraphic = Image(Point(0, 0), "graphics/win.png")
  winGraphic.draw(win)
  againbutton = Button(win, Point(4, -2), 8, 3, " ")
  againbutton.activate()
  playagain = Image(Point(4, -2), "graphics/playagain.png")
  playagain.draw(win)
  quitbutton = Button(win, Point(4, -7), 8, 3, " ")
  quitbutton.activate()
  quit = Image(Point(4, -7), "graphics/quit.png")
  quit.draw(win)
  
  wordmess = Text(Point(0, 3.2), word)
  wordmess.setFill(color_rgb(237, 73, 151))
  wordmess.setSize(13)
  wordmess.draw(win)  
  
  flag = False
  userSelect = win.getMouse()
  while flag == False:
    if againbutton.clicked(userSelect):
      restart = True
      flag = True
    elif quitbutton.clicked(userSelect):
      restart = False 
      flag = True
  win.close()
  return(restart)


#Losing Page
def lose(word):
  lose = GraphWin("BETTER LUCK NEXT TIME!", 500, 500)
  lose.setCoords(-10, -10, 10, 10)
  lose.setBackground("lightcyan2")
  grass = Rectangle(Point(-11, -11), Point(11, -7.7))
  grass.setFill(color_rgb(113, 198, 113))
  grass.setOutline(color_rgb(113, 198, 113))
  grass.draw(lose)
  wordmess = Image(Point(0, 6.8), "graphics/puzzlemess.png")
  wordmess.draw(lose)
  wordmess2 = Text(Point(0, 5.6), word)
  wordmess2.setFill(color_rgb(237, 73, 151))
  wordmess2.setSize(13)
  wordmess2.draw(lose)
  grow1 = Image(Point(-1, -4.2), "flowers/medium/22.png")
  grow1.draw(lose)
  regrow = Button(lose, Point(2, -5), 0.78, 0.6, " ")
  regrow.activate()
  growmess = Image(Point(4, 1), "graphics/growmess.png")
  growmess.draw(lose)
  hellokitty = Image(Point(4, -5), "graphics/hellokitty.png")
  hellokitty.draw(lose)
  flag = True
  while flag == True:
    userSelect = lose.getMouse()
    if regrow.clicked(userSelect):
      growmess.undraw()
      flowerGrow(lose, grow1)
      flag = False
  againbutton = Button(lose, Point(-5, 6), 8, 3, "PLAY AGAIN")
  againbutton.activate()
  playagain = Image(Point(-5, 6), "graphics/playagain.png")
  playagain.draw(lose)
  quitbutton = Button(lose, Point(5, 6), 8, 3, "QUIT")
  quitbutton.activate()
  quit = Image(Point(5, 6), "graphics/quit.png")
  quit.draw(lose)
  wordmess.undraw()
  wordmess2.undraw()
  userSelect2 = lose.getMouse()
  while flag == False:
    if againbutton.clicked(userSelect2):
      restart = True
      flag = True
    elif quitbutton.clicked(userSelect2):
      restart = False 
      flag = True
  lose.close()
  return(restart)

#Main Caller Function that Puts Every Function Together.
def main():
  flag = True
  while flag == True:
    music = audio.play_file("hellokittytheme.mp3")
    start2, menu2 = start()
    filename = categorySelect(start2, menu2)
    difficulty = difficultySelect(start2)
    play2 = play()
    buttonList = keyboard(play2)
    result, word = runGame(buttonList, filename, play2, difficulty)
    if result == True:
      reset = win(word)
    elif result == False:
      reset = lose(word)
    if reset == False:
      flag = False
    music.set_paused(True)
      
main()