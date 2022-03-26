import readline

def printMaze(maze):
    writeTxt = open("solution.txt", "w")
    writeTxt.close()
    writeTxt = open("solution.txt", "a")

    for i in range(len(maze)):
        for k in range(len(maze[len(maze) - i - 1])):
            writeTxt.write(maze[len(maze) - i - 1][k])
        writeTxt.write("\n")
    writeTxt.close()

filePath = "" #file path of maze and maze solution txts
mazeID = input("MazeID: ")
mazeFile = "maze_"+ mazeID +".txt"

startx = input("Start x: ")
starty = input("Start y: ")
endx = input("End x: ")
endy = input("End y: ")

mazeSolution = "maze_1_path_" + startx + "_" + starty + "_" + endx + "_" + endy + ".txt"

inputMazeFile = open(filePath+mazeFile)
inputSolutionFile = open(filePath+mazeSolution)

mazeLine1 = inputMazeFile.readline()

mazeLine1 = mazeLine1.split(" ")

mazeRow = mazeLine1[0]
mazeColumn = mazeLine1[1]

mazeInfo = []

for line in inputMazeFile:
    line = line[ : -1]
    tempList = line.split(" ")
    mazeInfoC = [int(tempList[3][-1]), int(tempList[5][-1])]
    mazeInfo.append(mazeInfoC)

inputMazeFile.close()

maze = []
counter = 0
counter2 = 0

for i in range(2 * int(mazeRow) + 1):
    if i == (2 * int(mazeRow)):
        mazeC = ["#"] * (3 * int(mazeColumn) + 1)
        maze.append(mazeC)
    elif i % 2 == 0:
        mazeC = ["#"]
        for k in range(int(mazeColumn)):
            if mazeInfo[(counter2 * int(mazeColumn)) + k][1] == 1:
                mazeC.append("###")
            else:
                if (mazeInfo[(counter2 * int(mazeColumn)) + k][0] == 1):
                    mazeC.append("  #")
                elif ((((counter2 - 1) * int(mazeColumn)) + k) >= 0) and (mazeInfo[((counter2 - 1) * int(mazeColumn)) + k][0] == 1):
                    mazeC.append("  #")
                else:
                    mazeC.append("   ")
        counter2 += 1
        maze.append(mazeC)
    elif i % 2 == 1:
        mazeC = ["#"]
        for k in range(int(mazeColumn)):
            if mazeInfo[(counter * int(mazeColumn)) + k][0] == 1:
                mazeC.append("  #")
            else:
                mazeC.append("   ")
        counter += 1
        maze.append(mazeC)

solutionInfo = []

for line in inputSolutionFile:
    line = line.split(" ")
    solC = [int(line[0]), int(line[1])]
    solutionInfo.append(solC)

inputSolutionFile.close()

value = maze[2 * solutionInfo[0][1] + 1][solutionInfo[0][0] + 1]
if solutionInfo[1][1] - solutionInfo[0][1] == 1:
    if value == "  #":
        value = "OO#"
        value2 = "▲▲#"
    else:
        value2 = maze[2 * solutionInfo[0][1] + 2][solutionInfo[0][0] + 1]
        if value2 == "  #":
            value = "OO "
            value2 = "▲▲#"
        else:
            value = "OOO"
            value2 = "▲▲▲"
    maze[2 * solutionInfo[0][1] + 2][solutionInfo[0][0] + 1] = value2
elif solutionInfo[1][1] - solutionInfo[0][1] == -1:
    if value == "  #":
        value = "OO#"
        value2 = "▼▼#"
    else:
        value2 = maze[2 * solutionInfo[0][1]][solutionInfo[0][0] + 1]
        if value2 == "  #":
            value = "OO "
            value2 = "▼▼#"
        else:
            value = "OOO"
            value2 = "▼▼▼"
    maze[2 * solutionInfo[0][1]][solutionInfo[0][0] + 1] = value2
elif solutionInfo[1][0] - solutionInfo[0][0] == 1:
    value = "OOO"
elif solutionInfo[1][0] - solutionInfo[0][0] == -1:
    if value == "  #":
        value = "OO#"
    else:
        value = "OOO"
maze[2 * solutionInfo[0][1] + 1][solutionInfo[0][0] + 1] = value


for i in range(1, len(solutionInfo) - 1):
    if solutionInfo[i + 1][0] - solutionInfo[i][0] == 1:
        maze[2 * solutionInfo[i][1] + 1][solutionInfo[i][0] + 1] = "►►►"
    elif solutionInfo[i + 1][0] - solutionInfo[i][0] == -1:
        value = maze[2 * solutionInfo[i][1] + 1][solutionInfo[i][0] + 1]

        if value == "  #":
            value = "◄◄#"
        else:
            value = "◄◄◄"
        maze[2 * solutionInfo[i][1] + 1][solutionInfo[i][0] + 1] = value
    elif solutionInfo[i + 1][1] - solutionInfo[i][1] == 1:
        value = maze[2 * solutionInfo[i][1] + 1][solutionInfo[i][0] + 1]

        if value == "  #":
            value = "▲▲#"
            value2 =  maze[2 * solutionInfo[i][1] + 2][solutionInfo[i][0] + 1]
            value2 = "▲▲#"

        else:
            value2 =  maze[2 * solutionInfo[i][1] + 2][solutionInfo[i][0] + 1]
            if value2 == "  #":
                value2 = "▲▲#"
                if solutionInfo[i][0] - solutionInfo[i - 1][0] == 1:
                    value = "▲▲ "
                elif solutionInfo[i][0] - solutionInfo[i - 1][0] == -1:
                    value = "▲▲◄"
            else:
                value = "▲▲▲"
                value2 = "▲▲▲"
        maze[2 * solutionInfo[i][1] + 1][solutionInfo[i][0] + 1] = value
        maze[2 * solutionInfo[i][1] + 2][solutionInfo[i][0] + 1] = value2
    elif solutionInfo[i + 1][1] - solutionInfo[i][1] == -1:
        value = maze[2 * solutionInfo[i][1] + 1][solutionInfo[i][0] + 1]

        if value == "  #":
            value = "▼▼#"
            value2 = "▼▼#"
        else:
            value2 = maze[2 * solutionInfo[i][1]][solutionInfo[i][0] + 1]

            if value2 == "  #":
                value2 = "▼▼#"

                if solutionInfo[i][0] - solutionInfo[i - 1][0] == 1:
                    value = "▼▼ "
                elif solutionInfo[i][0] - solutionInfo[i - 1][0] == -1:
                    value = "▼▼◄"
            else:
                value = "▼▼▼"
                value2 = "▼▼▼"
        maze[2 * solutionInfo[i][1] + 1][solutionInfo[i][0] + 1] = value
        maze[2 * solutionInfo[i][1]][solutionInfo[i][0] + 1] = value2            

        

value = maze[2 * solutionInfo[len(solutionInfo) - 1][1] + 1][solutionInfo[len(solutionInfo) - 1][0] + 1]
if value == "   ":
    value = "XXX"
else:
    value = "XX" + value[-1]
maze[2 * solutionInfo[len(solutionInfo) - 1][1] + 1][solutionInfo[len(solutionInfo) - 1][0] + 1] = value

printMaze(maze)