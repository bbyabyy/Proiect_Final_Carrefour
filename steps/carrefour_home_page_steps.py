from behave import *


@given('Home page: The user is on https://www.carrefour.ro/')
def step_impl(context):
    context.home_page.navigate_to_homepage()
    context.home_page.delete_all_cookies()


@when('Home page: The user search for "{product_name}" in search box')
def step_impl(context, product_name):
    context.home_page.insert_search_value(product_name)
    context.home_page.click_search_button()


@then('Home Page: The user have at least "{results_number}" results returned')
def step_impl(context, results_number):
    context.home_page.check_search_results(results_number)


@when('Home Page: The user type in search box "{cafea boabe}"')
def step_impl(context, cafea_boabe):
    context.home_page.insert_the_search_value(cafea_boabe)


@when('Home page: The user clicks the search button')
def step_impl(context):
    context.home_page.click_search_button()


@when('Home page: The user navigate to first returned product page')
def step_impl(context):
    context.home_page.navigate_to_first_product_returned()


@when('Home page: The user clicks on add to basket product')
def step_impl(context):
    context.home_page.add_to_bascket_product()


@when('Home page: The user should receive a confirmation that the product has been added to basket')
def step_impl(context):
    context.home_page.message_receved()


@when('Home page: I click on careers link')
def step_impl(context):
    context.home_page.click_on_carers_link()


@when('Home page: The user clicks on account button')
def step_impl(context):
    context.home_page.click_on_login_link()


@then('Home page: The user should be redirected to login page')
def step_impl(context):
    context.home_page.redirect_on_login_page()



