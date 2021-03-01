from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

from parser.settings import (
    link_to_site,
    next_page_xpath,
    for_links_selector,
    with_link_selector,
    link_attribute,
    title_selector,
    rating_selector,
    rating_attribute,
    track_list_selector,
    link_to_download_selector,
    link_to_download_attribute,
)


class Parser:
    def __init__(self):
        self.__browser = webdriver.Firefox(options=self.__set_options())

    @staticmethod
    def __set_options():
        """return headless options for parser driver"""
        options = Options()
        options.add_argument("--headless")

        return options

    def start_parse(self, count=None):
        self.__open_site()

        info_about_all_albums = []
        for _step in range(count):
            links = self.__get_links()

            info_about_albums = self.__get_info_about_albums(links)
            info_about_all_albums.extend(info_about_albums)

            self.__next_page()

        print(info_about_all_albums)
        return info_about_all_albums

    def __next_page(self):
        self.__browser.find_element_by_xpath(next_page_xpath).click()

    def __open_site(self):
        """open site for parsing"""
        self.__browser.get(link_to_site)

    def __get_links(self):
        elements_for_links = self.__browser.find_elements_by_css_selector(
            for_links_selector
        )

        elements_with_links = []
        for element_for_link in elements_for_links:
            try:
                element_with_link = element_for_link.find_element_by_css_selector(
                    with_link_selector
                )
                elements_with_links.append(element_with_link)
            except NoSuchElementException:
                continue

        links = []
        for element_with_link in elements_with_links:
            link = element_with_link.get_attribute(link_attribute)
            links.append(link)

        return links

    def __get_info_about_albums(self, links):
        info_about_albums = []

        self.__browser.execute_script("window.open('');")
        self.__browser.switch_to.window(self.__browser.window_handles[1])

        for link in links:
            info_about_album = self.__get_info_about_album(link)
            info_about_albums.append(info_about_album)

        self.__browser.close()
        self.__browser.switch_to.window(self.__browser.window_handles[0])

        return info_about_albums

    def __get_info_about_album(self, link):
        self.__browser.get(link)

        info_about_album = {
            "title": self.__browser.find_element_by_css_selector(title_selector).text,
            "rating": self.__browser.find_element_by_css_selector(
                rating_selector
            ).get_attribute(rating_attribute),
            "track_list": self.__browser.find_element_by_css_selector(
                track_list_selector
            ).text,
            "link_to_download": self.__browser.find_element_by_css_selector(
                link_to_download_selector
            ).get_attribute(link_to_download_attribute),
        }

        return info_about_album

    def stop_parse(self):
        self.__browser.quit()
