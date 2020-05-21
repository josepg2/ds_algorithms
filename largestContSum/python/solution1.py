# largest continuous sum of elements in a list

values = [-1,  -2, -10, -2, -4 , -5 , -10, -10, -1, -4]

def largestContSum(values):

    maxSum = currentmax = values[0]

    for value in values[1:]:

        currentmax = max(currentmax + value, value)

        maxSum = max(currentmax, maxSum)

    print(maxSum)

largestContSum(values)