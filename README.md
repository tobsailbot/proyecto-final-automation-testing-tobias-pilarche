# Proyecto Final - Framework de Automatización de Pruebas

## Propósito del Proyecto
Framework de automatización desarrollado en Python y Selenium para validar funcionalidades UI de SauceDemo y API de ReqRes.

## Tecnologías Utilizadas
- **Lenguaje:** Python 3
- **UI Testing:** Selenium WebDriver
- **API Testing:** Requests
- **Test Runner:** Pytest
- **Reporting:** Pytest-html
- **Patrón de Diseño:** Page Object Model (POM)

## Estructura del Proyecto
- `pages/`: Clases POM (Lógica de negocio)
- `tests/`: Scripts de prueba (UI y API)
- `reports/`: Resultados de ejecución y capturas de pantalla

## Instalación
1. Clonar el repositorio.
2. Crear entorno virtual: `python3 -m venv venv`
3. Activar entorno: `source venv/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`

## Ejecución de Pruebas
Para correr todos los tests y generar reporte:
`pytest --html=reports/reporte.html --self-contained-html`