# 🚀 Parallel and Distributed Computing Repository

## 📖 Overview
This repository contains Python scripts and accompanying resources focused on **Parallel and Distributed Computing**. The projects explore key concepts, including:

- 🛠️ **Inter-Process Communication (IPC)**
- 🔄 **Synchronization Techniques**
- ✉️ **Message Passing Interface (MPI)**
- ⚙️ **Thread and Process Management**

The repository is organized into structured chapters to aid systematic learning and exploration of these concepts.

---

## 📂 Repository Structure

### 📁 **chapter1**
Core topics in **Parallel and Distributed Computing**:

- `IPC.py` - 🛠️ Demonstrates Inter-Process Communication.
- `MPI.py` - ✉️ Implements Message Passing Interface for distributed systems.
- `ProcessCreationAndManagement.py` - ⚙️ Introduces process creation and management in Python.
- `SynchronizationPrimitive.py` - 🔒 Covers synchronization mechanisms for shared resources.

### 📁 **chapter2**
Advanced topics and practical applications of synchronization:

- `Rlock.py` - 🔒 Demonstrates recursive locks.
- `Semaphore.py` - 📏 Explores semaphore concepts.
  - `Semaphore.txt` - 📄 Notes explaining semaphores.
- `ThreadSyncWithBarrier.py` - 🔗 Implements thread synchronization using barriers.
  - `ThreadSyncWithBarrier.txt` - 📄 Explanation of the implementation.
- `ThreadSyncWithCondition.py` - ⚙️ Demonstrates thread synchronization with condition variables.
  - `ThreadSyncWithCondition.txt` - 📄 Supporting notes for condition variables.
- `ThreadSyncWithEvent.py` - 📡 Thread synchronization using events.
  - `ThreadSyncWithEvent.txt` - 📄 Explanation of event-driven synchronization.
- `ThreadSyncWithQueue.py` - 📦 Thread communication using queues.

---

## 🛠️ Getting Started

### 🔧 Clone the Repository
To get started, clone the repository to your local system:
```bash
git clone https://github.com/<YourUsername>/<RepositoryName>.git

📂 Navigate and Run

Navigate to the desired chapter and run the script:

cd chapter1
python IPC.py

🧰 Requirements

    Python 3.x (Ensure you have Python installed on your system)
    Additional dependencies (if required) can be installed via:

    pip install -r requirements.txt

🗂️ Topics Covered

This repository covers the following topics:

    🛠️ Inter-Process Communication (IPC)
    ✉️ Message Passing Interface (MPI)
    ⚙️ Process Creation and Management
    🔒 Synchronization Techniques:
        Recursive locks
        Semaphores
        Barriers
        Condition variables
        Events
        Queues

🤝 Contributing

Contributions are welcome! Here's how you can contribute:

    Fork the repository.
    Create a new branch for your feature or bugfix:

git checkout -b feature-name

Commit your changes:

git commit -m "Add feature-name"

Push your changes and create a pull request:

    git push origin feature-name

Feel free to explore, modify, and expand this repository to enhance its utility. 😊
