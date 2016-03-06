#!/usr/bin/python

import csv
import operator

queries = {}
with open("query_doi.csv") as csvfile:
	csvreader = csv.reader(csvfile)

	for (query, doi, clicks) in csvreader:
		if query not in queries:
			queries[query] = 1
		else:
			queries[query] += 1

sorted_queries = sorted(queries.items(), key=operator.itemgetter(1), reverse=True)
for t in sorted_queries:
	print t
