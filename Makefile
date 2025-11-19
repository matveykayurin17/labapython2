IMAGE_NAME = labapython2
FILE = Dockerfile

build:
  docker build -f $(FILE) -t $(IMAGE_NAME) .

run:
  docker run --rm $(IMAGE_NAME)

build-run: build run