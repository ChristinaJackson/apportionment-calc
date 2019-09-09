
def residual():
    if prevremaining < estvisits:
        effects = round(prevremaining/estvisits * 100)
        print(effects, "% of the patient's residual effects were pre-existing from the first accident.")
    else:
        print("Score 2 must be greater than score 1 consider using a different method")


while True:
    try:
        prevremaining = int(input("How many visits were remaining on first treatment plan?  "))
        break
    except ValueError:
        print("Make sure to enter a numerical value! ")

while True:
    try:
        estvisits = int(input("How many visits are estimated to treat subsequent injury?  "))
        break
    except ValueError:
        print("Make sure to enter a numerical value! ")

residual()