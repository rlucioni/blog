clean:
	rm -rf public

build: clean
	hugo

serve:
	hugo server -D
