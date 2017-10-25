import itertools
chars = 'abcdefghiblabla'   #here define the chars you want to creat in the word list
n=9
for xs in itertools.product(chars, repeat=n):
    print ''.join(xs)
