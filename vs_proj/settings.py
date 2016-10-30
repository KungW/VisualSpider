#coding:utf-8
"""
Django settings for find_mentor_proj project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#-&5y4z-9p$b)#!^bn5qh%ova+xl5zed97+x48t5_uw-q&)=gl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','visualspider.applinzi.com','45.32.113.65']


SESSION_COOKIE_AGE = 10*600

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'scholar',
    'gunicorn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'vs_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vs_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# 修改上传时文件在内存中可以存放的最大size为10m
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760
# sae的本地文件系统是只读的，修改django的file storage backend为Storage
DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'
# 使用findmentor这个bucket
STORAGE_BUCKET_NAME = 'visualspider'
# ref: https://docs.djangoproject.com/en/dev/topics/files/


if 'SERVER_SOFTWARE' in os.environ:
    #直接访问外网
    DOMAIN = 'visualspider.applinzi.com'
    DB_HOST = 'w.rdc.sae.sina.com.cn'
    DB_PORT = 3307
    DB_USER = '3w0nx1ozoy'
    DB_PASS = 'ih1hmhzki3kh12yikm1214kmwkwkkwwjjixjy450'
    DB_DB = 'app_visualspider'
    UEDITOR_UPLOAD = {
        'BACKEND':'DjangoUeditor.saebackend',
        'DOMAIN':'visualspider',
    }
else:
    #在本地测试
    local_db = True
    DOMAIN = 'http://localhost:8000'
    CACHES_BACKEND = 'django.core.cache.backends.memcached.MemcachedCache'
    if local_db:
        #使用本地数据库
        DB_HOST = None#'10.8.3.97'
        DB_PORT = 5432
        DB_USER = 'lyn'
        DB_PASS = 'tonylu716'
        DB_DB = 'sf_development'
    else:
        #使用sae远程数据库
        from sae._restful_mysql import monkey
        monkey.patch()
        DOMAIN = 'visualspider.applinzi.com'
        DB_HOST = 'w.rdc.sae.sina.com.cn'
        DB_PORT = 3307
        DB_USER = '3w0nx1ozoy'
        DB_PASS = 'ih1hmhzki3kh12yikm1214kmwkwkkwwjjixjy450'
        DB_DB = 'app_visualspider'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_DB,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
        os.path.join(BASE_DIR,'static'),
)
