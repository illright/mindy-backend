"""Application views"""

from datetime import datetime
import mimetypes
import json
import math
import operator

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

@api.route('/account/<int:id>')
def get_account(id):
    account = Account.query.get_or_404(id)
    school = School.query.get(account.school_id or -1)
    obj = {
        'id': account.id,
        'name': account.name,
        'email': account.email,
        'is_teacher': account.is_teacher,
        'class_number': account.class_numb,
        'class_letter': account.class_letter,
        'school': {
            'id': school.id,
            'name': school.name,
            'is_verified': school.is_verified,
        } if school is not None else None,
        'interest_1': account.interest1 if account.interest1 is not None else None,
        'interest_2': account.interest2 if account.interest2 is not None else None,
        'interest_3': account.interest2 if account.interest3 is not None else None,
        'phycho_test': {
            'communication': account.testresult.communication,
            'reflexion': account.testresult.reflexion,
            'prof_orientation': account.testresult.prof_orientation,
            'leader': account.testresult.leader,
            'critical_thinking': account.testresult.critical_thinking,
            'family': account.testresult.family,
            'logic': account.testresult.logic,
            'science': account.testresult.science,
        } if account.testresult is not None else None,
    }
    return jsonify(obj)


@api.route('/account/<int:id>')
def get_account(id):
    account = Account.query.get_or_404(id)
    school = School.query.get(account.school_id or -1)
    obj = {
        'id': account.id,
        'name': account.name,
        'email': account.email,
        'is_teacher': account.is_teacher,
        'class_number': account.class_numb,
        'class_letter': account.class_letter,
        'school': {
            'id': school.id,
            'name': school.name,
            'is_verified': school.is_verified,
        } if school is not None else None,
    }
    return jsonify(obj)


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


def list_courses_arr():
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

    return courses


def give_ones_courses(id):
    courses = []
    for course in Enrollment.query.get_or_404(enrollee_id=id):
        course_json = {
            'id': course.id,
            'name': course.name,
            'teacher': course.creator,
            'start_time': course.start_time,
            'end_time': course.end_time,
            'grade': course.grade,
            'tag': course.tag
        }
        courses.append(course_json)
    return courses


@api.route('/course/<int:id>')
def get_course(id):
    course = Course.query.get_or_404(id)
    lessons = Lesson.query.filter_by(course_id=id).all()
    school = course.creator.school
    obj = {
        'id': course.id,
        'name': course.name,
        'teacher': {
            'id': course.creator.id,
            'name': course.creator.name,
            'email': course.creator.email,
        },
        'school': {
            'id': school.id,
            'name': school.name,
            'is_verified': school.is_verified,
        } if school is not None else None,
        'start_time': course.start_time,
        'end_time': course.end_time,
        'lessons': [{'id': l.id, 'name': l.name, 'description': l.description, 'order': l.order} for l in lessons]
    }
    return jsonify(obj)


@api.route('/course/<int:course_id>/lessons')
def get_lessons(course_id):
    lessons = Lesson.query.filter_by(
        course_id=course_id).order_by(Lesson.order.asc()).all()
    obj = [{
        'id': lesson.id,
        'name': lesson.name,
        'description': lesson.description,
        'order': lesson.order,
        'quiz': json.loads(lesson.quiz)
    } for lesson in lessons]
    return jsonify(obj)


def student_quiz_average(student, course):
    enrollment = Enrollment.query.filter_by(
        enrollee_id=student.id, course_id=course.id).one()
    lessons = Lesson.query.filter_by(enrollment_id=enrollment.id).all()
    total_grade = sum(lesson.quiz_grade for lesson in lessons) / len(lessons)
    return total_grade

def student_task_average(student, course):
    enrollment = Enrollment.query.filter_by(
        enrollee_id=student.id, course_id=course.id).one()
    lessons = Lesson.query.filter_by(enrollment_id=enrollment.id).all()
    counter=lessons.query.practice_sessions.query.score.count()
    a = sum(lessons.query.practice_sessions.query.score)/sum(lessons.query.practice_sessions.query.questions)
    a = round(a/counter)
    return a
    # total_grade = sum(lesson.quiz_grade for lesson in lessons) / len(lessons)
#     return total_grade


def course_average_grades(student_id):
    courses_list = give_ones_courses(student_id)
    for i in courses_list:
        # Enrollment.query.filter_by(enrollee_id=student_id)
        grade = ((student_quiz_average(student=student_id, course=i) +student_task_average(student=student_id, course=i))/2)

    return grade



@api.route('/course/<int:course_id>/lesson/<int:lesson_id>')
def get_lesson(course_id, lesson_id):
    user = None
    if current_user.is_authenticated:
        user = Account.query.get(current_user.get_id())
    course = Course.query.get_or_404(course_id)
    lesson = Lesson.query.get_or_404(lesson_id)
    blocks = LearningBlock.query.filter_by(lesson_id=lesson_id).all()
    varieties = []
    if user is None:
        for block in blocks:
            block_vars = LearningBlockVariety.query.filter_by(
                block_id=block.id).all()
            varieties.push(block_vars[len(block_vars) // 2])
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


def reccomend_course():
    results = {
        'communication': 0,
        'reflexion': 0,
        'prof_orientation': 0,
        'leader': 0,
        'critical_thinking': 0,
        'family': 0,
        'logic': 0,
        'science': 0
    }
    if current_user.is_authenticated:
        user = Account.query.get(current_user.get_id())
    acc = json.loads(get_account(user))
    int1 = acc.get('interest_1')
    int2 = acc.get('interest_2')
    int3 = acc.get('interest_3')
    courses = give_ones_courses(user)
    naming = []
    counting = {}
    for i in range(len(courses)):
        if courses[i].get('tag') not in counting.keys():
            naming.append(courses[i].get('name'))
            counting[courses[i].get('tag')] = 2
            results[courses[i].get('tag')] = results.get(courses[i].get('tag')) + courses[i].get('grade')
        else:
            naming.append(courses[i].get('name'))
            counting[courses[i].get('tag')] = 1 + counting.get(courses[i].get('tag'))
            results[courses[i].get('tag')] = results.get(courses[i].get('tag')) + courses[i].get('grade')
    for i in results.keys():
        results[i] = (results.get(i) + acc.get('phycho_test', {}).get(i)) / counting.get(i)

    sorted_res = sorted(results.items(), key=operator.itemgetter(1))
    all_courses = list_courses_arr()
    all_courses_names = []
    for i in all_courses:
        all_courses_names.append(i.get('name'))
    all_courses_names = list(set(all_courses_names) - set(naming))
    possible_rec = []
    for i in all_courses:
        if i.get('name') in all_courses_names:
            if i.get('tag') in sorted_res[0:3]:
                if i.get('interest_1') == int1 or i.get('interest_2') == int2 or int3 == i.get('interest_3'):
                    possible_rec.append(i)
    if len(possible_rec) == 0:
        return "Ask your teacher for a personal advice"
    else:
        return possible_rec


''' WIP
@api.route('/course/<int:course_id>/lesson/<int:lesson_id>/complete', methods=['POST'])
def complete_block(course_id, lesson_id):
    req = request.get_json(force=True)
    block_var_id = req['block']
    needs_help = req['needs_help']

    block_var = LearningBlockVariety.query.filter_by(id=block_var_id)
'''
