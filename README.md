# 🏥 Patient Registration System (Flask + C Integration)

## 📌 Overview

This project is a **hybrid system** that combines:

* **Flask (Python)** → Handles web interface and routing
* **C Program (.exe)** → Handles core processing and file storage

The system allows users to:

1. Fill a patient registration form
2. Process data using a C backend
3. Store patient details in a file
4. Display confirmation on the webpage

# 🧠 Architecture

```
Frontend (HTML)
      ↓
Flask (Python)
      ↓
Subprocess (OS call)
      ↓
C Executable (.exe)
      ↓
File Storage (patients.txt)
      ↓
Output → Flask → HTML
```

---

# 🔁 Complete Workflow

### Step 1: User Input (Frontend)

* User fills the patient form (name, age, phone, etc.)
* Form is submitted using **POST request**

---

### Step 2: Flask Receives Data

Flask extracts data using:

```python
request.form["name"]
```


### Step 3: Data Serialization

Flask converts all fields into a single string:

```python
data_string = "name|age|gender|phone|address|..."
```

👉 This is done because C programs receive input via command-line arguments (`argv`).

---

### Step 4: Subprocess Call

Flask calls the C program:

```python
subprocess.run([exe_path, data_string])
```

---

### Step 5: C Program Execution

The C program:

1. Receives input via `argv[1]`
2. Splits data using `strtok()` with delimiter `|`
3. Stores data in a `struct`
4. Writes data into `patients.txt`
5. Generates patient ID
6. Returns output using `printf()`

---

### Step 6: Output Handling

Flask captures output:

```python
result.stdout
```

Splits it and sends it to HTML using:

```python
render_template()
```

---

### Step 7: Display to User

User sees:

* Patient ID
* Visit Type
* Priority

---

# ⚙️ Role of Flask

Flask acts as the **controller (middle layer)**:

### Responsibilities:

* Handle HTTP requests (GET/POST)
* Collect form data
* Prepare data for C program
* Call external program using subprocess
* Receive output
* Render HTML templates

👉 Flask does **NOT process core logic** — it delegates that to C.

---

# ⚙️ What is Subprocess?

## Definition:

`subprocess` is a Python module used to **run external programs**.

---

## Why use subprocess?

Because:

* Python cannot directly execute C code
* But it CAN execute compiled programs (.exe)

---

## How it works internally:

```python
subprocess.run(["program.exe", "input"])
```

### OS does:

1. Creates a new process
2. Loads `.exe` into memory
3. Passes input as arguments (`argv`)
4. Executes program
5. Returns output to Python

---

## In this project:

```python
subprocess.run([exe_path, data_string])
```

* `exe_path` → C executable
* `data_string` → passed as `argv[1]`

---

# 🔗 Integration of Subprocess

This is the **bridge between Flask and C**

| Flask (Python)   | C Program                |
| ---------------- | ------------------------ |
| Sends string     | Receives via argv        |
| Calls subprocess | Runs as separate process |
| Gets stdout      | Uses printf()            |

---

# 💻 Why `.exe` and not `.c` file?

## ❌ You cannot run `.c` file directly

Because:

* `.c` is source code
* Needs compilation

---

## ✅ `.exe` is compiled code

Created using:

```bash
gcc patient.c -o patient.exe
```

---

## Advantages of `.exe`:

* Faster execution
* OS can run it directly
* No need to compile every time
* More efficient for backend processing

---

# 🧠 Role of C Program

The C program acts as the **core processing engine**

### Responsibilities:

* Parse input data
* Store structured data
* Handle file operations
* Generate unique ID
* Return output

---

# 📁 File Storage (Database Simulation)

File used:

```
Backend/patients.txt
```

---

## Format:

```
id|name|age|gender|phone|address|symptoms|visit_type|priority
```

---

## Example:

```
1|Sarvesh|23|Male|7904515049|Chennai|fever|New|Normal
```

---

# 🧱 Key Concepts Used

### 1. Flask (Web Framework)

* Routing
* Templates
* Form handling

---

### 2. Subprocess (OS Interaction)

* Running external programs
* Process creation

---

### 3. C Programming

* `struct`
* `strtok()` (string parsing)
* File handling (`fopen`, `fprintf`)

---

### 4. Data Serialization

* Using `|` to pass structured data

---

### 5. File as Database

* Simple storage system

---

# ⚠️ Challenges Faced

### Bug:

Data misalignment (phone + address merged)

### Cause:

* Struct field size too small
* Memory overflow

### Fix:

* Increased buffer sizes
* Used safe string handling

---

# 🚀 Future Improvements

* Replace `|` with JSON (more robust)
* Use database (MySQL / SQLite)
* Add queue system (priority handling)
* Add search & update features
* Improve UI/UX

---

# 🧾 Summary

This project demonstrates:

* Integration of **web + system programming**
* Communication between **Python and C**
* Use of **OS-level process execution**
* Real-world backend architecture

---

# 🗣️ One-Line Explanation

> “This system uses Flask as a controller to collect user input, sends it to a C program via subprocess for processing and storage, and returns the result to the frontend.”

---

# 🙌 Learning Outcome

After this project, you understand:

* How frontend connects to backend
* How different languages can work together
* How OS executes programs
* How real systems handle data flow

---
