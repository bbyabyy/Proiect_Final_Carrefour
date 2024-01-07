from behave import *


@then('Home page: The user should be redirected to login page')
def step_impl(context):
    context.home_page.redirect_on_login_page()


@given('Login page: The user is on login page')
def step_impl(context):
    context.base_page.skip_current_step()


@when('Login page: The user enters "{username}" on the username field')
def step_impl(context, username):
    context.login_page.enter_any_username(username)


@when('Login page: The user enters "{password}" on the password field')
def step_impl(context, password):
    context.login_page.enter_any_password(password)


@when('Login page: The user clicks on login button')
def step_impl(context):
    context.login_page.click_on_login_button()