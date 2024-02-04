def printShortPath():
    bx,by,px,py = -1,-1,-1,-1
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j]=='m'):
                bx, by = i,j
            elif(grid[i][j]=='p'):
                px, py = i,j
    #print(bx,by,px,py)
    x = bx - px
    y = by - py
    #print(x,y)
    if(x>0):
        for i in range(x):
            print("UP")
    if(x<0):
        for i in range(-x):
            print("DOWN")
    if(y>0):
        for i in range(y):
            print("LEFT")
            
    if(y<0):
        for i in range(-y):
            print("RIGHT")
            

            
    
    
n = int(input())
#grid = [['0']*n]*n
#print(n)
#print(grid)
grid = []
for r in range(0,n):
    # print(input())
    grid.append(input().strip())
#print(grid)

printShortPath()
