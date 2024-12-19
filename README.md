A backend service built with Django and Django REST Framework (DRF) to manage user registration, login, and notification distribution using JWT authentication. This API allows users to send and receive notifications securely and efficiently.

Key Features: User Registration and Authentication: Users can create an account with a unique username and password. Passwords are securely hashed using bcrypt to protect user credentials. After registration, users can log in by providing their credentials.

Authenticated users can send notifications to other users. A notification contains: Title,Message,List of user IDs to send the notification to Notification type (which could categorize the notification, such as "info", "alert", etc.) Notifications are logged and stored in the database. Users can retrieve their notifications from the system, which are associated with their user ID.

Logging: The project uses Python's built-in logging module to track important actions like sending notifications and errors (e.g., when a user is not found). CORS Support: CORS (Cross-Origin Resource Sharing) headers are configured to allow requests from different origins. This is particularly useful in a development environment where the frontend and backend might be running separately.
