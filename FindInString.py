def countChar(ch, teststring):
    count = 0;
    for i in range(len(teststring)):
        if teststring[i] == ch:
            count += 1
        return count

print(countChar('e', "The quick brown fox jumped over the lazy dogs."))

