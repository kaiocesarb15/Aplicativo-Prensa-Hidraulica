from flet import *


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
                    ElevatedButton("Sei lá", on_click=lambda _: page.go("/seila"))
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

                        # Prensa.py in here
                    ],
                )
            )
        if page.route == "/seila":
            page.views.append(
                View(
                    "/seila",
                    [
                        AppBar(title=Text("Sei lá"), bgcolor=colors.SURFACE_VARIANT),
                        #ElevatedButton("Go Home", on_click=lambda _: page.go("/")),

                        # Prensa.py in here
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

app(main)