import numpy as np


def poem(dct, lines, words):
    out = ["" for i in range(lines)]
    for i in range(lines):
        line = ""
        for j in range(words):
            n = np.random.randint(len(dct))
            line = line + str(dct[n]) + ' '
        out[i] = line
        print(out[i])
    return out


try:
    f = open("_input_file1.txt",
             'r', encoding='utf-8')
except:
    print("open file error")
else:
    S = f.read()
    print(S)
    f.close()
    S = S.lower()
    S = S.replace(".", "")
    A = S.split(" ")
    # print(A)
    B = []
    for word in A:
        if word not in B:
            B.append(word)

    P1 = poem(B, 3, 4)
    print(P1)
