count = 0
numtimes = len(s)
newstr = ''
begin = 0
for numtimes in s:
    while begin+2 < len(s):
        newstr= s[begin]+s[begin+1]+s[begin+2]
        if newstr == 'bob':
            count +=1
        begin +=1
      
print 'Number of times bob occurs is: '  + str(count)