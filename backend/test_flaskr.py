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
        self.database_path = "postgres://{}/{}".format('postgres:1234@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            'question': 'How many faces for the cube?',
            'answer': 6,
            'difficulty': 1,
            'category': '6'
        }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['categories'])
    def test_404_sent_category_typo_requesting(self):
        res = self.client().get('/catagorieshttp')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'page not found')
        
    def test_get_questions_pagenate(self):
        res = self.client().get('/questions/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['categories'])
        self.assertTrue(data['questions'])
    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/questions/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'page not found')

    def test_delete_question(self):
        """Tests question deletion success"""
        
        # create a new question to be deleted
        question = Question(question=self.new_question['question'], answer=self.new_question['answer'],
                            category=self.new_question['category'], difficulty=self.new_question['difficulty'])
        question.insert()
        question_id = question.id
        questions_before = Question.query.all()
        res = self.client().delete('/questions/{}'.format(question_id))
        data = json.loads(res.data)
        questions_after = Question.query.all()
        question = Question.query.filter(Question.id == 1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], question_id)
        self.assertTrue(len(questions_before) - len(questions_after) == 1)
        self.assertEqual(question, None)

    def test_create_new_question(self):
        """Tests question creation success"""
        questions_before = Question.query.all()
        res = self.client().post('/questions/create', json=self.new_question)
        data = json.loads(res.data)
        questions_after = Question.query.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(questions_after) - len(questions_before) == 1)
    def test_422_if_question_creation_fails(self):
        """Tests question creation failure 422"""
        questions_before = Question.query.all()
        res = self.client().post('/questions/create', json={})
        data = json.loads(res.data)
        questions_after = Question.query.all()
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(questions_after) == len(questions_before))

    def test_search_questions(self):
        """Tests search questions success"""
        res = self.client().post('/questions', json={'searchTerm': 'How many'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    def test_404_if_search_questions_fails(self):
        """Tests search questions failure 404"""
        res = self.client().post('/questions', json={'searchTerm': 'asafdgfgv'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_questions_by_category(self):
        """Tests getting questions by category success"""
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    def test_400_if_questions_by_category_fails(self):
            """Tests getting questions by category failure 400"""
            res = self.client().get('/categories/100/questions')
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 400)
            self.assertEqual(data['success'], False)
    
    def test_play_quiz_game(self):
        """Tests playing quiz game success"""
        res = self.client().post('/quizzes',json={"quiz_category": "6", "previous_questions": [2, 6]})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
    def test_play_quiz_fails(self):
        """Tests playing quiz game failure 400"""

        # send post request without json data
        response = self.client().post('/quizzes', json={})

        # load response data
        data = json.loads(response.data)

        # check response status code and message
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'cannot process this request')


    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()