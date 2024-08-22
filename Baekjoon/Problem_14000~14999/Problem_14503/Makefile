file=Problem_$(NUM)
cxx=g++
dst=$(file)
src=$(file).cpp

all: $(dst)

$(dst): $(src)
	$(cxx) $^ -o $@

run:
	make
	./$(dst) < input.txt
	make clean

python:
	python3 $(file).py < input.txt

clean:
	rm $(dst)