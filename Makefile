install:
	./scripts/install.sh

clean:
	rm -rf public

compile:
	npm run compile

build: clean compile
	hugo --minify --gc

serve: compile
	hugo server --buildDrafts --disableFastRender

public: compile
	hugo server --buildDrafts --disableFastRender --bind=0.0.0.0 --baseURL=http://$$(ipconfig getifaddr en0):1313

post-%:
	hugo new posts/$*.md

deploy:
	./scripts/deploy.sh

ping:
	curl -v 'https://www.google.com/ping?sitemap=https://renzolucioni.com/sitemap.xml'
