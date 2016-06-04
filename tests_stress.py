import subprocess32
import config
import time
import tests_app_android


def test_other_apps_in_background(appiumSetup, moduleSetup, testSetup):
    tests_app_android.get_all_packages()
    for i in config.all_packages:
        print i
        subprocess32.call(['adb', '-s', config.udid, 'shell', 'monkey','-p', i, '-c', 'android.intent.category.LAUNCHER 1'])
        time.sleep(5)
        app_process = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'ps', '|', 'grep', config.app_package])
        assert app_process, 'app is not running in background, process = %s' % app_process
        tests_app_android.bringAppToForeground()
        time.sleep(2)
        focused_app = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys window windows', '|', 'grep', '-E', 'mCurrentFocus'])
        assert config.app_package in focused_app, 'app package %s, not found in %s after %s' % (config.app_package, focused_app, i)


def test_monkey(appiumSetup, moduleSetup, testSetup):
        temp = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'monkey', '-p', config.app_package, '--throttle 1000', '-v 50'])
        assert temp