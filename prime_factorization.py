# find the prime factorization and the prime factors of a number
import re

def prime_factorization(n):
    # create a dictionary to store the information
    dct = {}
    dct["factorization"] = ""
    dct["factors"] = []
    try:
        n = int(n)
        if n > 1 :
    # check if a prime divides n
            while n > 1:
                for i in range(2, n+1):
                    if n % i == 0:
                        dct["factors"].append(i)
                        n = n // i
                        break
    # describe the factorization
            s = ""
            for i in set(dct["factors"]):
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
