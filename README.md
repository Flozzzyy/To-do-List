# Django Todo List

A simple and elegant todo list application built with Django. Features user authentication and CRUD operations for tasks.

## Features

- User Registration and Authentication
- Create, Read, Update, and Delete Tasks
- Mark Tasks as Complete/Incomplete
- Modern and Responsive UI
- User-specific Tasks

## Technologies Used

- Django 5.2.1
- Python 3.x
- HTML5/CSS3
- JavaScript
- Font Awesome Icons

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/todo-django.git
cd todo-django
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ in your browser

## Usage

1. Register a new account or login
2. Create new tasks using the "Create New Task" button
3. Mark tasks as complete by clicking the checkbox
4. Edit or delete tasks using the respective buttons
5. Logout when done

## Project Structure

```
todo/
├── todolist/           # Main application
│   ├── static/        # Static files (CSS, JS)
│   ├── templates/     # HTML templates
│   ├── models.py      # Database models
│   ├── views.py       # View logic
│   └── urls.py        # URL configurations
├── todo/              # Project settings
└── manage.py          # Django management script
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 