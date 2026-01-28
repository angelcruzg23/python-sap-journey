# -*- coding: utf-8 -*-
"""
Sistema de Gestión de Recetas - Versión Funcional Senior
Autor: Angel Cruz (Versión mejorada)
Fecha: Enero 2025

Características:
- Manejo robusto de errores
- Type hints completos
- Docstrings profesionales
- Código limpio y mantenible
- Cross-platform compatible
"""

import os
import sys
from pathlib import Path
from typing import List, Optional, Tuple


# ============================================================================
# UTILIDADES GENERALES
# ============================================================================

def limpiar_pantalla() -> None:
    """Limpia la pantalla de forma multiplataforma"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar() -> None:
    """Pausa la ejecución esperando input del usuario"""
    input('\n📌 Presiona ENTER para continuar...')


def mostrar_titulo(titulo: str) -> None:
    """
    Muestra un título formateado
    
    Args:
        titulo: Texto del título a mostrar
    """
    ancho = 60
    print('\n' + '=' * ancho)
    print(f'{titulo:^{ancho}}')
    print('=' * ancho + '\n')


def validar_opcion(mensaje: str, opciones_validas: List[str]) -> str:
    """
    Solicita y valida una opción del usuario
    
    Args:
        mensaje: Mensaje a mostrar al usuario
        opciones_validas: Lista de opciones válidas
        
    Returns:
        str: Opción válida seleccionada
    """
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print(f"❌ Opción inválida. Opciones válidas: {', '.join(opciones_validas)}")


# ============================================================================
# FUNCIONES DE NEGOCIO - INFORMACIÓN
# ============================================================================

def obtener_ruta_base() -> Path:
    """
    Obtiene la ruta base del recetario
    
    Returns:
        Path: Ruta base del recetario
    """
    return Path(__file__).parent / 'Recetas'


def asegurar_directorio_existe(ruta: Path) -> None:
    """
    Asegura que el directorio existe, lo crea si no
    
    Args:
        ruta: Ruta del directorio a verificar/crear
    """
    if not ruta.exists():
        ruta.mkdir(parents=True, exist_ok=True)
        print(f"📁 Directorio creado: {ruta}")


def contar_recetas(ruta_base: Path) -> int:
    """
    Cuenta el total de recetas en todas las categorías
    
    Args:
        ruta_base: Ruta base del recetario
        
    Returns:
        int: Número total de archivos .txt
    """
    return sum(1 for _ in ruta_base.rglob('*.txt'))


def obtener_categorias(ruta_base: Path) -> List[Path]:
    """
    Obtiene lista de categorías (subdirectorios)
    
    Args:
        ruta_base: Ruta base del recetario
        
    Returns:
        List[Path]: Lista de rutas a categorías
    """
    return [
        item for item in ruta_base.iterdir() 
        if item.is_dir() and not item.name.startswith('.')
    ]


def obtener_recetas(ruta_categoria: Path) -> List[Path]:
    """
    Obtiene lista de recetas en una categoría
    
    Args:
        ruta_categoria: Ruta de la categoría
        
    Returns:
        List[Path]: Lista de rutas a archivos de recetas
    """
    return list(ruta_categoria.glob('*.txt'))


# ============================================================================
# FUNCIONES DE NEGOCIO - SELECCIÓN
# ============================================================================

def seleccionar_categoria(ruta_base: Path) -> Optional[Path]:
    """
    Permite al usuario seleccionar una categoría
    
    Args:
        ruta_base: Ruta base del recetario
        
    Returns:
        Optional[Path]: Ruta de la categoría seleccionada o None si cancela
    """
    limpiar_pantalla()
    mostrar_titulo('SELECCIONAR CATEGORÍA')
    
    categorias = obtener_categorias(ruta_base)
    
    if not categorias:
        print("⚠️  No hay categorías disponibles.")
        print("💡 Crea una categoría primero (Opción 3 en el menú principal)")
        pausar()
        return None
    
    # Mostrar opciones
    for i, categoria in enumerate(categorias, 1):
        print(f"  {i}. 📁 {categoria.name}")
    print(f"  0. ⬅️  Cancelar")
    
    # Validar selección
    opciones_validas = [str(i) for i in range(len(categorias) + 1)]
    opcion = validar_opcion('\n➡️  Selecciona una opción: ', opciones_validas)
    
    if opcion == '0':
        return None
    
    return categorias[int(opcion) - 1]


def seleccionar_receta(ruta_categoria: Path) -> Optional[Path]:
    """
    Permite al usuario seleccionar una receta
    
    Args:
        ruta_categoria: Ruta de la categoría
        
    Returns:
        Optional[Path]: Ruta de la receta seleccionada o None si cancela
    """
    limpiar_pantalla()
    mostrar_titulo(f'RECETAS EN: {ruta_categoria.name}')
    
    recetas = obtener_recetas(ruta_categoria)
    
    if not recetas:
        print("⚠️  No hay recetas en esta categoría.")
        print("💡 Crea una receta primero (Opción 2 en el menú principal)")
        pausar()
        return None
    
    # Mostrar opciones
    for i, receta in enumerate(recetas, 1):
        print(f"  {i}. 📄 {receta.stem}")
    print(f"  0. ⬅️  Cancelar")
    
    # Validar selección
    opciones_validas = [str(i) for i in range(len(recetas) + 1)]
    opcion = validar_opcion('\n➡️  Selecciona una receta: ', opciones_validas)
    
    if opcion == '0':
        return None
    
    return recetas[int(opcion) - 1]


# ============================================================================
# FUNCIONES DE NEGOCIO - OPERACIONES CRUD
# ============================================================================

def leer_receta(ruta_base: Path) -> None:
    """
    Lee y muestra el contenido de una receta
    
    Args:
        ruta_base: Ruta base del recetario
    """
    categoria = seleccionar_categoria(ruta_base)
    if not categoria:
        return
    
    receta = seleccionar_receta(categoria)
    if not receta:
        return
    
    limpiar_pantalla()
    mostrar_titulo(f'RECETA: {receta.stem}')
    
    try:
        with open(receta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            
            if contenido.strip():
                print(contenido)
            else:
                print("⚠️  Esta receta está vacía.")
    
    except FileNotFoundError:
        print(f"❌ Error: Archivo no encontrado: {receta}")
    except PermissionError:
        print(f"❌ Error: Sin permisos para leer: {receta}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    
    pausar()


def crear_receta(ruta_base: Path) -> None:
    """
    Crea una nueva receta en una categoría
    
    Args:
        ruta_base: Ruta base del recetario
    """
    categoria = seleccionar_categoria(ruta_base)
    if not categoria:
        return
    
    limpiar_pantalla()
    mostrar_titulo('CREAR NUEVA RECETA')
    
    # Solicitar nombre
    while True:
        nombre = input('📝 Nombre de la receta: ').strip()
        if nombre:
            # Limpiar nombre de archivo
            nombre_archivo = "".join(
                c for c in nombre if c.isalnum() or c in (' ', '-', '_')
            ).strip()
            if nombre_archivo:
                break
        print("❌ Nombre inválido. Intenta de nuevo.")
    
    # Verificar si ya existe
    ruta_receta = categoria / f"{nombre_archivo}.txt"
    if ruta_receta.exists():
        respuesta = input(f"⚠️  La receta '{nombre_archivo}' ya existe. ¿Sobrescribir? (s/n): ")
        if respuesta.lower() != 's':
            print("❌ Operación cancelada.")
            pausar()
            return
    
    # Solicitar contenido
    print('\n📄 Contenido de la receta (presiona ENTER dos veces para finalizar):')
    lineas = []
    lineas_vacias = 0
    
    while lineas_vacias < 2:
        linea = input()
        if linea.strip():
            lineas.append(linea)
            lineas_vacias = 0
        else:
            lineas_vacias += 1
    
    contenido = '\n'.join(lineas)
    
    # Guardar receta
    try:
        with open(ruta_receta, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
        
        print(f"\n✅ Receta '{nombre_archivo}' creada exitosamente!")
        print(f"📁 Ubicación: {ruta_receta}")
    
    except PermissionError:
        print(f"❌ Error: Sin permisos para crear archivo en: {categoria}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    
    pausar()


def crear_categoria(ruta_base: Path) -> None:
    """
    Crea una nueva categoría
    
    Args:
        ruta_base: Ruta base del recetario
    """
    limpiar_pantalla()
    mostrar_titulo('CREAR NUEVA CATEGORÍA')
    
    # Solicitar nombre
    while True:
        nombre = input('📁 Nombre de la categoría: ').strip()
        if nombre:
            # Limpiar nombre de carpeta
            nombre_carpeta = "".join(
                c for c in nombre if c.isalnum() or c in (' ', '-', '_')
            ).strip()
            if nombre_carpeta:
                break
        print("❌ Nombre inválido. Intenta de nuevo.")
    
    ruta_categoria = ruta_base / nombre_carpeta
    
    # Verificar si ya existe
    if ruta_categoria.exists():
        print(f"⚠️  La categoría '{nombre_carpeta}' ya existe.")
        pausar()
        return
    
    # Crear categoría
    try:
        ruta_categoria.mkdir(parents=True, exist_ok=True)
        print(f"\n✅ Categoría '{nombre_carpeta}' creada exitosamente!")
        print(f"📁 Ubicación: {ruta_categoria}")
    
    except PermissionError:
        print(f"❌ Error: Sin permisos para crear carpeta en: {ruta_base}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    
    pausar()


def eliminar_receta(ruta_base: Path) -> None:
    """
    Elimina una receta existente
    
    Args:
        ruta_base: Ruta base del recetario
    """
    categoria = seleccionar_categoria(ruta_base)
    if not categoria:
        return
    
    receta = seleccionar_receta(categoria)
    if not receta:
        return
    
    # Confirmar eliminación
    limpiar_pantalla()
    print(f"⚠️  ¿Estás seguro de eliminar la receta '{receta.stem}'?")
    confirmacion = input("Escribe 'ELIMINAR' para confirmar: ")
    
    if confirmacion != 'ELIMINAR':
        print("❌ Operación cancelada.")
        pausar()
        return
    
    # Eliminar
    try:
        receta.unlink()
        print(f"\n✅ Receta '{receta.stem}' eliminada exitosamente!")
    
    except FileNotFoundError:
        print(f"❌ Error: Archivo no encontrado: {receta}")
    except PermissionError:
        print(f"❌ Error: Sin permisos para eliminar: {receta}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    
    pausar()


def eliminar_categoria(ruta_base: Path) -> None:
    """
    Elimina una categoría (solo si está vacía)
    
    Args:
        ruta_base: Ruta base del recetario
    """
    categoria = seleccionar_categoria(ruta_base)
    if not categoria:
        return
    
    # Verificar si tiene recetas
    recetas = obtener_recetas(categoria)
    if recetas:
        print(f"\n⚠️  La categoría '{categoria.name}' contiene {len(recetas)} receta(s).")
        print("💡 Elimina todas las recetas primero.")
        pausar()
        return
    
    # Confirmar eliminación
    limpiar_pantalla()
    print(f"⚠️  ¿Estás seguro de eliminar la categoría '{categoria.name}'?")
    confirmacion = input("Escribe 'ELIMINAR' para confirmar: ")
    
    if confirmacion != 'ELIMINAR':
        print("❌ Operación cancelada.")
        pausar()
        return
    
    # Eliminar
    try:
        categoria.rmdir()
        print(f"\n✅ Categoría '{categoria.name}' eliminada exitosamente!")
    
    except OSError as e:
        if e.errno == 66:  # Directory not empty (macOS)
            print(f"❌ Error: La categoría no está vacía")
        else:
            print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    
    pausar()


# ============================================================================
# INTERFAZ DE USUARIO
# ============================================================================

def mostrar_bienvenida(ruta_base: Path) -> None:
    """
    Muestra mensaje de bienvenida y estadísticas
    
    Args:
        ruta_base: Ruta base del recetario
    """
    limpiar_pantalla()
    
    print('\n' + '=' * 60)
    print('🍳  BIENVENIDO AL RECETARIO PY9  🍳'.center(60))
    print('=' * 60)
    
    nombre = input('\n👤 ¿Cómo te llamas?: ').strip()
    if nombre:
        print(f'\n¡Hola {nombre}! 👋')
    
    # Asegurar que existe el directorio
    asegurar_directorio_existe(ruta_base)
    
    # Mostrar estadísticas
    num_categorias = len(obtener_categorias(ruta_base))
    num_recetas = contar_recetas(ruta_base)
    
    print(f'\n📊 Estadísticas:')
    print(f'   📁 Categorías: {num_categorias}')
    print(f'   📄 Recetas: {num_recetas}')
    print(f'   📂 Ubicación: {ruta_base.absolute()}')
    
    pausar()


def mostrar_menu() -> str:
    """
    Muestra el menú principal y retorna la opción elegida
    
    Returns:
        str: Opción seleccionada por el usuario
    """
    limpiar_pantalla()
    mostrar_titulo('MENÚ PRINCIPAL')
    
    opciones = {
        '1': '📖 Leer Receta',
        '2': '➕ Crear Receta',
        '3': '📁 Crear Categoría',
        '4': '🗑️  Eliminar Receta',
        '5': '🗂️  Eliminar Categoría',
        '6': '🚪 Salir'
    }
    
    for num, texto in opciones.items():
        print(f'  {num}. {texto}')
    
    print()
    return validar_opcion('➡️  Selecciona una opción: ', list(opciones.keys()))


def ejecutar_aplicacion() -> None:
    """Función principal que ejecuta la aplicación"""
    ruta_base = obtener_ruta_base()
    
    # Bienvenida
    mostrar_bienvenida(ruta_base)
    
    # Loop principal
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            leer_receta(ruta_base)
        elif opcion == '2':
            crear_receta(ruta_base)
        elif opcion == '3':
            crear_categoria(ruta_base)
        elif opcion == '4':
            eliminar_receta(ruta_base)
        elif opcion == '5':
            eliminar_categoria(ruta_base)
        elif opcion == '6':
            limpiar_pantalla()
            print('\n👋 ¡Gracias por usar el Recetario PY9!')
            print('🍳 ¡Que disfrutes cocinando!\n')
            break


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == '__main__':
    try:
        ejecutar_aplicacion()
    except KeyboardInterrupt:
        print('\n\n❌ Programa interrumpido por el usuario.')
        sys.exit(0)
    except Exception as e:
        print(f'\n❌ Error crítico: {e}')
        sys.exit(1)