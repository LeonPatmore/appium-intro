# Appium Intro

Intended to be a simple introduction to Appium in Python, with some good examples. All examples are using Android apps.

## Requirements

- Appium

- Android SDK

- Android Emulator

## Setting Android home environment variable

### Windows

`set ANDROID_HOME=C:\Users\Leon\AppData\Local\Android\Sdk`

## Setting up a device

You need to set up a viable emulator or device to run the test on, connected via Android ADB
[(see more)](https://developer.android.com/studio/command-line/adb).

### Emulator

You can use Android studio to setup an emulator, namely using Android Virtual Device Manager. The OS and ABI of the
emulator are very important and must match, for example:

```python
'platformName': 'Android',
'platformVersion': '9.0',
'deviceName': 'Android Emulator',
```

The above should have a matching emulator with regards to OS, OS version and ABI.

### ABIs

For Android, different phones have different CPUs, and as a result they support different instruction sets.
Each different CPU requires a different ABI (Application Binary Interface), and APKs are built with varying
levels of compatibilities with regard to the ABIs.

As a result, you should ensure that the APK you are using is compatible with the ABI of the emulator you are running.

## Running Tests

1. Start Appium `appium`.

2. Run `pipenv run python -m pytest`

### Environment Variables

None

## Start UI Automator

UI Automator is included in Android SDK tools. This can be used to get the element IDs of an app.

1. `C:\Users\Leon\AppData\Local\Android\Sdk\tools\bin\uiautomatorviewer.bat`
