import unittest
from crawler import Crawler


class MyTest(unittest.TestCase):
    def setUp(self):
        url = 'https://courses.insma.urfu.ru/oop/java_oop_2_java_cs/'
        self.crawler = Crawler(url, 10)

    def testNormalInit(self):
        expected_max_limit = 10
        self.assertEqual(expected_max_limit, self.crawler.max)
        self.assertEqual(expected_max_limit, self.crawler.allowable_amount)

    def testReboot(self):
        self.crawler.allowable_amount = 33
        self.crawler.save_queue.append('pipiska')
        self.crawler.visited.append('pipiska')
        self.crawler.reboot()
        self.assertEqual(self.crawler.allowable_amount, self.crawler.max)
        self.assertEqual(len(self.crawler.save_queue), 0)
        self.assertEqual(len(self.crawler.visited), 0)

    def testCrawl(self):
        with open('testpage/page.html', 'r', encoding="utf-8") as f:
            test_content = f.read()
        self.crawler.max = self.crawler.allowable_amount = 1
        self.crawler.crawl()
        path = 'websites/ООП  2 Java C/page.html'
        with open(path, 'r', encoding="utf-8") as f:
            content = f.read()
        self.assertEqual(test_content, content)

    def testHash(self):
        test_hash = 'edbb3d68a849606992d4a889da5768d0'
        self.crawler.max = self.crawler.allowable_amount = 1
        self.crawler.crawl()
        path = 'websites/ООП  2 Java C/hashcode.txt'
        with open(path, 'r', encoding="utf-8") as f:
            hashcode = f.read()
        self.assertEqual(test_hash, hashcode)


if __name__ == '__main__':
    unittest.main()
