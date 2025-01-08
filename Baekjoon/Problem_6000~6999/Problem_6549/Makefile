file=Problem_$(NUM)
cxx=g++
dst=$(file)
src=$(file).cpp

all: $(dst)

$(dst): $(src)
	$(cxx) -std=c++14 $^ -o $@

run:
	make
	time ./$(dst) < input.txt
	make clean

python:
	time python3 $(file).py < input.txt

clean:
	rm $(dst)

move: 
	cd .. && python3 move.py $(NUM)