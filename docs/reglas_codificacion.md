# Cinco reglas de codificación del equipo

1. Seguir PEP 8; nombres de funciones y variables en snake_case y en español.
2. Toda función pública lleva docstring y anotaciones de tipo.
3. Nada de números mágicos: porcentajes y tarifas van en constantes con nombre.
4. Las entradas inválidas se rechazan con excepciones explícitas (ValueError), nunca se ignoran.
5. Ningún cambio se integra sin prueba unitaria asociada y sin revisión en un pull request.
