from selenium import webdriver


class Crawler:

    def __init__(self):
        self.url = 'http://view.websudoku.com/?level=4'
        self.driver = webdriver.Chrome("C:\\Users\\Will\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get(self.url)

        self.html_board = self.get_html_board()

    def get_html_board(self):
        puzzle_grid = self.driver.find_element_by_xpath("//table[@id='puzzle_grid']/tbody")
        html_board = []
        for rows in puzzle_grid.find_elements_by_xpath("tr"):
            html_board.append(rows.find_elements_by_xpath("td/input"))
        return html_board

    def parse_html_boar(self):
        readable_board = []
        for row in self.html_board:
            cur_row = []
            for cell in row:
                cell_val = cell.get_attribute("value")
                if cell_val:
                    cur_row.append(int(cell_val))
                else:
                    cur_row.append(0)
            readable_board.append(cur_row)
        return readable_board

