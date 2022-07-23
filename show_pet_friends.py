import pytest
from settings import valid_email, valid_password

def show_pet_friends():
   '''Проверяем карточки питомцев'''

   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)

   # Вводим валидный email
   pytest.driver.find_element_by_id('email').send_keys(valid_email)

   # Вводим валидный пароль
   pytest.driver.find_element_by_id('pass').send_keys(valid_password)

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   # Проверяем, что оказались на странице пользователя с питомцами
   assert pytest.driver.current_url == 'http://petfriends.skillfactory.ru/all_pets'

   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

   assert names[0].text != ''

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ',' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
