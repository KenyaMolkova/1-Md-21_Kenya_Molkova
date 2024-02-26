n = int(input())
for i in range(n):
    word = input()
    if 'ф' in word:
        print('Ого! Это редкое слово!')
    else:
        print('Эх, это не очень редкое слово...')