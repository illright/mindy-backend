"""Database models"""
from datetime import datetime
from enum import Enum, auto

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PracticeSessionEventType(Enum):
    question = auto()
    answer = auto()
    problem_solved = auto()
    difficulty_inc = auto()
    difficulty_dec = auto()


class School(db.Model):
    __tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    # property `teachers` created with a backref


class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    # active=db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    is_teacher = db.Column(db.Boolean, default=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=True)
    class_numb = db.Column(db.String(5), nullable=True)
    class_letter = db.Column(db.String(5), nullable=True)
    interest1 = db.Column(db.String(256), nullable=True)
    interest2 = db.Column(db.String(256), nullable=True)
    interest3 = db.Column(db.String(256), nullable=True)
    # property `enrollments` created with a backref
    # property `created_courses` created with a backref

    school = db.relationship('School',
                             backref=db.backref('teachers',
                                                lazy=True,
                                                cascade='all, delete-orphan'))


class TestResult(db.Model):
    __tablename__ = 'test_results'
    last_test_id = db.Column(db.Integer, nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow, primary_key=True)
    reflexion = db.Column(db.Float, nullable=True)
    prof_orientation = db.Column(db.Float, nullable=True)
    leader = db.Column(db.Float, nullable=True)
    critical_thinking = db.Column(db.Float, nullable=True)
    family = db.Column(db.Float, nullable=True)
    logic = db.Column(db.Float, nullable=True)
    science = db.Column(db.Float, nullable=True)
    communication = db.Column(db.Float, nullable=True)
    student_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=True)

    test_owner = db.relationship('Account',
                                 backref=db.backref('testresult',
                                                    lazy=True,
                                                    cascade='all, delete-orphan'))


# class Quiz(db.Model):
#     __tablename__ = 'quiz'
#
#     id = db.Column(db.Integer, primary_key=True)
#     questions = db.Column(db.Integer, nullable=False)
#     correct = db.Column(db.Integer, nullable=False)
#     tasks = db.Column(db.String(4096), nullable=True)
#     in_class = db.Column(db.Boolean, nullable=True)
#     solutions = db.Column(db.String(4096), nullable=True)
#     student_id = db.Column(db.Integer, db.ForeignKey(
#         'enrollments.enrollee_id'), nullable=False)
#
#     quiz_owner = db.relationship('Enrollment',
#                                  backref=db.backref('quiz_owner',
#                                                     lazy=True,
#                                                     cascade='all, delete-orphan'))


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey(
        'accounts.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    elective = db.Column(db.Boolean, nullable=True)
    interest1 = db.Column(db.String(256), nullable=True)
    interest2 = db.Column(db.String(256), nullable=True)
    interest3 = db.Column(db.String(256), nullable=True)
    grade = db.Column(db.Integer, nullable=True)
    tag = db.Column(db.String(256), nullable=True)
    # property `lessons` created with a backref
    # property `enrollments` created with a backref

    creator = db.relationship('Account',
                              backref=db.backref('created_courses',
                                                 lazy=True,
                                                 cascade='all, delete-orphan'))


class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    enrollee_id = db.Column(db.Integer, db.ForeignKey(
        'accounts.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.id'), nullable=False)
    # property `block_reports` created with a backref
    # property `lesson_reports` created with a backref

    enrollee = db.relationship('Account',
                               backref=db.backref('enrollments',
                                                  lazy=True,
                                                  cascade='all, delete-orphan'))
    course = db.relationship('Course',
                             backref=db.backref('enrollments',
                                                lazy=True,
                                                cascade='all, delete-orphan'))


class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey(
        'quiz.id'), nullable=False)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    consultation_time = db.Column(db.DateTime, nullable=True)
    order = db.Column(db.Integer, nullable=False)
    quiz = db.Column(db.String(4096), nullable=True)
    # property `learning_blocks` created with a backref
    # property `reports` created with a backref
    # property `practice_sessions` created with a backref

    course = db.relationship('Course',
                             backref=db.backref('lessons',
                                                lazy=True,
                                                cascade='all, delete-orphan'))
    quizes = db.relationship('Quiz',
                             backref=db.backref('lessons_with_quizes',
                                                lazy=True,
                                                cascade='all, delete-orphan'))


