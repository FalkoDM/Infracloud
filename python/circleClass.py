# de straal gegeven, geef de omtrek van een cirkel
# formule omtrek cirkel = pi * 2 * radius
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def omtrek(self):
        pi = 3.14
        omtrekValue = pi * 2 * self.radius
        return omtrekValue
    
    def printOmtrekValue(self):
        resultaatOmtrek = self.omtrek()
        print(f"de omtrek van een cirkel met straal {str(self.radius)} bedraagd {str(resultaatOmtrek)}")

# roep de class op en geef een waarde mee voor de radius
circle1 = Circle(2)
circle2 = Circle(5)
circle3 = Circle(7)

# roep de printfunctie op en geef het resultaat weer
circle1.printOmtrekValue()
circle2.printOmtrekValue()
circle3.printOmtrekValue()

