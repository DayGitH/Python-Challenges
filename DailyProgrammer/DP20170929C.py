"""
[2017-09-29] Challenge #333 [Hard] Build a Web API-driven Data Site

https://www.reddit.com/r/dailyprogrammer/comments/739j8c/20170929_challenge_333_hard_build_a_web_apidriven/

# Description
A common theme in present-day programming are web APIs. We've had a previous challenge where you had to _consume_ an
API, today's challenge is to _implement_ one. Today's is relatively simple: a single CSV file as input that can
probably be represented by a single database table. 
Your solution may use whatever technologies you wish to build on:
* Web server software, e.g. Flask, Rails, Play!, etc
* Database software, e.g. MySQL, MongoDB, etc - or none, using a database is optional
* Database interaction layer, e.g. SQLAlchemy, ActiveRecord, Ecto, etc
This challenge focuses less on the guts of the server and more on routing requests, transforming a request into a data
extraction method, and returning those results. 
Today's challenge will utilize the State of Iowa - Monthly Voter Registration Totals by County data set: 
    https://data.iowa.gov/Communities-People/State-of-Iowa-Monthly-Voter-Registration-Totals-by/cp55-uurs
Download the JSON, CSV or other and use that as your input. It contains 19 columns and over 20,000 rows. Now expose the
data via a web API. 
Your solution **must** implement the following API behaviors:
* A "get_voters_where" endpoint that takes the following optional arguments: county, month, party affiliation,
active_status, and limit (the max number of results to return). The endpoint must return a JSON-formatted output, but
the schema is up to you. 
* All APIs must be RESTful (see [The REST API in five minutes](https://developer.marklogic.com/try/rest/index) for some
background if you need it).
This challenge extends Wednesday's idea of practicality and real world scenarios. Wednesday was some basic data
science, today is some basic application development. It's open ended.
# Bonus
Ensure your API is immune to attack vectors like SQL injection. 
"""


def main():
    pass


if __name__ == "__main__":
    main()
