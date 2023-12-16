.PHONY: default run build clean

default: run

build: server

run: server
	@./server

server: .setup_artifact src/*
	@gprbuild -j0

.setup_artifact:
	@./setup.py

clean:
	rm -r server obj *.cgpr .setup_artifact
