# Task Management API

## Student Information
- Name: 
- Department: Department of Informatics
- University: Ionian University
- Course: Software Engineering
- Academic Year: 

## Περιγραφή

Αυτό το έργο υλοποιεί ένα απλό RESTful API για τη διαχείριση εργασιών.
Κάθε εργασία περιλαμβάνει:

- id
- username
- title
- description
- deadline

Το API έχει δημιουργηθεί χρησιμοποιώντας **Python και Flask** και αποθηκεύει δεδομένα σε μια βάση **SQLite**.

## Διαθέσιμα Endpoints

- `GET /tasks` – Retrieve all tasks
- `GET /tasks/{id}` – Retrieve a task by ID
- `POST /tasks` – Create a new task
- `DELETE /tasks/{id}` – Delete a task by ID

## Δοκιμές

Οι δοκιμές μονάδας έχουν γραφτεί χρησιμοποιώντας το πλαίσιο `unittest` της Python και επαληθεύουν:

- Task creation
- Task retrieval
- Error handling
