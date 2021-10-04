def count_ears(bunnies):
    '''We have a number of bunnies and each bunny has two big floppy ears. 
    We want to compute the total number of ears across all the bunnies 
    recursively (without loops or multiplication).'''

    if bunnies == 0:
        return 0
    return 2 + count_ears(bunnies - 1)

bunnies = 10
print ((count_ears(bunnies)))