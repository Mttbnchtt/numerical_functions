# find the prime factorization and the prime factors of a number
import re
import math

def prime_factorization(n):
    try:
        n = int(n)
        if n > 1 :
    # create a dictionary to store the information
            dct = {
                "factorization" : "",
                "factors" : [1]
            }
    # check if a prime divides n
        # if n is even, find the power of 2
            while n % 2 == 0:
                dct["factors"].append(2)
                n = n // 2
        # check the remaining odd factors
        # use sqrt(n) as an upper bound because only prime numbers
        # have a prime factor greater than their square roots
            for i in range(3, int(math.sqrt(n)+1), 2):
                if n % i == 0:
                    dct["factors"].append(i)
                    n = n // i
                    break
        # check if n is prime
            if len(dct["factors"]) == 1:
                dct["factors"] == [n]
            else:
                del dct["factors"][0]
    # describe the factorization
            s = ""
            for i in sorted(list(set(dct["factors"]))):
                s += f"({i}**{dct['factors'].count(i)})*"
            t = re.findall("(.+)\*", s)[0]
            dct["factorization"] = t
    # list the factors
            dct["factors"] = sorted(list(set(dct["factors"])))
    # return factorization and factors
            return dct
        else:
    # handle error if input is less than 1
            print("Input error: must be greater than 1.")
    except:
    # handle error if input is not an integer
        print("Input error: must be integer.")

# uncomment to try with a specific number
# inp = input("Number: ")
# print(prime_factorization(inp))
