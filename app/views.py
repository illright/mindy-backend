"""Application views"""

from datetime import datetime
import mimetypes
import json

# pylint: disable=import-error
import requests
from flask import Blueprint, abort, jsonify, request, current_app
from flask.views import MethodView
from psycopg2.extras import DateRange
from sqlalchemy import or_
import werkzeug
from werkzeug.exceptions import BadRequestKeyError
# pylint: enable=import-error

from app.models import (Course, Enrollment, Lesson, LearningBlock, LearningBlockVariety)

api = Blueprint('api', __name__)  # pylint: disable=invalid-name

# ----- Projects -----

@api.route('/courses')
def list_courses():
    # yapf: disable
    courses = []
    for course in Course.query.all():
        course_json = {
            'id': course.id,
            'name': course.name,
            'teacher': course.creator,
            'start_time': course.start_time,
            'end_time': course.end_time,
        }
        courses.append(course_json)
    # yapf: enable

    return jsonify(courses)

@api.route('/course/<int:id>')
def get_course(id):
	course = Course.query.get_or_404(id)
	lessons = Lesson.query.filter_by(course_id=id).all()
	obj = {
		'id': course.id,
		'name': course.name,
		'teacher': course.creator,
		'school': course.creator.school,
		'start_time': course.start_time,
		'end_time': course.end_time,
		'lessons': [{'name': l.name, 'description': l.description, 'order': l.order} for l in lessons]
	}
	return jsonify(obj)

@api.route('/course/<int:course_id>/lessons')
def get_lessons(course_id):
	lessons = Lesson.query.filter_by(course_id=course_id).order_by(Lesson.order.asc()).all()
	return jsonify(lessons)

@api.route('/course/<int:course_id>/lesson/<int:lesson_id>')
def get_lesson(course_id, lesson_id):
	lesson = Lesson.query.get_or_404(lesson_id)
	blocks = LearningBlock.query.filter_by(lesson_id=lesson_id).all()
	varieties = [LearningBlockVariety.query.filter_by(block_id=block.id).all() for block in blocks]

	obj = {
		'name': lesson.name,
		'description': lesson.description,
		'order': lesson.order,
		'blocks': varieties,
		'quiz': lesson.quiz,
	}
	return jsonify(obj)

@api.route('/course/<int:course_id>/lesson/<int:lesson_id>/quiz', methods=['POST'])
def submit_quiz(course_id, lesson_id):
	lesson = Lesson.query.get_or_404(lesson_id)
	correct_quiz = json.loads(lesson.quiz)
	submitted_quiz = request.get_json(force=True)

	correct = 0
	for problem in correct_quiz:
		if problem.answer == next(q.answer for q in submitted_quiz if question == problem.question):
			correct += 1
	return jsonify({
		'result': correct / len(correct_quiz),
	})

''' WIP
@api.route('/course/<int:course_id>/lesson/<int:lesson_id>/complete', methods=['POST'])
def complete_block(course_id, lesson_id):
	req = request.get_json(force=True)
	block_var_id = req['block']
	needs_help = req['needs_help']

	block_var = LearningBlockVariety.query.filter_by(id=block_var_id)
'''