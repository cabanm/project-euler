class int(int):
    def properDivisors(self): # Lists divisors other than the number itself
        return self.divisors()[:-1]

    def divisors(self): # Lists divisors of number
        divisors = list()
        for d in range(1,int(self**(1/2))+1):
            if self%d == 0: # Runs if d divides the number
                divisors.append(d)
                divisors.append(int(self/d))
        return sorted(list(set(divisors)))
