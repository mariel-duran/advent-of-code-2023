bag_configuration = {"red":12, "green":13, "blue":14}

def games_is_possible(games:list) -> list: # outputs the Game number that is possible
    games_possible = []
    
    for line in games:
        is_possible = True
        game_number =  line.split()[1].strip(":")  # get game number
        game_grabs = line.replace(line.split(":")[0],"")
        
        for grab in game_grabs.split(";"):
            for word in grab.strip(":").split(","):
                cubes = word.split()
                if int(cubes[0]) > bag_configuration[cubes[1]]:
                    is_possible = False
        if is_possible:
            games_possible.append(int(game_number))
    return games_possible

# Part 2 

def games_is_possible_part2(games:list) -> list: # outputs the Game number that is possible
    games_setpower_list = []
    
    for line in games:
        game_number =  line.split()[1].strip(":")  # get game number
        game_grabs = line.replace(line.split(":")[0],"")
        min_set = {"red":0, "green":0, "blue":0}
        for grab in game_grabs.split(";"):
            for word in grab.strip(":").split(","):
                cubes = word.split() # number[0] color [1]
                if int(cubes[0]) > min_set[cubes[1]]: # adjust minimum set if the game grab has more cubes
                    min_set[cubes[1]] = int(cubes[0])
        print(min_set)            
        games_setpower_list.append(min_set["red"]*min_set["blue"]*min_set["green"])
    return games_setpower_list


with open("sample_day2.txt") as file:
    data = file.readlines()
    print(sum(games_is_possible_part2(data)))
