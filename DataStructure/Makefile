compiler=gcc
flag=-g -Wall -o
target=main.out
source=main.c

$(target): $(source)
	$(compiler) $(flag) $@ $^

clean:
	rm $(target)
