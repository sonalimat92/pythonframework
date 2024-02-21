from behave import *
from base.testbase import Testbase
from selenium import webdriver

from config.configreader import ConfigFileReader
from database.databaseconnection import DBLoader
from logs import loggerhelper

log=loggerhelper.get_logs()

use_step_matcher("re")


@when("I hover on bags")
def step_impl(context):
    Testbase.get_webdriver()
    Testbase.get_webdriver()
    log.info("Chrome launched")

    config_reader = ConfigFileReader.get_config_file_reader()
    url=config_reader.get_url()
    wait=config_reader.get_wait()
    db_loader = DBLoader()
    db_loader.return_values_from_db()

    Testbase.load_url(url)
    Testbase.close_driver()


@then("Select hand bags")
def step_impl(context):
    print("hi")


@given("Open Chrome and Launch the URL")
def step_impl(context):
    print("hi")


@when("I hover on tote bags")
def step_impl(context):
  print("hi")