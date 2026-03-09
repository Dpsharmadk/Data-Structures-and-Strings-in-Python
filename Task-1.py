#this is the program for task 1 of assignment 5 
#creating a dictionary first 
student_marks = {
    "Dev":99,
    "Pritish":69,
    "Aryan":78,
    "Sameer":44,
    "Adarsh":92,
    "Riya":55
}

# Ask user to input student's name
name = input("Enter the student's name: ")

# Retrieve and display the marks
if name in student_marks:
    print("Marks of", name, "are:", student_marks[name])
else:
    print("Student not found in the record.")