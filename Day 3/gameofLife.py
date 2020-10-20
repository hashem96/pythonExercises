#Count neighbours
def countneighbours(current_generation,x,y):
    count=0
    for i in range(-1,1):
        for j in range(-1,1):
            count+=current_generation[x+i][y+j]
    #In order not to count the current position as a neighbour we substract it 
    #from the count

    count-=current_generation[x][y]
    return count


current_generation = [[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0],
 [0, 1, 0, 1, 0, 0],
 [0, 0, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0]]

next_generation = [[0 for i in range(6)] for i in range(6)]


#Compute next generation based on current generation

#Loop through every column and every row

for i in range(len(current_generation)):
    for j in range(len(current_generation)):

        neighbours = countneighbours(current_generation,i,j)
        state = current_generation[i][j]

        #RULE1: Any dead cell with exactly three live neighbours becomes a 
        #live cell, as if by reproduction.
        if (state == 0) and (neighbours == 3):
            next_generation[i][j] = 1    

        #RULE 2 : Any live cell with fewer than two live neighbours dies, 
        # as if by underpopulation   

        #RULE 3 : Any live cell with more than three live neighbours dies,
        #  as if by overpopulation.

        elif(state == 1 and (neighbours <2 or neighbours >3)):
            next_generation[i][j] = 0 


        #Any other cases the state will be the same 
        else:
            next_generation[i][j] = state 

print(next_generation)






