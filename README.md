# Contador interactivo con Flet

Proyecto académico: contador interactivo desarrollado en Python con **Flet** y programación orientada a objetos.

## Funciones
- Mostrar el valor actual.
- **Incrementar** el contador.
- **Reiniciar** el contador a cero.
- Actualizar la interfaz al hacer clic.

## Requisitos
Python y Flet instalados. Consulta los requisitos de versión actual en la documentación oficial.

## Instalación
```bash
pip install flet
```

## Ejecutar
```bash
python main.py
```

## Explicación
La clase `ContadorApp` mantiene el estado (`self.contador`) y configura los controles. Los botones enlazan sus eventos `on_click` a los métodos `incrementar` y `reiniciar`. Estos modifican el valor y llaman al método `actualizar`, que cambia el texto visible y refresca la página con `page.update()`.

## Evidencia
Incluye una captura real de la aplicación ejecutándose para completar la evidencia solicitada. Esta captura aún debe agregarse por el estudiante.

## Documentación oficial
- https://flet.dev/
- https://docs.flet.dev/
