import os
import sys
from daphne.cli import CommandLineInterface

# #* Définir les variables d'environnement GDAL
# os.environ['GDAL_LIBRARY_PATH'] = r'C:\Users\Lenovo\Desktop\WEBsite\fire_detection_web\.site\Lib\site-packages\osgeo\gdal.dll'
# os.environ['PATH'] += os.pathsep + r'C:\Users\Lenovo\Desktop\WEBsite\fire_detection_web\.site\Lib\site-packages\osgeo'

#* Définir la variable d'environnement pour les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


#* Initialiser Django avant d'importer d'autres modules
import django
django.setup()

#* Passer les arguments de la ligne de commande à Daphne
sys.argv = ["daphne", "-p", "8000", "project.asgi:application"]
CommandLineInterface.entrypoint()
