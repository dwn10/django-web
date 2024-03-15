import requests # python3 -m pip install requests beautifulsoup4
from bs4 import BeautifulSoup

# Modifica la URL y el término de búsqueda
url = "https://www.arbeitsagentur.de/m/stelle/suche?q=anwendungsentwickler"
search_term = "Anwendungsentwickler"

# Realiza la petición y analiza el HTML
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Encuentra ofertas de trabajo (reemplaza 'data-sb' con el selector correcto)
results = soup.find_all("div", attrs={"data-sb": True})  # Cambia el selector

# Extrae y muestra información de cada oferta
for job in results:
    try:
        # Extrae título, empresa y enlace (modifica los selectores según la estructura HTML)
        title_element = job.find("h2", class_="job-title")  # Cambia el selector
        title = title_element.get_text().strip() if title_element else "N/A"

        company_element = job.find("span", class_="job-company")  # Cambia el selector
        company = company_element.get_text().strip() if company_element else "N/A"

        job_link = "https://www.arbeitsagentur.de" + job["data-href"]  # Modifica la forma de obtener el enlace

        # Agrega una sección para salario (si la información está disponible)
        salary_element = job.find("span", class_="job-salary")  # Cambia el selector
        salary = salary_element.get_text().strip() if salary_element else "N/A"

        # Da formato y muestra la información
        job_info = f"Titel: {title}\nUnternehmen: {company}\nOrt: {job['data-city']}\nLink: {job_link}\nGehalt: {salary}"
        print(job_info)

    except Exception as e:
        print("Error:", e)
        pass