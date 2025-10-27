Feature: Buscar una pelicula en imdb y validar el titulo de la pelicula y el rating
    Scenario: validar el titulo de la pelicula y el rating
        Given el usuario esta en el home page de lmdb
        When el usuario busca la palicula "Inception"
        And presiona el primer resultado
        Then el titulo de la pelicual debe ser "Origen" y el rating debe ser "8,8"