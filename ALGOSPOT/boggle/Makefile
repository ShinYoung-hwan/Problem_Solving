
run:
	g++ main.cpp -o main
	./main < sample_input.txt > sample_output.txt
	diff -w sample_answer.txt sample_output.txt
	rm main

python:
	python3 main.py < sample_input.txt > sample_output.txt
	diff -w sample_answer.txt sample_output.txt

move:
	rm sample_output.txt
	@mkdir -p ../$(file)
	@echo "Moving all files to ../$(file)"
	cp * ../$(file)