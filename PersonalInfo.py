name = input('Enter your name: ')
address = input('Enter your address with state, city and zip code: ')
tel_no = input('Enter your telephone number: ')
college_major = input('Enter your college major: ')

print(name, address,tel_no,college_major,sep='\n')
# print('Your details are: %s,%s,%s,%s' %(name,address,tel_no,college_major), sep='\n')
print('Your details are: {name},{address},{tel_no},{major}'.format(name = name, address = address, tel_no = tel_no,
       major = college_major), sep='\n')