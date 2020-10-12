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
        # self.database_name = "trivia_test"
        self.database_name = 'trivia'
        self.logInfo  = 'postgres:root'
        self.database_path = "postgresql://{}@{}/{}".format(self.logInfo,'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

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
    DONE
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertAlmostEqual(res.status_code,200)
        self.assertAlmostEqual(data['success'],True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])

    def test_categorized_questions(self):

        res = self.client().get('/categories/1/questions')
        # print('\n***************************\n',res,'\n***************************\n')
        data = json.loads(res.data)
        
        self.assertAlmostEqual(res.status_code,200)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_length'])
        self.assertEqual(data['Category_name'],'Science')
       

    def test_delete_question(self):

        req = self.client().delete('/questions/7')
        data = json.loads(req.data)
        # print('\n*****************************\n',data,'\n******************\n')

        self.assertAlmostEqual(req.status_code,200)
        self.assertTrue(data['deleted'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
               
    def test_quizzes(self):

        quiz =  self.client().post('/quizzes',json={"previous_questions":1 ,"quiz_category":2})
        d = json.loads(quiz.data)

        self.assertAlmostEqual(quiz.status_code,200)
        self.assertTrue(d['questions'])
        self.assertTrue(d['question_length'])

    def test_Search(self):
        
        search =  self.client().post('/questions/search',json={"searchTerm":"what"})

        results = json.loads(search.data) 
        # print('\n**************************\n',results,'\n**************************\n')

        self.assertAlmostEqual(search.status_code,200)
        self.assertTrue(results['questions'])
        self.assertTrue(results['total_questions'])

    def test_create_question(self):

        req = self.client().post('/questions',json={"question":"how old are you?" , "answer":"fine", "difficulty":3,"category":2})

        results = json.loads(req.data)

        self.assertEqual(req.status_code,200)
        self.assertTrue(results['Created'])
        self.assertTrue(results['questions'])
        self.assertTrue(results['total_questions'])



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
