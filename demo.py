def function():
    print 'string'


def vovct(a):
	count=0
	for char in a:
		if char in 'aeiou':
			count = count+1
		return count


if __name__=='__main__':
    #when direct running
    print'direct execution'
    function()
    a = 'counter'
    print vovct(a)
    a=raw_input()
    print vovct(a)
else:
	#when importing
	print 'imported'