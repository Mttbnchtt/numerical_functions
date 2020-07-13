def number_of_factors(n):
    try:
        n = int(n)
        if n > 0:
    #     find prime factors and determine their coefficients
            prime_factors = [1]
            q = math.sqrt(n)
            while n % 2 == 0:
                prime_factors.append(2)
                n = n // 2
            while n > 1 and max(prime_factors) <= q:
                for i in range(3, n+1, 2):
                    if n % i == 0:
                        prime_factors.append(i)
                        n = n // i
                        break
            prime_factors.remove(1)
    # the factors of n are the products of prime factors with coefficients between 0 
    # and the coefficients that they have in the prime decomposition of n
    # therefore, the number of factors of n is the products of the cardinality of the ranges of the powerss
            m = 1
            for i in list(set(prime_factors)):
                m = m * (prime_factors.count(i)+1)
            return m
        else:
            print("Input error: must be positive.")
    except:
        print("Input error: must be integer.")
