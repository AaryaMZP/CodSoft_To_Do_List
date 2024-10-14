import speech_recognition as sr
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Initialize the recognizer
recognizer = sr.Recognizer()

# Global to-do list
tasks = []

# Function to add tasks using voice
def add_task_voice():
    try:
        with sr.Microphone() as source:
            print("Listening for task...")
            audio = recognizer.listen(source)
            task = recognizer.recognize_google(audio)
            print(f"Task Recognized: {task}")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            tasks.append({"task": task, "deadline": deadline})
    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
    except sr.RequestError as e:
        print(f"Error with speech service: {e}")

# Function to add tasks manually
def add_task_manual():
    task = input("Enter task: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    tasks.append({"task": task, "deadline": deadline})

# Function to display all tasks
def display_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. Task: {task['task']}, Deadline: {task['deadline']}")
    print()

# Function to prioritize tasks
def prioritize_tasks():
    if not tasks:
        print("No tasks to prioritize.")
        return
    
    task_descriptions = [task['task'] for task in tasks]
    
    # Vectorize task descriptions
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(task_descriptions)
    
    # Use KMeans to cluster and prioritize tasks (can be tweaked for larger lists)
    

def prioritize_tasks(tasks):
    # Assuming 'tasks' is a list of tasks and each task has a priority score
    # Transform tasks into a suitable format for clustering
    X = [[task['priority']] for task in tasks]  # Example structure, adjust as needed

    # Check the number of tasks and set clusters accordingly
    kmeans = KMeans(n_clusters=min(len(X), 3))  # Ensure n_clusters is not more than the number of tasks

    # Fit the KMeans model
    kmeans.fit(X)

    # Get cluster labels and priorities
    labels = kmeans.labels_
    prioritized_tasks = sorted(zip(tasks, labels), key=lambda x: x[1])  # Sort tasks based on their cluster label

    return prioritized_tasks

    
    # Sort tasks by clusters (High to Low)
    clustered_tasks = sorted(zip(tasks, labels), key=lambda x: x[1])
    
    print("\nPrioritized Tasks:")
    for i, (task, priority) in enumerate(clustered_tasks, start=1):
        priority_label = "High" if priority == 0 else "Medium" if priority == 1 else "Low"
        print(f"{i}. Task: {task['task']}, Deadline: {task['deadline']}, Priority: {priority_label}")
    print()

# Main app
def to_do_list_app():
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task (Voice)")
        print("2. Add Task (Manual)")
        print("3. Display All Tasks")
        print("4. Prioritize Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task_voice()
        elif choice == '2':
            add_task_manual()
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            prioritize_tasks()
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    to_do_list_app()
