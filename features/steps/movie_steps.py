from selenium import webdriver
from behave import given, when, then
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_results_page import ImdbResultsPage
from pages.imdb_movie_page import ImdbMoviePage


@given('el usuario esta en el home page de lmdb')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")
    context.imdb_home = ImdbHomePage(context.driver)

@when('el usuario busca la palicula "{movie_name}"')
def step_search_page(context, movie_name):
    context.imdb_home.search_movie(movie_name)
    context.imdb_results = ImdbResultsPage(context.driver)

@when('presiona el primer resultado')
def step_press_first_result(context):
    context.imdb_results.press_link()
    context.imdb_movie = ImdbMoviePage(context.driver)

@then('el titulo de la pelicual debe ser "{expected_title}" y el rating debe ser "{expected_rating}"')
def step_impl(context, expected_title, expected_rating):
    actual_title = context.imdb_movie.get_movie_title()
    actual_rating = context.imdb_movie.get_movie_rating()
    assert actual_title == expected_title, f"Expected title {expected_title}, but got {actual_title}"
    assert actual_rating == expected_rating, f"Expected rating {expected_rating}, but got {actual_rating}"
    context.driver.quit()
