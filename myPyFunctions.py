
def readCSV(fileName,delim):
    import csv
    # Need csv module
    # delim is delimiter, and quoting is set to none. It has something to do with escape character. Not sure what that means
    # identation  =  4 spaces
    newFile = []
    with open(fileName,'rb') as f:
        reader = csv.reader(f,delimiter=delim)
        for row in reader:
            newFile.append(row)
    return newFile