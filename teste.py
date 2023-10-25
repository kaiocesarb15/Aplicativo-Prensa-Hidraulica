import flet as ft
from flet import colors

def main(page: ft.Page):
    page.window_width = 1400
    page.window_height = 500
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
        label="Variável que deseja calcular",
        options=[
            ft.dropdown.Option("Área do embolo 1"),
            ft.dropdown.Option("Área do embolo 2"),
            ft.dropdown.Option("Força no embolo 1"),
            ft.dropdown.Option("Força no embolo 2")],
    )

    a1 = ft.TextField(label="Área do embolo 1", width=330)
    a2 = ft.TextField(label="Área do embolo 2", width=330)
    f1 = ft.TextField(label="Força no embolo 1", width=330)
    f2 = ft.TextField(label="Força no embolo 2", width=326)
    display = ft.Column()

    a1.disabled = True
    a2.disabled = True
    f1.disabled = True
    f2.disabled = True


    def addVariavel(e):
        a1.disabled = False
        a2.disabled = False
        f1.disabled = False
        f2.disabled = False

        variavel = variavel_dropdown.value
        if variavel == a1.label:
            # Impossibilita o usuário de digitar um valor para `a1`
            a1.disabled = True
            a1.value = "a1"
            #nome_variavel = "área do embolo 1"
            #nome_multilpicacao1 = "área do embolo 2"
            #nome_multilpicacao2 = "força no embolo 1"
            #nome_divisao = "força no embolo 2"

        elif variavel == a2.label:
            # Impossibilita o usuário de digitar um valor para `a2`
            a2.disabled = True
            a2.value = "a2"
            #nome_variavel = "área do embolo 2"
            #nome_multilpicacao1 = "área do embolo 1"
            #nome_multilpicacao2 = "força no embolo 2"
            #nome_divisao = "força do embolo 1"

        elif variavel == f1.label:
            # Impossibilita o usuário de digitar um valor para `f1`
            f1.disabled = True
            f1.value = "F1"
            #nome_variavel = "força no embolo 1"
            #nome_multilpicacao1 = "área do embolo 1"
            #nome_multilpicacao2 = "força no embolo 2"
            #nome_divisao = "área do embolo 2"
        elif variavel == f2.label:
            # Impossibilita o usuário de digitar um valor para `f2`
            f2.disabled = True
            f2.value = "F2"
            #nome_variavel = "força no embolo 2"
            #nome_multilpicacao1 = "área do embolo 2"
            #nome_multilpicacao2 = "força no embolo 1"
            #nome_divisao = "área do embolo 1"
        page.update()


    def calcular(e):
        display.controls.clear()
        dados = f"* Dados da questão: Área do embolo 1: {a1.value}(cm²), Área do embolo 2: {a2.value}(cm²), Força do embolo 1: {f1.value}(N), Força do embolo 2: {f2.value}(N).\n\n* Método de resolução: Formula do teorema de pascal: F1/a1 = F2/a2."
        #calculo = f"Para descobri a {nome_variavel}, basta multiplicar a {nome_multilpicacao1} pela {nome_multilpicacao2} e dividir pela {nome_divisao}"
        #display.controls.append(ft.Text(f"Dados: Área do embolo 1: {a1.value}(cm²), Área do embolo 2: {a2.value}(cm²), Força do embolo 1: {f1.value}(N),Força do embolo 2: {f2.value}(N)\nFormula do teorema de pascal: F1/a1 = F2/a2.\n"))

        if a1.value == "a1":
            calculo = f"* Resolução: Para descobrir a área do embolo 1, basta multiplicar a área do embolo 2 pela força do embolo 1 e dividir pela força do embolo 2. "
            resposta = (float(a2.value) * float(f1.value)) / float(f2.value)
            texto = f"{dados}\n\n{calculo}\n    F1/a1 = F2/a2\n    a1*F2 = F1*a2\n    a1 = (F1*a2)/F2\n    a1 = ({f1.value}*{a2.value})/{f2.value}\n    a1 = {resposta}cm²"
            display.controls.append(ft.Text(texto))

        elif a2.value == "a2":
            calculo = f"* Resolução: Para descobrir a área do embolo 2, basta multiplicar a área do embolo 1 pela força do embolo 2 e dividir pela força do embolo 1. "
            resposta = (float(a1.value) * float(f2.value)) / float(f1.value)
            texto = f"{dados}\n\n{calculo}\n    F1/a1 = F2/a2\n    a2*F1 = F2*a1\n    a2 = (F2*a1)/F1\n    a2 = ({f2.value}*{a1.value})/{f1.value}\n    a2 = {resposta}cm²"
            display.controls.append(ft.Text(texto))

        elif f1.value == "F1":
            calculo = f"* Resolução: Para descobrir a força no embolo 1, basta multiplicar a área do embolo 1 pela força do embolo 2 e dividir pela área do embolo 2. "
            resposta = (float(a1.value) * float(f2.value)) / float(a2.value)
            texto = f"{dados}\n\n{calculo}\n    F1/a1 = F2/a2\n    F1*a2 = F2*a1\n    F1 = (F2*a1)/a2\n    F1 = ({f2.value}*{a1.value})/{a2.value}\n    F1 = {resposta}N"
            display.controls.append(ft.Text(texto))

        else:
            calculo = f"* Resolução: Para descobrir a força no embolo 2, basta multiplicar a área do embolo 2 pela força do embolo 1 e dividir pela área do embolo 1. "
            resposta = (float(a2.value) * float(f1.value)) / float(a1.value)
            texto = f"{dados}\n\n{calculo}\n    F1/a1 = F2/a2\n    F2*a1 = F1*a2\n    F2 = (F1*a2)/a1\n    F2 = ({f1.value}*{a2.value})/{a1.value}\n    F2 = {resposta}N"
            display.controls.append(ft.Text(texto))
        
        #ft.Container(display, width=100, height=100, background_color=colors.blue)
        page.update()

    addVariavel_bt = ft.ElevatedButton("Adicionar Variável", on_click=addVariavel)
    addValores_bt = ft.ElevatedButton("Calcular", on_click=calcular)


    page.add(
        ft.Row([theme], alignment=ft.MainAxisAlignment.END),
        variavel_dropdown,
        addVariavel_bt,
        ft.Row([a1, a2, f1, f2], width=1400),
        addValores_bt,
        ft.Container(display, bgcolor=colors.BLUE_50, border=ft.border.all(1, colors.BLUE_100), border_radius=ft.border_radius.all(5))
    )

ft.app(target=main)
