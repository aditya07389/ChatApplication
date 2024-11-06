# ChatApplication

A real-time chat application built with Django.

# Screenshots of the Application:

<img src="https://github.com/user-attachments/assets/f3186d84-d684-48d5-9efd-50d2020e4af2" alt="Screenshot 1" width="200" style="display:inline;">
<img src="https://github.com/user-attachments/assets/f8b209c6-d358-4235-992d-434a4a967e1e" alt="Screenshot 2" width="200" style="display:inline;">
<img src="https://github.com/user-attachments/assets/6de739a4-a848-48f5-8f7d-4e2881b15e42" alt="Screenshot 3" width="200" style="display:inline;">
<img src="https://github.com/user-attachments/assets/93443b16-f135-4877-9f28-eb88fe3a54ca" alt="Screenshot 4" width="200" style="display:inline;">
<img src="https://github.com/user-attachments/assets/1e426390-852e-4aaf-991c-5c1911570872" alt="Screenshot 5" width="200" style="display:inline;">





# How to use ?

1) Create a superuser(this is the user who will be the customer support).
2) Register/Signup another user.
3) Login with credentials of the registered user in one window.
4) Login with admin credentials in another window.
5) Test out the chat functionality.






## Prerequisites

Make sure you have the following installed:
- Python 3.8+
- pip
- Virtualenv (optional but recommended)

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd ChatApp
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**

   Install the required packages listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```
4. **Apply Migrations**

   Run the following commands to set up the database schema:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a Superuser (Optional)**

   To access the Django admin interface, create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**

   Start the Django development server to test your app locally.

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**

    Open your browser and go to:

    ```
    http://127.0.0.1:8000
    ```


## License

This project is licensed under the MIT License.
