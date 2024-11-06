
# ChatApp

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

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory to store environment variables. Add your configurations such as secret keys and database settings:

   ```plaintext
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```

5. **Database Configuration**

   This project uses **SQLite** as the default database for demonstration purposes. SQLite is suitable for local development but not recommended for production.

   ### Replacing SQLite for Production
   - For production, consider replacing SQLite with a more robust database, like **PostgreSQL** or **MySQL**.
   - Update the `DATABASES` setting in `settings.py` with your chosen database configuration.

   Example configuration for PostgreSQL:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

6. **Channel Layers Configuration**

   This project uses Django Channels with an **InMemoryChannelLayer** for demonstration. The `InMemoryChannelLayer` is a basic in-memory backend useful for development and testing.

   ### Replacing InMemoryChannelLayer for Production
   - For production, use **Redis** as the channel layer backend, which is more reliable for handling real-time events in a distributed system.
   - Update the `CHANNEL_LAYERS` setting in `settings.py`:

   Example configuration with Redis:
   ```python
   CHANNEL_LAYERS = {
       'default': {
           'BACKEND': 'channels_redis.core.RedisChannelLayer',
           'CONFIG': {
               "hosts": [('127.0.0.1', 6379)],
           },
       },
   }
   ```

7. **Apply Migrations**

   Run the following commands to set up the database schema:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Create a Superuser (Optional)**

   To access the Django admin interface, create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

9. **Run the Development Server**

   Start the Django development server to test your app locally.

   ```bash
   python manage.py runserver
   ```

10. **Access the Application**

    Open your browser and go to:

    ```
    http://127.0.0.1:8000
    ```


## License

This project is licensed under the MIT License.
