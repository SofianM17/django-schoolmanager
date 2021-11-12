SETUP:

	1. To start a django project:

		django-admin startproject <project_name>

	2. Make migrations inside project directory:
	
		python manage.py migrate

	3. Make superuser for admin page

		python manage.py createsuperuser

		SUPERUSER INFO:
		Sofian
		Sofianmustafa17@gmail.com
		12345

	4. Create the app

		python manage.py startapp <app_name>

	5. Update settings.py in the project dir
	
		Under INSTALLED_APPS, add:
		
			'rest_framework',
			'<app_name>',

	6. Update urls.py in the project dir
		from django.urls import include
		in urlpatterns, add path('', include('<app_name>.urls'))
	
	7. Create urls.py in the app folder 
		Copy everything from the urls.py file from the project directory but remove admins

CREATE MODELS:
	
	1. Create a class for a model (table) in models.py

	2. Migrate the model

		python manage.py makemigrations
		python manage.py migrate
	
	3. Register the model in admin.py to see it on the admin dashboard
		from .models import <model_name>
		admin.site.register(<model_name>)

SERIALIZATION: A serializer translates to/from JSON
	
	1. Create a new file serializers.py

	2. from .models import <model_name>
	
	3. class <model_name>Serializer(serializers.ModelSerializer):
		class Meta:
		Model = <model_name>
		fields = ('<model_fields>')
	

