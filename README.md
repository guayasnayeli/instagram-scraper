# 📊 Instagram Scraper

## 📌 Descripción

Aplicación en Python que permite extraer información de perfiles de Instagram utilizando requests y una sesión autenticada.

El sistema permite:

* Obtener datos del perfil de un usuario
* Extraer seguidores (followers)
* Extraer seguidos (following)
* Exportar resultados a CSV
* Modo avanzado (deep scrape) para enriquecer datos

---

## 🚀 Tecnologías utilizadas

* Python 3.10+
* requests
* python-dotenv

---

## ⚙️ Instalación

1. Clonar repositorio:

```bash
git clone https://github.com/guayasnayeli/instagram-scraper.git
cd instagram-scraper
```

2. Crear entorno virtual:

```bash
python -m venv venv
```

3. Activar entorno:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuración

Crear archivo `.env` en la raíz del proyecto:

```env
INSTAGRAM_SESSIONID=tu_sessionid_aqui
TARGET_USER=usuario_default
LIMIT=5
```

---

## ▶️ Uso

Ejecutar el programa:

```bash
python src/main.py
```

Luego el sistema solicitará:

* Usuario a analizar (puedes presionar Enter para usar el default)
* Tipo de extracción:

  * 1 → Followers
  * 2 → Following
  * 3 → Ambos
* Cantidad de resultados (número o `all`)
* Activar modo avanzado (y/n)

---

## 🧠 Funcionalidades

### 🔹 Datos del usuario

* ID
* Username
* Nombre completo
* Biografía
* Cantidad de seguidores
* Cantidad de seguidos

---

### 🔹 Relaciones

* Lista de seguidores
* Lista de seguidos
* Control de límite
* Paginación automática

---

### 🔹 Modo avanzado (Deep Scrape)

Permite obtener información adicional de cada usuario:

* Bio
* Número de seguidores
* Número de seguidos

Incluye un pequeño delay entre requests para evitar bloqueos.

---

### 🔹 Exportación

* Exporta resultados a archivos CSV
* Los archivos se guardan en la carpeta `/outputs`
* Incluyen timestamp automático

---

## 📁 Estructura del proyecto

```plaintext
src/
 ├── config/
 │    └── settings.py
 │
 ├── session/
 │    └── session_manager.py
 │
 ├── scraper/
 │    ├── user_scraper.py
 │    ├── relationships_scraper.py
 │    └── user_details_scraper.py
 │
 ├── export/
 │    └── exporter.py
 │
 └── main.py
```

---

## ⚠️ Notas importantes

* Es necesario contar con un `sessionid` válido de Instagram
* Instagram puede bloquear solicitudes si detecta uso excesivo
* Se recomienda:

  * usar límites bajos
  * activar delays
  * no abusar del modo deep

---

## 🚧 Mejoras futuras

* Interfaz gráfica (GUI)
* Exportación a JSON / Excel
* Análisis de seguidores (engagement)
* Dashboard visual

---

## 👨‍💻 Autor

Proyecto académico - Arquitectura de Software
Desarrollado por: Guayas Nayeli

## Ejecución

python src/main.py

## Resultados

Se guardan en:
outputs/

Ejemplo incluido:
outputs/example_analysis.txt