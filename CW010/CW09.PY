users = {
    'jperez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo':	{
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa':	{
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2},
}

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users and password == users[username]["password"]:
        break
    
    rol = users[username]["rol"]
    name = users[username]['name']

        if rol == 'student':
        
        print(f"Welcome {name} ({rol})")
        print(f"Grades of {name}")
        
        approved = set()
    
            for subject in subjects:
                grade = notes[username][subject]
                print(f"{subject}: {grade}")
                
                if grade >= 8.0:
                    approved.add(subject)
                    
            pending = set(subjects) - approved
            
            print(f"Approved subject: {approved}")
            print(f"Pending subject: {pending}")

        elif rol == "teacher":
            print("Rol:", users[username]["rol"])
            print("Students:")
            for user in grades:
                print( users[user]["name"])
                print()
            print("Subjects:")
            for subject in subjects:
                print("-", subject)
            change = input("Do you want to change a student's grade? (yes/no)")
            while change == "yes":
                student = input("Student: ")
                subject = input("subject: ")
                if student in grades and subject in subjects:
                    new_grade = float(input("Grade New: "))
                    confirm = input("Are you sure (yes/no):  ")
                    if confirm == "yes":
                        grades[student][subject] = new_grade
                        print("Updated ratings of", users[student]["name"])
                        for subject in subjects:
                            print(subject, grades[student][subject])
                else:
                    print("Student don't exists")
                change = input("Do you want to change a student's grade? (yes/no)")

        elif rol == "coordinator":

            print("Teachers:")
            for user, data in users.items():
                if data["rol"] == "teacher":
                    print(data["name"])
                    
            print("-" * 60)
            print(f"{'Student':20}|{'Discrete Mathematics':12}|{'Programming':12}|{'English II':8}")
            print("-" * 60)
            
            for student, notes in grades.items():
                print(
                    f"{users[student]['name']:20}|"
                    f"{notes['Discrete Mathematics']:12}|"
                    f"{notes['Programming']:12}|"
                    f"{notes['English II']:8}"
                    )
            

        else:
            print("User/password don't exist")