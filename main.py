import flet as ft


class ContadorApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.contador = 0
        self.texto_contador = ft.Text(
            "0",
            size=96,
            weight=ft.FontWeight.BOLD,
            color="#F7F3FF",
            text_align=ft.TextAlign.CENTER,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
        )
        self.boton_restar = ft.OutlinedButton(
            "Restar",
            icon=ft.Icons.REMOVE,
            on_click=self.decrementar,
            disabled=True,
            height=48,
            width=130,
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
        self.page.theme = ft.Theme(color_scheme_seed="#BA9AFF")
        self.page.bgcolor = "#110E1B"
        self.page.padding = 20
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        marcador = ft.Container(
            width=300,
            bgcolor="#151021",
            border=ft.Border.all(1, "#392A52"),
            border_radius=20,
            padding=ft.Padding.symmetric(vertical=14, horizontal=12),
            content=ft.Column(
                [
                    ft.Text("Valor actual", size=14, color="#D5C7F2"),
                    ft.Semantics(content=self.texto_contador, live_region=True),
                ],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        boton_sumar = ft.FilledButton(
            "Sumar",
            icon=ft.Icons.ADD,
            on_click=self.incrementar,
            bgcolor="#C7ABFF",
            color="#241340",
            height=48,
            width=130,
        )
        self.page.add(
            ft.Container(
                width=488,
                padding=24,
                bgcolor="#20182E",
                border=ft.Border.all(1, "#3D3054"),
                border_radius=28,
                content=ft.Column(
                    [
                        ft.Container(
                            content=ft.Icon(ft.Icons.EXPOSURE, color="#E2D1FF", size=27),
                            bgcolor="#382653",
                            border_radius=16,
                            padding=12,
                        ),
                        ft.Text(
                            "Contador interactivo",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                            color="#F7F3FF",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            "Suma o resta de uno en uno.",
                            color="#D5C7F2",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        marcador,
                        ft.Row(
                            [self.boton_restar, boton_sumar],
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

    def decrementar(self, _):
        self.contador = max(0, self.contador - 1)
        self.actualizar()

    def reiniciar(self, _):
        self.contador = 0
        self.actualizar()

    def actualizar(self):
        self.texto_contador.value = str(self.contador)
        en_cero = self.contador == 0
        self.boton_restar.disabled = en_cero
        self.boton_reiniciar.disabled = en_cero
        self.page.update()


def main(page: ft.Page):
    ContadorApp(page)


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
