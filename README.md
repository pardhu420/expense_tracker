# Expense Tracker Web Application

A Flask-based Expense Tracker that allows multiple users to register, log in, and manage their personal expenses.  
It includes dark mode, Bootstrap styling, category summaries, and persistent JSON-based storage — all in a simple and functional web interface.

---

## Features

- User authentication (login and registration)
- Multiple user support (each user has their own expense data)
- Add, view, and delete expenses
- Dark mode toggle for better user experience
- Category-wise total expense summary
- JSON-based local storage (no database required)
- Clean Bootstrap interface with responsive design

---

## Technologies Used

| Component | Technology |
|------------|-------------|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript, jQuery |
| Data Storage | JSON (Local Files) |
| Environment | Works on Windows, macOS, and Linux |

---

## Folder Structure

```
expense_tracker/
│-- app.py
│-- users.json
│-- expenses.json
│-- requirements.txt
│-- README.md
│-- templates/
│   │-- login.html
│   │-- register.html
│   │-- index.html
│-- static/
│   │-- style.css
│   │-- script.js
```

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/pardhu420/expense_tracker
cd expense-tracker
```

### 2. Create a Virtual Environment (Optional)
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate   # On macOS/Linux
```

### 3. Install Dependencies
Create a `requirements.txt` file with:
```
flask
```

Then run:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access in Browser
Open your web browser and visit:
```
http://127.0.0.1:5000
```

---

## Usage

### Login and Registration
- Default credentials:
  ```
  username: admin
  password: admin
  ```
- New users can register through the **Register** page.

### Adding an Expense
1. Fill out the expense form with date, amount, category, and description.
2. Click **Add Expense**.
3. The expense will appear in your list along with the total and category summary.

### Deleting an Expense
- Click the **Delete** button beside any entry to remove it.

### Dark Mode
- Click the **Toggle Dark Mode** button to switch themes.

---

## Data Storage

- **User Data (users.json)**  
  Example:
  ```json
  [
      {"username": "admin", "password": "admin"},
      {"username": "user1", "password": "pass1"}
  ]
  ```

- **Expense Data (expenses.json)**  
  Example:
  ```json
  [
      {
          "username": "admin",
          "date": "2025-10-08",
          "amount": 250,
          "category": "Food",
          "description": "Lunch"
      }
  ]
  ```

---

## Future Enhancements

- Visual charts for expense breakdowns using Chart.js
- Search and filter features
- Monthly spending reports
- Export data to CSV or Excel
- Password hashing for improved security
- Cloud database integration (SQLite/MySQL)

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|----------|----------------|-----------|
| `TemplateNotFound: index.html` | Templates folder missing or misplaced | Ensure `templates/` exists with all HTML files |
| `JSONDecodeError` | Empty or invalid JSON file | Replace file content with `[]` |
| `All fields are required!` | Incomplete form submission | Fill all form fields before submitting |
