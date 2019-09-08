

def questions(score1, score2):
    injury1 = score1/score2
    global injury1percent
    injury1percent = round(injury1 * 100)
    global injury2percent
    injury2percent = abs(round(injury1percent - 100))

def bothscores():
    score1 = 0
    score2 = 0
    while True:
        try:
            score1 = int(input("What is the first DASH, NDI, Roland Morris or Oswestry Score?   "))
            score2 = int(input("What is the second score?   "))
            if score1 < score2:
                questions(score1, score2)
                print(injury1percent, "% can be attributed to injury 1 and", injury2percent,
                      "% can be attributed to injury 2")
                break
            else:
                print("Score 2 must be greater than score 1 consider using a different method")
                break
        except ValueError:
            print("Make sure to enter a numerical value! ")

#loop returns to score one, instead score two... figure that out


bothscores()