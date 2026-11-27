import flet as ft

class ContadorApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.contador = 0
        self.valor = ft.Text("0", size=76, weight=ft.FontWeight.BOLD, color="#F8FAFC")
        self.configurar_pantalla()

    def configurar_pantalla(self):
        self.page.title = "Contador Interactivo"
        self.page.bgcolor = "#0B1120"
        self.page.padding = 30
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        encabezado = ft.Column(
            controls=[
                ft.Text("CONTADOR DIGITAL", size=13, color="#94A3B8", weight=ft.FontWeight.BOLD),
                ft.Text("Controla tu conteo", size=28, color="#F8FAFC", weight=ft.FontWeight.BOLD),
                ft.Text("Usa los botones para cambiar el valor", size=14, color="#94A3B8"),
            ],
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        pantalla_numero = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("VALOR ACTUAL", size=12, color="#93C5FD", weight=ft.FontWeight.BOLD),
                    self.valor,
                    ft.Text("Conteo en tiempo real", size=13, color="#94A3B8"),
                ],
                spacing=4,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#17233A",
            padding=30,
            border_radius=22,
            width=300,
            alignment=ft.Alignment(0, 0),
            border=ft.Border.all(1, "#263B5C"),
        )

        boton_menos = ft.Button(
            text="− 1",
            on_click=self.disminuir,
            style=ft.ButtonStyle(bgcolor="#24344F", color="#E2E8F0", padding=18,
                                 shape=ft.RoundedRectangleBorder(radius=14)),
        )
        boton_reset = ft.Button(
            text="Reiniciar",
            on_click=self.reiniciar,
            style=ft.ButtonStyle(bgcolor="#334155", color="#F8FAFC", padding=18,
                                 shape=ft.RoundedRectangleBorder(radius=14)),
        )
        boton_mas = ft.Button(
            text="+ 1",
            on_click=self.incrementar,
            style=ft.ButtonStyle(bgcolor="#2563EB", color="#FFFFFF", padding=18,
                                 shape=ft.RoundedRectangleBorder(radius=14)),
        )

        botones = ft.Row(
            controls=[boton_menos, boton_reset, boton_mas],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )

        tarjeta = ft.Container(
            content=ft.Column(
                controls=[encabezado, pantalla_numero, botones],
                spacing=24,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#111B2E",
            padding=30,
            border_radius=28,
            width=360,
            border=ft.Border.all(1, "#1F2D45"),
        )

        pie = ft.Text("Proyecto académico • Python + Flet", size=12, color="#64748B")
        self.page.add(
            ft.Column(
                controls=[tarjeta, pie],
                spacing=18,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    def incrementar(self, e):
        self.contador += 1
        self.actualizar()

    def disminuir(self, e):
        self.contador -= 1
        self.actualizar()

    def reiniciar(self, e):
        self.contador = 0
        self.actualizar()

    def actualizar(self):
        self.valor.value = str(self.contador)
        self.page.update()


def main(page: ft.Page):
    ContadorApp(page)

ft.run(main)
