[app]

title = Chirry Love

package.name = chirrylove

package.domain = com.timothy

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

source.include_patterns = assets/*

version = 1.0

requirements = python3,kivy==2.3.0,Pillow

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2


[android]

android.api = 35

android.minapi = 23

android.ndk = 25b

android.accept_sdk_license = True

android.archs = arm64-v8a, armeabi-v7a