import itertools
import csv
from __future__ import division

#def generateNumbers(number_unique):


def scrambleNumber(number_unique):
    # require itertool
  number = [1,2,3,4,5,6,7,8,9]
        # this line gives me a list of tuples, each element is a subset of the set number
        # we fix the size of the subset by parameter number_unique
  combo = map(tuple,itertools.combinations(number,number_unique))
        
        # then let's create another combo
  allOrdering = map(tuple,itertools.permutations(range(number_unique)))
        
        # then I can check for equalities.
  return combo


def EulerAlgo(N1,N2):
  while (N2 != 0):
    t = N2
    N2 = N1%N2
    N1 = t
  return N1


def generateLinear(constant,degree1):
  a = range(1,constant+1)  # i dont have 0 in the constant term too ... idk
  # it makes later on when i dont want to have denomiator that are multiple of each other harder.
  b = range(1,degree1+1)
  linearTerm = [(x,y) for x in a for y in b]
  return linearTerm

def produceFraction(numerator1,linearTerm1=None):
  c = range(1,numerator1+1)   # c is the constant term in the numerator
  polyFrac = []
  for it in c:
    for they in linearTerm1:
      multipleBot=EulerAlgo(they[0],they[1])   # this step makes sure the fraction is fully reduced.
      commFactor = EulerAlgo(multipleBot,it)
      if commFactor == 1:
        polyFrac.append((it,they))
  return polyFrac


def produceExpression(term1,term2):
    # term 1 and ter2 are produced by produceFraction above...
  sum1 = []
# checking the 2 fractions have different denominator, or denominators taht are not multiple of each other.
  for f1 in term1:
    for f2 in term2:
      if f1 != f2:
        fac1 = EulerAlgo(f1[1][0],f2[1][0])
        fac2 = EulerAlgo(f1[1][1],f2[1][1])
        #g1 = f2[1][0]/f1[1][0]
      #g2 = f2[1][1]/f1[1][1]
      #if g1 != g2:
        if fac1 != fac2:
          sum1.append((f1,f2))
  return sum1


linearTerm = generateLinear(10,20)
fr1 = produceFraction(9,linearTerm)
sum1 = produceExpression(fr1,fr1)



def addPoly(term1,term2):
  constantTerm = term1[0]*term2[1][0] + term2[0]*term1[1][0]
  degree1Term = term1[0]*term2[1][1] + term2[0]*term1[1][1]
  Denominator1 = (term1[1][0]*term2[1][0], term1[1][0]*term2[1][1]+term1[1][1]*term2[1][0],term1[1][1]*term2[1][1])
  return [(constantTerm,degree1Term),Denominator1]


def solveLinear(linearEqn):
# when i say linearEqn, i mean degree1 polynomial. i expect an ordered pair, with 1st term constant, 2nd term degree1
# then i will find the x value that makes it 0
  return -1*linearEqn[0]/linearEqn[1]



# big question, can i assume constant root? probably not. so i will use estimate then.
def doTheMath(sum1):
  exactRoot =[]
  estimatedRoot = []
  for item in sum1:
    res1 = addPoly(item[0],item[1])
    zeroz = solveLinear(res1[0])
    rootcheck = zeroz*zeroz*res1[1][2]+zeroz*res1[1][1]+res1[1][0]
    if rootcheck == 0:
      exactRoot.append(item)
    if abs(rootcheck) < 0.00001 and abs(rootcheck) > 0 :
      estimatedRoot.append(item)
  return [exactRoot,estimatedRoot]


AllMath = doTheMath(sum1)
# then i just need to format it

st1 = []
for item in AllMath[0]: # AllMath[0] has all the exact roots, aka reduciable
  st2 = '%d / (%d + %dX) + %d / (%d + %dX)' %(item[0][0],item[0][1][0],item[0][1][1],item[1][0],item[1][1][0],item[1][1][1])
  st1.append(st2)


with open('steveLinearFraction.txt','w') as f:
  for item in st1:
    f.write('\n'+item)







