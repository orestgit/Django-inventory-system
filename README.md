# python3-django-inventory
An inventory management system, based on buckets you can place items in

# Install Guide
**Requirements (Global Installations)**
 - Python3
 - NGINX
 - python3-django
 - python3-django-crispy-forms
 - uwsgi
 - uwsgi-plugin-python3
 
 **Install Steps**

 **Django**
 1. Create a new User and login as User
	 - `adduser inventory`*
	 - `su - inventory`*
 2. Create Django-Project
	 - `django-admin startproject website`*
	 - `cd website`*
  3. Get python3-django-inventory
	  - `git clone https://github.com/ChaosRambo/python3-django-inventory.git inventory`
	4. Configure Django
		-  `vim website/settings.py`*
		- Add to `INSTALLED_APPS`:
			- `'inventory',`
			- `'crispy_forms',`
		- Add to the end of the Settings:
			- STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
	5. Migrate
		- `./manage.py --migrate`
	 6. Optional Step
		 - Test Django
			 - `./manage.py --runserver`  
			 - You will see the Django Test site
			 - ![enter image description here](https://github.com/ChaosRambo/python3-django-inventory/blob/master/screenshots/django_testpage.jpeg?raw=true)
	 7. Add URL Config
		 - `vim website/urls.py`
		 - Add if not exists:
			 - `from django.conf.urls import url, include`
		 - Add in `urlpatterns`
			 - `url(r'^', include('inventory.urls', namespace='inventory')),`
	  8.  Collectstatics
		  - `./manage.py --collectstatics` 
	  9. Optional Step
		 - Test Django
			 - `./manage.py runserver`
			 - You will see an empty inventory
			 - ![enter image description here](https://github.com/ChaosRambo/python3-django-inventory/blob/master/screenshots/empty_inventory.jpeg?raw=true)
	 10. Add Admin
		 - `./manage.py createsuperuser` 
		11. Close User
			- `exit`

**uWSGI**
	 
1. Optional Step - Try if uWSGI correct work
	-  `uwsgi --master --http :5000  --chdir /home/inventory/website --module website.wsgi:application`
	- Don't worry, if you open the site in your browser, you won't see any static stuff
2. Write Systemd Service
	- Download the Service file with the following line:
	- `wget https://raw.githubusercontent.com/ChaosRambo/python3-django-inventory/master/documents/uwsgi.service -P /etc/systemd/system`
	- Optional: DIY
		- Write your own `uwsgi.service` in
		- `/etc/systemd/system/`
		- You will find more examples here:
			- http://uwsgi-docs.readthedocs.io/en/latest/Systemd.html
3. Write uWSGI config
	- Create folder `sites`  in:
		- `/etc/uwsgi`
	- Download inventory.ini:
		- `wget https://raw.githubusercontent.com/ChaosRambo/python3-django-inventory/master/documents/inventory.ini -P /etc/uwsgi/sites`
	- Optional: DIY
		- Write your own config in `sites`
		- You will find more examples here:
			- http://uwsgi-docs.readthedocs.io/en/latest/Configuration.html
4. Systemd
	- `systemctl enable uwsgi.service`
	- `systemctl start uwsgi.service` 

**NGINX**

1. Write NGINX Config
	- Download this config
		- `wget https://raw.githubusercontent.com/ChaosRambo/python3-django-inventory/master/documents/nginxconf -O inventory -P /etc/nginx/sites-available`
		- `ln -s /etc/nginx/sites-available/inventory /etc/nginx/sites-enabled/`
	- Optional: DIY
		- Write your Own Nginx config and create a Softlink to `sites-enabled`
		- Yor will find more examples here:
		- http://nginx.org/en/docs/
	

