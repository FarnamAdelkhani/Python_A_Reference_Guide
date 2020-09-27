import sys

# Check for matches in string(input) with A/B; return happiness
def remove_doubles_A_B(input):
    # Dictionaries
    likeDict = {}
    dislikeDict = {}

    # Add inputs to Dictionary
    for x in like:
        likeDict[x] = 1
    for x in dislike:
        dislikeDict[x] = 1

    # Count happiness
    happiness = 0
    for i in input:
        if i in likeDict:
            happiness += 1
    for j in input:
        if j in dislikeDict:
            happiness -= 1

    # print(likeDict)
    # print(dislikeDict)
    return happiness


if __name__ == '__main__':
    # Remember to Import sys
    # Since input is given in 4 lines, utilize readline
    n, m = sys.stdin.readline().split(' ')
    input = sys.stdin.readline().strip().split(' ')
    like = sys.stdin.readline().strip().split(' ')
    dislike = sys.stdin.readline().strip().split(' ')

    print(remove_doubles_A_B(input))
