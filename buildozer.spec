[app]
title = Matdoush
package.name = matdoush
package.domain = org.matdoush
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 24
android.archs = arm64-v8a,armeabi-v7a
