import flet as ft
from flet import colors

def main(page: ft.Page):
    #page.window_width = 1000
    #page.window_height = 800
    page.title = 'Prensa hidráulica'
    page.window_always_on_top = True

    #dark mode
    def theme_changed(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT
    theme = ft.Switch(label="Light mode", on_change=theme_changed)

    variavel_dropdown = ft.Dropdown(
        label="Variável",
        hint_text="O que irá variar?",
        options=[
            ft.dropdown.Option("Área do embolo 1"),
            ft.dropdown.Option("Área do embolo 2"),
            ft.dropdown.Option("Força do embolo 1"),
            ft.dropdown.Option("Força do embolo 2")],
    )

    a1 = ft.TextField(label="Área do embolo 1")
    a2 = ft.TextField(label="Área do embolo 2")
    f1 = ft.TextField(label="Força do embolo 1")
    f2 = ft.TextField(label="Força do embolo 2")
    display = ft.Column()

    def addVariavel(e):
        a1.disabled = False
        a2.disabled = False
        f1.disabled = False
        f2.disabled = False

        variavel = variavel_dropdown.value
        if variavel == a1.label:
            # Impossibilita o usuário de digitar um valor para `a1`
            a1.disabled = True
            a1.value = "?"
        elif variavel == a2.label:
            # Impossibilita o usuário de digitar um valor para `a2`
            a2.disabled = True
            a2.value = "?"
        elif variavel == f1.label:
            # Impossibilita o usuário de digitar um valor para `f1`
            f1.disabled = True
            f1.value = "?"
        elif variavel == f2.label:
            # Impossibilita o usuário de digitar um valor para `f2`
            f2.disabled = True
            f2.value = "?"
        page.update()

    def addValores(e):
        display.controls.clear()
        display.controls.append(ft.Text(f"Área do embolo 1: {a1.value}cm²\nÁrea do embolo 2: {a2.value}cm²\nForça do embolo 1: {f1.value}N\nForça do embolo 2: {f2.value}N"))
        page.update()

    addVariavel_bt = ft.ElevatedButton("Adicionar Variável", on_click=addVariavel)
    addValores_bt = ft.ElevatedButton("Adicionar Valores", on_click=addValores)

    page.add(
        theme,
        variavel_dropdown,
        addVariavel_bt,
        ft.Row([a1, a2, f1, f2]),
        addValores_bt,
        display
    )

ft.app(target=main)
