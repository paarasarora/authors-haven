# Authors Haven

## Technical Overview

Authors Haven is a Django-based platform implementing a microservices architecture for content creation and sharing. This project demonstrates advanced backend engineering techniques and modern development practices.

## Architecture

The application follows a microservices-inspired architecture where different components handle specific business domains:

### Core Services
- **API Service**: Django REST Framework application exposing endpoints
- **Database Service**: PostgreSQL for persistent data storage
- **Search Service**: Elasticsearch for article indexing and searching
- **Cache & Message Broker**: Redis for caching and Celery task queuing
- **Task Workers**: Celery workers for asynchronous processing
- **Email Service**: Email delivery through Celery workers
- **Web Server**: Nginx for request routing and static file serving

### Domain-Specific Modules
- `core_apps/users`: Authentication and user management
- `core_apps/profiles`: User profile information and settings
- `core_apps/articles`: Content creation and management
- `core_apps/comments`: Discussion functionality for articles
- `core_apps/ratings`: Rating system for content quality feedback
- `core_apps/search`: Custom Elasticsearch integration for full-text search

## Technical Implementation

### Django Configuration
- Custom settings structure with base, local, and production configurations
- Environment-based configuration using django-environ
- ASGI support for asynchronous capabilities
- Custom viewsets and response formatting

### Elasticsearch Integration
- Custom document mapping for article content
- Signal-based indexing to keep search data in sync
- Django Elasticsearch DSL integration for ORM-like operations
- Custom search filters and query capabilities

### API Development
- RESTful API with Django REST Framework
- Comprehensive endpoints for all core functionality
- API documentation with drf-yasg (Swagger/ReDoc)
- Custom pagination and response formatting

### Container Orchestration
- Multi-container setup using Docker Compose
- Volume management for persistent data
- Environment isolation through Docker networks
- Service dependency management

### Asynchronous Processing
- Celery task queue for background operations
- Redis as message broker and result backend
- Celery Flower for task monitoring
- Email sending via Celery workers

### Code Quality & Development Tools
- Black for code formatting
- isort for import sorting
- flake8 for code quality checking
- pytest for comprehensive testing

## Technical Details

### Elasticsearch Documents

The search module implements custom Elasticsearch documents:

```python
@registry.register_document
class ArticleDocument(Document):
    title = fields.TextField(attr="title")
    description = fields.TextField(attr="description")
    body = fields.TextField(attr="body")
    author_first_name = fields.TextField(attr="author__first_name")
    author_last_name = fields.TextField(attr="author__last_name")
    
    class Index:
        name = "articles"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
```

### Custom API Response Formatting

The application uses custom response formatting for consistent API responses:

```python
def custom_success_response(serialized_data, message='success', status=status.HTTP_200_OK, headers=None, **kwargs):
    data = {}
    data['data'] = serialized_data
    for key, value in kwargs.items():
        data[key] = value
    data['status'] = '1'
    return JsonResponse(data, status=status, headers=headers)
```

### Docker Compose Service Configuration

The microservices are orchestrated using Docker Compose:

```yaml
services:
    es:
        image: elasticsearch:7.17.9
        environment:
            - discovery.type=single-node
        ports:
            - "9200:9200"
        networks:
            - authors-api-live
            
    api:
        build:
            context: .
            dockerfile: ./docker/local/django/Dockerfile
        command: /start
        volumes:
            - .:/app
            - static_volume:/app/authorsHaven/staticfiles
            - media_volume:/app/authorsHaven/mediafiles
        depends_on:
            - postgres
            - mailhog
            - redis
            - es
        networks:
            - authors-api-live
```

### Nginx Configuration

Custom Nginx configuration for routing requests:

```nginx
upstream api {
    server api:8000;
}

server {
    client_max_body_size 20M;
    listen 80;
    
    location /api/v1/ {
        proxy_pass http://api;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }
    
    location /supersecret/ {
        proxy_pass http://api;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }
}
```

## Development Operations

The project uses a Makefile for streamlined operations:

```
build:              Build the entire Docker environment
up:                 Start all containers
down:               Stop all containers
migrate:            Run database migrations
makemigrations:     Create new migrations
superuser:          Create superuser account
collectstatic:      Collect static files
show-logs:          Display container logs
show-logs-api:      Display API logs
authors-db:         Connect to PostgreSQL database
elasticsearch:      Create Elasticsearch index
elasticsearch-populate: Populate search index
```

## Key Technologies

- **Django 4.1.7**: Web framework for backend development
- **Django REST Framework **: API building toolkit
- **PostgreSQL**: Relational database for data persistence
- **Elasticsearch **: Search engine for article indexing
- **Redis**: Message broker and caching layer
- **Celery **: Distributed task queue
- **Docker & Docker Compose**: Container orchestration
- **Nginx**: Web server and reverse proxy
- **Python 3.9**: Primary programming language

## Performance and Scaling Considerations

- Microservices architecture enables independent scaling of components
- Docker containerization for consistent deployment across environments
- Celery for handling resource-intensive background tasks
- PostgreSQL database optimized for read/write operations
- Elasticsearch for efficient full-text search capabilities
- Redis caching for improved performance

## Setup and Installation

1. Clone the repository
2. Configure environment variables in `.envs/.local/.django` and `.envs/.local/.postgres`
3. Run `make build` to build and start the Docker environment
4. Run `make migrate` to apply database migrations
5. Run `make superuser` to create an admin account
6. Access the API at `http://localhost:8080/api/v1/`
7. View API documentation at `http://localhost:8080/redoc/`
8. Access admin panel at `http://localhost:8080/supersecret/`

## Developer Tools

- **Mailhog**: Local SMTP testing at `http://localhost:8025`
- **Flower**: Celery task monitoring at `http://localhost:5555`
- **Django Debug Toolbar**: Development debugging (when enabled)
- **PostgreSQL Maintenance**: Database backup/restore utilities

---

Developed by Paaras Arora
