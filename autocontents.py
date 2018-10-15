#!/usr/bin/env python3

# Load all essential statistics from AWS SAM including almost-exact number of Lambdas as well as metadata.

import urllib.request
import json
import itertools
import math
import csv
import datetime

def pullstatistics(stamp):
	neededpages = None

	f = open("autocontents-{}.csv".format(stamp), "w")
	w = csv.writer(f)

	for page in itertools.count(start=1):
		link = "https://shr32taah3.execute-api.us-east-1.amazonaws.com/Prod/applications/browse?pageSize=100"
		if page > 1:
			link += "&pageNumber=" + str(page)

		resource = urllib.request.urlopen(link)
		content = resource.read().decode("utf-8")
		struct = json.loads(content)

		if page == 1:
			neededpages = math.ceil(struct["approximateResultCount"] / 100)
			print("Approximately {} results.".format(struct["approximateResultCount"]))
			print("Applications:")

			stf = open("autostats.csv", "a")
			stw = csv.writer(stf)
			stw.writerow([stamp, struct["approximateResultCount"]])
			stf.close()

		for app in struct["applications"]:
			if not "homePageUrl" in app.keys():
				app["homePageUrl"] = ""

			if "github.com" in app["homePageUrl"]:
				github_stats(app, app["homePageUrl"].replace("github.com", "api.github.com/repos"))

			print("- {} / {}".format(app["name"], app["id"]))
			print("  by: {}".format(app["publisherAlias"]))
			print("  deployments: {}".format(app["deploymentCount"]))
			print("  labels: {}".format(",".join(app["labels"])))
			print("  homepage: {}".format(app["homePageUrl"]))

			fields = []
			fields.append(app.get("name"))
			fields.append(app.get("id"))
			fields.append(app.get("publisherAlias"))
			fields.append(app.get("deploymentCount"))
			fields.append(app.get("homePageUrl", ""))
			fields.append(app.get("stars", ""))
			fields.append(app.get("watchers", ""))
			fields.append(app.get("forks", ""))
			fields.append(app.get("language", ""))
			fields.append(",".join(app.get("labels")))
			fields.append(app.get("description"))

			w.writerow(fields)

		if page == neededpages:
			break

	f.close()

def github_stats(app, link):
	try:
		print("-> fetch github: {}".format(link))

		resource = urllib.request.urlopen(link)
		gh_content = resource.read().decode("utf-8")
		struct = json.loads(gh_content)

		app["stars"] = struct["stargazers_count"]
		app["watchers"] = struct["subscribers_count"]
		app["forks"] = struct["forks_count"]
		app["language"] = struct["language"]
	except:
		print("-> fetch github: ERROR")

pullstatistics(datetime.date.isoformat(datetime.date.today()))
