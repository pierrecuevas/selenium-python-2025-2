Feature: Buscar un artista en last.fm y validar la fecha de su ultimo release
    Scenario: validar la fecha del ultimo release de Drake
        Given el usuario esta en el home page de last fm
        When el usuario busca el artista busca "Drake"
        And presiona el link del primer resultado
        Then la fecha del ultimo release debe ser "25 July 2025"