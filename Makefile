clean:
	rm -rf public

build: clean
	hugo --minify --gc

serve:
	hugo server --buildDrafts --disableFastRender

post-%:
	hugo new posts/$*.md
