def identify(*cube):
    if_missing = "Missing {}"
    row_num = 0
    Real_O = 0
    missing = False
    element_num = cube[0].count('O')
    for row in cube:
        current = 0
        row_num += 1
        for o in row:
            Real_O += 1
            current += 1
        if current != element_num:
            missing = True
    standard = row_num ** 2
    if row_num != element_num and missing == False:
        return "Non-full"
    elif missing == True:
        return if_missing.format(max(standard, Real_O) - min(standard, Real_O))
    else:
        return "Full"
    
    

print(identify(["O", "O"],
  ["O", "O", "O"],
  ["O", "O", "O"]))
