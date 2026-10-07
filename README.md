# Sistema de Gestión y Control de Mantenimiento de Flota Aeronáutica
**Reto de Programación — Unidad #4**  
**Facultad de Ingeniería Aeronáutica**  
**Universidad Pontificia Bolivariana (UPB)**

---

## 1. Identificación del Proyecto y Metadatos Académicos

* **Institución:** Universidad Pontificia Bolivariana (UPB) — Sede Central Medellín
* **Programa Académico:** Ingeniería Aeronáutica
* **Asignatura:** Programación / Algoritmos y Programación
* **Autores:** 
  * José Miguel Vásquez
  * Isabela Montaño
* **Fecha Límite de Entrega:** 13 de octubre de 2026
* **Entorno de Ejecución:** Python 3.10+ (Intérprete estándar / Vanilla Python)

---

## 2. Descripción General y Justificación Operativa

En el ámbito del mantenimiento aeronáutico y el cumplimiento de las normativas de aeronavegabilidad continua (FAR/EASA/RAC), la gestión de tiempos operativos en componentes críticos (*Hard-Time* y *On-Condition*) resulta esencial para evitar eventos catastróficos o paradas de flota no programadas (*AOG - Aircraft On Ground*).

Este desarrollo implementa una plataforma de consola orientada a la auditoría técnica de una aerolínea regional. El software automatiza:
1. El registro centralizado de aeronaves comerciales con sus respectivas horas globales de vuelo.
2. La asignación e inspección de piezas críticas vinculadas estructuralmente a cada aeronave.
3. La ejecución de un motor de auditoría determinista que identifica componentes cuyo desgaste operativo ha alcanzado o sobrepasado el umbral técnico de servicio ($\text{Horas Actuales} \ge \text{Límite Técnico}$), emitiendo reportes de alerta preventiva y correctiva inmediata.

---

## 3. Arquitectura del Software y Modelo de Memoria RAM

El sistema no depende de bases de datos externas ni de serialización secundaria; toda la persistencia opera de forma volátil durante el tiempo de ejecución mediante estructuras compuestas anidadas en memoria RAM.

### 3.1. Estructura Jerárquica de Datos (`diccionario_flota`)
El núcleo de almacenamiento está gobernado por un diccionario principal donde cada clave (*key*) corresponde a la matrícula unica e irremplazable de la aeronave, apuntando a un sub-diccionario de atributos y una lista de sub-diccionarios para sus componentes:

```text
diccionario_flota = {
    "HK-5001": {
        "modelo": "Airbus A320",
        "horas": 12500.5,
        "componentes": [
            {
                "nombre": "Bomba Hidráulica Principal",
                "horas_uso": 1200.0,
                "limite_horas": 1000.0
            },
            {
                "nombre": "Actuador de Flaps",
                "horas_uso": 450.0,
                "limite_horas": 600.0
            }
        ]
    }
}