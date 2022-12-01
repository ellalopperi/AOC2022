with open('Day 1/input.txt') as f:
    contents = f.read()
    contentsSplit = contents.split("\n\n")

#This processes e.g. 2642\n11252\n3981\n7926\n9800 into list of summed calories
parseElf = lambda chunk : sum(list(map(int, chunk.split("\n"))))

elfCalories = list(map(parseElf, (contentsSplit)))

elfCaloriesSorted = sorted(elfCalories, reverse=True)

print("Answer 1:" + str(elfCaloriesSorted[0]),"\nAnswer 2:" + str(sum(elfCaloriesSorted[:3])))