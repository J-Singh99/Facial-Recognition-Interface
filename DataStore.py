DB = {}

i = 1
a = 'LOL'
print('All training files should be within the "Training Folder"!!!')

while(a != 'N'):
	Name = input('Enter the full name: ')
	Age = int(input('Enter the age: '))
	Gender = input('Enter gender (M/F): ')
	Number = int(input('Enter phone number: '))
	Balance = int(input('Enter account balance: '))
	FileName = input('Enter the file name: ')

	Entry = {
		"ID" : i,
		"Name": Name,
		"Age" : Age,
		"Gender" : Gender,
		"Number" : Number,
		"Balance" : Balance,
		"FileName" : 'Training Folder/' + FileName
	}
	
	DB[i] = Entry
	
	i += 1
	a = input('Enter "N" to exit!')
	print()
	print()