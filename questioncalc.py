
score1 = (input("What is the first DASH, NDI, Roland Morris or Oswestry Score?   "))
try:
    score1 =int(score1)
except ValueError:
    print("Please enter a numerical value")
    exit()

score2 = (input("What is the second score?   "))
try:
    score2 =int(score2)
except ValueError:
    print("Please enter a numerical value")
    exit()

injury1percent = None
injury2percent = None


def questions(score1, score2):
    injury1 = score1/score2
    global injury1percent
    injury1percent = round(injury1 * 100)
    global injury2percent
    injury2percent = abs(round(injury1percent - 100))


if score1 < score2:
    questions(score1, score2)
    print(injury1percent, "% can be attributed to injury 1 and", injury2percent, "% can be attributed to injury 2")
else:
    print("Score 2 must be greater than score 1")
