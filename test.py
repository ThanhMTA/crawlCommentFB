from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Khởi tạo trình duyệt
driver = webdriver.Chrome()
# Truy cập trang đăng nhập và đăng nhập bằng thông tin tài khoản
driver.get('https://mbasic.facebook.com/')
username_input = driver.find_element(By.ID,"m_login_email")
password_input = driver.find_element(By.NAME,"pass")
login_button = driver.find_element(By.NAME,"login")
username_input.send_keys("sieucute2001@gmail.com")
password_input.send_keys("Phuong21042001@")
login_button.click()
# Lấy tất cả các cookie sau khi đăng nhập thành công
logged_in_cookies = driver.get_cookies()
# Đóng trình duyệt
driver.quit()
# Sử dụng cookie đã lấy để đăng nhập tự động trong phiên sau
driver = webdriver.Chrome()
driver.get("https://mbasic.facebook.com/")
for cookie in logged_in_cookies:
    driver.add_cookie(cookie)
# Refresh trang để sử dụng cookie đã lưu
driver.refresh()
#  lấy ID của các bài viết của một fanpage
def getId(url):
    driver.get(url)
    time.sleep(10)  # Đợi một chút để trang tải xong
    # Scroll xuống để tải thêm bài viết
    scroll_pause_time = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Lấy danh sách các ID bài viết
    post_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/posts")]')
    post_ids = []
    for link in post_links:
        post_url = link.get_attribute("href")
        post_id = post_url.split("/")[-1]  # Lấy phần cuối của URL là ID bài viết
        post_ids.append(post_id)
    for post_id in post_ids:
        url="https://mbasic.facebook.com/toilahs12/posts/"+post_id
        getcomment(url)
def getcomment(url):
    
    driver.get(url)
    scroll_pause_time = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    links = driver.find_elements(By.XPATH,'//a[contains(@href, "/comment/replies/")]')
    if (len(links)):
        for link in links:
            takeLink = link.get_attribute('href').split('ctoken=')[1].split('&')[0]
            textCommentElement = driver.find_element(By.XPATH,'//*[@id="' + takeLink.split('_')[1] + '"]/div/div[1]')
            name = driver.find_element(By.XPATH,'//*[@id="' + takeLink.split('_')[1] + '"]/div/h3/a')
            if (takeLink not in ids):
                file_path='comment.txt'
                ids.append(takeLink)
                with open(file_path, "a", encoding="utf-8") as file:
                     file.write("name:"+ name.text + "\n")
                     file.write("Id:"+name.get_attribute('href')+"\ns" )
                     file.write("comment:"+ textCommentElement.text + "\n") 

    next_button = driver.find_elements(By.XPATH, '//*[contains(@id,"see_next")]/a') 

    if next_button:

        next_button[0].click()

        getcomment(driver.current_url)
    

getcomment('https://mbasic.facebook.com/FcThuyTien/posts/pfbid02svuQKB3wLAmZTw4Natfx3WzWfaYdimk3Vyy1TdvtqLRXXYqxAKZdfhciuYrB3C14l')
# childComment('https://mbasic.facebook.com/comment/replies/?ctoken=876241977201830_3440206542911846&p=-8&count=2&pc=1&ft_ent_identifier=876241977201830&eav=AfZUQhjxftIiNxTNRdhaqq8pHwY-k73jCMhhmwGzwltk9BEm9s0JrJNmmY8lqLylamg&gfid=AQDfE7gm93_0b_vvFA4&paipv=0&__tn__=R')
# Đóng trình duyệt
# getId('https://www.facebook.com/FcThuyTien')
# getcomment('https://mbasic.facebook.com/toilahs12/posts/pfbid0nYg6eg5k599U9zkyurtbKbzEATw7ozdVu3ZXKHuRTqDwcCCtYupiuQhWU39K4aKhl')
driver.quit()


