#modulos
import flet 
from flet import *

def main(page: Page):
    #maximizar ventana 
    def _max(e):
        _b.controls[0].width = 300
        _b.controls[0].scale = transform.Scale(1,
        alignment=alignment.center_right)
        _b.controls[0].border_radius = 35

        _b.controls[0].disabled =False
        _b.controls[0].update()
    
    #eliminamos la animacion
    def DeleteAnimation(e):
        if e.data == 'true':
            e.control.content.controls[0].offset = transform.Offset(-0.6, 0)
            e.control.content.controls[0].update()
            
            e.control.content.controls[0].opacity = 1
            e.control.content.controls[0].update()
        else: 
            e.control.content.controls[0].offset = transform.Offset(0,0)
            e.control.content.controls[0].update()
            
            e.control.content.controls[0].opacity = 0
            e.control.content.controls[0].update()
    
    #funcion para minimizar menu
    def _min(e):
        _b.controls[0].width = 110
        _b.controls[0].scale = transform.Scale(0.9,
        alignment=alignment.center_right)
        _b.controls[0].border_radius = border_radius.only(
            top_right=0, bottom_right=0, top_left=35, bottom_left=35
        )
        _b.controls[0].disabled =True
        
        _b.controls[0].update()
    
    _a = Container(
        width=300,
        height=550,
        bgcolor='#211865',
        border_radius=35,
        padding=padding.only(left=20, top=60, right=120),
        content=Column(
            controls=[
                Row(
                    alignment='end',
                    controls=[
                        Container(
                            on_click=lambda e: _max(e),
                            content=Text(
                                'X',
                                size=12,
                                weight='bold',
                            )
                        ),
                    ],
                ),
                Container(
                    content=Text(
                        'Menu',
                        size=22,
                        weight='bold'
                    )
                ),
                Container(
                    padding=padding.only(top=10, bottom=10)
                ),
                Container(
                    content=Column(
                        controls=[
                            Text(
                                'Ajustes',
                                size=13,
                                weight='bold',
                                col='white60'
                            ),
                            Text(
                                'Cuenta',
                                size=13,
                                weight='bold',
                                col='white60'
                            ),
                            Text(
                                'Perfil',
                                size=13,
                                weight='bold',
                                col='white60'
                            ),
                        ],
                    ),
                ),
                Container(padding=padding.only(top=150)),
                Container(
                    content=Text(
                        'Cerrar seccion',
                        weight='bold'
                    )
                )
                ]
            ),
    )
    
    
    #container de tareas
    _container_tareas = Column()
    
    
    _card_container = Row(scroll='auto')
    
    #contenido  del Dashboard
    _dash = Container(
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=['#111827', '#1f2937']
        ),
        border_radius=30,
        padding=padding.only(top=15, left=15, right=10),
        content=Column(
            controls=[
                Container(
                    content=ResponsiveRow(
                        alignment= "spaceBetween",
                        controls=[
                            Text(
                                'DocSentinel',
                                col={'xs': 8},
                                no_wrap=True,
                                size=20,
                                weight='bold',
                            ),
                            Container(
                                col={'xs': 2},
                                on_click=lambda e: _min(e),
                                content=Text(
                                    '☰',
                                    weight='bold',
                                    no_wrap=True,
                                    size=18
                                ),
                            ),
                            
                        ],
                    ),
                ),
                Container(padding=padding.only(top=20)),
                Text(
                    'Categorias',
                    size=15,
                    color='white',
                    no_wrap=True,
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=_card_container,
                )
            ]
        )
    )
    
    
    
    #top content
    _b = Row(
        alignment="end",
        controls=[
            Container(
                width=300,
                height=550,
                bgcolor='#475569',
                border_radius=35,
                #animacion
                
                animate=animation.Animation(duration=500,
                curve="decelerate"),
                scale=transform.Scale(1, alignment=alignment.center_right),
                animate_scale=animation.Animation(duration=500,
                curve="decelerate"),
                padding=5,
                content=Column(
                    controls=[
                        _dash,
                        Container(
                            padding=padding.only(right=12,left=12),
                            content=Text(
                                'Tareas pendientes',
                                size=16,
                                color='white54',
                            )
                            ),
                        #segunda seccion del menu
                        Container(
                            padding=padding.only(right=12,left=12),
                            content=_container_tareas,
                        )
                    ]
                )
            )
        ],
    )
    
    #_container_tareas
    r = ['Conocer nuestro Equipo', 'Soporte']
    for index in range(2):
        _container_tareas.controls.append(
            ResponsiveRow(
                spacing=5,
                controls=[
                    Container(
                    col={'xs': 8},
                    height=40,
                    bgcolor='#1e293b',
                    padding=12,
                    border_radius=border_radius.only(
                        top_left=9, bottom_left=9, top_right=0, bottom_right=0,
                    ),
                    expand=True,
                    content=Text(
                        r[index],
                        size=10,
                        no_wrap=True,
                    )
                    ),
                    #esta seccion es una animacion
                    Container(
                        height=40,
                        col={'xs': 4},
                        alignment=animation.Animation(1000,'ease'),
                        bgcolor='#1e293b',
                        border_radius=border_radius.only(
                            top_left=0,
                            bottom_left=0,
                            top_right=9,
                            bottom_right=9,
                        ),
                        on_hover=lambda e: DeleteAnimation(e),
                        content=Row(
                            alignment='end',
                            spacing=0,
                            
                            controls=[
                                
                                Text(
                                    'Terminaste?',
                                    no_wrap=True,
                                    opacity=0,
                                    size=9,
                                    offset=transform.Offset(0,0),
                                    animate_offset=animation.Animation(duration=900,curve='ease'),
                                    animate_opacity=200,
                                )
                            ]
                        )
                        ),
                ],
            )
        )
    
    
    # card container
    #informacion de prueba que se debe reemplazar por real
    li = ['Archivos', 'Tareas', 'Ayuda']
    t = ['30 Archivos', '12 Tareas', '2 Tutoriales']
    p = [90, 123, 45]
    
    for index in range(3):
        _ = Card(
            elevation=15,
            content=Container(
                width=160,
                height=100,
                bgcolor='#1e293b',
                border_radius=15,
                padding=15,
                
                content=Column(
                    alignment='spaceBetween',
                    controls=[
                        Container(
                            content=Column(
                                spacing=3,
                                controls=[
                                    Text(
                                        t[index],
                                        color='white',
                                        size=12,
                                    ),
                                    Text(
                                        li[index],
                                        size=20,
                                    ),
                                ],
                            ),
                        ),
                        #barra de progreso
                        Container(
                            width=160,
                            height=5,
                            bgcolor="white12",
                            border_radius=20,
                            padding=padding.only(right=p[index]),
                            content=Container(
                                bgcolor='pink'
                            )
                        )
                    ],
                ),
            ),
        )
        _card_container.controls.append(_)
    
    
    
    #contenedor 
    _c = Container(
        width=300,
        height=550,
        border_radius= 35,
        bgcolor="pink",
        content=Stack(
            width=300,
            height=550,
            controls=[
                _a,
                _b,
            ]
        ),
    )
    
    page.add(_c)


if __name__ == '__main__':
    flet.app(target=main)