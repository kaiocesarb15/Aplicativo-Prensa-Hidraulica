import flet as ft
from flet import colors

def main(page: ft.Page):
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
        #result.color=textcolor
        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT
    theme = ft.Switch(label="Light mode", on_change=theme_changed)

    def inicio():
        return ft.Column(
            [
                ft.Text("Inicio")
            ]
        )
    
    def problemas():
        return ft.Column(
            [
                ft.Text("Problemas")
            ]
        )
    
    def config():
        return ft.Column(
            [
                ft.Text("Configurações")
            ]
        )

    def mudar_pagina(index):
        if index == 0:
            inicio()
        elif index == 1:
            problemas()
        elif index == 2:
            config()
        page.update()

    def barra_navegacao():
        rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=2000,
            #leading=ft.FloatingActionButton(icon=ft.icons.CABLE, text="Inicio"),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.CABLE_SHARP,
                    selected_icon=ft.icons.CABLE,
                    label="Inicio"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.BOOKMARK_BORDER,
                    selected_icon=ft.icons.BOOKMARK,
                    label="Second"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon=ft.icons.SETTINGS,
                    label = "Settings"
                )
            ],
            on_change=lambda e: mudar_pagina(e.control.selected_index),
        )
        
        return ft.Row(
                [
                    rail,
                    ft.VerticalDivider(width=1, color=colors.BLUE),
                    ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
                ],
                width=400,
                height=400
            )

    page.add(barra_navegacao(), theme)
ft.app(target=main)