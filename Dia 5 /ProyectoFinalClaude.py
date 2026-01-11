"""
Juego del Ahorcado - Versión Mejorada
Autor: Angel Cruz
Fecha: Enero 2025
"""

from random import choice
from typing import List, Tuple


class Ahorcado:
    """
    Clase que representa el juego del Ahorcado
    
    Attributes:
        PALABRAS: Lista de palabras disponibles
        MAX_VIDAS: Número máximo de intentos
    """
    
    PALABRAS = ['Buseta', 'Camion', 'Bicicleta', 'Patin', 'Motocicleta', 'Avion']
    MAX_VIDAS = 6
    
    def __init__(self):
        """Inicializa el juego con valores por defecto"""
        self.palabra = self._seleccionar_palabra()
        self.palabra_oculta = ['_'] * len(self.palabra)
        self.vidas = self.MAX_VIDAS
        self.letras_intentadas = set()
        self.letras_correctas = set()
        
    def _seleccionar_palabra(self) -> str:
        """
        Selecciona una palabra aleatoria de la lista
        
        Returns:
            str: Palabra seleccionada en mayúsculas
        """
        return choice(self.PALABRAS).upper()
    
    def _normalizar_letra(self, letra: str) -> str:
        """
        Normaliza la letra ingresada (mayúscula, sin espacios)
        
        Args:
            letra: Letra ingresada por el usuario
            
        Returns:
            str: Letra normalizada
        """
        return letra.strip().upper()
    
    def _validar_entrada(self, letra: str) -> Tuple[bool, str]:
        """
        Valida que la entrada sea correcta
        
        Args:
            letra: Letra a validar
            
        Returns:
            Tuple[bool, str]: (es_valida, mensaje_error)
        """
        if not letra:
            return False, "⚠️  Debes ingresar una letra"
        
        if len(letra) > 1:
            return False, "⚠️  Solo puedes ingresar una letra a la vez"
        
        if not letra.isalpha():
            return False, "⚠️  Solo se permiten letras"
        
        if letra in self.letras_intentadas:
            return False, f"⚠️  Ya intentaste la letra '{letra}'"
        
        return True, ""
    
    def _procesar_intento(self, letra: str) -> bool:
        """
        Procesa el intento del jugador
        
        Args:
            letra: Letra ingresada
            
        Returns:
            bool: True si la letra está en la palabra
        """
        self.letras_intentadas.add(letra)
        
        if letra in self.palabra:
            self.letras_correctas.add(letra)
            # Actualizar todas las posiciones de la letra
            for i, char in enumerate(self.palabra):
                if char == letra:
                    self.palabra_oculta[i] = letra
            return True
        else:
            self.vidas -= 1
            return False
    
    def _mostrar_estado(self):
        """Muestra el estado actual del juego"""
        print("\n" + "="*60)
        print(f"🎮 AHORCADO - Vidas restantes: {'❤️ ' * self.vidas}")
        print("="*60)
        print(f"\n📝 Palabra: {' '.join(self.palabra_oculta)}")
        print(f"📊 Progreso: {len(self.letras_correctas)}/{len(set(self.palabra))} letras encontradas")
        
        if self.letras_intentadas:
            intentadas = sorted(self.letras_intentadas)
            print(f"🔤 Letras intentadas: {', '.join(intentadas)}")
        
        print()
    
    def _dibujar_ahorcado(self):
        """Dibuja el ahorcado según las vidas restantes"""
        estados = [
            # 0 vidas
            """
               ___
              |   |
              |   O
              |  /|\\
              |  / \\
             _|_
            """,
            # 1 vida
            """
               ___
              |   |
              |   O
              |  /|\\
              |  / 
             _|_
            """,
            # 2 vidas
            """
               ___
              |   |
              |   O
              |  /|\\
              |   
             _|_
            """,
            # 3 vidas
            """
               ___
              |   |
              |   O
              |  /|
              |   
             _|_
            """,
            # 4 vidas
            """
               ___
              |   |
              |   O
              |   |
              |   
             _|_
            """,
            # 5 vidas
            """
               ___
              |   |
              |   O
              |   
              |   
             _|_
            """,
            # 6 vidas
            """
               ___
              |   |
              |   
              |   
              |   
             _|_
            """
        ]
        
        print(estados[self.vidas])
    
    def ha_ganado(self) -> bool:
        """
        Verifica si el jugador ha ganado
        
        Returns:
            bool: True si adivinó toda la palabra
        """
        return '_' not in self.palabra_oculta
    
    def ha_perdido(self) -> bool:
        """
        Verifica si el jugador ha perdido
        
        Returns:
            bool: True si se quedó sin vidas
        """
        return self.vidas <= 0
    
    def jugar(self):
        """Loop principal del juego"""
        print("\n🎮 ¡BIENVENIDO AL JUEGO DEL AHORCADO! 🎮\n")
        print(f"Tienes {self.MAX_VIDAS} vidas para adivinar la palabra.")
        print("Cada letra incorrecta te costará una vida.\n")
        input("Presiona ENTER para comenzar...")
        
        while True:
            self._mostrar_estado()
            self._dibujar_ahorcado()
            
            # Verificar condiciones de fin de juego
            if self.ha_ganado():
                print("\n" + "="*60)
                print("🎉 ¡FELICIDADES! ¡HAS GANADO! 🎉")
                print(f"La palabra era: {self.palabra}")
                print(f"Intentos usados: {len(self.letras_intentadas)}")
                print("="*60 + "\n")
                break
            
            if self.ha_perdido():
                print("\n" + "="*60)
                print("💀 GAME OVER 💀")
                print(f"La palabra era: {self.palabra}")
                print("="*60 + "\n")
                break
            
            # Solicitar entrada
            letra = input("➡️  Ingresa una letra: ")
            letra = self._normalizar_letra(letra)
            
            # Validar entrada
            es_valida, mensaje_error = self._validar_entrada(letra)
            if not es_valida:
                print(f"\n{mensaje_error}\n")
                continue
            
            # Procesar intento
            if self._procesar_intento(letra):
                print(f"\n✅ ¡Correcto! La letra '{letra}' está en la palabra.\n")
            else:
                print(f"\n❌ ¡Incorrecto! La letra '{letra}' no está en la palabra.\n")


def jugar_partida():
    """Función principal para iniciar una partida"""
    juego = Ahorcado()
    juego.jugar()
    
    # Preguntar si quiere jugar de nuevo
    while True:
        respuesta = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if respuesta in ['s', 'si', 'sí']:
            print("\n" + "="*60 + "\n")
            juego = Ahorcado()
            juego.jugar()
        elif respuesta in ['n', 'no']:
            print("\n👋 ¡Gracias por jugar! ¡Hasta pronto!\n")
            break
        else:
            print("Por favor, responde 's' o 'n'")


if __name__ == "__main__":
    jugar_partida()