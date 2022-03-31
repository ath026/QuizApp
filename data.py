import requests

response = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')

questions = response.json()
print(questions)

question_data = questions["results"]
