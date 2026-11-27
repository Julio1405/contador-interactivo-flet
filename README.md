# Contador interactivo con Flet

[Abre el contador en el navegador](https://contador-interactivo-flet-julio1405.jokeylatte6.chatgpt.site/)

Proyecto académico de programación orientada a objetos con Python y Flet. El contador empieza en cero cada vez que se abre la aplicación.

- **Sumar** aumenta el valor en uno.
- **Restar** disminuye el valor en uno y admite valores negativos.
- **Reiniciar** devuelve el contador a cero desde cualquier valor.
- Cuando el contador está a cero, el botón **Reiniciar** se desactiva.

## Investigación sobre Flet

### Qué es y para qué sirve

Flet es un framework de código abierto para crear interfaces gráficas con Python. Utiliza Flutter para dibujar los controles. Con una misma base de código se pueden crear aplicaciones web, de escritorio (Windows, macOS y Linux) y móviles (Android e iOS). Por ejemplo, sirve para construir formularios, paneles de datos y herramientas interactivas como este contador. [Documentación de Flet](https://flet.dev/docs/)

### Componentes gráficos

| Control | Función |
| --- | --- |
| `Page` | Representa la pantalla principal y contiene los controles de la sesión. |
| `Text`, `Icon`, `Image` | Muestran texto, un icono o una imagen, respectivamente. |
| `FilledButton`, `OutlinedButton`, `TextButton` | Ofrecen distintas apariencias para botones interactivos. |
| `TextField` | Permite introducir texto. |
| `Row`, `Column`, `Container` | Distribuyen controles en fila o columna, o agrupan contenido con márgenes internos, fondo y borde. |

### Cómo maneja los eventos

Se asigna una función o un método a la propiedad del evento. Por ejemplo, un botón recibe `on_click` y un campo de texto puede usar `on_change`. Flet llama al manejador con un objeto de evento. Para procesar pulsaciones a nivel de página se puede usar `page.on_keyboard_event`, cuyo evento informa qué tecla se pulsó y si se usaron modificadores. En este contador se implementa `on_click` y también se puede activar un botón enfocado con el teclado. [Catálogo de controles](https://flet.dev/docs/controls/) · [Referencia de Page](https://flet.dev/docs/controls/page/)

### Ventajas y limitaciones frente a Tkinter

| Aspecto | Flet | Tkinter |
| --- | --- | --- |
| Plataformas | Permite reutilizar código en web, escritorio y móvil. | Está orientado a interfaces de escritorio mediante Tcl/Tk. |
| Controles y diseño | Incluye controles de estilo Material y permite componer pantallas con filas y columnas. | Ofrece widgets clásicos y temáticos de `ttk`, con gestores de geometría como `pack` y `grid`. |
| Instalación y distribución | Requiere instalar dependencias con pip. La publicación depende de la plataforma y puede requerir compilación o empaquetado adicional. | Suele venir con Python. Algunas distribuciones requieren instalar el soporte de Tcl/Tk por separado. |

Para este proyecto, la ventaja de Flet es poder publicar el mismo contador en la web. Para una herramienta sencilla que solo se ejecuta en el escritorio, Tkinter puede requerir menos dependencias. [Publicación de Flet para web](https://flet.dev/docs/publish/web/static-website/) · [Documentación oficial de Tkinter](https://docs.python.org/es/3/library/tkinter.html)

## Instalación y ejecución

Necesitas Python 3.10 o posterior, pip y un navegador. `requirements.txt` fija Flet y su cliente web en la versión 1.1.4. Desde la raíz del repositorio, instala las dependencias y abre la aplicación en el navegador.

```bash
python -m pip install -r requirements.txt
python main.py
```

## Cómo funciona

1. **Pantalla principal.** En [`main.py`](main.py), `ft.run(main, view=ft.AppView.WEB_BROWSER)` inicia Flet en el navegador. Flet entrega una instancia de `Page` a `main(page)`, que crea el objeto `ContadorApp`.
2. **Componentes visuales.** `configurar_pantalla()` ajusta el tema y crea los controles. `Text` muestra el valor inicial, `Row` agrupa los botones **Restar** y **Sumar**, y `Column` organiza la tarjeta. `page.add(...)` incorpora la tarjeta a la pantalla.
3. **Evento y respuesta.** El botón **Sumar** se crea con `on_click=self.incrementar`. Al activarlo, Flet ejecuta `incrementar()`, que agrega uno a `self.contador` y llama a `actualizar()`. **Restar** y **Reiniciar** llaman a `disminuir()` y `reiniciar()`, respectivamente.
4. **Actualización visible.** `actualizar()` convierte el número a texto, lo asigna a `self.texto_contador.value` y ajusta el estado de **Reiniciar**. Luego `page.update()` refleja los cambios en pantalla.

### Reto adicional · Programación orientada a objetos

Flet permite construir interfaces con objetos como `Page`, `Text` y `FilledButton`. La única clase propia, `ContadorApp`, conserva el valor y las referencias a los controles por sesión, construye la pantalla y responde a los eventos mediante sus métodos. La función `main(page)` es el punto de entrada y crea una instancia de esa clase para cada página.

## Evidencia de ejecución

| Captura | Estado |
| --- | --- |
| [01 · Inicio](evidencia/01-inicio.png) | Valor 0. Reiniciar está desactivado. |
| [02 · Después de sumar](evidencia/02-despues-de-sumar.png) | Valor 5 tras cinco pulsaciones de Sumar. |
| [03 · Después de restar](evidencia/03-despues-de-restar.png) | Valor −1 tras restar desde cero en una ventana de 390 px de ancho. |

## Fuentes consultadas

- [Flet · Introducción y plataformas](https://flet.dev/docs/)
- [Flet · Instalación](https://flet.dev/docs/getting-started/installation/)
- [Flet · Catálogo de controles](https://flet.dev/docs/controls/)
- [Flet · Referencia de Page y eventos de teclado](https://flet.dev/docs/controls/page/)
- [Flet · Publicación como sitio web estático](https://flet.dev/docs/publish/web/static-website/)
- [PyPI · Flet 1.1.4 y requisitos de Python](https://pypi.org/project/flet/1.1.4/)
- [Python · Documentación oficial de Tkinter](https://docs.python.org/es/3/library/tkinter.html)
