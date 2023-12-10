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



with open("sample_day2.txt") as file:
    data = file.readlines()
    print(sum(games_is_possible(data)))
