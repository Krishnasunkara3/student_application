import requests
from flask_restful import Resource, fields, marshal_with, reqparse, abort, request
from models.student_model import StudentModel
import requests
from db import db
from tasks.manage import manage_session
from tasks.celery_task import url_method

student_args = reqparse.RequestParser()
student_args.add_argument("student_id", type=int, help="Student id is required", required=True)
student_args.add_argument("student_name", type=str, help="Student name is required", required=True)
student_args.add_argument("student_class", type=str, help="Student name is required", required=True)
student_args.add_argument("student_age", type=int, help="Student id is required", required=True)
student_args.add_argument("student_address", type=str, required=False)

resource_fields = {
                        'student_id': fields.Integer,
                        'student_name': fields.String,
                        'student_class': fields.String,
                        'student_age': fields.Integer,
                        'student_address': fields.String
                 }


class StudentDetails(Resource):

    @manage_session
    def get(self, student_id):
        pass
        # url_method1.apply_async(args=(student_id,))
        # return "success"

    @marshal_with(resource_fields)
    def post(self, student_id):
        args = student_args.parse_args()
        result = StudentModel.query.filter_by(student_id=student_id).first()

        if result:
            abort(404, message='student id is already available')
        student_details = StudentModel(student_id=student_id, student_name=args['student_name'],
                                        student_class=args['student_class'],
                                        student_age=args['student_age'],
                                        student_address=args['student_address'])
        student_details.save_to_db()
        return student_details, 201


class AcedemicDetails(Resource):

    def get(self, student_id):
        url_method.apply_async(args=(student_id,))
        return "success"


class AcedemicResult(Resource):

    def post(self, student_id):

        response = request.get_json()
        print(response)
        return "success"

