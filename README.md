# Contador interactivo con Flet

Proyecto académico de programación orientada a objetos con Python y Flet. El contador empieza en cero cada vez que se abre la aplicación.

- **Sumar** aumenta el valor en uno.
- **Restar** disminuye el valor en uno hasta llegar a cero.
- **Reiniciar** devuelve el contador a cero desde cualquier valor.
- Cuando el contador está a cero, los botones **Restar** y **Reiniciar** se desactivan.

## Instalación y ejecución

Necesitas Python 3.10 o posterior. Desde la raíz del repositorio, instala las dependencias y abre la aplicación en el navegador.

```bash
python -m pip install -r requirements.txt
python main.py
```

## Cómo funciona

La clase `ContadorApp` mantiene el valor de la sesión y enlaza los botones a sus eventos. Después de cada operación, `actualizar()` cambia el valor visible y el estado de los botones. La interfaz se ajusta al ancho de la ventana y anuncia los cambios de valor a los lectores de pantalla.

## Evidencia de ejecución

| Captura | Estado |
| --- | --- |
| [01 · Inicio](evidencia/01-inicio.png) | Valor 0. Restar y Reiniciar están desactivados. |
| [02 · Después de sumar](evidencia/02-despues-de-sumar.png) | Valor 5 tras cinco pulsaciones de Sumar. |
| [03 · Después de restar](evidencia/03-despues-de-restar.png) | Valor 2 tras sumar tres veces y restar una vez en una ventana de 390 px de ancho. |

## Documentación oficial

- [Flet](https://flet.dev/)
- [Documentación de Flet](https://docs.flet.dev/)
