# Trivia Game API

## Full Stack Trivia

Source code for a trivia game API, for Udacity's Full Stack Nanodegree.  The project involved creating an API and test suite to implement the following functionality:

* Display questions and categories from a psql database.
* Add and remove new questions to the database from the browser interface.
* Search for specific questions based on their content.
* Sort questions based on their category.
* Play the quiz game with either all categories or a specific category.

## Getting Started

### Installing Dependencies
Developers using this project should already have Python3, pip, node, and npm installed.

#### Frontend dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```
npm install
```

#### Backend Dependencies

Install dependencies by naviging to the `/backend` directory and running:
```
pip install -r requirements.txt
```

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```
createdb trivia
psql trivia < trivia.psql
```

## Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>
```
npm start
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

## Tests

To run the test suite, first navigate to the project folder in the terminal.
```
cd ../trivia-api/

```

Then run the following commands
    
```
createdb trivia_test
psql trivia_test < trivia.psql
python3 test_flaskr.py
```

## API Reference

### Getting Started

* Base URL: Currently this application is only hosted locally. The backend is hosted at http://127.0.0.1:5000/
* Authentication: This version does not require authentication or API keys.

### Error Handling

Errors are returned as JSON in the following format:<br>

    {
        "success": False,
        "error": 404,
        "message": "resource not found"
    }

The API will return three types of errors:

* 400 – bad request
* 404 – resource not found
* 422 – unprocessable

### Endpoints

#### GET /categories

* General: Returns a list categories.
* Sample: `curl http://127.0.0.1:5000/categories`<br>

        {
            "categories": {
            "1": "science",
            "2": "art",
            "3": "geography",
            "4": "history",
            "5": "entertainment",
            "6": "sports"
          },
          "success": true,
          "total_categories": 6
        }

#### GET /questions

* General:
  * Returns a list questions.
  * Results are paginated in groups of 10.
  * Also returns list of categories and total number of questions.
