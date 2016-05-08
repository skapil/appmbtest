def wifi_off():
    subprocess32.call(['adb', 'shell', 'am start -n io.appium.settings/.Settings -e wifi off'])


def wifi_on():
    subprocess32.call(['adb', 'shell', 'am start -n io.appium.settings/.Settings -e wifi on'])
