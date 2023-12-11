import string


with open("sample.txt") as file:
    
    data = file.readlines()
    part_numbers = []
    line_position = 0
    line_length = len(data[0])

    for line in data:
        
        numbers = [x.strip(".\n") for x in line.split(".")]
        
        nums = [x for x in numbers if x != "" and x not in string.punctuation]
        
        
        print(nums)

        if len(nums) == 0: # ignore empty lists
            line_position += 1
            continue

        for num in nums:
            num_position = line.find(num)
            num_length = len(num)
            if num_position == 0:
                line_range = [x for x in range(num_position, num_position + (num_length + 1)) if x <= line_length and x >= 0]
            else:
                line_range = [x for x in range(num_position -1, num_position + (num_length + 1)) if x <= line_length and x >= 0]
            print(num)
            # first scenario: number has special character next to it in the same line - either before or after num
            if any(x in string.punctuation for x in num):
                for spec_char in string.punctuation:
                    if spec_char in num:
                        try:
                            holder = [x for x in num.split(spec_char) if x != ""]
                            print(holder)
                            part_numbers.append(int(holder[0].strip(string.punctuation)))
                            part_numbers.append(int(holder[1].strip(string.punctuation)))
                            print("Try completed")
                            break
                        except:
                            part_numbers.append(int(num.strip(string.punctuation)))
                            print("except completed")
                            break
            # second scenario: number has special character adjacent in the previous line or next line
            # previous line
            elif line_position > 0:
                for spec_char in string.punctuation:
                    if spec_char in data[line_position - 1]:
                        if data[line_position - 1].find(spec_char) in line_range:
                            part_numbers.append(int(num))
                            break
                        else:
                            continue

            # next line
            elif line_position < len(data) - 1:
                for spec_char in string.punctuation:
                    if spec_char in data[line_position + 1]:
                        if data[line_position + 1].find(spec_char) in line_range:
                            part_numbers.append(int(num))
                            break
                        else:
                            continue

        line_position += 1
    print(sum(part_numbers))

