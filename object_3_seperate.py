def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) /4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student))

students = [
     
    create_student("김선우", 100, 99, 98, 97),                  
    create_student("김", 100, 59, 28, 97),
    create_student("선우", 100, 79, 98, 77),
    create_student("김우", 100, 39, 88, 97)        
    
]

print("이름", "총점", "평균", sep= "\t")
for student in students:
    print(student_to_string(student))