Descripción del Proyecto
El sistema de Gestión de Servicios Hospitalarios es una solución de software desarrollada en Python bajo el paradigma de Programación Orientada a Objetos (POO).
Su propósito fundamental es administrar el flujo de atención médica mediante el registro detallado de pacientes y la facturación diferenciada de servicios.
El programa permite la creación de registros clínicos validados, distinguiendo entre atenciones de rutina y situaciones críticas. A través de una arquitectura modular,
el sistema automatiza el cálculo de costos aplicando reglas de negocio específicas (impuestos y recargos) según el tipo de servicio y provee herramientas estadísticas 
para clasificar el volumen de atención y los ingresos totales del hospital.

Explicación de Clases
La clase Paciente constituye el módulo de identidad del sistema. Su función es crear objetos que representan a los usuarios del servicio, almacenando datos demográficos como nombre, edad y contacto. 
Esta clase integra mecanismos de encapsulamiento robustos para validar la información al momento de la entrada, evitando errores de formato o datos ilógicos antes de que estos sean procesados por el resto del programa.

La clase ServicioMedico actúa como la estructura base o padre de toda la jerarquía de atención. Define los atributos esenciales de tiempo (fecha y hora) y vincula cada servicio a un objeto Paciente. 
Además de estandarizar los datos, establece los métodos base para el cálculo de precios y determinación de urgencia, permitiendo que el sistema trate cualquier atención de forma polimórfica.

La clase ConsultaGeneral es una especialización destinada a la atención médica programada. Hereda la estructura de la clase base pero añade el atributo de especialidad médica. 
Sobrescribe la lógica financiera para aplicar un impuesto específico del 15% sobre el precio base, representando así las operaciones rutinarias que no constituyen una emergencia.

La clase Urgencia modela los eventos críticos del hospital. Al heredar de la clase base, incorpora un nivel de gravedad (baja, media, alta) y modifica sustancialmente el cálculo del costo final. 
Esta clase añade al precio base tanto el impuesto como un recargo fijo por emergencia, y marca administrativamente el servicio como "urgente" para su posterior clasificación.

La clase Gestor funciona como el controlador administrativo del sistema. No representa un dato clínico, sino una herramienta de organización que almacena una colección de todos los servicios generados. 
Sus métodos permiten recorrer dicha colección para segregar los servicios en listas de urgentes y no urgentes, así como calcular la sumatoria total de los ingresos, proveyendo la información necesaria para la toma de decisiones.

Instrucciones para ejecutar
Para poner en marcha el sistema desde un archivo de ejecución principal, debe comenzar importando todas las clases necesarias desde sus respectivos archivos origen. El primer paso lógico y obligatorio es la creación de los objetos de 
la clase Paciente, ya que el sistema tiene una dependencia estricta de estos datos; no es posible crear un servicio médico sin un paciente válido asociado. Debe instanciar la clase Paciente proporcionando los argumentos requeridos 
(nombre, apellido, edad, género y correo), asegurándose de que cumplan con las validaciones internas para evitar errores inmediatos.

Una vez que las instancias de paciente existen en memoria, proceda a crear los objetos de los servicios médicos, ya sea ConsultaGeneral o Urgencia. Al instanciar cualquiera de estas clases, deberá pasar como argumentos la fecha, la hora 
y la variable del objeto paciente que creó anteriormente. Dependiendo del tipo de servicio, deberá añadir también la especialidad o el nivel de gravedad. En este punto, puede verificar la información individual imprimiendo los objetos o 
permitiendo que sus constructores muestren los datos automáticamente en la consola.

Finalmente, para unificar y procesar la información, debe instanciar la clase Gestor. Con el objeto gestor inicializado, utilice su método de agregar servicio para incorporar uno a uno los objetos de consulta y urgencia creados previamente. 
Para concluir la ejecución y obtener el reporte final, invoque los métodos del gestor encargados de clasificar los servicios y calcular el total de gastos, imprimiendo el propio objeto gestor o los retornos de sus funciones para visualizar 
el resumen estadístico y financiero de todas las atenciones registradas.
---CAPTURAS DE LA EJECUCIÓN--
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/8475ebc6-1e73-49fe-a8cd-fad2b7e1de1f" />

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/b0361b7e-754f-417d-b8d3-1828340cd7b3" />





