"""Application views"""

from datetime import datetime
import mimetypes
import json
import math

# pylint: disable=import-error
import requests
from flask import Blueprint, abort, jsonify, request, current_app
from flask_login import current_user
from flask.views import MethodView
from psycopg2.extras import DateRange
from sqlalchemy import or_
import werkzeug
from werkzeug.exceptions import BadRequestKeyError
# pylint: enable=import-error


from .models import (Course, Enrollment, Lesson,
                     LearningBlock, LearningBlockVariety, Account, School)

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


def student_quiz_average(student, course):
    enrollment = Enrollment.query.filter_by(
        enrollee_id=student.id, course_id=course.id).one()
	lessons = Lesson.query.filter_by(enrollment_id=enrollment.id).all()
	total_grade = sum(lesson.quiz_grade for lesson in lessons) / len(lessons)
	return total_grade


@api.route('/course/<int:course_id>/lesson/<int:lesson_id>')
def get_lesson(course_id, lesson_id):
	user = None
	if current_user.is_authenticated():
		user = Account.query.get_or_404(current_user.get_id())
	course = Course.query.get_or_404(course_id)
	lesson = Lesson.query.get_or_404(lesson_id)
	blocks = LearningBlock.query.filter_by(lesson_id=lesson_id).all()
	varieties = []
	if user is None:
		for block in blocks:
            block_vars = LearningBlockVariety.query.filter_by(
                block_id=block.id).all()
			varieties.push(block_vars[len(block_vars)//2])
	elif user.is_teacher:
		for block in blocks:
            block_vars = LearningBlockVariety.query.filter_by(
                block_id=block.id).all()
			varieties.append(block_vars)
	else:
		for block in blocks:
            block_vars = LearningBlockVariety.query.filter_by(
                block_id=block.id)
			avg_grade = student_quiz_average(user, course)
			difficulty = math.ceil(avg_grade * len(block_vars))
			block_var = block_vars.filter_by(difficulty=difficulty).one()
			varieties.push(block_var)

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
        if problem.answer == next(q.answer for q in submitted_quiz if q.question == problem.question):
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
