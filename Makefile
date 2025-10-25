build: clean
	npm run build

clean:
	rm -rf dist
	rm -rf src/assets/bundles

deploy:
	./scripts/deploy.sh

dev: clean
	npm run dev

install:
	./scripts/install.sh

lint:
	npm run lint

post:
	./scripts/new-post.sh $(slug)

prettier:
	npm run prettier
