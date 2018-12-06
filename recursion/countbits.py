
'''
Count the number of bits set to 1.

'''
def countbits(n):

    bits = 0
    while n:
        bits = bits + (n & 1)
        n >>= 1
    return bits

print(countbits(5))



