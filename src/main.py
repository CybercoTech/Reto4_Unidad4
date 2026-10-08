from colors import print_error, print_exito, print_alerta, print_azul


diccionario_flota = {} 
estado_sistema = True 

while estado_sistema:
    print("------ Inicio: Sistema De Gestion - Mantenimiento Y Seguimiento Estado Flota")
    print("1. Registrar Aeronave")
    print("2. Registrar Componente Critico")
    print("3. Reporte de Mantenimiento - Consultar")
    print("4. Actualizacion Horas Componente Critico")
    print("5. Salir")

    opcion = input("------ Seleccione una opcion (1-5): ").strip()

    if opcion == "1":
        print("------ Opcion 1 Seleccionada - REGISTRO DE LA AERONAVE")
        matricula = input("Ingrese la matricula de la aeronave: ").strip().upper()

        if matricula in diccionario_flota:
            print_error(f"------ Error: La matrícula '{matricula}' ya se encuentra registrada en el sistema.")

        else:
            modelo = input("Ingrese el modelo de la aeronave: ").strip()
            entrada_horas = input("Ingrese las horas de vuelo acumuladas: ").strip()
            entradas_maximas = input("Ingrese las horas de vuelo maximas permitidas: ").strip()

            try:
                horas_globales = float(entrada_horas)
                horas_maximas = float(entradas_maximas)

                if horas_globales >= 0 and horas_maximas > 0:
                    diccionario_flota[matricula] ={ 

                        "modelo": modelo,
                        "horas": horas_globales,
                        "horas_maximas": horas_maximas,
                        "componentes": []
                       
                        }

                    print_exito(f"------ Exito: Aeronave '{matricula}' registrada exitosamente.")
                else:
                    print_error("------ Error: Las horas de vuelo no pueden ser negativas, Adicionalmente las horas maximas deben ser mayores a 0.")

            except ValueError:
                print_error("------ Error: El valor ingresado debe ser numérico.")

    elif opcion == "2":
            print("------ REGISTRO DE COMPONENTE CRÍTICO")
            matricula = input("Ingrese la matricula de la aeronave a vincular: ").strip().upper()
    
            if matricula in diccionario_flota:
                nombre_componente = input("Ingrese el nombre del componente critico: ").strip()
                entrada_horas_actuales = input("Ingrese las horas de uso actuales: ").strip()
                entrada_limite_horas = input("Ingrese el limite máximo de horas permitidas: ").strip()
    
                try:
                    horas_actuales = float(entrada_horas_actuales)
                    limite_horas = float(entrada_limite_horas)
    
                    if horas_actuales >= 0 and limite_horas > 0:
                        estructura_pieza = {

                            "nombre": nombre_componente,
                            "horas_uso": horas_actuales,
                            "limite_horas": limite_horas
                        
                        }

                        diccionario_flota[matricula]["componentes"].append(estructura_pieza)
                        print_exito(f"------ Éxito: Componente '{nombre_componente}' vinculado a la aeronave '{matricula}'.")
                    else:
                        print_error("------ Error: Las horas de uso deben ser >= 0 y el limite debe ser estrictamente > 0.")
                except ValueError:
                    print_error("------ Error: Los parametros deben ser valores numericos validos.")
            else:
                print_error(f"------ Error: La aeronave con matricula '{matricula}' no existe en la base de datos.")

    elif opcion == "3":
            print("------ REPORTE DE ALERTAS DE MANTENIMIENTO")
    
            indicador_alertas = False
    
            for matricula in diccionario_flota:
                datos_aeronave = diccionario_flota[matricula]
                lista_piezas = datos_aeronave["componentes"]


                print(f"\n------ AERONAVE Matrícula: {matricula} | Modelo: {datos_aeronave['modelo']}")
                
                if datos_aeronave["horas"] >= datos_aeronave["horas_maximas"]:
                    indicador_alertas = True 
                    print_alerta(f"------ [ALERTA AERONAVE] Horas de vuelo: {datos_aeronave['horas']} / Max: {datos_aeronave['horas_maximas']}")                  
                else:
                    print(f"------ Horas de vuelo actuales: {datos_aeronave['horas']} / Max: {datos_aeronave['horas_maximas']}")

                print("------ Componentes Instalados:")


                for pieza in lista_piezas:
                    if pieza["horas_uso"] == 0:

                        print_azul(f"   * {pieza['nombre']}: [NUEVO / RESETEADO] (Límite: {pieza['limite_horas']} horas)")
                    
                    elif pieza["horas_uso"] >= pieza["limite_horas"]:

                        indicador_alertas = True
                        print_error(f"   * [ALERTA CRÍTICA] {pieza['nombre']}: {pieza['horas_uso']} horas (Límite Máximo: {pieza['limite_horas']} horas)")
                    
                    else:

                        print(f"   * {pieza['nombre']}: {pieza['horas_uso']} horas (Límite: {pieza['limite_horas']} horas)")
                
                if not lista_piezas:
                    print("   * No hay componentes registrados para esta aeronave.")


            print("\n----------------------------------------")
            if indicador_alertas:
                print_error("!!! ALERTA: mantenimiento inmediato requerido !!!")
            else: 
                print_exito("------ Estado Nominal: Ningún componente crítico requiere mantenimiento.")




    elif opcion == "4":
        print("------ ACTUALIZAR / RESETEAR HORAS DE COMPONENTE")
        matricula = input("Ingrese la matricula de la aeronave: ").strip().upper()

        if matricula in diccionario_flota:
            nombre_buscar = input("Ingrese el nombre del componente a modificar: ").strip().lower()
            
            componente_encontrado = None
            for pieza in diccionario_flota[matricula]["componentes"]:
                if pieza["nombre"].lower() == nombre_buscar:
                    componente_encontrado = pieza
                    break

            if componente_encontrado:
                print(f"Componente actual: {componente_encontrado['nombre']} | Horas actuales: {componente_encontrado['horas_uso']}")
                entrada_nuevas_horas = input("Ingrese las nuevas horas de uso (0 para resetear): ").strip()

                try:
                    nuevas_horas = float(entrada_nuevas_horas)

                    if nuevas_horas >= 0:
                        componente_encontrado["horas_uso"] = nuevas_horas
                        print_exito(f"------ Éxito: Horas del componente '{componente_encontrado['nombre']}' actualizadas a {nuevas_horas} hrs.")
                    else:
                        print_error("------ Error: Las horas de uso no pueden ser negativas.")
                except ValueError:
                    print_error("------ Error: El valor ingresado debe ser numérico.")
            else:
                print_error(f"------ Error: El componente '{nombre_buscar}' no está registrado en esta aeronave.")
        else:
            print_error(f"------ Error: La aeronave con matrícula '{matricula}' no existe.")


    elif opcion == "5":
        estado_sistema = False
        print_exito("------ Terminando procesos de consola, Sistema cerrado exitosamente.")
    
    else:
        print_error("------ Error: Parámetro de menú inválido. Ingrese una opción entre 1 y 4.")
        