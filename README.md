# Herramientas de calificación de Calidad de Conjuntos

Esta herramienta se implementa en dos faces:
 1. Implementacion de script de calificacion en validadora.
 2. Implementación de plugin CKAN.

# Implementación Validadora

Para la instalación en validadora el script **calificacion.clj** se debe copiar directamente
en el projecto dentro del path `src/dora/p/`.

# Implementación de plugin CKAN

El plugin funciona bajo la version [2.5.2](http://docs.ckan.org/en/ckan-2.5.2/contents.html) de [CKAN](http://ckan.org/).
Para instalar el plugin se deben correr los siguientes comandos bajos el src/ de la instalación de CKAN.

```
  pip install -e git+https://github.com/opintel/CKAN_Calidad.git#egg=ckanext-mxopeness&subdirectory=ckanext-mxopeness
```

Dentro del archivo de configuracion agregar el plugin despues de los demas instalados.

```
ckan.plugins = ... mxopeness
```

Despues se reinicia el server de aplicación.
