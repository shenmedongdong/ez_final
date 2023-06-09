import csv
import sys
import io

# raw_data_file = "DB_students_tc_utf8.csv"
# block_size = 100

# def split_blocks():
#     with open(raw_data_file, "r", encoding='utf-8') as file:
#         reader = csv.reader(file)
#         data = list(reader)

#     num_blocks = len(data) // block_size + 1

#     for i in range(num_blocks):
#         block_data = data[i * block_size : (i + 1) * block_size]
#         block_filename = f"block_{i+1}.csv"
        
#         with open(block_filename, "w", newline="", encoding='utf-8') as block_file:
#             writer = csv.writer(block_file)
#             writer.writerows(block_data)

# split_blocks()

# def create_sequence_index():
#     sequence_index = {}

#     num_blocks = 4654

#     for i in range(1, num_blocks+1):
#         block_filename = f"block_{i}.csv"
        
#         with open(block_filename, "r", encoding='utf-8') as block_file:
#             reader = csv.reader(block_file)
#             for row in reader:
#                 student_id = row[0]
#                 course_id = row[1]
#                 course_name = row[2]

#                 if student_id in sequence_index:
#                     sequence_index[student_id].append((course_id, course_name))
#                 else:
#                     sequence_index[student_id] = [(course_id, course_name)]

#     return sequence_index

# # sequence index 생성
# index = create_sequence_index()

# def search_courses_by_student_id(student_id):
#     if student_id in index:
#         courses = index[student_id]
#         print(f"Student ID: {student_id}")
#         print("Courses:")
#         for course_id, course_name in courses:
#             print(f"{course_id}, {course_name}")
#     else:
#         print(f"No courses found for student ID: {student_id}")

# # 학번을 입력하여 수강 과목 조회
# student_id = input("Enter student ID: ")
# search_courses_by_student_id(student_id)

def create_sequence_index():
    sequence_index = {}
    course_index = {}

    num_blocks = 4654

    for i in range(1, num_blocks+1):
        block_filename = f"block_{i}.csv"
        
        with open(block_filename, "r", encoding='utf-8') as block_file:
            reader = csv.reader(block_file)
            for row in reader:
                student_id = row[0]
                course_id = row[1]
                course_name = row[2]

                if student_id in sequence_index:
                    sequence_index[student_id].append((course_id, course_name))
                else:
                    sequence_index[student_id] = [(course_id, course_name)]

                if course_id in course_index:
                    course_index[course_id].add(student_id)
                else:
                    course_index[course_id] = {student_id}

    return sequence_index, course_index

# sequence index와 course index 생성
sequence_index, course_index = create_sequence_index()

def search_courses_by_course_id(input):
    if input in course_index:
        student_ids = course_index[input]
        print(f"Course ID: {input}")
        print("Student IDs:")
        for student_id in student_ids:
            print(student_id)
    elif input in sequence_index:
        student_ids = sequence_index[input]
        print(f"Student ID: {input}")
        print("Course ID:")
        for student_id in student_ids:
            print(student_id)
        #print(f"No students found for course ID: {course_id}")
    else:
        print("hello")

# 수강 번호를 입력하여 수강 과목을 선택한 모든 학생의 학번 출력
input = input("Enter course ID: ")
search_courses_by_course_id(input)
