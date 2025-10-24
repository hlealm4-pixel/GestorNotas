cursos = []

def registrar_curso():
    """ Agrega un nuevo curso a la lista original de cursos. """
    nombre = solicitad_dato("\nIngrese el nombre del curso: ")
    nota = solicitad_dato("Ingrese la nota obtenida: ", lambda n: 0 <= int(n) <= 100, int)
    cursos.append({"nombre":nombre, "nota": nota})
    print("Curso regristrado exitosamente")

def mostrar_cursos_notas():
    """ Muestra todos los cursos agregados a la lista original. """
    hay_cursos()
    print("\nTodos los cursos:")
    for i in range(0, len(cursos)):
        curso = cursos[i]
        print(f"{i + 1}) {curso["nombre"]} - Nota: {curso["nota"]}")

def calcular_promedio():
    """ Calcula el promedio de todas las notas de todos los cursos """
    hay_cursos()
    total_notas = sum(c["nota"] for c in cursos)
    promedio = total_notas / len(cursos)
    print(f"\nPromedio general {promedio}")

def contar_cursos():
    """ Cuenta cuantos cursos son aprobados y cuantos son reprobados """
    hay_cursos()
    aprobados = sum(c for c in cursos if c["nota"] >= 60)
    reprobados = len(cursos) - aprobados
    print(f"\nCursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")

def buscar_curso_nombre_lineal():
    """ De manera lineal busca el nombre solicitado por el usuario en la lista orignal de cursos """
    hay_cursos()
    nombre = solicitad_dato("\nIngrese el nombre a buscar: ").lower()
    encontrados = 0
    print("\nCursos Encontrados:")
    for curso in cursos:
        if nombre in curso["nombre"].lower():
            encontrados += 1
            print(f"{encontrados}) {curso["nombre"]} - Nota: {curso["nota"]}")
    if encontrados == 0:
        print(f"No se encontraron cursos para la busqueda '{nombre}'")

def actualizar_nota():
    """ Actualiza la nota del curso indicado por el usuario. La nota debe esra en un rango de [0, 100] """
    curso = seleccionar_curso("actualizar su nota")
    nota = solicitad_dato("Ingrese la nota obtenida: ", lambda n: 0 <= int(n) <= 100, int)
    curso["nota"] = nota
    print("\nNota actualizada exitosamente")

def eliminar_curso():
    """ Elimina el curso indicado por el usuario de la lista original de cursos """
    curso_indice = seleccionar_curso("eliminar", indice=True)
    cursos.pop(curso_indice)
    print("\nCurso eliminado exitosamente")

def ordenar_curso_nota():
    """ Ordena los cursos segun la nota y muestra el orden resultante al usuario. Se utiliza ordenamiento de burbuja """
    hay_cursos()
    lista = cursos.copy()
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j]["nota"] < lista[j + 1]["nota"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print("\nCursos ordenados por nota:")
    for i in range(0, lista):
        curso = lista[i]
        print(f"{i + 1}) {curso['nombre']} - Nota: {curso['nota']}")

def ordenar_curso_nombre():
    """ Ordena los cursos segun el nombre y muestra el orden resultante al usuario. Se utiliza ordenamiento de insercion """
    hay_cursos()
    lista = cursos.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["nombre"].lower() > clave["nombre"].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    print("\nCursos ordenados por nombre:")
    for i in range(0, lista):
        curso = lista[i]
        print(f"{i + 1}) {curso['nombre']} - Nota: {curso['nota']}")

def buscar_curso_nombre_binaria():
    """ Buesca el curso en la lista orignal y muestra el resultado al usuario. Se utiliza busqueda binaria """
    hay_cursos()
    lista = cursos.copy()
    nombre = solicitad_dato("Ingrese el nombre del dato a buscar: ").lower()
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        curso_actual = lista[medio]["nombre"].lower()
        if curso_actual == nombre:
            print(f"\nCurso encontrado: {lista[medio]['nombre']} - Nota: {lista[medio]['nota']}\n")
            return
        elif curso_actual < nombre:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print("Curso no encontrado\n")

def simular_cola():
    """ El usuario da un listado de cursos que desea irse a revision. Recorre la cola mostrando que curso esta recorriendo """
    cola = []
    print("\nIngrese curso para revisión (escriba 'fin' para terminar):")
    while True:
        dato = solicitad_dato("> ")
        if dato.lower().replace(" ", "") == 'fin':
            break
        cola.append()
    print("\nProcesando solicitudes:")
    for elemento in cola:
        print(f"Revisando: {elemento}")

def hay_cursos():
    """ Verifica que la lista de cursos no este vacia, de lo contrario mostrara la excepcion y no continuara con la ejecucion """
    if not cursos:
        raise Exception("\nNo hay cursos")

def solicitad_dato(texto_solicitud, func = None, type=str):
    """ Solicita un dato cualquiera indicado desde el lugar donde se llama la funcion, donde tiene que cumplir los requirimientos de func y type"""
    while True:
        dato = input(texto_solicitud)
        if bool(dato.replace(" ", "")):
            if not func:
                return type(dato)
            try:
                if func(dato):
                    return type(dato)
            except Exception:
                pass
        print("Dato ingresado no valido")

def seleccionar_opcion(rango, texto_ingreso="- Seleccione una opcion: "):
    """ Devuelve un indice que este dentro del 'rango' esto sirve para cuando se muestra una lista de opciones al usuario """
    opciones = [n for n in range(1, rango + 1)]
    while True:
        opcion = input(texto_ingreso)
        if opcion.isdigit():
            if (opcion := int(opcion)) in opciones:
                return opcion
        print("Ingrese una opcion correcta")

def seleccionar_curso(accion, indice=False):
    hay_cursos()
    mostrar_cursos_notas()
    opcion = seleccionar_opcion(len(cursos), f"- Seleccione el curso que desea {accion}: ")
    return cursos[opcion - 1] if not indice else opcion - 1

def opciones():
    print("\n====== GESTOR DE NOTAS ACADEMICAS ======")
    print("1) Registrar nuevo curso")
    print("2) Mostrar todos los cursos y notas")
    print("3) Calcular promedio general")
    print("4) Contar cursos aprobados y reprobados")
    print("5) Buscar curso por nombre (busqueda lineal)")
    print("6) Actualizar nota del curso")
    print("7) Eliminar un curso")
    print("8) Ordenar cursos por nota (ordenamiento burbuja)")
    print("9) Ordenar cursos por nombre (ordenamiento insercion)")
    print("10) Buscar curso por nombre (busqueda binaria)")
    print("11) Simular cola de solicitudes de revision")
    print("13) Sair")
    return seleccionar_opcion(13)

def main():
    acciones = {
        1: registrar_curso,
        2: mostrar_cursos_notas,
        3: calcular_promedio,
        4: contar_cursos,
        5: buscar_curso_nombre_lineal,
        6: actualizar_nota,
        7: eliminar_curso,
        8: ordenar_curso_nota,
        9: ordenar_curso_nombre,
        10: buscar_curso_nombre_binaria,
        11: simular_cola,
    }
    while True:
        try:
            opcion = opciones()
            if opcion == 13:
                break
            acciones[opcion]()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
