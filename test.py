from itertools import*;m,p,q,r,s,l,a=dict(enumerate("276951438")),[[],[]],0,print,' │ │ ','─┼─┼─','XO';b=[*map(list,[s,l,s,l,s])];f=lambda:r('\n'.join(map(''.join,b)));f()
while m:
 i=int(input(a[q]+' move: '))-1;p[q]+=[int(m.pop(i))];b[~(i//3*2)][i%3*2]=a[q];f()
 if any(sum(d)==15for d in combinations(p[q],3)):r(a[q]+' wins');break
 q^=1
else:r('Draw')