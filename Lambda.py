
#Lambda square of number
square_of_number = lambda z: z**2
print(F'SQUARE: {square_of_number(20)}')


#Lambda quadratic equation: y = 3*(X**2) + 4*X + 5
quad = lambda X: 3*(X**2) + 4*X + 5
print(f'QUAD: {quad(3)}')

welcome = lambda fName, sName: f'You are welcome Mr {fName} {sName}'
print(welcome("Ibrahim", "Suleiman"))