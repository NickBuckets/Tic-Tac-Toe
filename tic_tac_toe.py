import os

class Tic_Tac_Toe:
    
    positions = [
        ["","",""],
        ["","",""],
        ["","",""]
    ]
    
    def __init__(self):
        self.gameboard = self.create_game_board()


    def create_game_board(self):

        gameboard = f"\
          {self.positions[0][0]}  |  {self.positions[0][1]}  |  {self.positions[0][2]}  \n\
        --------------\n\
          {self.positions[1][0]}  |  {self.positions[1][1]}  |  {self.positions[1][2]}  \n\
        --------------\n\
          {self.positions[2][0]}  |  {self.positions[2][1]}  |  {self.positions[2][2]}  "
        return gameboard


    def check_index_location(self, coordinates):
        coordinates = coordinates.split(",")
        if self.positions[int(coordinates[0])][int(coordinates[1])] != "":
            return False
        else:
            return None


    def check_winning_status(self):

        for i in range(3): # Check each row going to the right
            unique_vals = set()
            for j in range(3): # go
                unique_vals.add(self.positions[i][j])

            if len(list(unique_vals)) == 1 and list(unique_vals)[0] != "":
                return list(unique_vals)[0]

        for i in range(3): # Check each row going to the right
            unique_vals = set()
            unique_vals.add(self.positions[0][i])
            unique_vals.add(self.positions[1][i])
            unique_vals.add(self.positions[2][i])
            if len(list(unique_vals)) == 1 and list(unique_vals)[0] != "":
                return list(unique_vals)[0]

        
        unique_vals = set()
        unique_vals.add(self.positions[0][0])
        unique_vals.add(self.positions[1][1])
        unique_vals.add(self.positions[2][2])
        if len(list(unique_vals)) == 1 and list(unique_vals)[0] != "":
            return list(unique_vals)[0]

        unique_vals = set()
        unique_vals.add(self.positions[0][2])
        unique_vals.add(self.positions[1][1])
        unique_vals.add(self.positions[2][0])
        if len(list(unique_vals)) == 1 and list(unique_vals)[0] != "":
            return list(unique_vals)[0]
        
    
    def start_game(self):
        print("Instructions: To pick a location type the coordinates (ex. 0,0).")
        print("You are currently X, with first move.")
        print(self.create_game_board())

        count = 0
        while True:
            try:
                coordinates = input("Enter your position: ")
                check_position_existance = self.check_index_location(coordinates)
                if check_position_existance == False:
                    print("That position is already taken!")
                    continue
                
                if count % 2 == 0:
                    self.positions[int(coordinates.split(",")[0])][int(coordinates.split(",")[-1])] = "X"
                else:
                    self.positions[int(coordinates.split(",")[0])][int(coordinates.split(",")[-1])] = "O"
                
                count += 1
                print(self.create_game_board())
                winner = self.check_winning_status()
                if winner != None:
                    print(f"{winner} is the winner!")
                    os.system("python main.py")
            except:
                os.system("python main.py")
                
        

Tic_Tac_Toe().start_game()
