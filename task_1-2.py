count = int(input())
h = str(count // 3600).rjust(2, '0')
m = str(count // 60 % 60).rjust(2, '0')
s = str(count % 60).rjust(2, '0')

print(f'{h}:{m}:{s}')
