# Mable Bug Tracker

Mable is a web-based bug tracking application created using Python/Django. It provides a platform to create projects and track issues or tickets within those projects. This document describes how to run the Mable project locally.

## Account Choice
![mable-account-choice](https://user-images.githubusercontent.com/75034316/236364408-d68e0858-a895-462a-ac83-2466a3d044d4.png)
## Register
![mable-register](https://user-images.githubusercontent.com/75034316/236364423-5eceeeff-db0c-4534-a535-ffd07fcd7996.png)
## Login
![mable-login](https://user-images.githubusercontent.com/75034316/236364436-b010d85c-e1b0-4015-bccd-866c68e451c0.png)
## Dashboard
![new-mable-dashboard](https://user-images.githubusercontent.com/75034316/236109836-1b371ded-c5bb-4337-ba29-794b396fd0fb.png)
## User page
![mable-users](https://user-images.githubusercontent.com/75034316/236109980-72d21738-95e0-446a-8395-c018c440ff37.png)
## Analytics
![mable-analytics](https://user-images.githubusercontent.com/75034316/236109846-04801d59-d64c-4eee-bcbe-f55cac586dde.png)
## Project Home
![mable-projects](https://user-images.githubusercontent.com/75034316/236109865-92f03859-a328-4f2f-ade9-e1bd5147d24c.png)
## Project Form
![mable-project-form](https://user-images.githubusercontent.com/75034316/236109871-128a1d8e-cbbf-4607-ab31-e8acc747358c.png)
## Project Detail
![mable-project-detail](https://user-images.githubusercontent.com/75034316/236109898-749664dd-8502-4d27-8385-047ee6f3f4ac.png)
## Ticket Home
![mable-ticket-home](https://user-images.githubusercontent.com/75034316/236109939-dca68e56-8a1d-4d06-b3fb-1ddc6b1b94a2.png)
## Ticket Form
![mable-ticket-form](https://user-images.githubusercontent.com/75034316/236109928-b6e581bc-cb9d-43a4-9106-5018ad25b65d.png)
## Ticket Detail
![mable-ticket-detail](https://user-images.githubusercontent.com/75034316/236109913-451d01b2-046a-4b0e-8b6d-d79f2ad0e5b2.png)
## Profile settings
![mable-profile](https://user-images.githubusercontent.com/75034316/236109997-b2aecee7-201e-4adf-9ca4-a44f1e29aba1.png)


## Requirements

Before you begin, make sure your development environment meets the following requirements:

- Python 3.6 or higher
- Pip
- Virtualenv
- Git

## Installation

1. Clone the Mable repository from GitHub:
`git clone https://github.com/username/mable.git`

2. Create a virtual environment and activate it:
`virtualenv mable-env
source mable-env/bin/activate`

3. Install the project requirements:
`cd mable
pip install -r requirements.txt`

4. Run the Django database migrations:
`python manage.py migrate`

5. Create a superuser account:
`python manage.py createsuperuser`

6. Start the Django development server:
`python manage.py runserver`


The Mable project should now be running on `http://127.0.0.1:8000/`.

## Usage

To use Mable, follow these steps:

1. Open your web browser and navigate to `http://127.0.0.1:8000/`.

2. Log in using your superuser account credentials.

3. Click the "New Project" button to create a new project.

4. Once you have created a project, you can create new tickets within that project.

5. You can also search for tickets and filter them by various criteria.

## Conclusion

You have successfully set up and run the Mable bug tracker project locally. You can now use it to track issues and tickets within your projects.
