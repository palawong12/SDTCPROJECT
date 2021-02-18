from django.apps import AppConfig


class HellomobileappConfig(AppConfig):
    name = 'hellomobileapp'
    
    def ready(self):
    	import base.signals
