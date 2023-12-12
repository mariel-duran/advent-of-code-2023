with open("sample_day4.txt") as file:
    
    data = file.readlines()
    points = 0

    for line in data:
        # winning_nums = line.split("|")[0].split(":")[1].split()
        winning_nums = [int(x) for x in line.split("|")[0].split(":")[1].split()]
        given_nums = [int(x) for x in line.split("|")[1].split()]
        print(winning_nums)
        print(given_nums)
        points_holder = 0

        # ignore non matches

        if not any(x in winning_nums for x in given_nums):
            continue

        for win_num in winning_nums:
            for giv_num in given_nums:
                if win_num == giv_num:
                    if points_holder < 1:
                        points_holder+= 1
                    else:
                        points_holder = points_holder*2
        
        points = points + points_holder

    print(points)
