numbers = [1,-2,3,-4,5,6,-7,-8,9,10]

count_of_positive_num = 0

for number in numbers:
    if number > 0:
        count_of_positive_num += 1

print("Total Positive Numbers in list are",count_of_positive_num)