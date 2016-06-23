import config
import splinter
import time

def open_district_browser(district):
    """
    visit the district webpage
    :param dustrict: string of the district name (in hebrew)
    :return: the district browser webpage
    """
    browser = splinter.Browser()
    browser.visit('http://www.madlan.co.il/local/%D7%9B%D7%9C%20%D7%94%D7%90%D7%A8%D7%A5') # all districts page
    browser.click_link_by_partial_text("מחוזות")
    browser.click_link_by_partial_text("מחוז תל אביב")
    browser.click_link_by_partial_text("ישובים")
    return browser

def open_city_browser(city_link):
    """

    :param city_link: from list
    :return:
    """
    pass

def open_neighborhood_browser(neighborhood_link):
    pass

def parse_neighborhood_prices_data(neighborhood_browser):
    pass

def parse_neighborhood_social_data(neighborhood_browser):
    pass

def get_neighborhood_data(neighborhood_browser):
    pass

def get_district_cities_links(district_browser):
    pass

def get_city_neighborhoods_links(city_browser):
    pass


def main_scrapping():
    params = config.Params()
    district_browser = open_district_browser(params.district)
    # loop over cities and neighborhoods and extract data
