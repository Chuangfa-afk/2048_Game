import random
class game2048:
    matrix = None
    valid_move = "wsdaWSDA"
    def __init__(self):
        self.matrix = [[0] * 4 for _ in range(4)]
        x, y = self.generate()
        self.matrix[x][y] = 2

        i, j = self.generate()
        while self.matrix[i][j] != 0:
            i,j = self.generate()
        self.matrix[i][j] = 2

        print(self)
        self.move()

    
    def generate(self):
        return (random.randint(0,3), random.randint(0,3))
    
    def move(self):
        
        user_input = input("Enter W,S,A,D to move Up, Down, Left, Right: ")
        while user_input not in self.valid_move:
            user_input = input("Please enter a valid move W, S, A, D: ")
        
        if user_input in "Ww":
            self.move_up()
        elif user_input in "Ss":
            self.move_down()
        elif user_input in "Aa":
            self.move_left()
        elif user_input in "dD":
            self.move_right()
        print(self)
        
        if self.check_board() == "c":
            self.move()


        
    def move_up(self):
        moved = False
        for col in range(4):
            values = [self.matrix[row][col] for row in range(4) if self.matrix[row][col] != 0]
            for i in range(len(values) - 1):
                if values[i] == values[i + 1]:
                    values[i] *= 2
                    values[i + 1] = 0
            values = [val for val in values if val != 0]
            values += [0] * (4 - len(values))
            for row in range(4):
                if self.matrix[row][col] != values[row]:
                    moved = True
                self.matrix[row][col] = values[row]
        if moved:
            self.add_new_tile()

    def move_down(self):
        moved = False
        for col in range(4):
            values = [self.matrix[row][col] for row in range(4) if self.matrix[row][col] != 0]
            values.reverse()
            for i in range(len(values) - 1):
                if values[i] == values[i + 1]:
                    values[i] *= 2
                    values[i + 1] = 0
            values = [val for val in values if val != 0]
            values += [0] * (4 - len(values))
            values.reverse()
            for row in range(4):
                if self.matrix[row][col] != values[row]:
                    moved = True
                self.matrix[row][col] = values[row]
        if moved:
            self.add_new_tile()

    def move_left(self):
        moved = False
        for row in range(4):
            values = [self.matrix[row][col] for col in range(4) if self.matrix[row][col] != 0]
            for i in range(len(values) - 1):
                if values[i] == values[i + 1]:
                    values[i] *= 2
                    values[i + 1] = 0
            values = [val for val in values if val != 0]
            values += [0] * (4 - len(values))
            for col in range(4):
                if self.matrix[row][col] != values[col]:
                    moved = True
                self.matrix[row][col] = values[col]
        if moved:
            self.add_new_tile()

    def move_right(self):
        moved = False
        for row in range(4):
            values = [self.matrix[row][col] for col in range(4) if self.matrix[row][col] != 0]
            values.reverse()
            for i in range(len(values) - 1):
                if values[i] == values[i + 1]:
                    values[i] *= 2
                    values[i + 1] = 0
            values = [val for val in values if val != 0]
            values += [0] * (4 - len(values))
            values.reverse()
            for col in range(4):
                if self.matrix[row][col] != values[col]:
                    moved = True
                self.matrix[row][col] = values[col]
        if moved:
            self.add_new_tile()

    def check_board(self):
        empty_space = False
    
        for row in self.matrix:
            for element in row:
                if element == 0:
                    empty_space = True
                elif element == 2048:
                    self.status("victory")
                    return
        if empty_space == False:
            self.status("defeat")
            return
        return "c"

    def status(self, s):
        if s == "victory":
            print("Congrats, you reach to 2048!")
        elif s == "defeat":
            print("uff, you lost the game.")
        user_input = input("Enter Y to start over or any key to terminate the program: ")
        if user_input in "Yy":
            game2048()
        else:
            print("Program terminated.")
        
    def add_new_tile(self):
        x, y = self.generate()
        while self.matrix[x][y] != 0:
            x, y = self.generate()
        self.matrix[x][y] = 2
        
    
    
    def __str__(self,):
        output = ""
        divider = "+----" * 4 + "+\n"
        
        for row in self.matrix:
            output += divider
            for element in row:
                output += f"| {element if element != 0 else ' ':>2} "
            output += "|\n"
        output += divider 
        return output
    

if __name__ == "__main__":
    game = game2048()