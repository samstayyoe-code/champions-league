import json
f=open("test.json")

data=json.load(f)
# 1-shart------------------------

# for i in data['branches']:
#     print(i['name'])

# 2-shart----------------------

# for branches in data['branches']:
#     for teachers in branches["teachers"]:
#         if teachers["subject"]=="Python":
#             print(f"ism: {teachers["name"]}  branchi:{branches["name"]}   tajribasi:{teachers["experience"]}")

# 3-shart----------------------------------

# for branches in data["branches"]:
#     print(branches["name"], len(branches["students"]))

# 4-shart-------------------------------
# all_students=[]
# for branches in data["branches"]:
#     for student in branches["students"]:
#         all_students.append((student,branches["name"]))
# max_student=max(all_students,key=lambda x: x[0]["payment"])
# print(max_student[0]["name"],max_student[1])

# 5-shart---------------------------------

# for branches in data["branches"]:
#         total=0
#         for student in branches["students"]:
#                 total+=student["payment"]
#         print(branches["name"],total)

# 6-shart------------------------------

# for branches in data["branches"]:
#     for teachers in branches["teachers"]:
#         if teachers["experience"]>=5:
#             print(teachers["name"],branches["name"])

# 7-shart-------------------------------------

for branches in data["branches"]:
    check=True
    for students in branches["students"]:
        if students["course"]!="Python":
            check=False
    if check:
        print(branches["name"])
f.close()