from tasks.workers import celery
import requests
from models.student_model import StudentModel


@celery.task()
def url_method(acedemic_details_id):
    # result = StudentModel.query.filter_by(student_id=acedemic_details_id).first()
    # response = {
    #             "student_name": result.student_name,
    #             "student_class": result.student_class,
    #             "student_age": result.student_age,
    #             "student_address": result.student_address
    #             }
    #
    # print(response)

    response = requests.get(url=f"http://127.0.0.1:5001/acedemicdetails/{acedemic_details_id}")
    print('hello i am here')
    print(response.json())




