path=current_problem
src=main.cpp
dst=main


$(path)/$(dst): $(path)/$(src)
	g++ -std=c++14 $^ -o $@

cpp:
	make
	time ./$(path)/$(dst) < $(path)/input.txt
	make clean

python:
	time python3 $(path)/$(dst).py < $(path)/input.txt

clean:
	rm $(path)/$(dst)

move:
	python3 move.py $(num)

start:
	cp -r codebase/* current_problem