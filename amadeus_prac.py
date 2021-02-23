
from amadeus import Client, ResponseError

amadeus = Client()

def search_flight(origin, dest, depart, adlt):
	try:
	    # response = amadeus.shopping.flight_offers_search.get(
	    #     originLocationCode='SYD',
	    #     destinationLocationCode='BKK',
	    #     departureDate='2021-04-01',
	    #     adults=1)
	    response = amadeus.shopping.flight_offers_search.get(
	        originLocationCode=origin,
	        destinationLocationCode=dest,
	        departureDate=depart,
	        adults=adlt)
	    print(len(response.data), response.data[0])
	    for i, dat in enumerate(response.data):
	    	print('\n' * 5, i)
	    	for key, val in dat.items():
	    		print('%s = %s' % (key,  val))
	    		# if isinstance(val, dict):
	    		# 	print('\n%s=== ' % (key))
	    		# 	print_dict(val)	
	    		# elif isinstance(val, list):
	    		# 	print('\n%s ===' % (key))
	    		# 	print_list(val)	
	    		# else:
	    		# 	print('%s === %s' % (key,  val))

	except ResponseError as error:
   		print(error)

def print_dict(xmap):
	print('{')
	for key, val in xmap.items():
		if isinstance(val, list):
			print_list(val)	
		elif isinstance(val, dict):
			print_dict(val)	
		else:
			print('%s = %s' % (key, val))
	print('}')
def print_list(arr):
	print('[')
	for x in arr:
		if isinstance(x, dict):
			print_dict(x)
		else:
			print(x)
	print(']')

def main():
	# origin = input('origin: ')
	# dest = input('destination: ')
	# depart = input('Date (YYYY-MM-DD): ')
	# adlt = input('adults: ')
	# print(origin, dest, depart, adlt)
	# search_flight(origin, dest, depart, adlt)
	search_flight('SYD', 'BKK', '2021-04-01', 1)

if __name__ == '__main__':
	main()
