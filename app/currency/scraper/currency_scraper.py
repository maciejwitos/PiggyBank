from datetime import date
import re
from beautifulscraper import BeautifulSoup
from selenium import webdriver
from app.models import Currency

class GetCurrencies:
    """
    Modul resposible for scraping data about currencies from website
    """
    global current_day

    @staticmethod
    def scrap_currencies(current_day):

        if not current_day == date.today():

            # set a new option avoiding open new browser window
            options = webdriver.ChromeOptions()
            options.arguments.append('headless')

            # set browser
            driver = webdriver.Chrome("/home/maciej/projects/Final_Project/app/currency/scraper/chromedriver", options=options)

            # go to website
            driver.get('https://www.mybank.pl/')

            # collecting content from website
            content = driver.page_source
            soup = BeautifulSoup(content, features='html.parser')

            # closing browser
            driver.quit()

            # setting new value of currencies according downloaded data
            eur = Currency.objects.get(name='EUR')
            eur.in_pln = float(
                (re.search(r'\d[,]\d*', str(soup.find('td', attrs={'id': 'EURPLN_NBP'}))).group()).replace(',', '.'))
            eur.save()

            usd = Currency.objects.get(name='USD')
            usd.in_pln = float(
                (re.search(r'\d[,]\d*', str(soup.find('td', attrs={'id': 'USDPLN_NBP'}))).group()).replace(',', '.'))
            usd.save()

            gbp = Currency.objects.get(name='GBP')
            gbp.in_pln = float(
                (re.search(r'\d[,]\d*', str(soup.find('td', attrs={'id': 'GBPPLN_NBP'}))).group()).replace(',', '.'))
            gbp.save()

            nok = Currency.objects.get(name='NOK')
            nok.in_pln = float(
                (re.search(r'\d[,]\d*', str(soup.find('td', attrs={'id': 'NOKPLN_NBP'}))).group()).replace(',', '.'))
            nok.save()

            chf = Currency.objects.get(name='CHF')
            chf.in_pln = float(
                (re.search(r'\d[,]\d*', str(soup.find('td', attrs={'id': 'CHFPLN_NBP'}))).group()).replace(',', '.'))
            chf.save()

            #setting variable current_day for today
            current_day = date.today()

            return current_day

        else:
            pass


if __name__ == "__main__":
    currency = GetCurrencies.scrap_currencies(current_day=date.today())
