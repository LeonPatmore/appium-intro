# Appium Intro

Intended to be a simple introduction to Appium in Python, with some good examples.

## Requirements

- Appium

- Android SDK

- Android Emulator

## Setting Android home environment variable

### Windows

`set ANDROID_HOME=C:\Users\Leon\AppData\Local\Android\Sdk`

## Setting up a device

You need to set up a viable emulator or device to run the test on, connected via Android ADB
[see more](https://developer.android.com/studio/command-line/adb)

### Emulator

## Running Tests

1. Start Appium `appium`.

2. Run `pipenv run python -m pytest`

### Environment Variables

- `MESSENGER_EMAIL`:

## Start UI Automator

UI Automator is included in Android SDK tools. This can be used to get the element IDs of an app.

1. `C:\Users\Leon\AppData\Local\Android\Sdk\tools\bin\uiautomatorviewer.bat`
