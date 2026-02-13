# Guía de Creación de Posts para el Agente

Esta guía detalla el proceso para crear y listar un nuevo post en el blog de Fer Mavec.

## 1. Estructura del Archivo del Post

### Ubicación
Crear un nuevo archivo HTML en la carpeta `blog-posts/`.
El nombre del archivo debe ser URL-friendly (minúsculas, guiones en lugar de espacios).
Ejemplo: `blog-posts/titulo-del-post.html`.

### Plantilla Base
Utilizar la siguiente estructura HTML5. Asegúrate de ajustar las rutas relativas (`../`) para CSS, imágenes y scripts.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Título del Post] | Fer Mavec</title>
    <meta name="description" content="[Breve descripción para SEO]">
    <meta name="author" content="Fernando Mavec">
    <link rel="stylesheet" href="../css/style.css">
    <!-- Fuentes y FontAwesome -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <!-- Header -->
    <header id="main-header">
        <nav>
            <div class="logo"><a href="../index.html">Fer Mavec.</a></div>
            <ul class="nav-links">
                <li><a href="../index.html#hero">Manifiesto</a></li>
                <li><a href="../index.html#about">Bio-Algoritmos</a></li>
                <li><a href="../index.html#pillars">Pilares</a></li>
                <li><a href="../blog.html" class="active">Hello Wolf!</a></li> <!-- Note: Link to blog listing -->
                <li><a href="../index.html#contact" class="btn-primary">Conectar</a></li>
            </ul>
            <div class="hamburger"><i class="fas fa-bars"></i></div>
        </nav>
    </header>

    <main class="blog-container">
        <article class="single-post">
            <header class="post-header">
                <span class="post-date">[Día] de [Mes], [Año]</span>
                <h1>[Título del Post]</h1>
                <div class="tags">
                    <!-- Insertar tags aquí -->
                    <span>#[Tag1]</span>
                    <span>#[Tag2]</span>
                </div>
            </header>

            <div class="post-content">
                <p class="lead">[Introducción impactante/Lead]</p>
                
                <p>[Párrafo de contenido...]</p>

                <h2>[Subtítulo]</h2>
                <p>[Contenido...]</p>

                <blockquote class="bio-quote">
                    "[Cita destacada]"
                </blockquote>

                <p>[Más contenido...]</p>
            </div>

            <div class="post-footer">
                <a href="../blog.html" class="link-arrow"><i class="fas fa-arrow-left"></i> Volver a la Bitácora</a>
            </div>
        </article>
    </main>

    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-logo">Fer Mavec.</div>
                <p>&copy; 2026 Fer Mavec. Todos los derechos reservados.</p>
            </div>
        </div>
    </footer>
    <script src="../js/main.js"></script>
</body>
</html>
```

### Estilos Importantes
- **Quote**: Usar `<blockquote class="bio-quote">`.
- **Lead Paragraph**: Usar `<p class="lead">` para el primer párrafo.
- **Headers**: Usar `<h2>` para subtítulos.

## 2. Listado en `blog.html`

Agregar una nueva tarjeta de artículo (`article`) dentro del contenedor `#posts-container`, idealmente dentro de un `.posts-group`.
Si el mes/año cambia, crear un nuevo grupo `.posts-group.date-group` con el título del mes/año.

### Estructura de la Tarjeta

```html
<article class="blog-post-card" data-tags="[Tag1] [Tag2]"> <!-- Tags separados por espacio sin # -->
    <div class="card-meta">
        <span class="post-date">[Día] de [Mes], [Año]</span>
        <div class="card-tags">
            <span>#[Tag1]</span>
            <span>#[Tag2]</span>
        </div>
    </div>
    <h3><a href="blog-posts/[nombre-archivo].html">[Título del Post]</a></h3>
    <p>[Extracto breve del post...]</p>
    <a href="blog-posts/[nombre-archivo].html" class="read-more">Leer Más <i class="fas fa-arrow-right"></i></a>
</article>
```

## 3. Manejo de Tags

- Los tags deben ser consistentes (ej. Biohacking, Philosophy, AI, HealthTech).
- En `data-tags` del artículo de la lista: usar nombres sin `#`, separados por espacios.
- En el visual (`<span>`): usar `#` al inicio.
- **Importante**: Siempre consultar al usuario o inferir los tags del contexto si no se proporcionan explícitamente.
