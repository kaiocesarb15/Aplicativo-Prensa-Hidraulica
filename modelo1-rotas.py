import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors


def main(page: Page):
    page.title = "App Prensa Hidráulica"

    def route_change(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Pagina Inicial"), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton("Problemas", on_click=lambda _: page.go("/problemas")),
                ],
            )
        )
        if page.route == "/problemas":
            page.views.append(
                View(
                    "/problemas",
                    [
                        AppBar(title=Text("Problemas"), bgcolor=colors.SURFACE_VARIANT),
                        #ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


flet.app(main)