# financial-tracker-front-pt2

## ✨ Features
 * **User Management**
   * Register a new user
   * Login and verify credentials
   * Retrieve user details by ID
   * Update user information
   * Delete user account (along with all associated transactions)

 * **Transaction Management**
   * Create a new transaction for a user
   * Retrieve all transactions for a user (by user ID)
   * Update transaction details
   * Delete a transaction
***

## 🛠 Tech Stack
  * Frontend Framework: Tkinter
  * Backend Framework: FastAPI
  * Database: Firebase Firestore
  * Deployment: Heroku
  * Code Quality: Pre-commit hooks with flake8
***

## 🔐 Setup & Installation
  1. **Clone the Repository:**
```
git clone https://github.com/Bear-College/financial-tracker-front-pt2
cd financial-tracker-front-pt2
```

  2. **Create and Activate Virtual Environment:**

On Windows:
```
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:
```
python3 -m venv .venv
source .venv/bin/activate
```

  3. **Environment Variables:**

Create a .env file in the root directory with the following variable:
```
API_URL=./path/to/your/api.com
```

  4. **Pre-commit Hooks Setup (Optional):**

Installation:
```
pip install pre-commit flake8
pre-commit install
```

Running:
```
pre-commit run --all-files
```
***