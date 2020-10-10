printf "curl -d '{\"previous_questions\":1 , \"quiz_category\":2  }' -H \"Content-Type: application/json\" -X POST http://127.0.0.1:5000/quizzes\n\n"
curl -d '{"previous_questions":1 , "quiz_category":2  }' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/quizzes
printf "\n\n\n\n\n*********************************************\ntest\n*********************************************\n\n\n\n\n"
printf "curl -X GET http://127.0.0.1:5000/categories/6/questions\n\n"
curl -X GET http://127.0.0.1:5000/categories/6/questions
printf "\n\n\n\n\n*********************************************\ntest\n*********************************************\n\n\n\n\n" 
printf "curl http://127.0.0.1:5000/questions\n\n"
curl http://127.0.0.1:5000/questions
printf "\n\n\n\n\n*********************************************\ntest\n*********************************************\n\n\n\n\n"
curl -X DELETE http://127.0.0.1:5000/questions/8

