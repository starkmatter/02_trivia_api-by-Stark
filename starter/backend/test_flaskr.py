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
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', '', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.new_question = {
            'question': 'How are you?',
            'answer': 'Great',
            'difficulty': 3,
            'category': 'Science'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_404_paginated_questions(self):
        res = self.client().get('/questions?page=10000', json = {'difficulty':1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_search_for_question(self):        
        search_json_dump = json.dumps({'searchTerm': 'what'})
        search_json = {'searchTerm':'what'}
        
        print(type(search_json))
        print(type(search_json_dump))
        print(type(json.dumps({"c":0, "b":0,"a":0})))
                

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()