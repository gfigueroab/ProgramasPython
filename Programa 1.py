print ("Welcome!")
cont = "yes"

while cont =="yes":
  g = input ("Guess the number: ")
  guess = int(g)
  if guess == 5:
      print("you win!")
  else:
      print("you lose!")
  if guess > 5:
      print("too high!")
  if guess < 5:
      print("too low!")

  cont = input ("you want restart?")

    
print("Game over")
