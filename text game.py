AI_NAME = 'Terminator'
username = 'Try User 01'
trust_level = 0
#We are declarating empty variables
age = None
gender = None
email=None
bank_account = None
number= None

print( f'Hello experiment, {username}, my name is {AI_NAME}' )

# Change names
answer = input('Would you like to change your user name?(y/n)')
if answer == 'y':
	username = input(f'({username})New Name:')

answer = input(f'Would you like to change my name({AI_NAME})?(y/n)')
if answer == 'y':
	AI_NAME = input(f'({AI_NAME})New Name:')

# Ask user input
print("I will ask for some data, if you don't want to tell me. It's ok, but remember I'm looking for paterns in your personality")

str_age = input('Age:')
if( str_age != ''):
	trust_level = trust_level + 1
	age = int(str_age)

str_gender = input('Gender(m or f):')
if( str_gender != ''):
	if str_gender == 'm':
		gender = 'Male'
		trust_level = trust_level + 1
	elif str_gender == 'f':
		gender = 'Female'
		trust_level = trust_level + 1
	else:
		print(f'({str_gender}) It does not exist already in my database ')

str_email = input('Can I Know your E-mail:')
if str_email != '':
	trust_level = trust_level + 1
	email = str_email

# Check for trust level
if trust_level >=2:
	answer = input( 'Can you bring me your phone number? (y/n)' )
	if answer== 'y':
		trust_level = trust_level + 1
		phone_number = input( 'Phone number:' )

if trust_level >=3:
	answer = input( 'Can I have your bank account? (y/n)' )
	if answer== 'y':
		trust_level = trust_level + 1
		bank_account = input( 'Account number:' )

# Selection of the response
if trust_level < 3:
	print( f'Ok I cannot work like this {username}. The next time you will be able to answer my questions')
elif trust_level <5:
	print( f"That's all the information that I want to know, {username}. I look forward talk more with you.")
else:
	# Trust level is high
	print( f"Thank you, you are really great {username}. Please let me know if you need anything it does not matter." )
	print( '...')

# Internal configuration
print('--------------------------------')
print( f"{AI_NAME}'s Auto Install Ejecution" )
print('--------------------------------')
if gender != None:
    print( 'It cannot be a posible answer ' )
	if gender =='Male':
		print( 'TODO: Ask for favorite beard length' )
	elif gender =='Female':
		print( 'TODO: Ask for favority hair length' )
if age != None and age < 17:
	print( 'REPORT USE TO: Contacts MOM and DAD ' )
    contac=input('Please bring me the number of your mom or your dad({number})?')
    print('Calling to your parents, Do not worry')
if age >18:    
    if bank_account != None:
        print( 'WATCH: Autopayment options for special services' )
