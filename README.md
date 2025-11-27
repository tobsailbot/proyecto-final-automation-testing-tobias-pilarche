
# 🧪 Proyecto Final - Framework de Automatización de Pruebas - Tobias Pilarche

Este repositorio contiene el Trabajo Final Integrador del curso de Testing QA. Se trata de un framework de automatización robusto y escalable desarrollado en Python, diseñado para validar tanto interfaces de usuario (UI) como interfaces de programación de aplicaciones (API).

## 🎯 Propósito del Proyecto

El objetivo principal es demostrar la aplicación de conocimientos avanzados de automatización mediante la creación de un framework que incluye:

1.  **Pruebas de UI (End-to-End):** Automatización de flujos críticos de compra en el sitio *SauceDemo* (Login, Inventario, Carrito) utilizando **Selenium WebDriver**.
2.  **Pruebas de API:** Validación de códigos de estado y estructura de datos en endpoints REST de *JSONPlaceholder* utilizando **Requests**.
3.  **Patrones de Diseño:** Implementación del patrón **Page Object Model (POM)** para garantizar un código mantenible, modular y fácil de leer.
4.  **Reportes:** Generación automática de evidencia visual (reportes HTML y capturas de pantalla) para facilitar el análisis de resultados.

## 🛠 Tecnologías Utilizadas

*   **Lenguaje:** [Python 3.x](https://www.python.org/)
*   **Orquestador de Pruebas:** [Pytest](https://docs.pytest.org/) (Manejo de fixtures, aserciones y ejecución).
*   **Automatización Web:** [Selenium WebDriver](https://www.selenium.dev/).
*   **Gestión de Drivers:** [Webdriver Manager](https://pypi.org/project/webdriver-manager/) (Descarga automática de ChromeDriver/GeckoDriver).
*   **Automatización de API:** [Requests](https://pypi.org/project/requests/).
*   **Reportes:** [Pytest-HTML](https://pypi.org/project/pytest-html/).

## 📂 Estructura del Proyecto

La organización de carpetas sigue las mejores prácticas de la industria:

```text
proyecto_final/
├── pages/                  # Page Object Model (Lógica de las páginas web)
│   ├── base_page.py        # Métodos genéricos (Wrapper de Selenium)
│   ├── login_page.py       # Acciones de la página de Login
│   └── inventory_page.py   # Acciones del inventario y carrito
├── tests/                  # Scripts de prueba
│   ├── ui/                 # Tests de Interfaz (Selenium)
│   └── api/                # Tests de Backend (Requests)
├── data/                   # Datos de prueba externos (JSON/CSV)
├── reports/                # Aquí se generan los Reportes HTML y Screenshots
├── venv/                   # Entorno virtual (no se sube al repo)
├── conftest.py             # Configuración global (Hooks, Setup del Driver)
├── pytest.ini              # Configuración de ejecución y logs
├── requirements.txt        # Lista de dependencias del proyecto
└── README.md               # Documentación del proyecto
```

## ⚙️ ¿Cómo instalar las dependencias?

Seguir estos pasos para configurar el entorno en tu máquina local (Linux/Mac/Windows).

**1. Clonar el repositorio:**
```bash
git clone <URL_DEL_REPOSITORIO>
cd proyecto-final-automation
```

**2. Crear el Entorno Virtual:**
*En Linux/Debian:*
```bash
python3 -m venv venv
source venv/bin/activate
```
*En Windows:*
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Instalar librerías:**
Una vez activo el entorno (verás `(venv)` en la terminal), ejecuta:
```bash
pip install -r requirements.txt
```
*(Nota: Esto instalará Selenium, Pytest, Requests y todas las herramientas necesarias).*

## 🚀 ¿Cómo ejecutar las pruebas?

Gracias a la configuración en `pytest.ini`, el comando es muy sencillo. Asegúrate de tener el entorno virtual activado.

**Ejecutar TODAS las pruebas (UI + API):**
```bash
python3 -m pytest
```

## 📊 ¿Cómo interpretar los reportes generados?

Al finalizar la ejecución, se generará automáticamente un archivo en la carpeta `reports/`:

1.  Abre el archivo **`reports/reporte_final.html`** en tu navegador (Chrome/Firefox).
2.  **Verde (Passed):** El test pasó exitosamente. Haz clic en la fila para ver el **Log detallado** (pasos realizados).
3.  **Rojo (Failed):** El test falló. Al expandirlo encontrarás:
    *   **Error Log:** La razón técnica del fallo.
    *   **Screenshot:** Una captura de pantalla automática del momento exacto del error (fundamental para debugging).

---
**Autor:** Tobias Pilarche
**Fecha:** Noviembre 2025
```

---