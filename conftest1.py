
1. Нажмите **Add file** → **Create new file**.
2. В поле для имени файла введите: `conftest.py`.
3. В тело файла добавьте:
   ```python
   import pytest
   from selenium import webdriver

   @pytest.fixture(scope="function")
   def browser():
       driver = webdriver.Chrome()  
       yield driver
       driver.quit()
   
