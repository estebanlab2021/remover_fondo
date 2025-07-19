# 🛠️ Aplicación para remover el fondo de una imagen

## 🚀 Resumen del Proyecto

Este proyecto es una aplicación web simple que demuestra la **comunicación cliente-servidor** para procesar imágenes. El **front-end** (HTML y JavaScript) se encarga de que el usuario suba una imagen, la cual es enviada a un servidor **back-end** (Python con Flask) para ser procesada.

La aplicación utiliza la librería `rembg`, que usa redes neuronales profundas, para eliminar automáticamente el fondo de la imagen, devolviendo el resultado al cliente para su visualización.

<br>

![HTML](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white)

---

## ✨ Características Principales

-   **Interfaz Sencilla:** Carga una imagen de forma intuitiva a través de un simple "input file" 📥.
-   **Procesamiento Inteligente:** Un botón procesa la imagen enviándola al servidor.
-   **Eliminación de Fondo:** El back-end utiliza la poderosa librería `rembg` para remover el fondo de la imagen de manera eficiente.
-   **Visualización en Tiempo Real:** La imagen procesada se muestra en la página en cuestión de segundos ⏱️.


---

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto de forma local, necesitas tener instalado Python 3.7 o superior.

1.  Clona el repositorio:
```bash
git clone [https://github.com/estebanlab2021/remover_fondo.git](https://github.com/estebanlab2021/remover_fondo.git)
```

2.  Navega al directorio del proyecto:
```bash
cd remover_fondo
```

3.  Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```


---

## 🚀 Cómo ejecutar la aplicación

1.  **Inicia el servidor (back-end):**
Abre una terminal en el directorio del proyecto y ejecuta el servidor Python:
```bash
python app.py
```
El servidor se ejecutará en http://127.0.0.1:5000.

2.  **Abre el front-end:**
Abre tu archivo `remover_fondo.html` en un navegador web. Puedes usar una extensión como "Live Server" en VS Code o simplemente abrir el archivo directamente.

---

## 🌐 Versión en línea

El proyecto lo puedes visualizar en el siguiente link:
👉 [Enlace a la demo](https://tu-github-pages-link)

## 📄 Licencia

Este proyecto es de uso libre con fines educativos y de prueba.

---

## 👨‍💻 Autor

**Esteban Arroyo**
