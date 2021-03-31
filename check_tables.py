from selenium import webdriver
from driver_creation import SeleniumLibraryExt
from selenium.webdriver.chrome.options import Options


class WebTables:

    def __init__(self):
        self.dict = None
        self.dict2 = None
    
    def search(self, search_value):
        self.driver = SeleniumLibraryExt.create_driver()
        search_box = self.driver.find_element_by_xpath("//input[@id='searchBox']")
        search_box.click()
        search_box.send_keys(search_value)

    def retrieve_rows_per_page(self):
        self.driver = SeleniumLibraryExt.create_driver()
        values_dict = dict()
        values = self.driver.find_elements_by_xpath("//option")
        for elem in values:
            nr_rows = int(elem.get_attribute('value'))
            header = elem.text
            values_dict[nr_rows] = f"//option[text()='{header}']"
        self.dict = values_dict

    def select_rows_per_page(self, nr_rows):
        self.driver = SeleniumLibraryExt.create_driver()
        for key in self.dict:
            if nr_rows == key:
                self.driver.find_element_by_xpath(self.dict[key]).click()
                break

    def retrieve_data(self):
        self.driver = SeleniumLibraryExt.create_driver()
        columns = self.driver.find_elements_by_xpath("//div[@class='rt-resizable-header-content']")
        column_names = list()
        data = list()
        for i in range(len(columns) - 1):
            column_name = columns[i].text
            column_names.append(column_name)
        rows = self.driver.find_elements_by_xpath("//div[contains(@class,'rt-tr ')]")
        for elem in rows:
            if elem.get_attribute('class') != "rt-tr -padRow -odd" and elem.get_attribute('class') != "rt-tr -padRow " \
                                                                                                      "-even":
                cell = elem.find_elements_by_tag_name("div")
                my_dict = {}
                for i in range(len(cell) - 2):
                    cell_value = cell[i].text
                    my_dict[column_names[i]] = cell_value
                data.append(my_dict)
        print(data)

    def click_add(self):
        self.driver = SeleniumLibraryExt.create_driver()
        self.driver.find_element_by_xpath("//button[@id='addNewRecordButton']").click()
        labels_webelements = self.driver.find_elements_by_xpath("//form[@id='userForm']//label")
        labels = list()
        dict_value = dict()
        xpaths = list()
        for elem in labels_webelements:
            labels.append(elem.text)
        textboxes = self.driver.find_elements_by_xpath("//form[@id='userForm']//input")
        for elem in textboxes:
            id = elem.get_attribute('id')
            xpath = f"//form[@id='userForm']//input[@id='{id}']"
            xpaths.append(xpath)
        for i in range(len(labels)):
            dict_value[labels[i]] = xpaths[i]
        self.dict2 = dict_value

    def insert_data(self, values):
        self.driver = SeleniumLibraryExt.create_driver()
        for key in values:
            if key in self.dict2:
                text_box = self.driver.find_element_by_xpath(self.dict2[key])
                text_box.clear()
                text_box.send_keys(values[key])
        self.driver.find_element_by_xpath("//button[@id='submit']").click()