



def questions():
    score1 = int(input("What is the first DASH, NDI, Roland Morris or Oswestry Score?   "))
    score2 = int(input("What is the second score?   "))
    injury1 = score1/score2
    injury1percent = round(injury1 * 100)
    injury2 = abs(round(injury1percent - 100))
    return print(injury1percent, "% can be attributed to injury 1 and", injury2, "% can be attributed to injury 2")

questions()