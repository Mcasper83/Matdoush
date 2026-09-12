[app]
title = Matdoush
package.name = matdoush
package.domain = org.matdoush
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 24
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
android.sdk_path = /usr/local/lib/android/sdk
android.skip_update = True

[buildozer]
log_level = 2
warn_on_root = 1
