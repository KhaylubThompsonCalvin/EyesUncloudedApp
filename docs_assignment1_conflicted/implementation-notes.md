# Implementation Notes for Sprint 1

# Overall System Architecture

- **Front-end:** HTML/CSS/JavaScript pages for login, registration, sending notifications, etc.
- **Back-end:** Node.js server using Express (or PHP if preferred) to handle account management and notifications.
- **Database:** (To be decided) Could be MongoDB, MySQL, etc. to store user accounts and notification logs.

# Key Components & Classes

- **User Authentication Module:** Handles account creation, login, password hashing.
- **Notification Module:** For composing, sending, and logging notifications.
- **Template Module:** (Optional) For managing message templates with placeholders.

# High-Level Flow

1. User registers or logs in via the front-end.
2. For managers, a form allows entering notifications.
3. The notification is processed by the server, sent to subscribers, and logged.
4. Managers can review notification logs by selecting a date range.

# Potential Libraries/Technologies

- **Express:** For the Node.js back-end.
- **bcryptjs:** For password hashing.
- **Nodemailer:** For sending emails.
- **GUI Builder Tool:** IntelliJ's GUI Designer / Visual Studio / PHPStorm, depending on the technology chosen.
