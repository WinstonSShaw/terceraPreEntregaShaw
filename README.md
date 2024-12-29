# Entrega Final 

## Curso

- Curso de Python
- Comision N 60095
- Prof: Esteban Acevedo

## Alumno

- Nombre: Winston Shaw

## Objetivos del proyecto

- Desarrollar un Proyecto Web Django siguiendo el patrón MVT (Model-View-Template) que incluya
-- ✅ Herencia de HTML para mejorar la reutilización de código.
-- ✅ 3 Clases en Models: Consola, Juego y Jugador.
-- ✅ Formularios para insertar datos en todas las clases del modelo.
-- ✅ Readme Documentado para describir la estructura y funcionalidad del proyecto. 

## Aspectos tecnicos

- 🚀 Framework Django: Se utilizó Django para implementar el patrón MVT 
- 📊 Modelos:
-- Consola: Representa las consolas disponibles.
-- Juego: Representa los juegos asociados a una consola.
-- Jugador: Representa los jugadores vinculados a un juego.
- 📝 Formularios: Se implementaron formularios basados en modelos para Consola, Juego y Jugador.
- 💻 CRUD Completo: Se implementaron operaciones de Crear, Leer, Editar y Eliminar (CRUD) para todas las entidades.
- 🔒 Autenticación y Autorización:
-- Registro de usuarios.
-- Inicio y cierre de sesión.
-- Protección de vistas con @login_required.
- 🔍 Búsqueda en Listas:
-- Se agregó una barra de búsqueda para filtrar por nombre o DNI en las vistas de Consolas, Juegos y Jugadores.
- 🎨 Interfaz Estilizada:
-- Listas con estilos modernos.
-- Botones claros para Editar y Eliminar.
-- Encabezado dinámico con opciones de Login/Logout y nombre de usuario.

## 🛡️ Seguridad

- 🔑 Uso de CSRF Tokens en formularios.
- 🔐 Protección de vistas CRUD con el decorador @login_required.


## Puntos a mejorar

- 🖥️ Dashboard Inicial con estadísticas.
- 📣 Mensajes Flash: Mostrar mensajes de éxito al crear, editar o eliminar un registro.
- 📑 Paginado para Listas: Implementar paginación en las listas para mejorar la experiencia con grandes cantidades de datos.

## Iniciar proyecto
- python manage.py runserver
- Abrir web http://127.0.0.1:8000/
