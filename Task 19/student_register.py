# This python prograns allows students to register for an exam venue.
# It asks the user for the number of students, ans asks for their IDs and
# saves the information to a text file

no_of_students = int(input("Enter the number of students: "))

file = open('reg_form.txt', 'w')

# Loop through the number of students, ask for thier Ids and write them to
# the file
for i in range(no_of_students):
    id_num = input(f"Enter Id number for student #{i+1}: ")
    file.write(id_num+'\n')

file.close()
print("All ID numbers saved to reg_form.txt")
