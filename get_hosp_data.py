from selenium import webdriver
import time
import csv

driver = webdriver.PhantomJS()


def get_data(url):
    driver.get(url)
    time.sleep(5)
    elements = driver.find_elements_by_css_selector('.hospitals_score')
    grade = driver.find_element_by_css_selector('.d-col1')
    grade_att = grade.get_attribute('data-grade')
    lat = driver.find_element_by_css_selector('.d-col1')
    lat_att = lat.get_attribute('data-lat')
    lon = driver.find_element_by_css_selector('.d-col1')
    lon_att = lon.get_attribute('data-lon')
    address = driver.find_element_by_css_selector('.d-add')
    address_text = address.text
    txt_list = []
    txt_list.extend([grade_att, address_text, lat_att, lon_att])
    for element in elements:
        txt_list.append(element.text)
    return txt_list


def open_state_file(file):
    all_data = []
    s = open('url_data/' + file + '.csv')
    url_list = csv.reader(s)
    for line in url_list:
        data_result = get_data(line[1])
        line = line + data_result
        all_data.append(line)
    return all_data

states = ["AL", "AK", "AZ", "AR", "CA", "CO",
          "CT", "DC", "DE", "FL", "GA", "HI",
          "ID", "IL", "IN", "IA", "KS", "KY",
          "LA", "ME", "MD", "MA", "MI", "MN",
          "MS", "MO", "MT", "NE", "NV", "NH",
          "NJ", "NM", "NY", "NC", "ND", "OH",
          "OK", "OR", "PA", "RI", "SC", "SD",
          "TN", "TX", "UT", "VT", "VA", "WA",
          "WV", "WI", "WY"]

for state in states:
    with open('hosp_data/' + state + "_data.csv", "wb") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(open_state_file(state))

driver.close()
