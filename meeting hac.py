# Meeting Prep Agent (Simple VS Code Version)

memory = []

def add_meeting():
    print("\n📝 Add New Meeting")
    topic = input("Enter topic: ")
    notes = input("Enter notes: ")
    tasks = input("Enter tasks: ")

    memory.append({
        "topic": topic,
        "notes": notes,
        "tasks": tasks
    })

    print("✅ Meeting saved successfully!")

def show_history():
    print("\n📜 Meeting History:")
    
    if not memory:
        print("No meetings yet.")
        return

    for i, m in enumerate(memory):
        print(f"\nMeeting {i+1}")
        print("Topic:", m["topic"])
        print("Notes:", m["notes"])
        print("Tasks:", m["tasks"])

def suggest_meeting():
    print("\n💡 Smart Meeting Suggestion:")

    if not memory:
        print("No data available.")
        return

    last = memory[-1]

    print("👉 Continue discussion on:", last["topic"])
    print("👉 Review notes:", last["notes"])
    print("👉 Pending tasks:", last["tasks"])

    print("\n📊 Based on history:")
    for m in memory[:-1]:
        print("-", m["topic"])

while True:
    print("\n===== MEETING PREP AGENT =====")
    print("1. Add Meeting")
    print("2. Show History")
    print("3. Suggest Next Meeting")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_meeting()
    elif choice == "2":
        show_history()
    elif choice == "3":
        suggest_meeting()
    elif choice == "4":
        print("Exiting... Bye!")
        break
    else:
        print("Invalid choice. Try again.")