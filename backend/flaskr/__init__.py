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
    formatted_categories = [ category.format()['type'] for category in categories ]
    
    if len(formatted_categories) == 0: 
      abort(404)
    return jsonify({
     'success':True,
     'categories': formatted_categories 
    }),200

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
    # print('\n************************\n',page,'\n*****************\n')
    questions = Question.query.order_by(Question.id).all()

    current_questions = paginate_questions(request,questions)

    categories = Category.query.all()
    formatted_categories = [ category.format()['type'] for category in categories ]
    
    if len(current_questions) == 0:
      abort(404)
    return jsonify({
      'success':True,
      'questions':current_questions,
      'total_questions':len(Question.query.all()),
      'categories':formatted_categories,
      'current_category':1  # I don't know what should set here !!!
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
      # questions = Question.query.order_by(Question.id).all()
      # current_questions = paginate_questions(request,questions)

      return jsonify({
        'success':True,
        'deleted':id,
        # 'questions':current_questions,
        # 'total_questions':len(Question.query.all())
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

    question_description = body.get('question',None)
    question_answer = body.get('answer',None)
    question_difficulty = body.get('difficulty',None)
    question_category = body.get('category',None)

    try: 
      question = Question(question_description,question_answer,question_category,question_difficulty)
      question.insert()

      questions = Question.query.all()
      current_questions = paginate_questions(request,questions)

      return jsonify({
        'success':True,
        'Created':question.id,
        'questions': current_questions,
        'total_questions': len(Question.query.all())
      }),200

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
  @app.route('/questions/search',methods=['POST'])
  def Search():
    body = request.get_json()
    # print('\n************ body is ***********\n',body,'\n***********************\n')
    search = body.get('searchTerm',None)
    # print('\n***********************\n',search,'\n***********************\n')
    try: 
      if search: 
        question = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search))) 
        current_questions = paginate_questions(request,question)
        return jsonify({
          'success':True,
          'questions': current_questions,
          'total_questions':len(current_questions),
          'current_category':None
        }),200
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
      abort(404)
    category = category.format()
    categorized_questions = Question.query.filter(Question.category == category['id']).all()
    current_categorized_questions = paginate_questions(request,categorized_questions)
    
    if len(current_categorized_questions) == 0: 
      abort(404)
    return jsonify({
      'success':True,
      'questions':current_categorized_questions,  
      'current_category':category['type'], 
      'total_questions': len(current_categorized_questions)
      # 'Category_name':category['type'], 
      # 'total_length': len(current_categorized_questions)
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
    
    try:
      data = request.get_json()

      
      # questions =  Question.query.filter(Question.category == data['quiz_category']).filter(Question.id != data['previous_questions']).all()
      # questions =  Question.query.filter(Question.category == data['quiz_category']).filter(not(Question.id == (data['previous_questions']))).all()
      # data['quiz_category']['id']+=1
      # print('\n********************\n',data,'\n********************\n')
      # print('\n********************\n',type(data['quiz_category']['id']),'    ', data['previous_questions'],'\n********************\n')
      
      value = int(data['quiz_category']['id']) +1  #str((int(data['quiz_category']['id'])+1))
      data['quiz_category']['id']  = str(value)  
      questions =  Question.query.filter(Question.category == data['quiz_category']['id']).filter(not(Question.id == data['previous_questions'])).all()
      returned_questions = [ question.format() for question in questions]
      # print('\n********************\n',returned_questions,'\n********************\n')

      randval =  random.randint(0,(len(returned_questions)-1))
      question = returned_questions[randval]
      if len(returned_questions) == 0:
        abort(404)
      return jsonify({
        'success':True,
        'question':question,
      }),200 
    except:
      abort(500)  

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
  @app.errorhandler(500)  
  def InternalServerError(error):
    return jsonify({
      'success':False,
      'error': 500,
      'message': 'Internal Server Error'
    }),500  

  return app
