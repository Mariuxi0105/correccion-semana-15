# Sistema Restaurante

**Autora:** Mariuxi Jessenia Tejada Mayorga
**Trabajo:** Semana 15

## Descripción

Sistema Restaurante es una aplicación de escritorio desarrollada en Python con Tkinter/ttk. En esta entrega de Semana 15, conserva el acceso, la consulta y gestión de usuarios y el CRUD de productos, e incorpora el registro y consulta de ventas.

El proyecto conserva la separación entre datos JSON, modelos, servicios, vistas, recursos visuales y punto de entrada. Las vistas coordinan los componentes; las validaciones y persistencia de productos, usuarios y ventas se delegan a `RestauranteServicio` y `ArchivoServicio`.

## Estructura

```text
restaurante_app/
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── assets/
│   ├── logo-restaurante.jpg
│   ├── icono_inicio.xbm
│   ├── icono_productos.xbm
│   ├── icono_usuarios.xbm
│   └── icono_ventas.xbm
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   ├── restaurante.py
│   └── restaurante_servicio.py
└── ui/
    ├── __init__.py
    ├── estilos.py
    ├── login_view.py
    ├── main_view.py
    └── recursos.py
```

## Funcionamiento por componentes

- **Modelos:** representan productos, usuarios y la relación de una venta con el usuario, el producto y su fecha.
- **Servicios:** `RestauranteServicio` valida el acceso y las operaciones del dominio; `ArchivoServicio` persiste productos, usuarios y ventas en JSON.
- **Interfaz:** `estilos.py` centraliza el tema ttk; `assets/` proporciona logotipo e íconos. El panel usa navegación, `Combobox`, tablas `Treeview` y botones con `command=`.
- **Inicio:** presenta el conteo actual de usuarios, productos y ventas para acceder rápidamente al estado del restaurante.
- **Punto de entrada:** `main.py` prepara la ventana, carga la información y enlaza los componentes.

## Archivos de datos

La información utilizada por el programa se encuentra en la carpeta `datos/`:

- `productos.json`: catálogo disponible.
- `usuarios.json`: usuarios habilitados para ingresar.
- `ventas.json`: ventas registradas con identificadores de usuario y producto, y fecha/hora ISO.

## Ventas y flujo de eventos

En **Ventas** se seleccionan un usuario registrado y un producto registrado con listas desplegables. El botón **Registrar venta** declara `command=self._registrar_venta`: el callback obtiene las selecciones y delega el registro a `RestauranteServicio`. El servicio valida que las entidades existan y solicita la persistencia a `ArchivoServicio`; tras el éxito, la vista actualiza la tabla y muestra una confirmación. Al iniciar, las ventas se vuelven a cargar desde `ventas.json`.

El botón **Generar reporte PDF** abre un selector para guardar el historial completo de ventas. La vista envía la ruta a `RestauranteServicio`, que construye el reporte con referencias, usuario, producto y fecha. Para instalar la dependencia en el entorno del proyecto, ejecuta `pip install -r requirements.txt`.

Flujo: acción del usuario → `command=` → callback de la vista → `RestauranteServicio` → `ArchivoServicio` / `ventas.json` → tabla y respuesta visual.

## Operaciones de productos

En la sección **Productos** se utiliza un formulario para capturar el ID, nombre, precio, categoría y stock. Las acciones disponibles son:

- **Registrar:** crea un producto nuevo.
- **Cargar / Consultar:** busca un producto mediante su ID y muestra sus datos en el formulario.
- **Actualizar:** reemplaza la información del producto seleccionado por su ID.
- **Eliminar:** retira el producto del catálogo.

Todas las operaciones son solicitadas a `RestauranteServicio`. La interfaz no lee ni modifica directamente los archivos JSON; después de cada cambio vuelve a consultar el servicio y actualiza la tabla. La eliminación solicita confirmación.

## Registro de usuarios

En **Usuarios** se pueden consultar las cuentas registradas y crear nuevas mediante un formulario con nombre, apellido, usuario, contraseña, correo, fecha de nacimiento y rol. El servicio asigna el ID, evita duplicar el nombre de usuario o el correo y guarda la cuenta en `usuarios.json`; después de registrarse, puede ingresar con su usuario y contraseña.

## Cómo iniciar la aplicación

En VS Code, abre la carpeta `restaurante_app`, selecciona `main.py` y pulsa **Run Python File** (el botón ▶ de la esquina superior derecha). También puedes abrir una terminal en esa carpeta y ejecutar:

```bash
python main.py
```

## Credenciales de demostración

```text
Usuario: admin
Contraseña: 1234

Usuario: cajero
Contraseña: cajero2026

Usuario: cocina
Contraseña: cocina2026
```

Las contraseñas se almacenan como texto simple en el JSON; esta es una aplicación docente, no un sistema de autenticación para producción.

## Verificación de sintaxis

Para revisar que los archivos Python sean válidos, utiliza:

```bash
python -m compileall -q main.py modelos servicios ui
```

## Comprobación de la Semana 15

1. Ejecutar `python main.py` e ingresar con `admin` y `1234`.
2. Abrir **Usuarios** para consultar la información registrada.
3. Registrar un usuario en **Usuarios**, cerrar sesión y entrar con la cuenta recién creada.
4. Abrir **Productos** y probar el registro, consulta por ID, actualización y eliminación usando el formulario.
5. Abrir **Ventas**, seleccionar usuario y producto y pulsar **Registrar venta**; comprobar la tabla y `datos/ventas.json`.
6. Pulsar **Generar reporte PDF**, elegir una ubicación y comprobar que el documento contiene las ventas registradas.
7. Cerrar y volver a ejecutar la aplicación para comprobar que la venta se recupera desde el JSON.