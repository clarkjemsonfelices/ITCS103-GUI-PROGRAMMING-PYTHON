import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet['A1'] = "ID"
sheet['B1'] = "First Name"
sheet['C1'] = "Last Name"
sheet['D1'] = "Birth Year"
sheet['E1'] = "Age"

for fav in range(2, 5, 1):
	print(f"\nPerson {fav - 1}")
	fname = input("Enter first name: ")
	lname = input("Enter last name: ")
	birth = int(input("Enter birth year: "))
	age = 2026 - birth
	
	sheet[f'A{fav}'] = fav - 1
	sheet[f'B{fav}'] = fname
	sheet[f'C{fav}'] = lname
	sheet[f'D{fav}'] = birth
	sheet[f'E{fav}'] = age
print("\nFavorite people saved successfully!")

print("\n===== FAVORITE PEOPLE LIST =====")
for rows in sheet.iter_rows(values_only=True):
	print(rows)
workbook.save("favorite_people.xlsx")