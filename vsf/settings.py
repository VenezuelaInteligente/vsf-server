"""
Django settings for vsf project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import local_settings
from os.path import join

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = local_settings.BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = local_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = local_settings.DEBUG

ALLOWED_HOSTS = local_settings.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = local_settings.INSTALLED_APPS

MIDDLEWARE = local_settings.MIDDLEWARE

ROOT_URLCONF = local_settings.ROOT_URLCONF

TEMPLATES = local_settings.TEMPLATES

WSGI_APPLICATION = local_settings.WSGI_APPLICATION

# SSL secure

SECURE_SSL_REDIRECT = local_settings.SECURE_SSL_REDIRECT
SESSION_COOKIE_SECURE = local_settings.SESSION_COOKIE_SECURE
CSRF_COOKIE_SECURE = local_settings.CSRF_COOKIE_SECURE


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = local_settings.DATABASES

DATABASE_ROUTERS = local_settings.DATABASE_ROUTERS


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = local_settings.AUTH_PASSWORD_VALIDATORS


REST_FRAMEWORK = local_settings.REST_FRAMEWORK


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = local_settings.LANGUAGE_CODE

TIME_ZONE = local_settings.TIME_ZONE

USE_I18N = local_settings.USE_I18N

USE_L10N = local_settings.USE_L10N

USE_TZ = local_settings.USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = local_settings.STATIC_ROOT

STATIC_URL = local_settings.STATIC_URL

STATICFILES_DIRS = local_settings.STATICFILES_DIRS

MEDIA_ROOT = local_settings.MEDIA_ROOT

MEDIA_URL = local_settings.MEDIA_URL

# Login redirect url

LOGIN_URL = local_settings.LOGIN_URL
LOGIN_REDIRECT_URL = local_settings.LOGIN_REDIRECT_URL

INTERNAL_IPS = local_settings.INTERNAL_IPS
DEBUG_TOOLBAR_CONFIG = local_settings.DEBUG_TOOLBAR_CONFIG

EMAIL_BACKEND = local_settings.EMAIL_BACKEND
EMAIL_USE_TLS = local_settings.EMAIL_USE_TLS
EMAIL_HOST = local_settings.EMAIL_HOST
EMAIL_PORT = local_settings.EMAIL_PORT
EMAIL_HOST_USER = local_settings.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = local_settings.EMAIL_HOST_PASSWORD

# Django-modeltranslate setup.
LANGUAGES = local_settings.LANGUAGES

MODELTRANSLATION_DEFAULT_LANGUAGE = local_settings.MODELTRANSLATION_DEFAULT_LANGUAGE

# VSF plugin function
FLAG_TESTS = local_settings.FLAG_TESTS

LOGGING = local_settings.LOGGING
