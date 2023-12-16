.PHONY: default run build

default: run

build: server

run: server
	@./server

server: src/*
	@gprbuild -j0
