#/usr/bin/env python3
# -*- coding: utf-8 -*-
# Вариант 17


if __name__ == '__main__':
    s = input()

    words = s.split(' ')

    rez1 = []
    rez2 = []
    rez3 = []
    for i, word in enumerate(words):
        # начинающиеся и оканчивающиеся на одну и ту же букву
        if(word[0] == word[len(word)-1]):
            rez1.append(word)

        countE = 0
        countO = 0
        for j, wordd in enumerate(words):
            if (word[j] == "e"):
                countE += 1
            if (word[j] == "o"):
                countO += 1
        
        if countE == 3:
            rez2.append(word)
        
        if countO >= 1:
            rez3.append(word)
    print(rez1)
    print(rez2)
    print(rez3)