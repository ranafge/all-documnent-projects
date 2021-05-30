from splinter import Browser
browser = Browser('chrome')
browser.visit('https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced')

hem1=browser.find_link_by_partial_text('Sample')
first_element = hem1[0]
print(first_element['href'])

