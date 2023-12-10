special_char = "*#+$"


with open("sample.txt") as file:
    
    data = file.readlines()

    part_numbers = []
    line_position = 0

    for line in data:
        numbers = [x.strip(".\n") for x in line.split(".")]
        nums = [x for x in numbers if x != "" and x not in special_char]
        print(f"Current Line position :{line_position}")

        if len(nums) == 0: # ignore empty lists
            line_position += 1
            print(f"Increased Line position :{line_position}")
            continue
        print(nums)

        for num in nums:
            print(num)
            # first scenario: number has special character next to it in the same line - either before or after num
            for spec_char in special_char:
                if spec_char in num:
                    part_numbers.append(int(num.strip(special_char)))
                    break
            
            # second scenario: number has special character adjacent in the previous line or next line
            
            num_position = line.find(num)
            num_length = len(num)
            if num_position == 0:
                line_range = [x for x in range(num_position, num_position + (num_length + 1)) if x <= 9 and x >= 0]
            else:
                line_range = [x for x in range(num_position -1, num_position + (num_length + 1)) if x <= 9 and x >= 0]

            print(f"Line range: {line_range}")

            # previous line
            if line_position > 0:
                for spec_char in special_char:
                    if spec_char in data[line_position - 1]:
                        if data[line_position - 1].find(spec_char) in line_range:
                            part_numbers.append(int(num))
                            break
                        else:
                            continue
                # for position in line_range:
                #     print(f"Position previous line: {position}")
                #     for spec_char in special_char:
                #         print(f"Next line position currently looking at: {data[line_position + 1][position]}")
                #         if special_char in data[line_position - 1][position]:
                #             part_numbers.append(num)
                #             break
            
            # next line
            if line_position < len(data) - 1:
                for spec_char in special_char:
                    if spec_char in data[line_position + 1]:
                        if data[line_position + 1].find(spec_char) in line_range:
                            part_numbers.append(int(num))
                            break
                        else:
                            continue



            # for position in line_range:
            #     print(f"Position next line: {position}")
            #     for spec_char in special_char:
            #         print(f"Special char looking at: {spec_char}")
            #         print(f"Next line position currently looking at: {data[line_position + 1][position]}")
            #         if special_char in data[line_position + 1][position]:
            #             part_numbers.append(num)
            #             break

            # print(f"Part numbers: {part_numbers}")
        line_position += 1
        # print(f"Increased Line position :{line_position}")
        # print(f"Part numbers: {part_numbers}")
        print(sum(part_numbers))

