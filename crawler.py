from networking import Networking
from save import save
from _collections import deque
import sys
import argparse


class Crawler:
    def __init__(self, start_url, max_limit=10):
        self.max = max_limit
        self.allowable_amount = max_limit
        self.start_url = start_url
        self.save_queue = deque()
        self.visited = []
        self.links_graph = {}

    def crawl(self, curl=None):
        nt = Networking()
        cur_url = curl
        if cur_url is None:
            cur_url = self.start_url
        text = nt.get_beautiful_html_text(cur_url)
        title = nt.get_title(text)
        if title is None:
            title = nt.get_bad_title(cur_url)
        save(text, title)
        self.visited.append(cur_url)
        for link in nt.get_links(cur_url):
            if cur_url not in self.links_graph:
                self.links_graph[cur_url] = []
            self.links_graph[cur_url].append(link)
            if link not in self.visited:
                self.save_queue.append(link)
        self.allowable_amount -= 1
        count = self.max - self.allowable_amount
        print(f"\rСкачано {count} из {self.max}  {cur_url} ...", end=' ')
        if self.allowable_amount < 1:
            print("Загрузка завершена.")
            return
        next_url = self.save_queue.popleft()
        self.crawl(next_url)

    def reboot(self):
        self.allowable_amount = self.max
        self.save_queue = deque()
        self.visited = []

    def save_links_graph(self):
        result = ""
        for key in self.links_graph:
            result += f"***{key}***\n"
            for link in self.links_graph[key]:
                result += f"- {link} -\n"
        with open("links_graph.txt", 'w', encoding="utf-8") as f:
            f.write(result)


def create_parser():
    pars = argparse.ArgumentParser()
    pars.add_argument('url', type=str)
    pars.add_argument('count', type=int, default=10)
    return pars


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    crawler = Crawler(args.url, args.count)
    crawler.crawl()
    crawler.save_links_graph()
