

def residual():
    prevRemaining = int(input("How many visits were remaining on first treatment plan?  "))
    estVisits = int(input("How many visits are estimated to treat subsequent injury?  "))
    effects = round(prevRemaining/estVisits * 100)
    return print(effects, "% of the patient's residual effects were pre-existing from the first accident.")

residual()