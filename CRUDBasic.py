from flet import *


def main(page : Page):
    page.scroll = "always"
    
    
    name = TextField(label="Tareas")
    descripcion = TextField(label="Descripcion")
    elID = Text("")
    
    
    #tabla de tareas
    reiTabla = DataTable(
        columns=[
            DataColumn(Text("ID")),
            DataColumn(Text("Nombre")),
            DataColumn(Text("Descripcion"))
        ]
    )
    
    rows = []
    
    
    
    
    #Obtener el ID de la row
    def editindex(e,r):
        print("Tu ID es = ", e)
        print("Tu Nombre es =", r)

        name.value = r
        elID.value = int(e)
        
        addButton.visible = True
        deleteButton.visible = True
        updateButton.visible = True
        page.update()
        
        
        
        
    
    
    #agregar informacion a la tabla
    def addnewdata(e):
        reiTabla.rows.append(
            DataRow(
            cells=[
                DataCell(Text(len(reiTabla.rows))),
                DataCell(Text(name.value)),
                DataCell(Text(descripcion.value)),
                    
                ],
            on_select_changed=lambda e:editindex(e.control.cells[0].content.value,e.control.cells[1].content.value)
            )
        )
        name.value = ""
        descripcion.value = ""
        page.update()
    
    
    #boton agregar 
    addButton = ElevatedButton("Agregar",
        bgcolor="green",
        color="white",
        on_click=addnewdata
        )
    
    
    # Editamos y guardamos cambios
    def ediGuardar(e):
        reiTabla.rows[elID.value].cells[1].content = Text(name.value)
        reiTabla.rows[elID.value].cells[2].content = Text(descripcion.value)
        page.update()
        
    #boton actualizar
    updateButton = ElevatedButton("Actualizar",
        bgcolor="orange",
        color="white",
        on_click= ediGuardar
        )
    
    
    #eliminamos y guardamos
    def matarile(e):
         print('Tu ID es =', elID.value)
         del reiTabla.rows[elID.value]
    #mostramos mensaje de eliminado
    
    page.snack_bar = SnackBar(
        Text(f'Tarea {name.value} eliminado con Exito', color='white', weight='bold'),
        bgcolor='red',
    
    )
    
    page.snack_bar.open = True
    page.update()
    
    #boton eliminar
    deleteButton = ElevatedButton("Eliminar",
        bgcolor="red",
        color="white",
        on_click = matarile
        )
    addButton.visible = True
    deleteButton.visible = False 
    updateButton.visible = False
    
    page.add(
        Column([
            
                Text("CRUD de prueba", size=30, weight="bold"),
                
                name,
                descripcion,
                Row([addButton, updateButton, deleteButton]),
                reiTabla
            ])
        
    )
    
    
app(target=main)