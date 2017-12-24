from bs4 import BeautifulSoup
import requests

__author__ = 'enzoftware'

url_base = "https://github.com/enzoftware?"
extension = "tab=repositories"
max_pages = 3

counter = 0

for i in range(1, max_pages):
	if i > 1 :
		url = url_base + "page="+ str(i) + "&" + extension
	else:
		url = url_base + extension

	req = requests.get(url)

	status_code = req.status_code

	if status_code == 200 :
		html = BeautifulSoup(req.text,"html.parser")
		entradas = html.find_all('li',{'itemprop':'owns'})
		for i, entrada in enumerate(entradas):
			repo_name = entrada.find('a',{'itemprop':'name codeRepository'}).getText()
			descripcion = entrada.find('p',{'itemprop':'description'})
			language = entrada.find('span',{'itemprop':'programmingLanguage'})

			if (descripcion == None):
				descripcion = 'Empty'
			else :
				descripcion = descripcion.getText()


			if(language == None):
				language = 'Empty'
			else:
				language = language.getText()

			counter += 1
			print(	counter,
					repo_name,
					descripcion,
					language)

	else:
		break
