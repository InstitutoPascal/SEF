# -*- coding: utf-8 -*-

def buscar_dni():
    formulario= SQLFORM.factory(
        Field('dni', 'integer', label=T('DNI'), requires=[IS_NOT_EMPTY(error_message="Es necesario completar este campo"), IS_IN_DB(db,db.alumno.dni, error_message="El DNI ingresado no esta en la base de datos."), IS_LENGTH(8,error_message="Excedio la cantidad de digitos permitidos para este campo.")]))
    if formulario.accepts(request.vars, session):
        dni = formulario.vars.dni
        redirect(URL('generar_boleta',args=(),vars=dict(dni=dni)))
        response.flash='Formulario aceptado'
    elif formulario.errors:
        response.flash='Hay uno o más errores en el formulario'
    return dict(formulario=formulario)

def generar_boleta():
    dni_seleccionado=''
    curso_seleccionado=''
    cuota_seleccionado=''
    cuotaid=''
    dni = request.vars.dni
    dni_seleccionado = db(dni == db.alumno.dni).select(db.alumno.ALL) #mediante una consulta a la db obtiene un reg con los datos del usuario seleccionado
    for x in dni_seleccionado:
        curso=x.curso #guarda el id del curso seleccionao en una variable
        curso_seleccionado= db(curso == db.curso.id).select(db.curso.ALL)
        id_alumno_seleccionado= x.id
        #cuotas= db(db.cxa.id_alumno==id_alumno_seleccionado).select(db.cxa.ALL)
        #for y in cuotas:
         #   estado=y.estado
            #if estado=='False':
               #cuotaid=y.id_cuota
            #else:
             #   break
        #cuota_seleccionado=db((db.cxa.id_alumno==id_alumno_seleccionado) & (db.cxa.id_cuota==cuotaid)).select()
    return dict(dni_seleccionado=dni_seleccionado, curso_seleccionado=curso_seleccionado, cuota_seleccionado=cuotaid, cuotaid=cuotaid)
#lista alumnos por un lado y cuotas por otro, de ahi realiza una consulta para que el id del dni que se ingreso sea igual al del alumno y con el id del alumno y las cuotas realizar un for con consulta para saber cual esta en True 

def generar_recibo():
    return dict()

def index():
    alumnos = db(db.alumno).select()
    for x in alumnos:
        consulta = db(x.id==db.cxa.id_alumno).select()
        for y in consulta:
            estado= y.estado
            if estado==False:
                q=y
                return dict(message=q)
