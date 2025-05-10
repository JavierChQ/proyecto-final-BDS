from flask_restful import Resource,Api,abort
from flask import request
from . import bp_api
from .models import Student
from .schemas import StudentSchema


api = Api(bp_api)

class StudentApiResource(Resource):
    
    def get(self):

        data = Student.get_all()
        student_schema = StudentSchema(many=True)
                
        context = {
            'status':True,
            'message':'lista de estudiantes',
            'content':student_schema.dump(data)

        }
        
        return context,200

    def post(self):
        data = request.get_json()
        horas_estudio = data.get('horas_estudio')
        asistencia = data.get('asistencia')
        student = Student(horas_estudio,asistencia)
        student.save()
    
        data_schema = StudentSchema()
                
        context = {
            'status':True,
            'message':'Estudiante creado',
            'content':data_schema.dump(student)
        }
        return context,201

class StudentApiResourceDetail(Resource):
    
    def get_student(self,id):
        student = Student.get_by_id(id)
        if not student:
            abort(404, message="Estudiante no encontrado")
        return student
                
    def get(self,id):
        data = self.get_student(id)
        data_schema = StudentSchema()
        
        context = {
            'status':True,
            'message':'Estudiante encontrado',
            'content': data_schema.dump(data)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        
        
        student = self.get_student(id)
        student.horas_estudio = data.get('horas_estudio')
        student.asistencia = data.get('asistencia')
        student.save()
    
        data_schema = StudentSchema()
        
        context = {
            'status':True,
            'message':'Estudiante actualizado',
            'content': data_schema.dump(student)
        }
        
        return context
    
    def delete(self,id):
        student = self.get_student(id)
        student.delete()
        
        context = {
            'status':True,
            'message':'Estudiante eliminado',
        }
        
        return context, 204

api.add_resource(StudentApiResource, '/')
api.add_resource(StudentApiResourceDetail, '/<int:id>')