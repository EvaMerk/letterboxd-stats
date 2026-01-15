import requests

#-------- comment back in to get more information from letterboxd (e.g. imdb link, actors, crew,...) ---------
#from bs4 import BeautifulSoup
#import asyncio
#import aiohttp

# # --- for max. 10 paralell requests ---
# sem = asyncio.Semaphore(10)

# async def fetch_url(session, short_url, retries=3):
#     """Get the long letterboxd url instead of a boxd.it-short-url"""
#     for attempt in range(1, retries + 1):
#         try:
#             async with sem:  # concurrency limit
#                 async with session.get(short_url, allow_redirects=True, timeout=20) as resp:
#                     return resp.url.human_repr()
#         except Exception as e:
#             print(f"[Attempt {attempt}] Error for {short_url}: {e}")
#             await asyncio.sleep(1)  # wait before retrying
#     return None

# async def resolve_all(urls):
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch_url(session, url) for url in urls]
#         return await asyncio.gather(*tasks)

# def extract_base_url(letterboxd_url):
#     user_name = letterboxd_url.split('/')[-4]
#     letterboxd_url = letterboxd_url.replace('/'+user_name,'')
#     return letterboxd_url

# def get_elements(hrefs:list, prefix:str):
#     element = [s for s in hrefs if s.startswith(prefix)]
#     unique_element = list(set(element))
#     unique_element = [
#         s.removeprefix(prefix)
#         .removesuffix("/")
#         .replace("-", " ")
#         .title()
#         for s in unique_element
#         if s.startswith(prefix)
#     ]
#     return unique_element

# # ========== scrape letterboxd ==========
# def get_letterboxd_film_info(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#     }
#     r = requests.get(url, headers=headers)
#     soup = BeautifulSoup(r.text, "html.parser")
    
#     # Titel
#     title_tag = soup.find("h1", {"class": "headline-1"})
#     title = title_tag.text.strip() if title_tag else None
    
#     # get all hrefs - shows the imdb href too! also other very interesting links, e.g. showing all actors and the crew,..
#     hrefs = [a["href"] for a in soup.find_all("a", href=True)]

#     year = get_elements(hrefs, "/films/year/")
#     year = year[0] if year else None

#     return title, year, hrefs


def get_omdb_info(title, year, api_key):
    url = f"http://www.omdbapi.com/?t={title}&y={year}&plot=full&apikey={api_key}"
    r = requests.get(url)
    data = r.json()

    if data.get("Response") == "True":
        return data
    else:
        return None


