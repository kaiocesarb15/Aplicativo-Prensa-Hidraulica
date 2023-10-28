import flet as ft
from flet import colors

def main(page: ft.Page):
    page.window_width = 1400
    page.window_height = 500
    page.title = 'Aplicação Prensa hidráulica'
    page.window_always_on_top = True

    # Função que muda o tema do programa
    def theme_changed(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK

        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT
    theme = ft.Switch(label="Light mode", on_change=theme_changed)

    # Seleção da variável que o usuário deseja calcular
    variavel_dropdown = ft.Dropdown(
        label="Variável que deseja calcular",
        options=[
            ft.dropdown.Option("Área do êmbolo 1"),
            ft.dropdown.Option("Área do êmbolo 2"),
            ft.dropdown.Option("Força no êmbolo 1"),
            ft.dropdown.Option("Força no êmbolo 2")],
    )

    a1 = ft.TextField(label="Área do êmbolo 1", width=290)
    a2 = ft.TextField(label="Área do êmbolo 2", width=290)
    f1 = ft.TextField(label="Força no êmbolo 1", width=290)
    f2 = ft.TextField(label="Força no êmbolo 2", width=290)
    display = ft.Column()

    a1.disabled = True
    a2.disabled = True
    f1.disabled = True
    f2.disabled = True

    # Função que adiciona a variável que o usuário deseja calcular
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

        elif variavel == a2.label:
            # Impossibilita o usuário de digitar um valor para `a2`
            a2.disabled = True
            a2.value = "a2"

        elif variavel == f1.label:
            # Impossibilita o usuário de digitar um valor para `f1`
            f1.disabled = True
            f1.value = "F1"

        elif variavel == f2.label:
            # Impossibilita o usuário de digitar um valor para `f2`
            f2.disabled = True
            f2.value = "F2"

        page.update()

    # Função que calcula a variável que o usuário deseja calcular e exibe a resolução
    # Tentei fazer de tudo para deixar o código menos repetitivo, mas esse foi o único jeito que funcionou
    def calcular(e):
        display.controls.clear()
        dados = f"* Dados da questão: Área do êmbolo 1: {a1.value}(cm²), Área do êmbolo 2: {a2.value}(cm²), Força do êmbolo 1: {f1.value}(N), Força do êmbolo 2: {f2.value}(N).\n\n* Método de resolução: Formula do teorema de pascal: F1/a1 = F2/a2."

        if a1.value == "a1":
            calculo = f"* Resolução: Para descobrir a área do êmbolo 1, basta multiplicar a área do êmbolo 2 pela força do êmbolo 1 e dividir pela força do êmbolo 2. "
            resposta = (float(a2.value) * float(f1.value)) / float(f2.value)
            texto = f"{dados}\n\n{calculo}\n    F1/a1 = F2/a2\n    a1*F2 = F1*a2\n    a1 = (F1*a2)/F2\n    a1 = ({f1.value}*{a2.value})/{f2.value}\n    a1 = {resposta}cm²"

        elif a2.value == "a2":
            calculo = f"* Resolução: Para descobrir a área do êmbolo 2, basta multiplicar a área do êmbolo 1 pela força do êmbolo 2 e dividir pela força do êmbolo 1. "
            resposta = (float(a1.value) * float(f2.value)) / float(f1.value)
            texto = f"{dados}\n\n{calculo}\n    F1/a1 = F2/a2\n    a2*F1 = F2*a1\n    a2 = (F2*a1)/F1\n    a2 = ({f2.value}*{a1.value})/{f1.value}\n    a2 = {resposta}cm²"

        elif f1.value == "F1":
            calculo = f"* Resolução: Para descobrir a força no êmbolo 1, basta multiplicar a área do êmbolo 1 pela força do êmbolo 2 e dividir pela área do êmbolo 2. "
            resposta = (float(a1.value) * float(f2.value)) / float(a2.value)
            texto = f"{dados}\n\n{calculo}\n    F1/a1 = F2/a2\n    F1*a2 = F2*a1\n    F1 = (F2*a1)/a2\n    F1 = ({f2.value}*{a1.value})/{a2.value}\n    F1 = {resposta}N"

        else:
            calculo = f"* Resolução: Para descobrir a força no êmbolo 2, basta multiplicar a área do êmbolo 2 pela força do êmbolo 1 e dividir pela área do êmbolo 1. "
            resposta = (float(a2.value) * float(f1.value)) / float(a1.value)
            texto = f"{dados}\n\n{calculo}\n    F1/a1 = F2/a2\n    F2*a1 = F1*a2\n    F2 = (F1*a2)/a1\n    F2 = ({f1.value}*{a2.value})/{a1.value}\n    F2 = {resposta}N"
        
        display.controls.append(ft.Text(texto, color=colors.BLACK))
        page.update()

    # Botões que chamam as funções
    addVariavel_bt = ft.ElevatedButton("Adicionar Variável", on_click=addVariavel)
    addValores_bt = ft.ElevatedButton("Calcular", on_click=calcular)

    #função que muda a tela 
    def mudaTela(e):
        #"/" é a tela inicial
        if page.route == "/":
            if e.control.selected_index == 1:
                page.go("/store")
            elif e.control.selected_index == 2:
                page.go("/settings")
        elif page.route == "/store":
            if e.control.selected_index == 0:
                page.go("/")
            elif e.control.selected_index == 2:
                page.go("/settings")
        elif page.route == "/settings":
            if e.control.selected_index == 0:
                page.go("/")
            elif e.control.selected_index == 1:
                page.go("/store")
        rail.selected_index = 0
        rail2.selected_index = 1
        rail3.selected_index = 2

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        #leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_WORK, selected_icon=ft.icons.HOME_WORK_SHARP, label="Início"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.HARDWARE_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.HARDWARE),
                label="Simulação",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Configurações"),
            ),
        ],
        on_change=mudaTela
    )

    rail2 = ft.NavigationRail(
        selected_index=1,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        #leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_WORK, selected_icon=ft.icons.HOME_WORK_SHARP, label="Início" 
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.HARDWARE_OUTLINED), #icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.HARDWARE), #icons.BOOKMARK),
                label="Simulação",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Configurações"),
            ),
        ],
        on_change=mudaTela
    )

    rail3 = ft.NavigationRail(
        selected_index=2,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        #leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_WORK, selected_icon=ft.icons.HOME_WORK_SHARP, label="First"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.HARDWARE_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.HARDWARE),
                label="Simulação",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Configurações"),
            ),
        ],
        on_change=mudaTela
    )

    cano = ft.Container(
        width=150, 
        height=50, 
        bgcolor="blue", 
        top=150,                       #altura em que o objeto surge em relação ao topo da tela
        left=160,
        alignment=ft.alignment.center,
        animate_position=1000
    )

        #cria a coluna da esquerda
    emb2 = ft.Container(
        content=ft.Text(color=colors.WHITE),
        width=200,                      #largura da coluna (é o que varia)
        height=150,                     #altura da coluna
        bgcolor="blue",                 #cor do objeto
        left=10,
        top=50,
        alignment=ft.alignment.center,
        animate_position=1000           #não sei
    )

    #cria a coluna da direita
    emb1 = ft.Container(
        content=ft.Text(color=colors.WHITE),
        width=50, 
        height=150, 
        bgcolor="blue", 
        left=285, 
        top=50,
        alignment=ft.alignment.center,
        animate_position=1000
    )

    peso1 = ft.Container(
        content=ft.Text(value="(2)", color=colors.WHITE),
        width=200,                      #largura da coluna (é o que varia)
        height=30,                     #altura da coluna
        bgcolor="red",                 #cor do objeto
        left=10,
        top=50,
        alignment=ft.alignment.center,
        animate_position=1000           #não sei
    )

    #cria a coluna da direita
    peso2 = ft.Container(
        content=ft.Text(value="(1)", color=colors.WHITE),
        width=50, 
        height=30, 
        bgcolor="red", 
        left=285, 
        top=50,
        alignment=ft.alignment.center,
        animate_position=1000
    )
        
    img = ft.Image(
        src=f"seta_p_baixo.png",
        width=50,
        height=50,
        left=85,
        fit=ft.ImageFit.CONTAIN,
    )

    img2 = ft.Image(
        src=f"seta_p_baixo.png",
        width=50,
        height=50,
        left=285,
        fit=ft.ImageFit.CONTAIN,
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [   
                    ft.AppBar(title=ft.Text("Início"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Row(
                            [
                            rail,
                            ft.VerticalDivider(width=1),
                            ],
                            expand=True,
                        ),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Prensa"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Row(controls=[
                            rail2,
                            ft.VerticalDivider(width=1),
                            ft.Column(controls=[
                                # Container que contém o título do programa
                                ft.Container(ft.Text(" Aplicação Prensa hidráulica/ Problemas", color=colors.BLUE_50), bgcolor=colors.BLUE_900, border=ft.border.all(1, colors.BLUE_100), border_radius=ft.border_radius.all(5), width=1200, height=25),
                                # Linha que contém a seleção da variável que o usuário deseja calcular
                                variavel_dropdown,
                                #Linha que contem o botão que adiciona a variável que o usuário deseja calcular
                                addVariavel_bt,
                                # Container que cria linha azul, só estético
                                ft.Container(bgcolor=colors.BLUE_900, border=ft.border.all(1, colors.BLUE_100), border_radius=ft.border_radius.all(5), width=1200, height=5),
                                # Linha que contém os campos de texto para o usuário digitar os valores
                                ft.Row([a1, a2, f1, f2], width=1200),
                                # Linha que contém o botão que calcula a variável que o usuário deseja calcular
                                addValores_bt,
                                # Container que cria linha azul, só estético
                                ft.Container(bgcolor=colors.BLUE_900, border=ft.border.all(1, colors.BLUE_100), border_radius=ft.border_radius.all(5), width=1200, height=5),
                                # Container que contém a resolução do problema
                                ft.Container(display, bgcolor=colors.BLUE_50, border=ft.border.all(1, colors.BLUE_100), border_radius=ft.border_radius.all(5)),
                                #cria a imagem do êmbolo
                                ft.Column([ft.Stack([emb1, emb2, cano, peso1, peso2, img, img2], height=220)], alignment=ft.MainAxisAlignment.START, expand=True,)
                                ], scroll=ft.ScrollMode.ALWAYS), 
                        ], expand=True),
                    ], 
                )
            )
        elif page.route == "/settings":
            page.views.append(
            ft.View(
                "/settings",
                [   
                    ft.AppBar(title=ft.Text("Configurações"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Row(
                            [
                            rail3,
                            ft.VerticalDivider(width=1),
                            ft.Column([
                                # Linha que contém o tema do programa
                                ft.Row([theme], alignment=ft.MainAxisAlignment.CENTER),
                                ], 
                                alignment=ft.MainAxisAlignment.START, 
                                expand=True)
                            ],
                            expand=True,
                        ),
                ],
            )
        )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)