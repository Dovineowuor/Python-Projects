def load_road_network(filename):
# inititialising dictionary
#intersection
	intersection0 = "road_sample0.txt"
	intersection1 = "road_sample1.txt"

	# printing initial json
	print ("initial 1st dictionary", intersection0)
	print ("initial 2nd dictionary", intersection1)

	# intersecting two dictionaries
	final_dict = {x: intersection0[x] for x in  intersection0
								if x in  intersection1}

	# printing final result
	print ("final dictionary", str(final_dict))

load_road_network()

