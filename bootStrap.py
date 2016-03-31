import itertools

sampleItem = [1,2,3,4,5,6,6]
numDraws = 3

allCombo = map(tuple,itertools.combinations(sampleItem,numDraws))


allCombo =map(tuple,itertools.permutations(sampleItem,3))


def drawWithReplacement(pool,size):
  bigPool = pool*size
  allCombo =map(tuple,itertools.permutations(bigPool,size))
  return allCombo

