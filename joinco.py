import scrapy
from scrapy.crawler import CrawlerProcess
import json

class InvestLikeTheBestScraper(scrapy.Spider):
	name = "joincolossus"
	#url = 'https://www.joincolossus.com/episodes?prod-episode-release-desc%5BrefinementList%5D%5BpodcastName%5D%5B0%5D=Invest%20Like%20the%20Best&prod-episode-release-desc%5Bpage%5D=4'

	custom_settings = {
		"FEED_FORMAT": "csv",
		"FEED_URI": "Invest Like The Best.csv",
	}
	page = 1
	
	def start_requests(self):
		yield scrapy.Request(url='https://zxbnfwz0nl-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.5)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.16.0)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.3)%3B%20JS%20Helper%20(3.4.4)&x-algolia-api-key=120e68b948a0b077503dc46ba5f3c733&x-algolia-application-id=ZXBNFWZ0NL'
							,method='POST', body='{"requests":[{"indexName":"prod-episode-release-desc","params":"facetingAfterDistinct=true&hitsPerPage=8&clickAnalytics=true&distinct=true&attributesToSnippet=%5B%22transcript%3A40%22%5D&maxValuesPerFacet=10&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&page=1&facets=%5B%22podcastName%22%5D&tagFilters=&facetFilters=%5B%5B%22podcastName%3AInvest%20Like%20the%20Best%22%5D%5D"},{"indexName":"prod-episode-release-desc","params":"facetingAfterDistinct=true&hitsPerPage=1&clickAnalytics=false&distinct=true&attributesToSnippet=%5B%22transcript%3A40%22%5D&maxValuesPerFacet=10&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&tagFilters=&analytics=false&facets=podcastName"}]}'
							,callback=self.parse_json)

	def parse_json(self, response):
		data = json.loads(response.text)
		number_of_pages = data["results"][0]["nbPages"]

		for hit in data["results"][0]["hits"]:
			item = {}
			item["title"] = hit["title"]
			item["desc"] = hit['_snippetResult']['transcript']['value']	
			yield item
			
		if self.page < number_of_pages:
			self.page += 1
			yield scrapy.Request(url='https://zxbnfwz0nl-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.5)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.16.0)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.3)%3B%20JS%20Helper%20(3.4.4)&x-algolia-api-key=120e68b948a0b077503dc46ba5f3c733&x-algolia-application-id=ZXBNFWZ0NL'
								,method='POST', body='{"requests":[{"indexName":"prod-episode-release-desc","params":"facetingAfterDistinct=true&hitsPerPage=8&clickAnalytics=true&distinct=true&attributesToSnippet=%5B%22transcript%3A40%22%5D&maxValuesPerFacet=10&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&page='+ str(self.page) + '&facets=%5B%22podcastName%22%5D&tagFilters=&facetFilters=%5B%5B%22podcastName%3AInvest%20Like%20the%20Best%22%5D%5D"},{"indexName":"prod-episode-release-desc","params":"facetingAfterDistinct=true&hitsPerPage=1&clickAnalytics=false&distinct=true&attributesToSnippet=%5B%22transcript%3A40%22%5D&maxValuesPerFacet=10&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&page=' + str(self.page) + '&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&tagFilters=&analytics=false&facets=podcastName"}]}'
								,callback=self.parse_json)




if __name__ == '__main__':
	process = CrawlerProcess()
	process.crawl(InvestLikeTheBestScraper)
	process.start()