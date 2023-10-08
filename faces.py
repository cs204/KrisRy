a = str(input())
def conv(x):
    x = x.replace(':)','\N{Slightly Smiling Face}')
    x = x.replace(':(','\N{Slightly Frowning Face}')
    return x
print(conv(a))