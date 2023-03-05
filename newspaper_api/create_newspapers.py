from scrape_newspapers import scrape_wsj, scrape_nyt

ny_times_url = 'https://www.nytimes.com/2023/03/02/briefing/chatgpt-ai.html'
wsj_url = 'https://www.wsj.com/articles/hackathons-target-coronavirus-11586424603'

newspaper_one = scrape_nyt(ny_times_url)
newspaper_two = scrape_wsj(wsj_url)

print(newspaper_one.title)
print(newspaper_two.title)