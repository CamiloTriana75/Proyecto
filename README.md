# 🐍 Juego de la Culebrita

Este es un sencillo juego de la culebrita creado con **Python** y la biblioteca **Turtle**. El objetivo del juego es controlar la culebra, comer la comida que aparece en la pantalla y evitar chocar con las paredes o con tu propio cuerpo.

## 📋 Requisitos

Para ejecutar este juego, necesitas tener instalado lo siguiente:

- **Python 3.x**
- **Turtle** (suele venir preinstalado con Python, pero puedes instalarlo ejecutando `pip install PythonTurtle`)

## 🚀 Cómo Jugar

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd tu-repositorio
    ```
3. Ejecuta el script principal:
    ```bash
    python culebrita.py
    ```

### Controles 🎮

- **Arriba:** Tecla de flecha "Arriba"
- **Abajo:** Tecla de flecha "Abajo"
- **Izquierda:** Tecla de flecha "Izquierda"
- **Derecha:** Tecla de flecha "Derecha"

## 📝 Funcionalidades

- **Puntaje:** Se muestra en la parte superior de la pantalla y se actualiza a medida que comes más comida.
- **Registro de Puntaje Más Alto:** El juego guarda y muestra el puntaje más alto alcanzado durante la sesión actual.
- **Crecimiento de la Serpiente:** La culebra crece en tamaño cada vez que come la comida.
- **Colisiones:** El juego termina si la culebra choca contra las paredes o contra su propio cuerpo.

## 🛠️ Desarrollo

El código base incluye las funcionalidades principales para jugar. A continuación, algunas áreas que podrías mejorar o expandir:

- **Pantalla de Inicio:** Actualmente se ha iniciado un diseño básico para una pantalla de inicio utilizando `Tkinter`.
- **Mejoras Visuales:** Se pueden agregar más efectos visuales, sonidos, o un sistema de menús.
- **Guardar Puntaje Más Alto:** Implementar la persistencia de datos para mantener el puntaje más alto incluso después de cerrar el juego.

## 🚧 Errores Conocidos

- Al chocar con el cuerpo de la serpiente, a veces el juego no se reinicia correctamente. Puedes solucionar esto depurando la dirección de la cabeza al reiniciar.
