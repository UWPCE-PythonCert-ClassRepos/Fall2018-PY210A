#standard waiting and date imports
import time
from datetime import date

#main selenium import
from selenium import webdriver

#other items needed - Please ignore these for now and I'll talk about them as they come up
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait

#very useful for knowing the HTML Layout - I don't use it in the execution of the code though
from bs4 import BeautifulSoup


#Global variables, website to look at as well as how many hotness games to look through
MAIN_PAGE = 'https://boardgamegeek.com/'
COUNT_OF_GAMES = 5

#Create a webdriver instance
driver = webdriver.Firefox()
driver.get(MAIN_PAGE)

#find element locates a specific HTML object
#find elementS locates all of the HTML objects matching the criteria
hot_games = driver.find_elements_by_xpath("//*[@class='moduletable hotitems']//*[starts-with(@href, '/boardgame')]")

# for game in hot_games:
#     print(game.get_attribute('href'))

hot_games_URLs = []

# for game in hot_games: #Stale!
#     driver.get(game.get_attribute('href'))

for game in hot_games:
    COUNT_OF_GAMES -= 1
    hot_games_URLs.append(game.get_attribute('href'))
    if COUNT_OF_GAMES <= 0:
        break

print('Log in now')
time.sleep(15) #time to log in

for game_URL in hot_games_URLs:
    driver.get(game_URL)

    Wait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@class='game-header']")))

    rating = driver.find_element_by_xpath("//*[@ng-show='showRating']").text
    best_player_count = driver.find_element_by_xpath("//*[@ng-show='::geekitemctrl.geekitem.data.item.polls.userplayers.totalvotes > 0']").text[-1:]
    weight = driver.find_element_by_xpath("//*[starts-with(@class, 'gameplay-weight-')]").text
    print('rating: ', rating, 'players: ', best_player_count, 'weight: ', weight)
    time.sleep(5)
    try:
        if float(rating) > 7 and int(best_player_count) > 3 and float(weight) < 3.5:
            driver.find_element_by_xpath("//*[@class='toolbar-actions']//*[starts-with(@class, 'btn btn-sm btn-primary toolbar-action-full')]").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//input[@ng-model='item.status.wanttoplay']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//textarea[@id='comment']").send_keys('Hotness List: ' + str(date.today())) # Send Keys, Can do Keys.TAB, Keys.ESC
            time.sleep(5)
            save_button = driver.find_elements_by_xpath("//*[@class='switch-slide switch-primary']//button[@type='submit']")[1]
            ActionChains(driver).move_to_element(save_button).click().perform() #Action Chains - double click, click and hold, Shift+Tab
            time.sleep(2)
    except ValueError:
        print("No Ratings Yet!")
        continue