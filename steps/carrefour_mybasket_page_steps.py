from behave import *


@when('My basket page: The user clicks on My basket')
def step_impl(context):
    context.home_page.click_on_my_basket()


@when('My basket page: The user clicks on remove product from the cart button')
def step_impl(context):
    context.mybasket.click_on_remove_button()


@then('My basket page: The user received a message that the basket is empty')
def step_impl(context):
    context.mybasket.the_product_is_removed()