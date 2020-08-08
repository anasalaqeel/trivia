# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```

## Endpoints
### GET/categories
- #### General:
    - Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
    - Returns: An Array of Objects that has a single key, categories, that contains a object of id: category_string key:value pairs. 
- #### Sample: `http://localhost:5000/categories`
```

"categories": [
    {
    "category": "Science",
    "id": 1
    },
    {
    "category": "Art",
    "id": 2
    },
    {
    "category": "Geography",
    "id": 3
    },
    {
    "category": "History",
    "id": 4
    },
    {
    "category": "Entertainment",
    "id": 5
    },
    {
    "category": "Sports",
    "id": 6
    }
]

```

### GET/questions/```<quesstion number>```
- #### General:
    - Fetches a dictionary of categories and questions arrays which have categories objects and questions objects.
    - Returns: An Array of questions limeted to 10 questions for each number of page which can defined in params.
- #### Sample: ```http://localhost:5000/questions/1```
```
{
        "categories": [
        {
        "category": "Science",
        "id": 1
        },
        {
        "category": "Art",
        "id": 2
        },
        {
        "category": "Geography",
        "id": 3
        },
        {
        "category": "History",
        "id": 4
        },
        {
        "category": "Entertainment",
        "id": 5
        },
        {
        "category": "Sports",
        "id": 6
        }
    ],

"questions": [
        {
        "answer": "Muhammad Ali",
        "current_category": "History",
        "difficulty": 1,
        "id": 9,
        "question": "What boxer's original name is Cassius Clay?",
        "total_questions": 25
        },
        {
        "answer": "Apollo 13",
        "current_category": "Entertainment",
        "difficulty": 4,
        "id": 2,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
        "total_questions": 25
        },
        {
        "answer": "Tom Cruise",
        "current_category": "Entertainment",
        "difficulty": 4,
        "id": 4,
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
        "total_questions": 25
        },
        {
        "answer": "Edward Scissorhands",
        "current_category": "Entertainment",
        "difficulty": 3,
        "id": 6,
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
        "total_questions": 25
        },
        {
        "answer": "Brazil",
        "current_category": "Sports",
        "difficulty": 3,
        "id": 10,
        "question": "Which is the only team to play in every soccer World Cup tournament?",
        "total_questions": 25
        },
        {
        "answer": "Uruguay",
        "current_category": "Sports",
        "difficulty": 4,
        "id": 11,
        "question": "Which country won the first ever soccer World Cup in 1930?",
        "total_questions": 25
        },
        {
        "answer": "George Washington Carver",
        "current_category": "History",
        "difficulty": 2,
        "id": 12,
        "question": "Who invented Peanut Butter?",
        "total_questions": 25
        },
        {
        "answer": "Lake Victoria",
        "current_category": "Geography",
        "difficulty": 2,
        "id": 13,
        "question": "What is the largest lake in Africa?",
        "total_questions": 25
        },
        {
        "answer": "The Palace of Versailles",
        "current_category": "Geography",
        "difficulty": 3,
        "id": 14,
        "question": "In which royal palace would you find the Hall of Mirrors?",
        "total_questions": 25
        },
        {
        "answer": "Agra",
        "current_category": "Geography",
        "difficulty": 2,
        "id": 15,
        "question": "The Taj Mahal is located in which Indian city?",
        "total_questions": 25
        }
    ]
}

```

### GET/categories/```<categorie id>```/questions
- #### General:
    - Returns: An Array of questions Objects filtered by category which can defined by id in parameters.
- #### Sample: `http://localhost:5000/categories/5/questions`
```

"questions": [
    {
    "answer": "Apollo 13",
    "current_category": "Entertainment",
    "difficulty": 4,
    "id": 2,
    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
    "total_questions": 3
    },
    {
    "answer": "Tom Cruise",
    "current_category": "Entertainment",
    "difficulty": 4,
    "id": 4,
    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
    "total_questions": 3
    },
    {
    "answer": "Edward Scissorhands",
    "current_category": "Entertainment",
    "difficulty": 3,
    "id": 6,
    "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
    "total_questions": 3
    }
]

```

### POST/quizzes
- #### General:
    - this will take a JSON object request included a category id and previou 
s questions array return a random question base on category sent, and show question which not showed yet for each request.
- #### Sample: 
```
curl http://localhost:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"quiz_category": 6, "previous_questions": [2, 6]}' 
```
```
{
  "answer": "Brazil",
  "id": 10,
  "question": "Which is the only team to play in every soccer World Cup tournament?"
}
```

### POST/questions
- #### General:
    - this endpoint allows you to search questions by taking a JSON object included search term.
    - Return: this will return an array of questions objects that inculded the search term.
- #### Sample: 
```
curl http://localhost:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "who"}'
```
```
"questions": [
    {
      "answer": "George Washington Carver",
      "current_category": "History",
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?",
      "total_questions": 2
    },
    {
      "answer": "Alexander Fleming",
      "current_category": "Science",
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?",
      "total_questions": 2
    }
  ]
```

### POST/questions/create
- #### General:
    - this endpoint create a new JSON object of question which included question, answer, difficulty and category id.
    - Return: this will return a success object.
- #### Sample: 
```
curl http://localhost:5000/questions/create -X POST -H "Content-Type: application/json" -d '{"question": "what are you?", "answer": "god call us human but actually we are the devils", "difficulty": 6, "category": 1}'
```
```
{
  "success": "question added successfully"
}
```

### DELETE /questions/`<question id>`
- #### General:
    - this endpoint delete the question using question id by take question id as a param.
- #### Sample: 
```
curl http://localhost:5000/questions/38 -X DELETE
```
### Return
```
{
  "sucsess": "deleted"
}
```

## Error handling

Errors are returned as JSON objects in the following format:
```
{
  "error": 400,
  "message": "cannot process this request",
  "success": false
}
```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```