from utils.db import db
from student_predictor import StudentPerformancePredictor

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    horas_estudio = db.Column(db.Float, nullable=False)
    asistencia = db.Column(db.Float, nullable=False)
    puntaje_examen = db.Column(db.Float, nullable=False)

    def __init__(self, horas_estudio,asistencia):
        self.horas_estudio = horas_estudio
        self.asistencia = asistencia
        self.puntaje_examen = 0
    
    @staticmethod
    def get_all():
        return Student.query.all()

    @staticmethod
    def get_by_id(id):
        return Student.query.get(id)
    
    def save(self):
        ml_student = StudentPerformancePredictor()
        self.puntaje_examen = ml_student.predict(self.horas_estudio, self.asistencia)
        
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()