from collections import deque

# List of job postings
jobs = [
    {"id": 1, "title": "Software Engineer", "company": "TechCorp", "location": "Remote", "description": "Develop and maintain software applications."},
    {"id": 2, "title": "Graphic Designer", "company": "DesignWorks", "location": "Remote", "description": "Create engaging visual content."},
    {"id": 3, "title": "Data Scientist", "company": "DataCo", "location": "Remote", "description": "Analyze and interpret complex data."},
    {"id": 4, "title": "Project Manager", "company": "BuildIt", "location": "Remote", "description": "Oversee and manage projects."}
]

job_postings_queue = deque()
undo_stack = []

def display_jobs():
    print("\nAvailable Job Opportunities:")
    for job in jobs:
        print(f"{job['id']}: {job['title']} at {job['company']} | Location: {job['location']}")
        print(f"   Description: {job['description']}")
    print()

def apply_for_job(job_id, name, email, resume_link):
    job = next((job for job in jobs if job["id"] == job_id), None)
    if job:
        application = {"job": job, "name": name, "email": email, "resume_link": resume_link}
        job_postings_queue.append(application)
        undo_stack.append({"action": "apply", **application})
        print(f"Successfully applied for {job['title']} at {job['company']}!")
    else:
        print("Job not found!")

def undo_application():
    if undo_stack:
        last_action = undo_stack.pop()
        if last_action["action"] == "apply":
            application_to_remove = {"job": last_action["job"], "name": last_action["name"], "email": last_action["email"], "resume_link": last_action["resume_link"]}
            if application_to_remove in job_postings_queue:
                job_postings_queue.remove(application_to_remove)
                print(f"Application for {last_action['job']['title']} at {last_action['job']['company']} has been undone.")
    else:
        print("No actions to undo.")

def view_applications():
    print("\nYour Job Applications:")
    if job_postings_queue:
        for application in job_postings_queue:
            job = application["job"]
            print(f"Name: {application['name']} - {job['title']} at {job['company']} | Resume: {application['resume_link']}")
    else:
        print("You have no applications.")

def main():
    while True:
        display_jobs()
        print("1. Apply for a job")
        print("2. View my applications")
        print("3. Undo last application")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            job_id = int(input("Enter job ID to apply: "))
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            resume_link = input("Enter link to your resume: ")
            apply_for_job(job_id, name, email, resume_link)
        elif choice == '2':
            view_applications()
        elif choice == '3':
            undo_application()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()