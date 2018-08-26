#z = list(range(1,11,1))
h = [z/10 for z in range(11)]
print(h)
ss = [{s, s**2, s**3} for s in range(-10 ,10)]
#[f**2 for f in range(5)]
print(ss)
slownik = {'aaa', 'b', 'c'}
c = {x: len(x) for x in slownik}
print(c)

