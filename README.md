# Proyecto: AI Math Challenge (AIMO Progress Prize 3)

Este repositorio contiene la información, recursos y la planificación interna del equipo para la competencia
---

## Participantes

| Nombre | Usuario Kaggle | Usuario GitHub |
| :--- | :--- | :--- |
| Jerónimo Hoyos Botero | [Scratchbox](https://www.kaggle.com/Scratchbox) | [Usuario](https://github.com/jerohoyos) |
| Jose Miguel García Vélez | [jmiguelgarciav](https://www.kaggle.com/jmiguelgarciav) | [Usuario](https://github.com/Usuario) |
| Juan Camilo Ramón Pérez | [juanoff](https://www.kaggle.com/juanoff) | [Usuario](https://github.com/Usuario) |
| Daniel Fernando Verdecia Goyeneche | [danielverdecia](https://www.kaggle.com/danielverdecia) | [Usuario](https://github.com/Usuario) |
| Samuel Vasco Gonzalez | [SamuVG](https://www.kaggle.com/SamuVG) | [Usuario](https://github.com/Usuario) |

---

## Asignación de Tareas

**Regla obligatoria del equipo:** Todos los miembros deben registrar su nombre en al menos una tarea. Las tareas se actualizarán periódicamente para revisar el progreso. Los miembros que no participen activamente ni actualicen su estado podrán ser retirados del equipo antes del cierre de la competencia.

**Instrucciones de uso:**
* Añadir su nombre en la columna *Responsables*.
* Actualizar el estado (*Pendiente, En progreso, Completado*).
* Se recomienda un mínimo de 2 personas por tarea.

| Tarea | Descripción | Estado | Responsables |
| :--- | :--- | :--- | :--- |
| **Testing de Resultados Actuales** | Evaluar y documentar los resultados actuales del modelo con la configuración vigente. | Pendiente | [Nombre 1], [Nombre 2] |
| **Búsqueda de Datos en Texto** | Recopilar datasets en formato texto para alimentar la base de conocimiento de los RAGs. | Pendiente | [Nombre 1], [Nombre 2] |
| **Implementación de RAG** | Desarrollar el sistema de Generación Aumentada por Recuperación (RAG). | Pendiente | [Nombre 1], [Nombre 2] |
| **LangChain Personalizado** | Diseñar y estructurar un pipeline personalizado con LangChain. | Pendiente | [Nombre 1], [Nombre 2] |
| **Implementación de MCP** | Configurar e implementar los Model Context Protocol (MCP). | Pendiente | [Nombre 1], [Nombre 2] |
| **Optimización de Inferencia** | Reducir latencia, mejorar determinismo y optimizar uso de memoria. | Pendiente | [Nombre 1], [Nombre 2] |
| **Post-processing & Output Control** | Garantizar que todas las predicciones cumplan el formato requerido por la competencia. | Pendiente | [Nombre 1], [Nombre 2] |

---

## Objetivo de la Competencia – AIMO Progress Prize 3

La competencia busca desarrollar modelos *open-weight* capaces de resolver problemas matemáticos de nivel olímpico mediante razonamiento matemático avanzado.

**Los problemas:**
* Están en formato LaTeX.
* Requieren:
  * Razonamiento simbólico.
  * Inferencia lógica multi-paso.
  * Resolución formal de problemas.
  * Generalización robusta (sin contaminación train-test).

**Áreas evaluadas:**
* Álgebra.
* Combinatoria.
* Geometría.
* Teoría de números.

---

## Formato de Output (Restricciones de Predicción)

Cada predicción debe ser:
* Un entero.
* En el rango `[0, 99999]`.

Si el problema involucra aritmética modular, el módulo será especificado explícitamente. Para problemas del tipo: *"What is the remainder when a is divided by b?"*, el modelo debe retornar el único entero `r` tal que: `0 ≤ r < b`. Se requerirá un manejo cuidadoso del post-procesamiento para asegurar que el output cumpla con estas restricciones.

---

## Protocolo de Evaluación

### Public Leaderboard
* Evaluación sobre *public test set*.
* **Métrica:** Accuracy simple (número de respuestas correctas).

### Private Leaderboard (Evaluación Final)
Cada submission se ejecuta dos veces (*double-run evaluation*).

**Puntaje por problema:**
* **1.0** → Ambas predicciones correctas.
* **0.5** → Solo una predicción correcta.
* **0.0** → Ambas incorrectas.

*Score final = suma total de todos los problemas.*

**Esto penaliza:**
* Inferencia con alta varianza.
* Decoding no determinístico.
* Cadenas de razonamiento inestables.

---

## Submission Pipeline

* Solo se permite submission vía Kaggle Notebooks.
* Debe usarse la *official evaluation API*.
* Evaluación streaming (instancias *one-by-one*).

---

## Restricciones de Cómputo

* **CPU runtime:** ≤ 9 horas.
* **GPU runtime:** ≤ 5 horas.
* **Internet:** Sin acceso a internet.
* Se permiten modelos pre-entrenados y datasets públicos.

**Esto implica una necesidad estricta de:**
* Optimización del modelo.
* Inferencia eficiente.
* Manejo cuidadoso de la memoria.
* Estrategias determinísticas de decoding.

---

## Timeline

* **Start Date:** 20 de noviembre de 2025.
* **Entry Deadline:** 8 de abril de 2026.
* **Team Merge Deadline:** 8 de abril de 2026.
* **Final Submission Deadline:** 15 de abril de 2026.

---

## Enlaces y Recursos

*(Nota: Reemplazar los `#` con las URLs correspondientes)*

**Repositorios Base**
* [AI Math Challenge (GitHub)](#)

**Material Audiovisual**
* [How to Build an AI Math Solver](#)
* [How to Run a 3B Reasoning Model](#)

**Datasets**
* [https://huggingface.co/datasets/AI-MO/NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT)
* [https://huggingface.co/datasets/AI-MO/NuminaMath-TIR](https://huggingface.co/datasets/AI-MO/NuminaMath-TIR)
* [OpenMathReasoning (NVIDIA)](#)
* [FineMath (HuggingFace)](#)
* [Problemas oficiales IMO](#)

**Modelos**
* [Nanbeige4.1-3B](#)

**Notebooks Kaggle**
* [Utility Notebook 1/2](#)
* [Submission Demo Notebook 2/2](#)
