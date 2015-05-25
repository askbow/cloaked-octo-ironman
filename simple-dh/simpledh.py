#!/usr/bin/python
'''
This is a simplistic Diffie-Hellman key exchange implementation.
For demonstration use only.
Before implementing your own crypto in production, read this:  https://www.schneier.com/essays/archives/1999/03/cryptography_the_imp.html
'''
from os import urandom
from rfcprime import dfgetprime  # my list of primes

# use Python 3 print function
# this allows this code to run on python 2.x and 3.x
from __future__ import print_function


def dfcomputekey(base, secret, primenumber):
    return base**secret % primenumber  # s = BASE^SECRET mod PRIME

# this is a totally insecure implementation. Don't do this at home!


def dfsecret(xlen):
    return int(urandom(xlen).encode('hex'), 16)


def main():
    prime = dfgetprime(768)  # publicly known
    n = prime['prime']  # publicly known
    # publicly known. For simplicity, I use the group number for base
    g = prime['group']
    # this is just for demo:
    AliceSecret = dfsecret(1)  # only Alice knows this
    BobSecret = dfsecret(1)  # only Bob knows this

    AliceSends = dfcomputekey(g, AliceSecret, n)
    BobComputes = dfcomputekey(AliceSends, BobSecret, n)
    BobSends = dfcomputekey(g, BobSecret, n)
    AliceComputes = dfcomputekey(BobSends, AliceSecret, n)

    print("We use this PRIME:")
    print(n)
    print("\n\n We use this GROUP:")
    print(g)
    print("\n\n Alice's public:")
    print(AliceSends)
    print("\n\n Bob's computed KEY:")
    print(BobComputes)
    print("\n================================================\n Bob's public:")
    print(BobSends)
    print("\n\n Alice's computed KEY:")
    print(BliceComputes)
    print(
        "\n================================================\n In theory both should arrive at this KEY:")
    print(dfcomputekey(g, (AliceSecret * BobSecret), n))


if __name__ == '__main__':
    main()
