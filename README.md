# Full Stack Trivia

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 



## APIs Documentation 
---- 
1) **Get the current categories**
      
      **URL** : `/categories`

      **Method** : `GET`

      **Auth required** : NO

      **Permissions required** : None

      #### Success Response

      **Code** : `200 OK`

      **Content examples**

      use curl http://127.0.0.1:5000/categories 
      
       **Json Response**:
       
          
            {
                "categories": [
                  {
                    "id": 1, 
                    "type": "Science"
                  }, 
                  {
                    "id": 2, 
                    "type": "Art"
                  }, 
                  {
                    "id": 3, 
                    "type": "Geography"
                  }, 
                  {
                    "id": 4, 
                    "type": "History"
                  }, 
                  {
                    "id": 5, 
                    "type": "Entertainment"
                  }, 
                  {
                    "id": 6, 
                    "type": "Sports"
                  }
                ], 
                "success": true
             }

2) **Get the current questions with Pagination**
      
      **URL** : `/questions`

      **Method** : `GET`

      **Auth required** : NO

      **Permissions required** : None

      #### Success Response

      **Code** : `200 OK`

      **Content examples**

      use curl http://127.0.0.1:5000/questions 
      
      **Json Response**:
       
          
            {
              "questions": [
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
                }, 
                {
                  "answer": "Escher", 
                  "category": 2, 
                  "difficulty": 1, 
                  "id": 16, 
                  "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
                }
              ], 
              "success": true, 
              "total_questions": 17
            }

3) **Delete Question with specific id**
      
      **URL** : `/questions/<int:id>`

      **Method** : `DELETE`

      **Auth required** : NO

      **Permissions required** : None

      #### Success Response

      **Code** : `200 OK`

      **Content examples**

      use curl -X DELETE http://127.0.0.1:5000/questions/9 
      
      **Json Response**:
       
          
               {
                      "deleted": 9, 
          "questions": [
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
            }, 
            {
              "answer": "Escher", 
              "category": 2, 
              "difficulty": 1, 
              "id": 16, 
              "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
            }, 
            {
              "answer": "Mona Lisa", 
              "category": 2, 
              "difficulty": 3, 
              "id": 17, 
              "question": "La Giaconda is better known as what?"
            }
          ], 
          "success": true, 
          "total_questions": 16
            }

4) **Search into question by a keyword**
      
      **URL** : `/questions/search`

      **Method** : `POST`

      **Auth required** : NO

      **Permissions required** : None

      #### Success Response

      **Code** : `200 OK`

      **Content examples**

      curl -X POST http://127.0.0.1:5000/questions/search -H "content-Type:application/json" -d '{"searchTerm":"what"}' 
      
      **Json Response**:
       
          
		       {
	  "questions": [
	    {
	      "answer": "Tom Cruise", 
	      "category": 5, 
	      "difficulty": 4, 
	      "id": 4, 
	      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
	    }, 
	    {
	      "answer": "Lake Victoria", 
	      "category": 3, 
	      "difficulty": 2, 
	      "id": 13, 
	      "question": "What is the largest lake in Africa?"
	    }, 
	    {
	      "answer": "Mona Lisa", 
	      "category": 2, 
	      "difficulty": 3, 
	      "id": 17, 
	      "question": "La Giaconda is better known as what?"
	    }, 
	    {
	      "answer": "The Liver", 
	      "category": 1, 
	      "difficulty": 4, 
	      "id": 20, 
	      "question": "What is the heaviest organ in the human body?"
	    }, 
	    {
	      "answer": "Blood", 
	      "category": 1, 
	      "difficulty": 4, 
	      "id": 22, 
	      "question": "Hematology is a branch of medicine involving the study of what?"
	    }, 
	    {
	      "answer": "Mostafa", 
	      "category": 1, 
	      "difficulty": 2, 
	      "id": 24, 
	      "question": "what is your name"
	    }
	  ], 
	  "success": true, 
	  "total_questions": 6
	}

5) **Create new question with specific category**
      
      **URL** : `/questions`

      **Method** : `POST`

      **Auth required** : NO

      **Permissions required** : None

      #### Success Response

      **Code** : `200 OK`

      **Content examples**

      	curl -X POST http://127.0.0.1:5000/questions -H "content-Type:application/json" -d '{"question":"what is your name" , "answer":"Mostafa", "difficulty":2,"category":1}'
 
      
      **Json Response**:
       
          
			       {
	  "Created": 24, 
	  "questions": [
	    {
	      "answer": "Maya Angelou", 
	      "category": 4, 
	      "difficulty": 2, 
	      "id": 5, 
	      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
	    }, 
	    {
	      "answer": "Tom Cruise", 
	      "category": 5, 
	      "difficulty": 4, 
	      "id": 4, 
	      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
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
	    }, 
	    {
	      "answer": "Escher", 
	      "category": 2, 
	      "difficulty": 1, 
	      "id": 16, 
	      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
	    }, 
	    {
	      "answer": "Mona Lisa", 
	      "category": 2, 
	      "difficulty": 3, 
	      "id": 17, 
	      "question": "La Giaconda is better known as what?"
	    }
	  ], 
	  "success": true, 
	  "total_questions": 17
	}
