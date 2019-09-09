
def final():
    if score1 < score2:
        injury1 = score1 / score2
        injury1percent = round(injury1 * 100)
        injury2percent = round(100 - injury1percent)
        print(injury1percent, "% can be attributed to injury 1 and", injury2percent,
                              "% can be attributed to injury 2")
    else:
        print("Score 2 must be greater than score 1 consider using a different method")


while True:
    try:
        score1 = int(input("What is the first DASH, NDI, Roland Morris or Oswestry Score?   "))
        break
    except ValueError:
        print("Make sure to enter a numerical value! ")
while True:
    try:
        score2 = int(input("What is the second DASH, NDI, Roland Morris or Oswestry Score?   "))
        break
    except ValueError:
        print("Make sure to enter a numerical value! ")


final()
