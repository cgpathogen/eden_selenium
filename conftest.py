import os
import pytest
import sqlite3
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from database.database import Database

@pytest.fixture(autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(0, 0)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(autouse=True)
def create_database():
    original_path = Database.db_path

    temp_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
    temp_db.close()
    Database.db_path = temp_db.name
    Database.create_db()
    yield

    try:
        conn = sqlite3.connect(Database.db_path)
        conn.close()
        os.unlink(Database.db_path)
    except Exception as e:
        print(f"Error cleaning up temp db: {e}")
    Database.db_path = original_path