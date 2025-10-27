from behave import given, when, then
from selenium import webdriver
from pages.lastfn_home_page import LastfmHomePage
from pages.lastfn_results_page import LastfmResultsPage
from pages.lastfn_artist_page import LastfmArtistPage

@given('el usuario esta en el home page de last fm')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.last.fm/")
    context.lastfm_home = LastfmHomePage(context.driver)

@when('el usuario busca el artista busca "{artist_name}"')
def step_search_page(context, artist_name):
    context.lastfm_home.search_artist(artist_name)
    context.lastfm_results = LastfmResultsPage(context.driver)

@when('presiona el link del primer resultado')
def step_press_first_result(context):
    context.lastfm_results.press_link()
    context.lastfm_artist = LastfmArtistPage(context.driver)


@then('la fecha del ultimo release debe ser "{expected_date}"')
def step_impl(context, expected_date):
    actual_date = context.lastfm_artist.get_latest_release_date()
    assert actual_date == expected_date, f"Expected date {expected_date}, but got {actual_date}"
    context.driver.quit()