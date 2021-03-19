# solr-perf-test
solr performance testing using docker

Solr docker container:
https://github.com/docker-solr/docker-solr

Get solr running (with core and sample documents indexed)
mkdir solrdata
chmod 777 solrdata
docker run -d -v "$PWD/solrdata:/var/solr" -p 8983:8983 --name my_solr solr:8 solr-precreate gettingstarted

URL of HN data:
https://github.com/sytelus/HackerNewsData
https://archive.org/download/HackerNewsStoriesAndCommentsDump/HNStoriesAll.7z

Extract HN data:
 7zr e HNStoriesAll.7z

Naive jq to strip out data (killed):
jq '.hits[] | {created_at: .created_at, title: .title, author: .author, created_at_i: .created_at_i, objectID: .objectID}' HNStoriesSample.json

Convert to jq streaming https://stackoverflow.com/questions/39232060/process-large-json-stream-with-jq:
https://devblog.songkick.com/parsing-ginormous-json-files-via-streaming-be6561ea8671

Jq syntax frustrating, use python and ijson:
https://pypi.org/project/ijson/


Next steps:
Create new solr core from UI
Could not find schema file
Create new core from command line
https://factorpad.com/tech/solr/reference/solr-create-core.html
solr create_core -c hn_stories2
See if solr post tool can work with ndjson (rename file to jsonl
https://factorpad.com/tech/solr/reference/solr-post.html
post -c hn_stories2 ../input/HackerNewsStories.jsonl
Index 1,333,789 documents



Solr version
Index Size
Indexing time
8
890.76
1m54
8
887.98
1m51
7.7
511.93
2m48
8.8
667.11mb
2m9s



Performance links:
https://stackoverflow.com/questions/12079269/speeding-up-solr-search
https://stackoverflow.com/questions/6954358/how-to-optimize-solr-index


Facet Query:
facet.range=created_at&facet=true&facet.range.start=2006-10-09T18:21:51Z&facet.range.end=2014-05-29T08:25:40Z&facet.range.gap=+1DAY

Full query:
http://localhost:8983/solr/hn_stories-8.8/select?df=title&facet.range.end=2014-05-29T08%3A25%3A40Z&facet.range.gap=%2B1DAY&facet.range.start=2006-10-09T00%3A00%3A00Z&facet.range=created_at&facet=true&q=and&rows=0


