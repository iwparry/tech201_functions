# Creating a function that converts cm to m and m to ft
def cm_to_m(length) -> float:
    return length / 100      # formula for converting cm to m
def m_to_ft(length) -> float:
    return length * 3.281    # formula for converting m to ft (gives an approximate result)

print(cm_to_m(200))   # prints 2.0
print(m_to_ft(2))   # prints 6.562