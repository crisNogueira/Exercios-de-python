import time
for c in range(10, -1, -1):
    time.sleep(1)
    print('\033[33m{}\033[m'.format(c))
time.sleep(1)
print('\033[31m Kabum\033[m')
