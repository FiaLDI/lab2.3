#/usr/bin/env python3
# -*- coding: utf-8 -*-
# Вариант 17


if __name__ == '__main__':
    s = input("Введите предложение: ")
    sym = input("Введите символ: ")

    k = 0

    for i in range(len(s)):
        if s[i] == sym:
            k += 1
    
    print(k)