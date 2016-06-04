import pytest
import subprocess32
import config
import conftest
import setup, time
import tests_app_android


@pytest.mark.parametrize("suiteSetup", ['emulator-5554', '04b2aec1251fafbb'], indirect=True)
def test_app_is_installed(suiteSetup, appiumSetup, moduleSetup, testSetup):
    print 'in test app installed'
    print 'driver'
    print config.appium_driver
    print 'udid'
    print config.udid
    # config.udid = udid
    # print 'udid'
    # print udid
    # setup.setup_appium_driver(app=config.app)
    # time.sleep(5)
    # tests_app_android.bringAppToForeground()
    print 'driver1 test'
    # app_package = subprocess32.check_output(['adb', '-s', 'emulator-5554', 'shell', 'pm list packages', '|', 'grep', config.app_package])
    # assert app_package, 'app is not installed, %s not found' % config.app_package
    print 'driver2 test'
    app_package = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'pm list packages', '|', 'grep', config.app_package])
    assert app_package, 'app is not installed, %s not found' % config.app_package

@pytest.mark.last
def test_app_is_uninstalled(appiumSetup, moduleSetup, testSetup):
    print 'in test app uninstalled'
    #setup.setup_appium_driver(app=config.app)
    # time.sleep(5)
    subprocess32.call(['adb', 'uninstall', config.app_package])
    app_package = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'pm list packages', '|', 'grep', config.app_package])
    assert not app_package, 'app is not uninstalled, %s not found' % config.app_package

def test_app_not_running_in_background(appiumSetup, moduleSetup, testSetup):
    print 'in test app background'
    # setup.setup_appium_driver(app=config.app)
    # time.sleep(5)
    # tests_app_android.get_package_name()
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'input', 'keyevent', 'KEYCODE_HOME'])
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'am', 'kill', config.app_package])
    app_process = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'ps', '|', 'grep', config.app_package])
    assert not app_process, 'app is running in background, process = %s' % app_process
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'monkey','-p', config.app_package, '-c', 'android.intent.category.LAUNCHER 1'])
    time.sleep(2)
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)

def test_app_force_stop(appiumSetup, moduleSetup, testSetup):
    print 'in test app force stop'
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'am', 'force-stop', config.app_package])
    app_process = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'ps', '|', 'grep', config.app_package])
    assert not app_process, 'app is not forced stopped, process = %s' % app_process
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'monkey','-p', config.app_package, '-c', 'android.intent.category.LAUNCHER 1'])
    config.appium_driver.background_app(5)
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)

#@pytest.mark.first
def test_reboot(appiumSetup, moduleSetup, testSetup):
    print 'in test reboot'
    subprocess32.call(['adb', 'reboot'])
    time.sleep(120)
    # conftest.testSetup()
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    print 'app'
    print focused_app
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)

def test_wifi_on_off(appiumSetup, moduleSetup, testSetup):
    print 'in test app wifi'
    tests_app_android.wifi_off()
    time.sleep(5)
    tests_app_android.wifi_on()
    time.sleep(5)
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)

def test_app_launch_wifi_off(appiumSetup, moduleSetup, testSetup):
    print 'in test app launch wifi off'
    tests_app_android.bringAppToBackground()
    tests_app_android.wifi_off()
    time.sleep(5)
    tests_app_android.bringAppToForeground()
    tests_app_android.wifi_on()
    time.sleep(5)
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)

def test_bluetooth_on_off(appiumSetup, moduleSetup, testSetup):
    print 'in test bluetooth on off'
    tests_app_android.bluetooth_toggle()
    tests_app_android.bringAppToForeground()
    time.sleep(2)
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)
    tests_app_android.bluetooth_toggle()
    tests_app_android.bringAppToForeground()
    time.sleep(2)
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)


def test_airplane_mode_on_off(appiumSetup, moduleSetup, testSetup):
    print 'in test airplane off'
    tests_app_android.airplane_mode_on()
    time.sleep(5)
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)
    tests_app_android.bringAppToBackground()
    tests_app_android.airplane_mode_off()
    tests_app_android.bringAppToForeground()
    time.sleep(5)
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)


def test_call(appiumSetup, moduleSetup, testSetup):
    print 'in test call'
    tests_app_android.makeCall()
    time.sleep(10)
    tests_app_android.bringAppToForeground()
    time.sleep(5)
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)


def test_message(appiumSetup, moduleSetup, testSetup):
    print 'in test message'
    tests_app_android.sendMessage()
    time.sleep(5)
    tests_app_android.bringAppToForeground()
    time.sleep(5)
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)


def test_email(appiumSetup, moduleSetup, testSetup):
    print 'in test email'
    tests_app_android.sendEmail()
    time.sleep(5)
    tests_app_android.bringAppToForeground()
    time.sleep(5)
    focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
    assert config.app_package in focused_app, 'app package %s, not found in %s' % (config.app_package, focused_app)


@pytest.mark.parametrize("suiteSetup", ['04b2aec1251fafbb'], indirect=True)
def test_meminfo(suiteSetup, appiumSetup, moduleSetup, testSetup):
    print 'in test mem info'
    mem_info = tests_app_android.get_mem_info()
    print 'mem Info'
    print mem_info
    assert mem_info, 'mem info is empty, %s' % mem_info
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'am', 'force-stop', config.app_package])
    mem_info = tests_app_android.get_mem_info()
    print 'mem Info after force stop'
    print mem_info
    assert 'No process found for' in mem_info, 'mem info is not empty, %s' % mem_info


@pytest.mark.parametrize("suiteSetup", ['04b2aec1251fafbb'], indirect=True)
def test_cpuinfo(suiteSetup, appiumSetup, moduleSetup, testSetup):
    print 'in test cpu info'
    cpu_info = tests_app_android.get_cpu_info()
    print 'mem Info'
    print cpu_info
    assert cpu_info, 'cpu info is empty, %s' % cpu_info
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'am', 'force-stop', config.app_package])
    time.sleep(5)
    cpu_info = tests_app_android.get_cpu_info()
    print 'cpu Info after force stop'
    print cpu_info
    assert not cpu_info, 'cpu info is not empty, %s' % cpu_info