import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import sys

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  CORS(app)


  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

  @app.route('/categories')
  def categories():
    getCategories = Category.query.order_by('id').all()
    categories=[]
    for c in getCategories:
      categories.append({'id': c.id, 'category':c.type})
    return jsonify({'categories': categories})

  @app.route('/questions/<int:page_num>')
  def index(page_num):
    getCategories = Category.query.order_by('id').all()
    getQuestions = Question.query.order_by('id').all()
    pages = Question.query.paginate(per_page=10, page=page_num, error_out=True)

    categories = []
    questions = []

    for c in getCategories:
      category = {
        'id': c.id,
        'category': c.type
      }
      categories.append(category)
    
    for q in pages.items:
      question = {
        'id': q.id,
        'question': q.question,
        'difficulty': q.difficulty,
        'answer': q.answer,
        'current_category': Category.query.filter_by(id=q.category).first().type,
        'total_questions': len(getQuestions)
      }
      questions.append(question)

    return jsonify({'categories': categories, 'questions': questions})

  @app.route("/questions/<int:question_id>", methods=['DELETE'])
  def question_delete(question_id):
    getQuestions = Question.query.filter_by(id=question_id).first()
    db.session.delete(getQuestions)
    db.session.commit()
    return jsonify({'success': True, 'deleted': question_id})


  @app.route('/questions/create', methods=['POST'])
  def create_question():
    error = False
    try:
      question = request.get_json()['question']
      answer = request.get_json()['answer']
      difficulty = request.get_json()['difficulty']
      category = request.get_json()['category']
      if question != "" and answer != "" and difficulty != "" and category != "":
        added_question = Question(
          question=question,
          answer=answer,
          difficulty=difficulty,
          category= category
        )
        db.session.add(added_question)
        db.session.commit()
      else:
        return jsonify({'success': False, "notext": "empty text"})

    except:
      error = True
      db.session.rollback()
      print(sys.exc_info())
    finally:
      db.session.close()
    if error:
      abort (422)
    else:
      return jsonify({'success': True, 'created': 'question added successfully'})


  @app.route('/questions', methods=['POST'])
  def questions_search():
    error = False
    text = request.get_json()['searchTerm']
    getQuestions = Question.query.filter(Question.question.ilike(f'%{text}%')).all()
    if getQuestions==[]:
      error = True
    try:
      questions=[]
      for q in getQuestions:
        question = {
          'id': q.id,
          'question': q.question,
          'difficulty': q.difficulty,
          'answer': q.answer,
          'current_category': Category.query.filter_by(id=q.category).first().type,
          'total_questions': len(getQuestions)
        }
        questions.append(question)
    except:
      error = True
      db.session.rollback()
      print(sys.exc_info())
    finally:
      db.session.close()
    if error:
      abort (404)
    else:
      return jsonify({'success': True, 'questions': questions})


  @app.route('/categories/<categorie_id>/questions')
  def questions_categorie(categorie_id):
    error = False
    getQuestions = Question.query.filter_by(category=categorie_id).all()
    if getQuestions==[]:
      error = True
    questions=[]
    try:
      for q in getQuestions:
        question = {
          'id': q.id,
          'question': q.question,
          'difficulty': q.difficulty,
          'answer': q.answer,
          'current_category': str(Category.query.filter_by(id=q.category).first().type),
          'total_questions': len(getQuestions)
        }
        questions.append(question)
    except:
      error = True
      db.session.rollback()
      print(sys.exc_info())
    finally:
      db.session.close()
    if error:
      abort (400)
    else:
      return jsonify({'success': True, 'questions': questions})


  @app.route('/quizzes', methods=['POST'])
  def random_quiz():
    error = False
    try:
      previous_questions = request.get_json()['previous_questions']
      quiz_category = request.get_json()['quiz_category']
      questions=[]
      
      if quiz_category != 0:
        getQuestions = Question.query.filter_by(category=quiz_category).all()
        for q in getQuestions:
          if q.id not in previous_questions:
            questions.append(q)
      else:
        getQuestions = Question.query.all()
        for q in getQuestions:
          if q.id not in previous_questions:
            questions.append(q)

      quizz = []
      if questions != []:
        quizz = random.choice(questions)

      if quizz != []:
        result = {'id': quizz.id, 'question': quizz.question, 'answer': quizz.answer, 'success': True}
      else:
        result = {"id": 0, "question": "", "answer": "", 'success': False}
      
    except:
      error = True
      db.session.rollback()
      print(sys.exc_info())
    finally:
      db.session.close()
    if error:
      abort (400)
    else:
      return jsonify(result)


  @app.errorhandler(400)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "cannot process this request"
    }), 400
  
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "page not found"
    }), 404
  
  @app.errorhandler(422)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "Unprocessable Entity"
    }), 422
  
  @app.errorhandler(500)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 500,
      "message": "Internal Server Error"
    }), 500
  
  return app