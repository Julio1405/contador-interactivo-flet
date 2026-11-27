import flet as ft


class ContadorApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.contador = 0
        self.texto_contador = ft.Text(
            "0",
            size=96,
            weight=ft.FontWeight.BOLD,
            color="#F8FAFC",
            text_align=ft.TextAlign.CENTER,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
        )
        self.boton_reiniciar = ft.TextButton(
            "Reiniciar",
            icon=ft.Icons.RESTART_ALT,
            on_click=self.reiniciar,
            disabled=True,
        )
        self.configurar_pantalla()

    def configurar_pantalla(self):
        self.page.title = "Contador interactivo"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.theme = ft.Theme(color_scheme_seed="#93C5FD")
        self.page.bgcolor = "#0B1120"
        self.page.padding = 20
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        marcador = ft.Container(
            width=300,
            bgcolor="#17233A",
            border=ft.Border.all(1, "#263B5C"),
            border_radius=20,
            padding=ft.Padding.symmetric(vertical=14, horizontal=12),
            content=ft.Column(
                [
                    ft.Text("Valor actual", size=14, color="#BFDBFE"),
                    ft.Semantics(content=self.texto_contador, live_region=True),
                ],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        boton_restar = ft.OutlinedButton(
            "Restar",
            icon=ft.Icons.REMOVE,
            on_click=self.disminuir,
            height=48,
            width=130,
        )
        boton_sumar = ft.FilledButton(
            "Sumar",
            icon=ft.Icons.ADD,
            on_click=self.incrementar,
            bgcolor="#93C5FD",
            color="#102744",
            height=48,
            width=130,
        )
        self.page.add(
            ft.Container(
                width=488,
                padding=24,
                bgcolor="#111B2E",
                border=ft.Border.all(1, "#263B5C"),
                border_radius=28,
                content=ft.Column(
                    [
                        ft.Container(
                            content=ft.Icon(ft.Icons.EXPOSURE, color="#DBEAFE", size=27),
                            bgcolor="#253A5D",
                            border_radius=16,
                            padding=12,
                        ),
                        ft.Text(
                            "Contador interactivo",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                            color="#F8FAFC",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            "Suma o resta de uno en uno.",
                            color="#BFDBFE",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        marcador,
                        ft.Row(
                            [boton_restar, boton_sumar],
                            alignment=ft.MainAxisAlignment.CENTER,
                            wrap=True,
                            spacing=12,
                            run_spacing=12,
                        ),
                        self.boton_reiniciar,
                    ],
                    spacing=16,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        )

    def incrementar(self, _):
        self.contador += 1
        self.actualizar()

    def disminuir(self, _):
        self.contador -= 1
        self.actualizar()

    def reiniciar(self, _):
        self.contador = 0
        self.actualizar()

    def actualizar(self):
        self.texto_contador.value = str(self.contador)
        self.boton_reiniciar.disabled = self.contador == 0
        self.page.update()


def main(page: ft.Page):
    ContadorApp(page)


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
