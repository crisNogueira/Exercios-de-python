from time import sleep
def maior(* a):
    ma = 0
    for c in range(0, len(a)):
        if c == 0:
            ma = a[c]
        if a[c] > ma:
            ma = a[c]
    print('-='*30)
    print('Analisando os valores passados...')
    for c in a:
        print(c, end=' ')
        sleep(0.5)
    print(f'foram informados {len(a)} valores ao todo.')
    print(f'O maior valor informado foi {ma}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
