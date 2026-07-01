python_skill = input("Do you know Python? (yes/no): ").lower()
experience = int(input("How many years of experience/projects do you have? "))
certificate = input("Do you have a degree or bootcamp certificate? (yes/no): ").lower()

if python_skill == "yes" and (experience >= 2 or certificate == "yes"):
    print("Congratulations! You have been accepted to the next interview stage.")
else:
    print("Sorry, your current qualifications do not match the job requirements.")