* Sample: `curl http://127.0.0.1:5000/questions`<br>

        {
          "categories": {
            "1": "science",
            "2": "art",
            "3": "geography",
            "4": "history",
            "5": "entertainment",
            "6": "sports"
          },
          "current_category": null,
          "questions": [
            {
              "answer": "Apollo 13",
              "category": 5,
              "difficulty": 4,
              "id": 2,
              "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            },
            {
              "answer": "Tom Cruise",
              "category": 5,
              "difficulty": 4,
              "id": 4,
              "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            },
            {
              "answer": "Maya Angelou",
              "category": 4,
              "difficulty": 2,
              "id": 5,
              "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            },
            {
              "answer": "Edward Scissorhands",
              "category": 5,
              "difficulty": 3,
              "id": 6,
              "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
            },
            {
              "answer": "Muhammad Ali",
              "category": 4,
              "difficulty": 1,
              "id": 9,
              "question": "What boxer's original name is Cassius Clay?"
            },
            {
              "answer": "Brazil",
              "category": 6,
              "difficulty": 3,
              "id": 10,
              "question": "Which is the only team to play in every soccer World Cup tournament?"
            },
            {
              "answer": "Uruguay",
              "category": 6,
              "difficulty": 4,
              "id": 11,
              "question": "Which country won the first ever soccer World Cup in 1930?"
            },
            {
              "answer": "George Washington Carver",
              "category": 4,
              "difficulty": 2,
              "id": 12,
              "question": "Who invented Peanut Butter?"
            },
            {
              "answer": "Lake Victoria",
              "category": 3,
              "difficulty": 2,
              "id": 13,
              "question": "What is the largest lake in Africa?"
            },
            {
              "answer": "The Palace of Versailles",
              "category": 3,
              "difficulty": 3,
              "id": 14,
              "question": "In which royal palace would you find the Hall of Mirrors?"
            }
          ],
          "success": true,
          "total_questions": 22


#### DELETE /questions/\<int:id\>

* General:
  * Deletes a question by id using url parameters.
  * Returns id of deleted question upon success.
* Sample: `curl http://127.0.0.1:5000/questions/6 -X DELETE`<br>

        {
        "deleted": "6",
        "questions": [
        {
          "answer": "Apollo 13",
          "category": 5,
          "difficulty": 4,
          "id": 2,
          "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
          "answer": "Tom Cruise",
          "category": 5,
          "difficulty": 4,
          "id": 4,
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
          "answer": "Maya Angelou",
          "category": 4,
          "difficulty": 2,
          "id": 5,
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
          "answer": "Muhammad Ali",
          "category": 4,
          "difficulty": 1,
          "id": 9,
          "question": "What boxer's original name is Cassius Clay?"
        },
        {
          "answer": "Brazil",
          "category": 6,
          "difficulty": 3,
          "id": 10,
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
          "answer": "Uruguay",
          "category": 6,
          "difficulty": 4,
          "id": 11,
          "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
          "answer": "George Washington Carver",
          "category": 4,
          "difficulty": 2,
          "id": 12,
          "question": "Who invented Peanut Butter?"
        },
        {
          "answer": "Lake Victoria",
          "category": 3,
          "difficulty": 2,
          "id": 13,
          "question": "What is the largest lake in Africa?"
        },
        {
          "answer": "The Palace of Versailles",
          "category": 3,
          "difficulty": 3,
          "id": 14,
          "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
          "answer": "Agra",
          "category": 3,
          "difficulty": 2,
          "id": 15,
          "question": "The Taj Mahal is located in which Indian city?"
        }
        ],
        "success": true,
        "total_questions": 21
        }


#### POST /questions/add
* General:
    * Adds a question to the database.
    * Returns JSON object with paginated matching questions.
* Sample: `curl http://127.0.0.1:5000/questions/add -X POST -H "Content-Type: application/json" -d '{
            "question": "How many protons does a hydrogen atom have?",
            "answer": "One",
            "difficulty": 1,
            "category": "1"
        }'`
        
        {
          "created": 59,
          "current_category": null,
          "question_created": "How many protons does a hydrogen atom have?",
          "questions": [
            {
              "answer": "Apollo 13",
              "category": 5,
              "difficulty": 4,
              "id": 2,
              "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            },
            {
              "answer": "Tom Cruise",
              "category": 5,
              "difficulty": 4,
              "id": 4,
              "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            },
            {
              "answer": "Maya Angelou",
              "category": 4,
              "difficulty": 2,
              "id": 5,
              "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            },
            {
              "answer": "Muhammad Ali",
              "category": 4,
              "difficulty": 1,
              "id": 9,
              "question": "What boxer's original name is Cassius Clay?"
            },
            {
              "answer": "Brazil",
              "category": 6,
              "difficulty": 3,
              "id": 10,
              "question": "Which is the only team to play in every soccer World Cup tournament?"
            },
            {
              "answer": "Uruguay",
              "category": 6,
              "difficulty": 4,
              "id": 11,
              "question": "Which country won the first ever soccer World Cup in 1930?"
            },
            {
              "answer": "George Washington Carver",
              "category": 4,
              "difficulty": 2,
              "id": 12,
              "question": "Who invented Peanut Butter?"
            },
            {
              "answer": "Lake Victoria",
              "category": 3,
              "difficulty": 2,
              "id": 13,
              "question": "What is the largest lake in Africa?"
            },
            {
              "answer": "The Palace of Versailles",
              "category": 3,
              "difficulty": 3,
              "id": 14,
              "question": "In which royal palace would you find the Hall of Mirrors?"
            },
            {
              "answer": "Agra",
              "category": 3,
              "difficulty": 2,
              "id": 15,
              "question": "The Taj Mahal is located in which Indian city?"
            }
          ],
          "success": true,
          "total_questions": 22
        }

#### POST/questions/searchTerm
* General:
    * Searches for a question using a search term
    * Returns JSON object with paginated matching questions.
* Sample: `curl http://127.0.0.1:5000/questions/searchTerm -X POST -H "Content-Type: application/json" -d '{"searchTerm": "Tom"}'`

            {
            "current_category": null,
            "questions": [
            {
              "answer": "Apollo 13",
              "category": 5,
              "difficulty": 4,
              "id": 2,
              "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            },
            {
              "answer": "One",
              "category": 1,
              "difficulty": 1,
              "id": 59,
              "question": "How many protons does a hydrogen atom have?"
            }
            ],
            "success": true,
            "total_questions": 22
            }

#### GET /categories/\<int:id\>/questions

* General:
  * Gets questions by category id using url parameters.
  * Returns JSON object with paginated matching questions.
* Sample: `curl http://127.0.0.1:5000/categories/1/questions`

        {
          "current_category": "science",
          "questions": [
            {
              "answer": "The Liver",
              "category": 1,
              "difficulty": 4,
              "id": 20,
              "question": "What is the heaviest organ in the human body?"
            },
            {
              "answer": "Alexander Fleming",
              "category": 1,
              "difficulty": 3,
              "id": 21,
              "question": "Who discovered penicillin?"
            },
            {
              "answer": "Blood",
              "category": 1,
              "difficulty": 4,
              "id": 22,
              "question": "Hematology is a branch of medicine involving the study of what?"
            },
            {
              "answer": "2",
              "category": 1,
              "difficulty": 1,
              "id": 50,
              "question": "What is 1 + 1?"
            },
            {
              "answer": "5",
              "category": 1,
              "difficulty": 1,
              "id": 57,
              "question": "What is 2 + 2"
            },
            {
              "answer": "One",
              "category": 1,
              "difficulty": 1,
              "id": 59,
              "question": "How many protons does a hydrogen atom have?"
            }
          ],
          "success": true,
          "total_questions": 22
        }

#### POST /quizzes

* General:
  * Allows users to play the quiz game.
  * Uses JSON request parameters of category and previous questions.
  * Returns JSON object with random question not among previous questions.
* Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [25, 2],
                                            "quiz_category": {"type": "Science", "id": "1"}}'`

        {
          "question": {
            "answer": "2",
            "category": 1,
            "difficulty": 1,
            "id": 50,
            "question": "What is 1 + 1?"
          },
          "success": true
        }

## Authors


* **Ryan Graham** - [Github](https://github.com/ryanxgraham) (README, API (`__init__.py`), test suite (`test_flaskr.py`))

* **Starter code provide by Udacity**