class LearningBlock(db.Model):
    __tablename__ = 'learning_blocks'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey(
        'lessons.id'), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    # property `varieties` created with a backref

    lesson = db.relationship('Lesson',
                             backref=db.backref('learning_blocks',
                                                lazy=True,
                                                cascade='all, delete-orphan'))


class LearningBlockVariety(db.Model):
    __tablename__ = 'learning_block_varieties'

    id = db.Column(db.Integer, primary_key=True)
    block_id = db.Column(db.Integer, db.ForeignKey(
        'learning_blocks.id'), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    text_file = db.Column(db.String(256), nullable=True)
    video_file = db.Column(db.String(256), nullable=True)
    audio_file = db.Column(db.String(256), nullable=True)

    block = db.relationship('LearningBlock',
                            backref=db.backref('varieties',
                                               lazy=True,
                                               cascade='all, delete-orphan'))


class LearningBlockReport(db.Model):
    __tablename__ = 'learning_block_reports'

    id = db.Column(db.Integer, primary_key=True)
    enrollment_id = db.Column(db.Integer, db.ForeignKey(
        'enrollments.id'), nullable=False)
    variety_id = db.Column(db.Integer,
                           db.ForeignKey('learning_block_varieties.id'),
                           nullable=False)
    help_needed = db.Column(db.Boolean, nullable=False)

    enrollment = db.relationship('Enrollment',
                                 backref=db.backref('block_reports',
                                                    lazy=True,
                                                    cascade='all, delete-orphan'))
    variety = db.relationship('LearningBlockVariety')


class LessonReport(db.Model):
    __tablename__ = 'lesson_reports'

    id = db.Column(db.Integer, primary_key=True)
    enrollment_id = db.Column(db.Integer, db.ForeignKey(
        'enrollments.id'), nullable=False)
    lesson_id = db.Column(db.Integer,
                          db.ForeignKey('lessons.id'),
                          nullable=False)
    quiz_grade = db.Column(db.Float, nullable=True)

    enrollment = db.relationship('Enrollment',
                                 backref=db.backref('lesson_reports',
                                                    lazy=True,
                                                    cascade='all, delete-orphan'))
    lesson = db.relationship('Lesson',
                             backref=db.backref('reports',
                                                lazy=True,
                                                cascade='all, delete-orphan'))


class PracticeSession(db.Model):
    __tablename__ = 'practice_sessions'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer,
                          db.ForeignKey('lessons.id'),
                          nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    solved = db.Column(db.Integer, nullable=True)
    questions = db.Column(db.Integer, nullable=True)
    # property `problems` created with a backref
    # property `session_events` created with a backref

    lesson = db.relationship('Lesson',
                             backref=db.backref('practice_sessions',
                                                lazy=True,
                                                cascade='all, delete-orphan'))


class PracticeProblem(db.Model):
    __tablename__ = 'practice_problems'

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer,
                           db.ForeignKey('practice_sessions.id'),
                           nullable=False)
    statement = db.Column(db.String(1024), nullable=False)
    answer = db.Column(db.String(512), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)

    session = db.relationship('PracticeSession',
                              backref=db.backref('problems',
                                                 lazy=True,
                                                 cascade='all, delete-orphan'))


class PracticeSessionEvent(db.Model):
    __tablename__ = 'practice_session_events'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'accounts.id'), nullable=False)
    session_id = db.Column(db.Integer,
                           db.ForeignKey('practice_sessions.id'),
                           nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    problem_id = db.Column(db.Integer,
                           db.ForeignKey('practice_problems.id'),
                           nullable=True)
    elaboration = db.Column(db.String(256), nullable=True)
    type = db.Column(db.Enum(PracticeSessionEventType), nullable=False)

    student = db.relationship('Account')
    session = db.relationship('PracticeSession',
                              backref=db.backref('session_events',
                                                 lazy=True,
                                                 cascade='all, delete-orphan'))
    problem = db.relationship('PracticeProblem')
