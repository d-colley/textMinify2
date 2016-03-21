
with open('test.txt', 'r') as src:
    with open('result.txt', 'w') as dest:
       for line in src:
           newline = line.replace("\t", " ")
           newline2 = newline.replace("  ", " ")
           dest.write((newline2))