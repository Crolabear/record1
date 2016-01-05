# this assumes the input to have integers, all pairs but 1.
# for example, (1,1,2,2,3,4,4) , number 1,2,4 are paired with only 3 being the unqiue value

# the function aims to output 3

def findUniq(input1):
    #input1 = [1,1,2,2,3,4,4,3]
    used =[]
    uniq = ''
    for i in range(len(input1)):
        if input1[i] not in used:
            for j in range(len(input1)):
                if i != j:
                    if input1[i] == input1[j]:
                        used.append(input1[i])


    v1 = set(input1)
    v2 = set(used)
    uniq = v1.difference(v2)

    return uniq


def main():
    input1 = [1,1,2,2,3,3,4]
    k = findUniq(input1)
    print k



if __name__ == "__main__":
    main()