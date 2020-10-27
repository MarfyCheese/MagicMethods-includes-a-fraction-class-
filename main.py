from math import gcd
class Fraction:

  def __init__(self,n,d):
    self.n = n
    self.d = d

  def reduce(self):
    n = self.n // gcd(self.n,self.d)
    d = self.d // gcd(self.n,self.d)
    return Fraction(n,d)

  def __add__(self, other):
    new_d = self.d * other.d
    new_n = (self.n * other.d) + (other.n * self.d)
    return  Fraction(new_n, new_d).reduce()

  def __sub__(self, other):
    new_d = self.d * other.d
    new_n = (self.n * other.d) - (other.n * self.d)
    return  Fraction(new_n, new_d).reduce()
    
  def __mul__(self,other):
    new_d = self.d * other.d
    new_n = other.n * self.n 
    return  Fraction(new_n, new_d).reduce()

  def __truediv__(self,other):
    new_d = self.d * other.n
    new_n = other.d * self.n
    return  Fraction(new_n, new_d).reduce()

  def __float__(self):
    return self.n / self.d

  def __str__(self):
    return "{}/{}".format(self.n,self.d)
    
def goldenRatio(iterations):
  phi = Fraction(1, 1)
  one = Fraction(1,1)
  for i in range(1,iterations+1,1):
    phi = one + one/phi
    print("on iteration {}, phi was {}".format(i,phi))

def main():
  goldenRatio(int(input("How many levels would you aproximate the golden ratio \n")))
if __name__ == "__main__":
  main()