# Bulk-Certificate-Generator
This [Python](https://www.python.org/) project aims to generate bulk certificates and personalize them using a template and a database that contains, by way of example, names, courses and dates.

## Inputs

### *Database*

> *Input/participants.xlsx*

Let's assume that we've finished teaching a coding bootcamp. In this way, we get data on the students, the courses in which they enrolled and the dates they finished the bootcamp.

<img src="https://github.com/dwn10/django-web/blob/main/PYTHON/readme-img/cert-1.JPG?raw=true" width="400">

### *Certificate template*

> *Input/certificate_template.pdf*

To avoid the laborious task of creating a template from scratch with Python, we found a way to use any template you want.

<img src="https://user-images.githubusercontent.com/64377961/213355641-b332e55f-29e1-4b73-adb8-9f42be1e6914.png" width="500">

## Output

> *Certificates/.pdf*

After running the [code](https://github.com/dwn10/django-web/blob/main/PYTHON/Certificates_Generator/generate_certificates.ipynb) -in which the font, position, size and color of the variables (name, course, date) to be added to the [certificate template](https://github.com/dwn10/django-web/blob/main/PYTHON/Certificates_Generator/Input/certificate_template.pdf) are customized-, personalized certificates will be stored in the [Certificates](https://github.com/dwn10/django-web/blob/main/PYTHON/Certificates_Generator/Certificates/Lulia_S._certificate.pdf) folder. In our case, this is an example of generated certificate.

<img src="https://github.com/dwn10/django-web/blob/main/PYTHON/readme-img/cert-2.JPG?raw=true" width="500">

