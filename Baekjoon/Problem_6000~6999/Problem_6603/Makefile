file=Problem_$(NUM)
cxx=g++
dst=$(file)
src=$(file).cpp

all: $(dst)

$(dst): $(src)
	$(cxx) -std=c++14 $^ -o $@

run:
	make
	./$(dst) < input.txt
	make clean

python:
	python3 $(file).py < input.txt

clean:
	rm $(dst)