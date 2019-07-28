PROJECT_NAME = 'hackathon'

SECRET_KEY = 'SUPERSECRET111'

DEBUG = True

ALLOWED_HOSTS = ['derter.asuscomm.com', '127.0.0.1', '192.168.1.207']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/work/projects/' + PROJECT_NAME + '/app'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                #'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hackathon',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }
}

SILENCED_SYSTEM_CHECKS = [
    'django_mysql.W002',
]

STATIC_ROOT = '/work/projects/'+PROJECT_NAME+'/static/'
MEDIA_ROOT = '/work/projects/'+PROJECT_NAME+'/media/'
STATICFILES_DIRS = ('/work/projects/hackathon/app/assets/', '/work/projects/hackathon/app/frontend/dist/')

