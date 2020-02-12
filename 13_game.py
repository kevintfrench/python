def InitializeGrid(board):
    #Initialize Grid by reading in from file
    print("Initializing grid")

def Initialize(board):
    #Initialize game
    #Initialize grid
    InitializeGrid(board)
    #Initialize Grid by random value
    for i in range (8):
        for j in range (8):
            board [i][j] = choice (['Q', 'R', 'S', 'T', 'U'])
            #Initialize score
    global score
    score = 0
    #Initialize turn number
    global turn
    turn = 1

#State main variables
score = 0
turn = 0
goalscore = 100
board = [[0, 0, 0, 0, 0, 0, 0, 0,],
         [0, 0, 0, 0, 0, 0, 0, 0,],
         [0, 0, 0, 0, 0, 0, 0, 0,],
         [0, 0, 0, 0, 0, 0, 0, 0,],
         [0, 0, 0, 0, 0, 0, 0, 0,],
         [0, 0, 0, 0, 0, 0, 0, 0,],
         [0, 0, 0, 0, 0, 0, 0, 0,],
         [0, 0, 0, 0, 0, 0, 0, 0,]]




def ContinueGame(current_score, goal_score = 100):
        #Return false if game should not end, true if game is not over
        if (current_score >= goal_score):
            return False
        else:
            return True

def DoRound():
    #Perform one round of game
    print("Doing one round")

#Intialize game
Initialize()
          
####ALTERNATE CODE####
score = 50
goalscore = 100
#Loop while game not over
while ContinueGame(score, goalscore):
        #Do a round of the game
        DoRound()