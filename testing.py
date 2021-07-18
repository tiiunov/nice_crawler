from crawler import Crawler


url = 'https://courses.insma.urfu.ru/oop/java_oop_2_java_cs/'
crawler = Crawler(url, 25)
crawler.crawl()
