# Antipatrones-entrega


## Identificación de características de "Spaghetti Code": Debes ser capaz de identificar las características de "Spaghetti Code" en el código proporcionado. (20%):

Control de flujo complejo y poco estructurado:
El código utiliza múltiples instrucciones if sin un bloque elif adecuado. Esto hace que todas las condiciones se evalúen, incluso si una de ellas es verdadera. Este enfoque puede llevar a un control de flujo confuso y difícil de seguir.

Falta de modularización: 
La lógica de cada operación está contenida en la función principal calcular. Este enfoque monolítico dificulta la comprensión del código y su mantenimiento a medida que crece.

Uso de cadenas de texto para control de flujo: 
El uso de cadenas de texto ('suma', 'resta', etc.) para determinar las operaciones introduce un nivel adicional de complejidad y potenciales errores. La comparación de cadenas de texto no es tan eficiente ni segura como el uso de estructuras de control más apropiadas.

Manejo de errores ineficaz: 
La función division imprime un mensaje directamente y devuelve None en caso de error. Este enfoque no es ideal para manejar errores, ya que mezcla la lógica de la aplicación con la presentación de mensajes, dificultando el manejo eficiente de errores en otros lugares del código.

Falta de comentarios y documentación: 
El código carece de comentarios y documentación, lo que dificulta la comprensión de su lógica y funcionamiento, especialmente para otros programadores que puedan leer o mantener el código.

No se verifica la validez de las operaciones: 
Aunque se imprime un mensaje para operaciones no soportadas, el código no verifica de manera explícita la validez de la operación antes de realizarla, lo que podría conducir a errores inesperados.

En resumen, el código presenta características de "Spaghetti Code" debido a su estructura de control compleja y poco estructurada, falta de modularización, uso de cadenas de texto para el control de flujo, manejo ineficaz de errores y falta de comentarios y documentación. Refactorizar el código siguiendo principios de diseño y buenas prácticas ayudará a mejorar su calidad y mantenibilidad.
