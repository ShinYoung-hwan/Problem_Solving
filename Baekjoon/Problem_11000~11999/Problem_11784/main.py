import sys

inputs = lambda: sys.stdin.readlines()

hex_map = { f'{i}':i for i in range(10) }
hex_map['A'], hex_map['B'], hex_map['C'], hex_map['D'], hex_map['E'], hex_map['F'] = 10, 11, 12, 13, 14, 15

def translate(hex_code):
    ascii_codes = [ hex_code[i:i+2] for i in range(0, len(hex_code), 2) ]
    
    for ascii_code in ascii_codes:
        n = hex_map[ascii_code[0]] * 16 + hex_map[ascii_code[1]]
        print(chr(n), end='')
    print()
        

if __name__ == "__main__":
    hex_codes = [ line.rstrip() for line in inputs() ]
    
    for hex_code in hex_codes:
        translate(hex_code)