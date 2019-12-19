from Crawler import Crawler
import Solver

if __name__ == '__main__':
    crawler = Crawler(2)
    html = crawler.get_html_board()
    readable = crawler.get_readable_board()
    Solver.solver(html, readable)

