AI_NAME = 'what kind of pozole are you'
username = 'User etc'
level_verde = 0
level_rojo = 0
age = None
gender = None
email=None
number= None

print( f'Hello experiment, {username},I am going to help you to know {AI_NAME}' )

fanswer=input(f'would you like some green sauce in your pozole?(yes/no)')
if fanswer =='yes':
    level_verde=level_verde + 1
else:
    level_rojo=level_rojo + 1

sanswer=input(f'would you like some chiken in your pozole?(yes/no)')
if sanswer=='yes':
    level_verde=level_verde+1
else:
    level_rojo=level_rojo+1

tanswer=input(f'would you like some oregano in your pozole?(yes/no)')
if tanswer=='yes':
    level_verde=level_verde+1
else:
    level_rojo=level_rojo+1

str_age = input('Introduce your Age:')
if( str_age != ''):
	level_rojo=level_rojo+1
	age = int(str_age)

str_gender = input('Introduce your Gender(m or f):')
if( str_gender != ''):
	if str_gender == 'm':
		gender = 'Male'
		level_verde=level_verde+1
	elif str_gender == 'f':
		gender = 'Female'
		level_rojo=level_rojo+1
	else:
		print(f'({str_gender}) does not exist in my database ')

if level_rojo < 3 or level_verde < 3:
	print( f'Well I cannot work like this {username}. Come again when you are decided')
elif level_rojo > 4 :
	print( f"That's all, {username}. I think you are green pozole.")
else:
	print( f"Thank you  {username}. I think you are red pozole." )
	print( '...')
