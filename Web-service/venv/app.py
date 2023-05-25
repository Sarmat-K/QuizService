from flask import Flask, request, jsonify
import requests
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0123456789@localhost:5432/postgres'
db = SQLAlchemy(app)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String)
    answer_text = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, question_text, answer_text):
        self.question_text = question_text
        self.answer_text = answer_text


@app.route('/api/questions', methods=['POST'])
def generate_questions():
    questions_num = request.json['questions_num']
    questions = []

    while len(questions) < questions_num:
        response = requests.get('https://jservice.io/api/random?count=1')
        data = response.json()

        for item in data:
            existing_question = Question.query.filter_by(question_text=item['question']).first()
            if existing_question:
                continue

            question = Question(item['question'], item['answer'])
            db.session.add(question)
            questions.append({'question': item['question'], 'answer': item['answer']})

    db.session.commit()

    return jsonify({'questions': questions})


if __name__ == '__main__':
    app.run()
