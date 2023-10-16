import flet as ft
from flet import colors

def main(page: ft.Page):
    f1 = 200 
    f2 = 2000
    
    def slider_p_a1(e):
        emb1.width = int(e.control.value) * 5
        cano.width = emb1.left + (emb1.width/2)
        result.value=f"""Área de p1: {emb1.width/5}cm²      F1: {f1}N
        \nÁrea de p2: {emb2.width/2}cm²      F2: {f2}N"""
        result.update()
        page.update()

    def slider_p_a2(e):
        emb2.width = int(e.control.value) 
        emb1.left = emb2.width + 60
        cano.width = emb1.left + (emb1.width/2)
        result.value=f"""Área de p1: {emb1.width/5}cm²      F1: {f1}N
        \nÁrea de p2: {emb2.width/2}cm²      F2: {f2}N"""
        result.update()
        page.update()

    def slider_p_f1(e):
        f1 = int(e.control.value)
        f2 = (emb2.width / 2) * f1 / (emb1.width / 5)
        result.value=f"""Área de p1: {emb1.width/5}cm²      F1: {f1}N
        \nÁrea de p2: {emb2.width/2}cm²      F2: {f2}N"""
        result.update()
        page.update()

    def slider_p_f2(e):
        f2 = int(e.control.value)
        f1 = (emb1.width / 5) * f2 / (emb2.width / 2)
        result.value=f"""Área de p1: {emb1.width/5}cm²      F1: {f1}N
        \nÁrea de p2: {emb2.width/2}cm²      F2: {f2}N"""
        result.update()
        page.update()

    #cria a 1º coluna com água
    emb2 = ft.Container(
        content=ft.Text(value="(2)", color=colors.WHITE),
        width=200,   #largura da coluna (é o que varia)
        height=150,  #altura da coluna
        bgcolor="blue", #cor do objeto
        #on_click=slider_p_1, #informa qual função executar quando clicar no objeto
        animate_position=1000 #não sei
    )

    #cria o cano horizontal por onde a água passa
    cano = ft.Container(
        width=300, 
        height=50, 
        bgcolor="blue", 
        top=100,      #altura em que o objeto surge em relação ao topo da tela
        animate_position=1000
    )

    #cria a 2º coluna com água
    emb1 = ft.Container(
        content=ft.Text(value="(1)", color=colors.WHITE),
        width=50, 
        height=150, 
        bgcolor="blue", 
        left=cano.width-25, 
        #on_click=slider_p_2,
        animate_position=1000
    )

    result = ft.Text(value=f"""Área de p1: {emb1.width/5}cm²      F1: {f1}N
        \nÁrea de p2: {emb2.width/2}cm²      F2: {f2}N""", color=ft.colors.WHITE, size=20)

    #slider para a área 1
    slider_a1 = ft.Slider(
        min=4,                 #valor mínimo
        max=20,                #valor máximo    
        divisions=17,          #divisões
        value=10,              #valor inicial
        label="{value}",       #valor que aparece na bolinha
        on_change=slider_p_a1,  
    )

    #slider para área 2
    slider_a2 = ft.Slider(
        min=60,                #valor mínimo
        max=300,               #valor máximo    
        divisions=240,         #divisões
        value=200,             #valor inicial
        label="{value}",       #valor que aparece na bolinha
        on_change=slider_p_a2,  
    )

    #slider para força 1
    slider_f1 = ft.Slider(
        min=100,               #valor mínimo
        max=300,               #valor máximo    
        divisions=200,         #divisões
        value=200,             #valor inicial
        label="{value}",       #valor que aparece na bolinha
        on_change=slider_p_f1,  
    )

    #slider para força 2
    slider_f2 = ft.Slider(
        min=1000,                #valor mínimo
        max=3000,               #valor máximo    
        divisions=500,          #divisões
        value=2000,             #valor inicial
        label="{value}",       #valor que aparece na bolinha
        on_change=slider_p_f2,  
    )


    display = ft.Row(
        width = 250,
        controls=[result]
    )

    page.add(
        ft.Stack([emb2, cano, emb1], height=250),
        display,
        ft.Column([ ft.Text("Área do êmbolo 1"), slider_a1]),
        ft.Column([ ft.Text("Área do êmbolo 2"), slider_a2]),
        ft.Column([ ft.Text("Intensidade da força 1"), slider_f1]),
        ft.Column([ ft.Text("Intensidade da força 2"), slider_f2]),
    )

ft.app(target=main)