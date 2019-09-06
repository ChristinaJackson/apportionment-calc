
score1 = int(input("What is the first DASH, NDI, Roland Morris or Oswestry Score?   "))
score2 = int(input("What is the second score?   "))
injury1percent = None
injury2 = None


def questions(score1, score2):
    injury1 = score1/score2
    global injury1percent
    injury1percent = round(injury1 * 100)
    global injury2
    injury2 = abs(round(injury1percent - 100))


if score1 < score2:
    questions(score1, score2)
    print(injury1percent, "% can be attributed to injury 1 and", injury2, "% can be attributed to injury 2")
else:
    print("Not valid")
