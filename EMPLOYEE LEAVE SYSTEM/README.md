# Employee Leave Management System

A web-based portal built using Django to streamline corporate employee registration, profile indexing, and leave request management workflows. The system establishes distinct permission boundaries separating standard personnel from administrators.

---

##  1. The Problem
Managing corporate leave requests manually via email chains, paper forms, or unorganized spreadsheets introduces significant operational friction. 

 **Lack of Role Segregation:** Without structural user authentication, regular employees can access backend pathways or inadvertently modify critical administrative data.
* **Visibility Blindspots:** Employees remain unaware of whether their submitted requests are pending, approved, or rejected until manual email notifications or verbal updates are given.
* **Data Integrity and Security Risks:** Forcing database interactions manually or leaving URL endpoints unprotected opens up potential vulnerabilities to unauthorized data modifications.

----

##  2. The Solution
This application centralizes management operations into a secure portal that automates processing, ensures validation, and establishes clear visibility rules based on authentication status.

* **Conditional Frontend Layouts:** Administrative actions (such as Approve/Reject triggers and the "Create Employee" navigation options) are automatically hidden from standard employee interfaces via dynamic condition checks (`{% if user.is_staff %}`).

* **Server-Side Access Guards:** Secure backend operations are structurally locked down using explicit Django decorators (`@login_required` and `@user_passes_test`) to actively block unauthorized manual URL manipulations.

* **Live Status Transparency:** Employees obtain real-time, immediate visual feedback across their personalized homepage dashboards with styled status badges (`Pending Review `, `Approved `, or `Rejected `).

* **Centralized Data Handling:** Input forms are managed cleanly through a dedicated abstraction layer (`forms.py`) to automatically handle deep server-side data validation and sanitation, safeguarding the SQLite backend.

---

##  3. Tech Stack Used
* **Backend Framework:** Django 5.2+ (Python Web Framework)
* **Database Engine:** SQLite (Default local development structured relational storage)
* **Frontend UI Layout:** Semantic HTML5, Component CSS3 Styling, and Django Template Language (DTL)

---

##  5. Core File Structure Configurations

### A. Redirection Routing Rules (`settings.py`)
Configured to seamlessly manage where unauthenticated users are intercepted, and where users land upon entering correct credentials:
```python
# leave_management/settings.py
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'


python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
