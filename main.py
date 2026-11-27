import flet as ft

class ContadorApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.contador = 0
        self.texto_contador = ft.Text(value=str(self.contador), size=32, weight=ft.FontWeight.BOLD)
        self.configurar_pantalla()

    def configurar_pantalla(self):
        self.page.title = "Contador Interactivo"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        boton_sumar = ft.Button("Incrementar", on_click=self.incrementar)
        boton_reiniciar = ft.Button("Reiniciar", on_click=self.reiniciar)

        self.page.add(
            ft.Column(
                controls=[
                    ft.Text("Contador interactivo con Flet", size=24),
                    self.texto_contador,
                    ft.Row([boton_sumar, boton_reiniciar], alignment=ft.MainAxisAlignment.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    def incrementar(self, e):
        self.contador += 1
        self.actualizar()

    def reiniciar(self, e):
        self.contador = 0
        self.actualizar()

    def actualizar(self):
        self.texto_contador.value = str(self.contador)
        self.page.update()


def main(page: ft.Page):
    ContadorApp(page)


ft.run(main)
