def haveThree(array):
    foro = len(array)
    if array.count(3) >= 3:
        return True
    return False

print haveThree([3, 1, 3, 1, 3])
print haveThree([3, 4, 3, 4])
