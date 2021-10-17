compiler=gcc
flag=-g -Wall -o
target=debug.out
source=debug.c

$(target): $(source)
	$(compiler) $(flag) $@ $^

clean:
	rm $(target)
