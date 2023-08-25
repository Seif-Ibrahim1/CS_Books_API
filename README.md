# CS_Books_API
The Computer Science Books API is a RESTful API built with Django that provides access to a collection of computer science books and authors. It allows you to retrieve book and author information, add new books and authors, and update existing book details.

## API Endpoints
* List all books: **`GET /v1/books/`**

* Create a new book: **`POST /v1/books/`**

* Retrieve a specific book: **`GET /v1/books/:id/`**

* Update a specific book: **`PUT /v1/books/:id/`**

* Delete a specific book: **`DELETE /v1/books/:id/`**

* List all authors: **`GET /v1/authors/`**

* Create a new author: **`POST /v1/authors/`**

* Retrieve a specific author: **`GET /v1/authors/:id/`**

* Update a specific author: **`PUT /v1/authors/:id/`**

* Delete a specific author: **`DELETE /v1/authors/:id/`**

## Usage
You can use tools like curl or Postman to interact with the API. Make requests to the above endpoints to manage books and authors in the database.

### Prerequisites

- Python 3.x
- Django
- Django REST framework

### Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:Seif-Ibrahim1/CS_Books_API.git
   cd CS_Books_API
   ```
   or
   ```bash
   git clone https://github.com/Seif-Ibrahim1/CS_Books_API.git
   cd CS_Books_API
   ```
2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```bash
       python manage.py makemigrations
       python manage.py migrate
   ```
5. Start the development server:
   ```bash
       python manage.py runserver
   ```
   
