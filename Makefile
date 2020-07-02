clean:
	rm -rf public

compile:
	npm run compile

build: clean compile
	hugo --minify --gc

serve: compile
	hugo server --buildDrafts --disableFastRender

post-%:
	hugo new posts/$*.md

ping:
	curl -v 'https://www.google.com/ping?sitemap=https://renzolucioni.com/sitemap.xml'

requirements:
	pip install -r requirements.txt
