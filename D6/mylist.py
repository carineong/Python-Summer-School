class mylist(list):
    def product(self):
        n = len(self)
        ans = 1
        for i in self:
            ans *= i
        return ans

    def __add__(self,other):
        if len(self) != len(other):
            raise Exception("Sorry, the length of both lists is not equal!")
        n = len(self)
        ans = mylist()
        for i,j in zip(self,other):
            ans.append(i + j)
        return ans
  
    def __mul__ (self, other):
        if len(self) != len(other):
            raise Exception("Sorry, the length of both lists is not equal!")
        ans = 0
        for i,j in zip(self,other):
            ans += (i * j)
        return ans






