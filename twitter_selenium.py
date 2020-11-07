import time
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests

username = input("Enter Twitter Username :")
password = input("Enter Twitter Password :")

#Chrome webdriver path - C:\Users\viki\AppData\Local\Programs\Python\Python36\misc\chromedriver.exe
path=input("Enter Selenium Chrome Driver path :")

session = requests.Session()

paramsGet = {"include_profile_interstitial_type":"1","ext":"mediaStats,highlightedLabel","include_cards":"1","include_followed_by":"1","include_mute_edge":"1","include_blocked_by":"1","count":"20","include_want_retweets":"1","include_reply_count":"1","send_error_codes":"true","include_ext_media_color":"true","include_ext_alt_text":"true","include_can_dm":"1","include_quote_count":"true","tweet_mode":"extended","skip_status":"1","cards_platform":"Web-12","include_can_media_tag":"1","include_ext_media_availability":"true","include_user_entities":"true","include_entities":"true","include_blocking":"1","simple_quoted_tweet":"true"}

headers = {"x-twitter-auth-type":"OAuth2Session","x-twitter-client-language":"en","Accept":"*/*","x-twitter-active-user":"yes","Connection":"close","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36","authorization":"X","x-csrf-token":"X","Referer":"https://twitter.com/i/bookmarks","Sec-Fetch-Site":"same-origin","Sec-Fetch-Dest":"empty","Accept-Encoding":"gzip, deflate","Sec-Fetch-Mode":"cors","Accept-Language":"en-US,en;q=0.9", "Cookie":"X"}

options=Options()
options.headless=True #Toggle headless
options.add_argument('--disable-gpu')
options.add_argument('log-level=3')

browser = webdriver.Chrome(path,chrome_options=options)

browser.get("https://twitter.com/login")
time.sleep(5)
usernameInput=browser.find_element_by_name("session[username_or_email]")
time.sleep(3)
passwordInput=browser.find_element_by_name("session[password]")
usernameInput.send_keys(username)
time.sleep(2)
passwordInput.send_keys(password)
time.sleep(2)
passwordInput.send_keys(Keys.ENTER)
time.sleep(10)

#bookmarks = browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[5]/div/div''')
#bookmarks.click()

for request in browser.requests:
    if('json' in request.url):
        print(request.url,
            request.response.status_code,)
        print(request.headers)
        selenium_header = request.headers

headers["authorization"] = selenium_header["authorization"]
headers["x-csrf-token"] = selenium_header["x-csrf-token"]

print("Cookies :",browser.get_cookies())

headers["Cookie"] = selenium_header['Cookie']
browser.close()
print("GET Headers :",headers)
response = session.get("https://twitter.com/i/api/2/timeline/bookmark.json", params=paramsGet, headers=headers)

print("Status code:   %i" % response.status_code)
print("Response body: %s" % response.content)


