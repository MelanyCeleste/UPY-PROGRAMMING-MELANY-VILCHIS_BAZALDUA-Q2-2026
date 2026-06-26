users = {
    'jperez':   {
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo':    {
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez':  {
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez':   {
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc':  {
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam':   {
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo': {
        'password': '1234',
        'rol': 'teacher',  # Corregido: antes decía 'professor'
        'name': 'Jorge Pedrozo'
    },
    'dgamboa':  {
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

# Cambiado el nombre de 'notes' a 'grades' para unificar con el resto del código
grades = {
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
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users and password == users[username]["password"]:
        rol = users[username]["rol"]
        name = users[username]['name']

        if rol == 'student':
            print(f"\nWelcome {name} ({rol})")
            print(f"Grades of {name}")
            
            approved = set()
            
            for subject in subjects:
                grade = grades[username][subject]
                print(f"{subject}: {grade}")
                
                if grade >= 8.0:
                    approved.add(subject)
                    
            pending = set(subjects) - approved
            
            print(f"\nApproved subjects: {approved}")
            print(f"Pending subjects: {pending}")

        elif rol == "teacher":
            print(f"\nRol: {rol}")
            print("Students:")
            for user in grades:
                print(users[user]["name"])
            
            print("\nSubjects:")
            for subject in subjects:
                print("-", subject)
                
            change = input("\nDo you want to change a student's grade? (yes/no): ")
            while change.lower() == "yes":
                # Se pide el username para poder buscarlo en el diccionario
                student = input("Student (username): ")
                subject = input("Subject: ")
                
                if student in grades and subject in subjects:
                    new_grade = float(input("Grade New: "))
                    confirm = input("Are you sure (yes/no): ")
                    
                    if confirm.lower() == "yes":
                        grades[student][subject] = new_grade
                        print("\nUpdated ratings of", users[student]["name"])
                        for subj in subjects:
                            print(f"{subj}: {grades[student][subj]}")
                else:
                    print("Student or subject doesn't exist.")
                    
                change = input("\nDo you want to change a student's grade? (yes/no): ")

        elif rol == "coordinator":
            print("\nTeachers:")
            for user, data in users.items():
                if data["rol"] == "teacher":
                    print(data["name"])
                    
            print("-" * 65)
            print(f"{'Student':20}|{'Discrete Mathematics':22}|{'Programming':12}|{'English II':10}")
            print("-" * 65)
            
            for student, student_grades in grades.items():
                print(
                    f"{users[student]['name']:20}|"
                    f"{student_grades['Discrete Mathematics']:<22}|"
                    f"{student_grades['Programming']:<12}|"
                    f"{student_grades['English II']:<10}"
                )
                
        # Sale del ciclo `while` después de ejecutar exitosamente el menú
        break
        
    else:
        print("User/password don't exist. Please try again.\n")