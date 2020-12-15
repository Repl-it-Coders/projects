# The main file
class MyLang:
    def __init__(self):
        # Left, right and the operator
        self.left = self.right = ""
        self.op = ""
        self.pos = 0 # Current position

        # For matching
        self.nums = [ str(x) for x in range(0, 10) ]
        self.ops = ["+", "-", "*", "/"]

    # Parse function
    def parse(self, code):
        # Remove whitespaces
        for part in code:
            if part == " ":
                code = code.replace(part, "")

        while not self.pos >= len(code):
            # The left!
            if code[self.pos] in self.nums:
                while code[self.pos] not in self.ops:
                    self.left += code[self.pos]
                    self.pos += 1
            else:
                print("Illegal operator place")

            # The operator!
            if code[self.pos] in self.ops:
                self.op = code[self.pos]
                self.pos += 1

            # The right!
            if code[self.pos] in self.nums:
                while self.pos < len(code):
                    self.right += code[self.pos]
                    self.pos += 1
            else:
                print("Illegal operator place")

        # Convert from string to int for convenient
        # For balance problem, the self.right use eval
        self.left = int(self.left)
        self.right = eval(self.right)
        
        # Calculate!
        if self.op == "+":
            print(self.left + self.right)
        elif self.op == "-":
            print(self.left - self.right)
        elif self.op == "*":
            print(self.left * self.right)
        elif self.op == "/":
            print(self.left / self.right)


# Let's test it!
code = "100 / 2"
mylang = MyLang()
mylang.parse(code)
