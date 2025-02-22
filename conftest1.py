#### g. Создайте файл `conftest.py`
1. Нажмите **Add file** → **Create new file**.
2. В поле для имени файла введите: `conftest.py`.
3. В тело файла добавьте:
   ```python
   import pytest
   from selenium import webdriver

   @pytest.fixture(scope="function")
   def browser():
       # Инициализация драйвера
       driver = webdriver.Chrome()  # Укажите путь к драйверу, если он не в PATH
       yield driver
       # Закрытие драйвера после теста
       driver.quit()
   
