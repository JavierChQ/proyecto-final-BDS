from student_predictor import StudentPerformancePredictor

predictor = StudentPerformancePredictor()
horas_estudio = float(input("Ingrese la cantidad de horas de estudio por semana: "))
asistencia = int(input("Ingrese el porcentaje de asistencia: "))

puntaje_examen = predictor.predict(horas_estudio, asistencia)
print(f"El puntaje predecido del examen es: {puntaje_examen:.2f}")