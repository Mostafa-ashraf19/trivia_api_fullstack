import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request,selection):
  page = request.args.get('page',1,type=int)
  start = (page -1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in selection ]
  current_questions = questions[start:end]
  return current_questions



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  DONE: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app,resources={r"/api/*":{"origins":"*"}})
  '''
  DONE: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE')
    return response
  '''
  DONE: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories',methods=['GET'])
  def Categories():
    categories = Category.query.all()
    formatted_categories = [ category.format() for category in categories ]
    
    if len(formatted_categories) == 0: 
      abort(404)
    return jsonify({
     'success':True,
     'categories': formatted_categories 
    })

  '''
  DONE: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions',methods=['GET'])
  def retrive_questions():
    questions = Question.query.order_by(Question.id).all()

    current_questions = paginate_questions(request,questions)

    if len(current_questions) == 0:
      abort(404)
    return jsonify({
      'success':True,
      'questions':current_questions,
      'total_questions':len(Question.query.all())
    })
    
  '''
  DONE: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:id>',methods=['DELETE'])
  def delete_question(id):
    try:
      question = Question.query.filter(Question.id == id).one_or_none()

      if question is None:
        abort(404)
      question.delete()
      questions = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request,questions)

      return jsonify({
        'success':True,
        'deleted':id,
        'questions':current_questions,
        'total_questions':len(Question.query.all())
      }),200   

    except:    
      abort(422)

  '''
  DONE: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions',methods=['POST'])
  def create_question():
    body = request.get_json()

    question_desc = body.get('question',None)
    question_ans = body.get('answer',None)
    question_diff = body.get('difficulty',None)
    question_cat = body.get('category',None)

    try: 
      question = Question(question_desc,question_ans,question_cat,question_diff)
      question.insert()

      questions = Question.query.all()
      current_questions = paginate_questions(request,questions)

      return jsonify({
        'success':True,
        'Created':question.id,
        'questions': current_questions,
        'total_questions': len(Question.query.all())
      })

    except:  
      abort(422)


  '''
  DONE: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions',methods=['POST'])
  def Search():
    body = request.get_json()

    question_desc = body.get('question',None)
    question_ans = body.get('answer',None)
    question_diff = body.get('difficulty',None)
    question_cat = body.get('category',None)
    search = body.get('searchTerm',None)
    try: 
      if search: 
        question = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search))) 
        current_questions = paginate_questions(request,question)
        return jsonify({
          'success':True,
          'questions': current_questions,
          'total_questions':len(current_questions)
        })
    except:
      abort(422)  
    
  '''
  DONE: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:id>/questions',methods=['GET'])
  def get_categorized_questions(id):
    
    category = Category.query.filter(Category.id == id).one_or_none()
    if category == None:
      return jsonify({
      'success':False,  
      'Category_name':'Not Found this category', 
    })
    category = category.format()
    categorized_questions = Question.query.filter(Question.category == category['id']).all()
    current_categorized_questions = paginate_questions(request,categorized_questions)
    
    if len(current_categorized_questions) == 0: 
      abort(404)
    return jsonify({
      'success':True,
      'questions':current_categorized_questions,  
      'Category_name':category['type'], 
      'total_length': len(current_categorized_questions)
    }),200  


  '''
  DONE: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes',methods=['POST'])
  def rand_play_Question():
    data = request.get_json()

    questions =  Question.query.filter(Question.category == data['quiz_category']).filter(Question.id != data['previous_questions']).all()
    returned_questions = [ question.format() for question in questions]

    if len(returned_questions) == 0:
      abort(404)
    return jsonify({
      'success':True,
      'questions':returned_questions,
      'question_length':len(returned_questions)
    })  

  '''
  DONE: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def notFound(error):
    return jsonify({
      'success':False,
      'error': 404,
      'message': 'Not Found'
    }),404
  @app.errorhandler(422)  
  def Unprocessable(error):
    return jsonify({
      'success':False,
      'error': 422,
      'message': 'unprocessable'
    }),422

  return app