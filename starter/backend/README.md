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

1. Use Flask-CORS to enable cross-domain requests and set response headers. DONE
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. DONE
3. Create an endpoint to handle GET requests for all available categories. DONE
4. Create an endpoint to DELETE question using a question ID. DONE
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. DONE
6. Create a POST endpoint to get questions based on category. DONE
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. DONE
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. DONE
9. Create error handlers for all expected errors including 400, 404, 422 and 500. DONE

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
DELETE '/questions/<int:question_id>'
GET '/questions'
POST '/questions'
POST '/searchQuestions'
GET '/categories/<int:category_id>/questions'
POST '/quizzes'


GET '/categories'
- Description: Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}


GET '/questions'
- Description: Fetches a dictionary of all questions (objects) as well as a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns:  an object with the current questions based on the selected page, total questions (integer), an object containing categories, and the current category. 
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, ...
    

DELETE '/questions/<int:question_id>'
- Description: Deletes a question based on the question id submitted
- Request Arguments: the question id is submitted by the user
- Returns: None 


POST '/questions'
- Description: Allows the user to create a new question using the input form
- Request Arguments: Recieves fields - question, answer, difficulty, and category
- Returns: None


POST '/searchQuestions'
- Description: Fetches a list of questions based on the search criteria submitted.  This is a partial search and not case sensitive, meaning that all questions containing the string, regardless of case, will be returned as a pageanated list.
- Request Arguments: Recieves a search criteria from the user as string
- Returns: A pagenated list of questions (dictionary of objects) that meet the search criteria.


GET '/categories/<int:category_id>/questions'
- Description: Fetches a list of questions based on the category selected.
- Request Arguments: Recieves the category id
- Returns: A pagenated list of questions (dictionary of objects)


POST '/quizzes'
- Description: Randomly selects a question that belongs to the selected category, and that has not previously been selected.
- Request Arguments: Recieves the category id
- Returns: A randomly selected question (as an object)
```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```