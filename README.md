# QA Automatizacion - Vita Wallet

## Descripcion
Este proyecto contiene pruebas automatizadas para la aplicacion **Vita Wallet** usando **Appium + Python**.
Incluye:

- Test de intercambio cripto ARS → USDT.
- Buenas practicas de automatizacion (Page Objects, locators separados).

## Flujos cubiertos
Este proyecto automatiza los siguientes flujos dentro de la aplicación Vita Wallet:
1. **Inicio de sesion**
   - Autenticacion con usuario y contraseña de prueba.

2. **Intercambio cripto ARS → USDT**
   - Seleccion de moneda de origen (ARS) y destino (USDT).
   - Ingreso de monto a intercambiar.
   - Continuar y confirmar el intercambio.

3. **Navegacion al inicio**
   - Regresa a la pantalla principal después de completar un intercambio.

4. **Historial de intercambio**
   - Accede al historial de transacciones cripto.
   - Espera a que el popup de historial esté completamente visible antes de interactuar.


## Requisitos
-Python 3.9+
-Appium
-Android Studio
-Git

## Instrucciones para ejecutar pruebas
## Instalacion
1. Clonar el repositorio:
```bash
git clone <URL_DEL_REPO>
cd <REPO>
```

2. Crear un entorno virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Con el entorno virtual activado, ejecutar los tests con:
```bash
pytest -v
```