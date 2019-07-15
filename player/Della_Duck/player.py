class Player:
    
    della = 0
    opponent = 0
    MAX = 1000
    MIN = -1000
    flag = False 
    def __init__(self):
        pass
    
    def play(self,game_board_state,player_n):       
#        #check who is player 1 and 2
        if player_n == 0:
            Player.della = 0
            Player.opponent = 1       
        else:
            Player.della = 1
            Player.opponent = 0
             
        bestVal = -1000
        bestMove = -1
        
        for i in range(0,16):
            if(game_board_state[i]==-1):               
                game_board_state[i] = Player.della              
                moveVal = self.minimax(game_board_state, 0, Player.opponent, Player.MIN, Player.MAX)                
                game_board_state[i] = -1
                
                if(moveVal > bestVal):
                    bestMove = i
                    bestVal = moveVal
        return bestMove
    
    #check for any available move
    def isMovesLeft(self, game_board_state):
        for i in range(0,16):
            if(game_board_state[i]==-1):
                return True
        return False
    
    #check winning condition
    def evaluate(self, game_board_state):              
        for i in range(0, 4):
            
            #check vertical wins
            if(game_board_state[i]==game_board_state[i+4]==game_board_state[i+8]==game_board_state[i+12]):
                if game_board_state[i]==Player.della:
                    return +10
                if game_board_state[i]==Player.opponent:
                    return -10                

            #check horizontal wins    
            if(game_board_state[i*4]==game_board_state[i*4+1]==game_board_state[i*4+2]==game_board_state[i*4+3]):
                if game_board_state[i*4]==Player.della: 
                    return +10
                if game_board_state[i*4]==Player.opponent:
                    return -10
            
        #check diagonal right wins    
        if(game_board_state[0]==game_board_state[5]==game_board_state[10]==game_board_state[15]):
            if game_board_state[0]==Player.della:
                return +10
            if game_board_state[0]==Player.opponent:
                return -10

        #check diagonal left wins
        if(game_board_state[3]==game_board_state[6]==game_board_state[9]==game_board_state[12]):
            if game_board_state[3]==Player.della:
                return +10
            if game_board_state[3]==Player.opponent:
                return -10  
         
        #Check dominating straight lines
        if (Player.flag==True):
            
            dominantDella = 0
            dominantOpp = 0
            
            for j in range(0,4):
            
                numDella = 0
                numOpp = 0
            
                #check vertical dominating lines
                for x in range (j,j+13,4):
                    if(game_board_state[x]==Player.della):
                        numDella +=1
                    if(game_board_state[x]==Player.opponent):
                        numOpp +=1   
                    
                if (numDella == 3):
                    dominantDella+=1
                if (numOpp == 3):
                    dominantOpp+=1
                numDella = 0
                numOpp = 0
            
                #check horizontal dominating lines
                for x in range (j*4, (j*4)+4, 1):
                    if(game_board_state[x]==Player.della):
                        numDella +=1
                    if(game_board_state[x]==Player.opponent):
                        numOpp +=1 
                    
                if (numDella == 3):
                    dominantDella+=1
                if (numOpp == 3):
                    dominantOpp+=1
                numDella = 0
                numOpp = 0
            
                #check if diagonal right is dominating 
                for x in range(0,16,5):
                    if(game_board_state[x]==Player.della):
                        numDella +=1
                    if(game_board_state[x]==Player.opponent):
                        numOpp +=1 
                    
                if (numDella == 3):
                    dominantDella+=1
                if (numOpp == 3):
                    dominantOpp+=1
                numDella = 0
                numOpp = 0
            
            #check if diagonal left is dominating
            for x in range(3,13,3):
                if(game_board_state[x]==Player.della):
                    numDella +=1
                if(game_board_state[x]==Player.opponent):
                    numOpp +=1 
                    
            if (numDella == 3):
                dominantDella+=1
            if (numOpp == 3):
                dominantOpp+=1
                
                
            if (dominantDella>dominantOpp):
                return +10
            if(dominantOpp>dominantDella):
               return -10
            
        return 0
    
    def minimax(self,game_board_state, depth, player_n, alpha, beta):       
        #evaluate the score based on the board state 
        score = self.evaluate(game_board_state)
        
        #base case: if depth has reach, stop checking for move and return score
        if (depth == 7):
            return score - depth 
        
        if (score == 10): 
            return score - depth  
        
        if (score == -10):
            return score + depth    
    
        #base case: if no move left return 0     
        if(self.isMovesLeft(game_board_state)==False):
            return 0 - depth 
        
        #check it is della's turn
        if(player_n == Player.della):
            
            #worst case for della
            bestDella = Player.MIN            
            
            #recursive function for della
            for i in range(0,16):
                if(game_board_state[i] == -1):
                    game_board_state[i] = Player.della                
                    bestDella = max(bestDella, self.minimax(game_board_state, depth+1, Player.opponent, alpha, beta))
                    game_board_state[i] = -1
                    alpha = max(alpha, bestDella) 
                      
                    #alpha beta pruning
                    if beta <= alpha:
                        break
            
            #return best move for della        
            return bestDella        
        else:        
            #worst case for opponent
            bestOpp = Player.MAX
            
            #recursive function for opponent
            for i in range(0,16):
                if(game_board_state[i] == -1):
                    game_board_state[i] = Player.opponent             
                    bestOpp = min(bestOpp, self.minimax(game_board_state, depth+1, Player.della, alpha, beta))
                    game_board_state[i] = -1
                    beta = min(beta, bestOpp)
                    
                    #alpha beta pruning
                    if beta <= alpha:
                        break
            
            #return best move for opponent       
            return bestOpp       