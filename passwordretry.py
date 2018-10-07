i = 3
while True :
	password = input('input pasword: ')
	if password == 'a123456':
		print('sign in success!')
		break
	else:
	    i = i - 1
	    print('wrong password ', i ,'chance to sign in')	
	    if i == 0:
		     break
		