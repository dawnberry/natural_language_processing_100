def p00():
    words = 'stressed'
    rev_str = words[::-1]
    print(rev_str)

def  p01():
    words = 'パタトクカシーー'
    pic_str = words[::2]
    print(pic_str)

def p02():
    words1 = 'パトカー'
    words2 = 'タクシー'
    lin_str = ''
    for i, j in zip(words1,words2):
        lin_str += i +j
    print(str(lin_str))

def p03():
    words = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".rstrip('.')
    sep_words = words.replace('.', ' ').split(' ')
    for i in range(len(sep_words)):
        count_words = len(sep_words[i])
        print(count_words)

def p04():
    words = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".rstrip('.').split(' ')
    res = {}
    num_1 = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    for i, name in enumerate(words, 1):
        if i in num_1:
            res[name[0:1]] = i
        else:
            res[name[0:2]] = i
    print(res)

def p05(N):
    words = "I am an NLPer".split(' ')
    letter = "I am an NLPer".replace(' ','')
    resw = []
    resl = []

    for i  in range(len(words)-N+1):
        resw.append(words[i]+words[i+1])
    print(resw)

    for j in range(len(letter)-N+1):
        resl.append(letter[j]+letter[j+1])
    print(resl)

def p06():
    X = "paraparaparadise"
    Y = "paragraph"
    setX = set()
    setY = set()
    for i in range(len(X)-1):
        setX.add(X[i]+X[i+1])

    for j in range(len(Y)-1):
        setY.add(Y[j]+Y[j+1])

    print(set.union(setX,setY))
    print(set.intersection(setX,setY))
    print(set.difference(setX,setY))
    print('se in setX ' + str('se' in setX))
    print('se in setY ' + str('se' in setY))

def p07(x,y,z):
    print('{}時の{}は{}'.format(x,y,z))

def p08(words):
    res = ''
    for i in words:
        if i.islower():
            res += chr(219-ord(i))
        else:
            res += i
    return res

import random
def p09():
    words = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .".split(' ')
    res = []
    for i in words:
        if len(i) <= 4:
            res.append(i)
        else:
            change_list = list(i[1:-1])
            random.shuffle(change_list)
            res.append(i[0] + ''.join(change_list) + i[-1])

    print(res)




p00()
p01()
p02()
p03()
p04()
p05(2)
p06()
p07(12,'気温','22.4')

words = input()
res = p08(words)
print(res)
res_composie = p08(res)
print(res_composie)
if res_composie!=words:
    print('composite error')
p09()
