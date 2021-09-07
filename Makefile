venv:
	rm -f venv -R
	python3 -m venv venv
	venv/bin/pip3 install scrapy==1.6.0

crawl-brand:
	rm -f  modeles.json
	venv/bin/scrapy crawl marques -o modeles.json

crawl-models:
	rm -f modeles -r
	mkdir -p modeles
	venv/bin/python3 main.py
