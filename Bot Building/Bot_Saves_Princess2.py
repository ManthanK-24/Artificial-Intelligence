def solve(n,r,c,grid):
    #print(n,r,c,grid)
    pr,pc = -1,-1
    mr,mc = -1,-1
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j]=='p'):
                pr, pc = i,j
            if(grid[i][j]=='m'):
                mr, mc = i,j
    
    dr = mr - pr
    dc = mc - pc
    #print(mr,mc,pr,pc)
    #print(dr,dc)
    if(dr>0):
        #for i in range(dr):
        print("UP")
    elif(dr<0):
        #for i in range(-dr):
        print("DOWN")
    elif(dc>0):
        #for i in range(dc):
        print("LEFT")
    elif(dc<0):
        #for i in range(-dc):
        print("RIGHT")
    

n = int(input())
r,c = map(int,input().strip().split())
#print(n,r,c)
grid = []
for r in range(0,n):
    grid.append(input().strip())
#print(grid)

solve(n,r,c,grid)
