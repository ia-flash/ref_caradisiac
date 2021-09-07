from ref_caradisiac.spiders.caradisiac import RefModeleSpider, RefMarqueSpider
from scrapy.crawler import CrawlerProcess
import re, io, json, os, time

os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'ref_caradisiac.settings')  #add path to scrapy settings to the project
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

def remove(filename):
    if os.path.exists(filename):
        os.remove(filename)

BASE_DIR = './'

f = open('modeles.json')
data = json.load(f)
f.close()

#print(data)


process = CrawlerProcess(settings)

for item in data:
    print (item['href'])
    marque = re.search('(?<=\/auto--)(.*)(?=\/)', item['href'])
    if marque:
        marque= marque.group(1)
    else :
        continue
    marque = marque.split('/modeles')[0]

    if marque is not None:
        json_path = os.path.join(BASE_DIR, 'modeles', '%s.json'%marque)

        process.settings.set('FEED_URI',json_path)
        print(10*'*')
        print(marque)
        print(10*'*')

        remove('%s.json'%marque)
        remove(json_path)

        process.crawl(RefModeleSpider,marque=marque)
        #time.sleep(3)
    #process.stop()
process.start() # the script will block here until the crawling is finished
