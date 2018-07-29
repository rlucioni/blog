clean:
	rm -rf public

build: clean
	hugo --gc

serve:
	hugo server -D
