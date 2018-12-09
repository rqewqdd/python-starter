def get_student(student_list,student_name,student_val):
    print(student_list[student_name][student_val])

stname = input()

student = {'철수':{'age':20,'tall':180},
           '영희':{'age':20,'tall':150}}

get_student(student, stname, 'age')
get_student(student, stname, 'tall')

