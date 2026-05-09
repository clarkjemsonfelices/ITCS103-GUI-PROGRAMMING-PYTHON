import os
# DREAMS FILE MANAGER

os.system('cls')
while True:
	print()
	print("===== DREAMS FILE MANAGER =====\n")
	print("1. Read inspiring messages")
	print("2. Add a new inspiring message")
	print("3. Rewrite the entire file")
	print("4. Exit\n")
	
	choice = input("Enter your choice: ")
	os.system('cls')
	
	# Read
	if choice == '1':
		file = open("dreams.txt", "r")
		content = file.read()
		file.close()
		
		print("----- Inspiring Messages -----")
		print(content)
		
	# Append
	elif choice == '2':
		new = input("Enter new inspiring line: ")
		
		file = open("dreams.txt", "a")
		file.write(f"\n{new}")
		file.close()
		print("\nYour inspiration has been added!")
		
	# Overwrite
	elif choice == '3':
		print("Warning: This will overwrite the file.")
		confirm = input("Type YES to continue: ").upper()
		
		if confirm == 'YES':
			new = input("Write your new set of inspiring messages: ")
			file = open("dreams.txt", "w")
			file.write(f"\n{new}")
			file.close()
			print("File has been overwritten.")
		else:
			print("Cancelled.")
			
	# Exit
	elif choice == '4':
		print("Dreams file manager exits")
		break
	
	else:
		print("Please enter a valid choice (1-4)")