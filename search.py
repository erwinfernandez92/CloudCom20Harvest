import time

class Searcher:
    def __init__(self, api):
        self.api = api

    def fetch(self, geo):
        # iterate over results, see how many we can fetch
        max_id = None
        count = 0
        while True:
            time.sleep(4.5)
            results = self.api.search(geocode=geo, count=100, max_id=max_id)

            for result in results:
                # print(result.text)
                # print(result.coordinates if hasattr(result, 'coordinates') else "Undefined location")
                # print(result.created_at)
                # print(result.id)
                max_id = result.id

            count += len(results)
            print(result.created_at)
            print(count)
            if len(results) == 0:
                print("gracefully finishing")
                break
