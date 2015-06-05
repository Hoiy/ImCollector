rm -f ./ImStore/full/*
scrapy crawl google -L INFO -a max_count=100 -a "key=$1"
