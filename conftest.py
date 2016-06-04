from random import randint
import time
import pytest
import subprocess32
import config
import setup
import tests_app_android

__author__ = 'sandesh'

@pytest.fixture(scope="function")
def suiteSetup(request):
    print 'in suite setup'
    print request.param
    config.udid = request.param
    config.port = str(randint(4000,5000))

@pytest.fixture(scope="function")
def appiumSetup(request):
    print 'in appium setup'
    setup.start_appium_session()
    time.sleep(5)
    request.addfinalizer(setup.stop_appium_session)

@pytest.fixture(scope="function")
def moduleSetup():
    print 'in module setup'
    setup.setup_appium_driver(app=config.app)
    tests_app_android.get_package_name()

@pytest.fixture(scope="function")
def testSetup(request):
    print 'im test setyp'
    tests_app_android.bringAppToForeground()
    time.sleep(5)
    request.addfinalizer(tests_app_android.bringAppToBackground)