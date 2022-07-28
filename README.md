
## Run Locally

### Clone the project

```bash
  git clone https://github.com/arjun-ms/Google-Image-Scraper
```

### Go to the project directory

```bash
  cd Google-Image-Scraper
```
### Install chromedriver

Ensure you have the [appropriate version](https://chromedriver.chromium.org/downloads) of ChromeDriver on your machine if you would like to scrape from Google Images.

### Install dependencies

```bash
  pip install -r requirements.txt
```
### Edit your desired parameters in main.py

```bash
  PATH = "/home/ams/chromedriver"   # path to chromedriver
  LIMIT = 100                       # how much images you want to download
  query = '"mohanlal"'              # keyword you want to search for
```

### Run the program

```bash
  python main.py
```

