search query string by default is "search"  

you can customize to different string : 
  
      # instead using search, we can use query
      query=search_data
      
rootproject/settings.py


      INSTALLED_APPS = [
          ...
          'rest_framework',
          'school',
          'django_filters',
      ]

      REST_FRAMEWORK = {
          'SEARCH_PARAM'='q',
          'DEFAULT_FILTER_BACKENDS':[
              'django_filters.rest_framework.DjangoFilterBackend'
          ]
      }
