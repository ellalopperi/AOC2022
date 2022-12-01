with open('input.txt') as f:
    contents = f.read()
    #print(contents)
    contentsSplit = contents.split("\n\n")
    #print(contentsSplit)

#This processes e.g. 2642\n11252\n3981\n7926\n9800
def parseElf(chunk):
  return sum(list(map(int, chunk.split("\n"))))

elfCalories = list(map(parseElf, (contentsSplit)))

elfCalories.sort(reverse=True)

topOneElfCalories = elfCalories[0]
topThreeElfCalories = elfCalories[:3]
sumTopElfCalories = sum(topThreeElfCalories)

print("Answer 1:" + str(topOneElfCalories),"\nAnswer 2:" + str(sumTopElfCalories))