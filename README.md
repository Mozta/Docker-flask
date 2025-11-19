# Flask + Docker + PostgreSQL

Aplicación web desarrollada con Flask, PostgreSQL y Docker. Este proyecto demuestra cómo containerizar una aplicación Flask con una base de datos PostgreSQL utilizando Docker Compose.

## Características

- **Flask 3.1.2**: Framework web minimalista y potente
- **PostgreSQL 13**: Base de datos relacional
- **Docker & Docker Compose**: Containerización y orquestación de servicios
- **Flask-SQLAlchemy**: ORM para gestión de base de datos
- **Hot Reload**: Desarrollo con recarga automática de código

## Prerequisitos

- Docker
- Docker Compose
- Git

## Estructura del Proyecto

```
flask-docker/
├── docker-compose.yml          # Orquestación de servicios
├── .env.dev                    # Variables de entorno para desarrollo
└── services/
    └── web/
        ├── Dockerfile          # Imagen Docker para Flask
        ├── manage.py           # Comandos CLI de gestión
        ├── requirements.txt    # Dependencias Python
        └── project/
            ├── __init__.py     # Inicialización de la app Flask
            └── config.py       # Configuración de la aplicación
```

## Configuración

### Variables de Entorno (.env.dev)

```env
FLASK_APP=project/__init__.py
FLASK_RUN_PORT=5000
FLASK_DEBUG=True
DATABASE_URL=postgresql://username:password@db:5432/database_name
```

### Servicios Docker

- **web**: Aplicación Flask en puerto `5001` (host) → `5000` (contenedor)
- **db**: PostgreSQL 13 en puerto `5432`

## Instalación y Ejecución

### 1. Clonar el repositorio (si aplica)

```bash
git clone <repository-url>
cd flask-docker
```

### 2. Construir y levantar los contenedores

```bash
docker-compose up -d --build
```

### 3. Crear las tablas de la base de datos

```bash
docker-compose exec web python manage.py create_db
```

### 4. Acceder a la aplicación

Abre tu navegador en: [http://localhost:5001](http://localhost:5001)

Deberías ver el mensaje:
```json
{
  "message": "Welcome to my Flask app with Docker!"
}
```

## Comandos Útiles

### Ver logs de los contenedores

```bash
docker-compose logs -f
```

### Detener los contenedores

```bash
docker-compose down
```

### Detener y eliminar volúmenes (reinicio completo)

```bash
docker-compose down -v
```

### Acceder al shell del contenedor web

```bash
docker-compose exec web bash
```

### Acceder a PostgreSQL

```bash
docker-compose exec db psql -U username -d database_name
```

### Recrear la base de datos

```bash
docker-compose exec web python manage.py create_db
```

## Modelo de Datos

### User

```python
class User(db.Model):
    id: Integer (Primary Key)
    email: String(120) (Unique, Not Null)
    active: Boolean (Default: True)
```

## Dependencias Principales

- **Flask**: Framework web
- **Flask-SQLAlchemy**: ORM para bases de datos
- **psycopg2-binary**: Adaptador PostgreSQL para Python
- **python-dotenv**: Gestión de variables de entorno
- **Werkzeug**: Utilidades WSGI

## Desarrollo

El proyecto está configurado con volúmenes que permiten **hot reload**. Los cambios en el código se reflejan automáticamente sin necesidad de reconstruir el contenedor.

```yaml
volumes:
  - ./services/web:/usr/src/app/
```

## Endpoints de la API

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | `/`      | Mensaje de bienvenida |

## Troubleshooting

### El contenedor no inicia
- Verifica que los puertos 5001 y 5432 no estén en uso
- Revisa los logs: `docker-compose logs`

### Error de conexión a la base de datos
- Asegúrate de que el servicio `db` esté ejecutándose: `docker-compose ps`
- Verifica las credenciales en `.env.dev`

### Cambios en el código no se reflejan
- Verifica que `FLASK_DEBUG=True` esté en `.env.dev`
- Reinicia el contenedor: `docker-compose restart web`

## Próximos Pasos

- [ ] Agregar más endpoints CRUD para el modelo User
- [ ] Implementar autenticación y autorización
- [ ] Agregar tests unitarios y de integración
- [ ] Configurar ambiente de producción
- [ ] Implementar migraciones con Flask-Migrate
- [ ] Agregar documentación API con Swagger/OpenAPI

## Autor

Proyecto de ejemplo para el curso de Tópicos Avanzados - Otoño 2025

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
