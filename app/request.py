import aiohttp
from bs4 import BeautifulSoup

async def featch_page():

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        uri = "https://goszakupki.by/tenders/posted?TendersSearch%5Bnum%5D=&TendersSearch%5BiceGiasNum%5D=&TendersSearch%5Btext%5D=&TendersSearch%5Bunp%5D=&TendersSearch%5Bcustomer_text%5D=&TendersSearch%5BunpParticipant%5D=&TendersSearch%5Bparticipant_text%5D=&TendersSearch%5Bprice_from%5D=&TendersSearch%5Bprice_to%5D=&TendersSearch%5Bcreated_from%5D=&TendersSearch%5Bcreated_to%5D=&TendersSearch%5Brequest_end_from%5D=&TendersSearch%5Brequest_end_to%5D=&TendersSearch%5Bauction_date_from%5D=&TendersSearch%5Bauction_date_to%5D=&TendersSearch%5Bindustry%5D=105%2C106%2C107%2C108%2C109%2C110%2C111%2C112%2C113%2C114%2C115%2C116%2C117%2C118%2C119%2C120%2C121%2C122&TendersSearch%5Btype%5D=&TendersSearch%5Bstatus%5D=&TendersSearch%5Bregion%5D=&TendersSearch%5Bappeal%5D=&TendersSearch%5Bfunds%5D="
        async with session.get(uri) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            rows_with_data_key = soup.find_all('a')
            # soup.find_all('tr', attrs={'data-key': True})

            print(*rows_with_data_key, sep='\n')