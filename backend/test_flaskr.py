import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.test_question = {
            'question':'question',
            'answer':'answer',
            'difficulty': 1,
            'category': 1
        }
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_paginated_books(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_categories'])
        self.assertTrue(len(data['categories']))

    def test_404_beyond_valid_page(self):
        res = self.client().get('/questtions?page=666')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_question_success(self):
        test_question = Question(question=self.test_question['question'], answer=self.test_question['answer'],category=self.test_question['category'], difficulty=self.test_question['difficulty'])
        test_question.insert()
        id=test_question.id
        res = self.client().delete('/questions/{}'.format(id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], str(test_question.id))
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_delete_question_fail(self):
        test_question = Question(question=self.test_question['question'], answer=self.test_question['answer'],category=self.test_question['category'], difficulty=self.test_question['difficulty'])
        id=test_question.id
        res = self.client().delete('/questions/{}'.format(id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_create_question_success(self):
        res = self.client().post('/questions/add', json=self.test_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question_created'])
        self.assertTrue(data['created'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

        def test_create_question_fail(self):
            res = self.client().post('/questions/add', json={})
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertFalse(data['created'])

    def test_question_search_with_results(self):
        res = self.client().post('/questions/searchTerm', json={'searchTerm': 'Tom'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertEqual(len(data['questions']), 1)

    def test_question_search_without_results(self):
        res = self.client().post('/questions/searchTerm', json={'searchTerm': 'Harambe'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertEqual(len(data['questions']), 0)

    def test_get_question_by_category_success(self):
        res = self.client().get('/categories/3/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['current_category'], 'Geography')
        self.assertEqual(len(data['questions']), 3)

    def test_get_question_by_category_fail(self):
        res = self.client().get('/categories/666/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_play_game_success(self):
        res = self.client().post('/quizzes', json={'previous_questions': [5], 'quiz_category':{'type':'Geography', 'id':4}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_play_game_fails(self):
        res = self.client().post('/quizzes', json={'previous_questions': [], 'quiz_category':None})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
