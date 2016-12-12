students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def studentsName(arr):
    for i in arr:
        print ('{} {}'.format(i['first_name'],i['last_name']))

studentsName(students)

print ('\n')

def studentsFaculty(arr):
    for i in arr:
        print (i)
        ol = 0
        for j in arr[i]:
            ol += 1
            print ('{} - {} {} - {}'.format(
                ol,
                j['first_name'].upper(),
                j['last_name'].upper(),
                (len(j['first_name'])+(len(j['last_name']))))
                )


studentsFaculty(users)
