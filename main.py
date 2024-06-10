
from flask import Flask, render_template

app = Flask(__name__)

lessons = [
    {
        "id": 1,
        "title": "Lesson 1",
        "content": "This is the content of Lesson 1."
    },
    {
        "id": 2,
        "title": "Lesson 2",
        "content": "This is the content of Lesson 2."
    },
    {
        "id": 3,
        "title": "Lesson 3",
        "content": "This is the content of Lesson 3."
    }
]

@app.route('/')
def index():
    return render_template('index.html', lessons=lessons)

@app.route('/lessons')
def lessons():
    return render_template('lessons.html', lessons=lessons)

@app.route('/lesson/<int:lesson_id>')
def lesson_detail(lesson_id):
    lesson = next((lesson for lesson in lessons if lesson["id"] == lesson_id), None)
    if lesson is None:
        return render_template('error.html'), 404
    return render_template('lesson_detail.html', lesson=lesson)

if __name__ == '__main__':
    app.run(debug=True)
