from datetime import date
import re
from beautifulscraper import BeautifulSoup
from selenium import webdriver
from app.models import Currency


class GetCurrencies:

    global current_day

    @staticmethod
    def scrap_currencies(current_day):

        if not current_day == date.today():

            driver = webdriver.Chrome("/home/maciej/Downloads/chromedriver_linux64/chromedriver")

            driver.get('https://www.mybank.pl/')
            content = driver.page_source
            soup = BeautifulSoup(content, features='html.parser')
            driver.quit()

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

            current_day = date.today()

            return current_day

        else:
            print("Up to date")
            pass


if __name__ == "__main__":
    currency = GetCurrencies.scrap_currencies(current_day=date.today())
