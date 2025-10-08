# // Time Complexity : O(n)
# // Space Complexity : O(h)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = []
        totalCount = 0
        rottenCount = 0 
        mins = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 2):
                    q.append([i,j])
                    rottenCount += 1
                if(grid[i][j] == 1 or grid[i][j] == 2):
                    totalCount += 1
        
        while(len(q) > 0):

            if(rottenCount == totalCount):
                return mins
            
            rotten = q.copy()
            mins+=1
            q=[]

            for i in rotten:
                
                if(i[0]>0):
                    if(grid[i[0]-1][i[1]] == 1):
                        grid[i[0]-1][i[1]] = 2
                        q.append([i[0]-1,i[1]])
                        rottenCount += 1 
                
                if(i[0]<len(grid)-1):
                    if(grid[i[0]+1][i[1]] == 1):
                        grid[i[0]+1][i[1]] = 2
                        q.append([i[0]+1,i[1]])
                        rottenCount += 1

                if(i[1]>0):
                    if(grid[i[0]][i[1]-1] == 1):
                        grid[i[0]][i[1]-1] = 2
                        q.append([i[0],i[1]-1])
                        rottenCount += 1
                
                if(i[1]<len(grid[0])-1):
                    if(grid[i[0]][i[1]+1] == 1):
                        grid[i[0]][i[1]+1] = 2                 
                        q.append([i[0],i[1]+1])
                        rottenCount += 1

        if(rottenCount == totalCount):
            return mins
        else:
            return -1    
            
                
                

        