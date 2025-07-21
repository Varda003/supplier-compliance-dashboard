# Supplier Compliance Dashboard 🚀

A full-stack web application to manage and monitor supplier compliance data using a clean, responsive frontend (React + Tailwind CSS) and a fast, scalable backend (FastAPI + SQLite).

---
## Here are some visuals to give you an idea of the project:

![UI Design](assets/image1.png) <!-- Replace with the actual path -->
*Figure 2: User Interface Design.*
<br><br>
<br><br>
![Project Overview](assets/image2.png) <!-- Replace with the actual path -->
*Figure 1: Overview of the project.*
<br><br>
<br><br>
![Features Demo](assets/image4.png) <!-- Replace with the actual path -->
*Figure 3: Features in action.*
<br><br>
<br><br>

---

## 🧩 Features

- 📂 Upload and manage supplier compliance data via Excel sheets  
- 🧾 View, add, update, and delete supplier entries  
- ⚡ Real-time communication between frontend and backend  
- 🎨 Intuitive and minimal UI using React + Tailwind CSS  
- 🛡️ Environment variable protection and clean Git repo setup  

---

## 🖥️ Tech Stack

| Layer       | Technology         |
|------------|--------------------|
| Frontend   | React, Tailwind CSS |
| Backend    | FastAPI, SQLAlchemy |
| Database   | SQLite (local)      |
| API Comm.  | REST (JSON)         |

---


---

## ⚙️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Varda003/supplier-compliance-dashboard.git
cd supplier-compliance-dashboard
```
### 2. Backend Setup (FastAPI)
bash
Copy
Edit
cd backend
pip install -r requirements.txt
python main.py
Make sure to set up a .env file in /backend using .env.example as reference.

### 3. Frontend Setup (React)
bash
Copy
Edit
cd ../frontend
npm install
npm start
Set up a .env file in /frontend using .env.example.

### 🧪 Sample .env.example Files
frontend/.env.example
```env
Copy
Edit
VITE_API_URL=http://localhost:8000
```
backend/.env.example
```env
Copy
Edit
DATABASE_URL=sqlite:///./supplier.db
```
---

## Contact
LinkedIn: [https://www.linkedin.com/in/varda15]

Email: varda.hanwant03@gmail.com

---

## Contributions
Contributions to enhance features or fix issues are welcome. Fork this repository, make changes, and create a pull request.

---

## License
This project is licensed under the MIT License.


