import flet as ft
from flet import colors

def main(page: ft.Page):
    page.window_width = 500
    page.window_height = 800
    page.title = 'Prensa hidráulica'
    page.window_always_on_top = True

    textcolor = colors.BLACK

    #dark mode
    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        theme.label = (
            "Light mode" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark mode"
        )
        textcolor = colors.BLACK if page.theme_mode == ft.ThemeMode.LIGHT else colors.WHITE
        result.color=textcolor
        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT
    theme = ft.Switch(label="Light mode", on_change=theme_changed)

    #valor inicial das forças
    global f1 
    global f2
    f1 = 200
    f2 = 2000
    
    #atualiza a página e o valor da intensidade das forças e as dimensões do objeto
    def atualizar(emb1, emb2, f1, f2):
        result.value=f"""Área (1): {emb1.width/5}cm²      F1: {f1}N
        \nÁrea (2): {emb2.width/2}cm²      F2: {f2}N"""
        result.update()
        page.update()

    #altera a área 1 (a da direita)
    def slider_p_a1(e):
        emb1.width = int(e.control.value) * 5
        F1 = f1
        F2 = f2 
        if choose_variable.value == "Área 2":
            emb2.width = (F2 * (emb1.width/5) / F1) * 2
            cano.left=emb2.width-75
            emb1.left = emb2.width + 70
        elif choose_variable.value == "Força 1":
            F1 = F2 * (emb1.width/5) / (emb2.width/2)
        elif choose_variable.value == "Força 2":
            F2 = F1 * (emb2.width/2) / (emb1.width/5)
        atualizar(emb1, emb2, F1, F2)

    #altera a área 2 (a da esquerda)
    def slider_p_a2(e):
        emb2.width = int(e.control.value) * 2
        cano.left = emb2.width-75
        emb1.left = emb2.width + 60
        F1 = f1
        F2 = f2 
        if choose_variable.value == "Área 1":
            emb1.width = (F1 * (emb2.width/2) / F2) * 5
        elif choose_variable.value == "Força 1":
            F1 = F2 * (emb1.width/5) / (emb2.width/2)
        elif choose_variable.value == "Força 2":
            F2 = F1 * (emb2.width/2) / (emb1.width/5)

        atualizar(emb1, emb2, F1, F2)

    #função que mexe com a força 1 (atua na direita)
    def slider_p_f1(e):
        f1 = int(e.control.value)
        F1 = f1
        F2 = f2 
        if choose_variable.value == "Área 1":
            emb1.width = (F1 * (emb2.width/2) / F2) * 5
        elif choose_variable.value == "Área 2":
            emb2.width = (F2 * (emb1.width/5) / F1) * 2
            cano.left=emb2.width-75
            emb1.left = emb2.width + 70
        elif choose_variable.value == "Força 2":
            F2 = F1 * (emb2.width/2) / (emb1.width/5)
        
        atualizar(emb1, emb2, F1, F2)

    #função que mexe com a força 2 (atua na esquerda)
    def slider_p_f2(e):
        f2 = int(e.control.value)
        F1 = f1
        F2 = f2
        if choose_variable.value == "Área 1":
            emb1.width = (F1 * (emb2.width/2) / F2) * 5
        elif choose_variable.value == "Área 2":
            emb2.width = (F2 * (emb1.width/5) / F1) * 2
            cano.left = emb2.width-75
            emb1.left = emb2.width + 70
        elif choose_variable.value == "Força 1":
            F1 = F2 * (emb1.width/5) / (emb2.width/2)
        
        atualizar(emb1, emb2, F1, f2)

    #cria a coluna da esquerda
    emb2 = ft.Container(
        content=ft.Text(value="(2)", color=colors.WHITE),
        width=200,                      #largura da coluna (é o que varia)
        height=150,                     #altura da coluna
        bgcolor="blue",                 #cor do objeto
        alignment=ft.alignment.center,
        animate_position=1000           #não sei
    )

    #cria a coluna da direita
    emb1 = ft.Container(
        content=ft.Text(value="(1)", color=colors.WHITE),
        width=50, 
        height=150, 
        bgcolor="blue", 
        left=275, 
        alignment=ft.alignment.center,
        animate_position=1000
    )

    #cria o cano horizontal por onde a água passa
    cano = ft.Container(
        width=150, 
        height=50, 
        bgcolor="blue", 
        top=100,                       #altura em que o objeto surge em relação ao topo da tela
        left=emb2.width-75,
        alignment=ft.alignment.center,
        animate_position=1000
    )

    #diz a intensidade das forças e as dimensões do objeto
    result = ft.Text(value=f"""Área (1): {emb1.width/5}cm²{" "*10}F1: {f1}N
        \nÁrea (2): {emb2.width/2}cm²{" "*9}F2: {f2}N""", color=ft.colors.BLACK, size=15)

    #informações dos sliders
    sliders = [
        {"nome": "Área do êmbolo 1", "min": 4,"max": 15, "div": 100, "value": 10, "on_change": slider_p_a1},
        {"nome": "Área do êmbolo 2", "min": 40,"max": 150, "div": 110, "value": 100, "on_change": slider_p_a2},
        {"nome": "Intensidade da força 1", "min": 100,"max": 300, "div": 200, "value": 200, "on_change": slider_p_f1},
        {"nome": "Intensidade da força 2", "min": 1000,"max": 3000, "div": 500, "value": 2000, "on_change": slider_p_f2}
    ]

    #criando os sliders
    slider = [ft.Slider(
        min=slider["min"],                  #valor mínimo
        max=slider["max"],                  #valor máximo    
        divisions=slider["div"],            #divisões
        value=slider["value"],              #valor inicial
        label="{value}",                    #valor que aparece na bolinha
        on_change=slider["on_change"],
    ) for slider in sliders]

    #variável que exibe os slides com suas descrições
    keyboard = ft.Row(
        width=500,
        wrap=True,
        controls=[
            ft.Text(value=sliders[0]['nome'], color=colors.BLACK, size=15), slider[0], 
            ft.Text(value=sliders[1]['nome'], color=colors.BLACK, size=15), slider[1], 
            ft.Text(value=sliders[2]['nome'], color=colors.BLACK, size=15), slider[2], 
            ft.Text(value=sliders[3]['nome'], color=colors.BLACK, size=15), slider[3]
        ]
    )

    #variável que guarda os valores das forças e as dimensões do objeto
    display = ft.Row(
        width = 250,
        controls=[result]
    )

    #função que reinicia os valores do experimento
    def reiniciar(e):
        emb2.width = 200
        cano.left=emb2.width-75
        emb1.width = 50
        emb1.left=275
        f1 = 200
        f2 = 2000
        atualizar(emb1, emb2, f1, f2)

    reiniciar_bottom = ft.ElevatedButton("Reiniciar experimento", on_click=reiniciar)
    
    choose_variable = ft.Dropdown(
            label="Variável",
            hint_text="O que irá variar?",
            options=[
                ft.dropdown.Option("Área 1"),
                ft.dropdown.Option("Área 2"),
                ft.dropdown.Option("Força 1"),
                ft.dropdown.Option("Força 2"),
            ],
            autofocus=True,
        )

    page.add(
        ft.Stack([emb2, cano, emb1], height=170),
        ft.Row(width=500, controls=[reiniciar_bottom, theme, choose_variable]),
        display,
        keyboard,
    )

ft.app(target=main)