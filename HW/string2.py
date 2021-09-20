
def verbing(s):
	if(len(s)>3):
		if(s[-3:]=='ing'):
			s+='ly'
		else:
			s=s+'ing'
	return s

def not_bad(s):
	if( "not" in s and "bad" in s and s.index('bad')>s.index('not')):
			s=s[:s.index('not')] + 'good' + s[s.index('bad')+3:]
	return s
	
def front_back(a, b):
	if(len(a)%2==1):
		ma=len(a)//2+1
	else:
		ma=len(a)//2
	if(len(b)%2==1):
		mb=len(b)//2+1
	else:
		mb=len(b)//2
	f=a[:ma] + b[:mb] + a[ma:] + b[mb:]
	return f


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print( 'verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()