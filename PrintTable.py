tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]
def printTable(T):
    Str=[0,0,0]
    for i in range(len(T)):
        max=len(T[i][0])
        for j in range(len(T[i])):
            if len(T[i][j])>max:
                max=len(T[i][j])
        Str[i]=max
    for i in range(len(T)):
        for j in range(len(T[i])):
            tableData[i][j]=tableData[i][j].rjust(Str[i])
    #print(tableData)
    tData=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(T[i])):
        for j in range(len(T)):
            tData[i][j]=tableData[j][i]
    #print(tData)
    for i in range(len(tData)):
        tData[i]=' '.join(tData[i])
        print(tData[i])
printTable(tableData)
