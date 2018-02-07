def bubble(us_list):
    
    for element in range(len(us_list)):
        for item in range(0, len(us_list) - element - 1):
            #the last i elements will be sorted due to the nature of bubblesort

            if (us_list[item] > us_list[item+1]):
                us_list[item], us_list[item+1] = us_list[item+1], us_list[item]


input = [53, 34, 67, 45, 24, 87, 53, 23, 49, 15]
#expected output = [15, 23, 24, 34, 45, 49, 53, 53, 67, 87]

bubble(input)
print(input)
