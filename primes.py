class int(int):
    def isPrime(self):
        for q in range(2, int(self**(1/2))):
            if self%q:
                print(self,q,self%q)
            else:
                return 0
        return 1
