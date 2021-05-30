import requests
from bs4 import BeautifulSoup
import time
import json
import pandas as pd
import numpy as np
import time
import os
import sys
from googletrans import Translator
from googletrans import Translator
from selenium.webdriver.chrome.options import Options
translator = Translator()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

translator = Translator()

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15"}

