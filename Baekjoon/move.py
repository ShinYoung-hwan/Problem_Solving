import os
import argparse
import shutil

def argument_parse():
    args = argparse.ArgumentParser()
    args.add_argument("num", type=int)
    return args.parse_args()

def get_py_file(files: list):
    for file in files:
        if file.find(".py") != -1:
            return file
        
def get_src_dst_num(num: int):
    snum = str(num)
    length = len(snum)
    
    src = int(snum[0:length-3] + "000")
    dst = int(snum[0:length-3] + "999")
    
    return src, dst

if __name__ == "__main__":
    # input checking
    args = argument_parse()
    while True:
        s = input(f"Is it right problem number({args.num})? Y/N: ").capitalize()
        if s == "Y": break
        elif s == "N":
            print("Wrong Number...")
            exit(1)
        
        print("unvalid submission.", end=' ')
        
    # get file  
    find_directory = os.path.join(".", "current_problem")
    files = os.listdir(find_directory)
    py_file = get_py_file(files)
    
    # rename file
    os.rename(
        os.path.join(find_directory, py_file),
        os.path.join(find_directory, f"Problem_{args.num}.py") 
    )
    
    # dest directory check
    src, dst = get_src_dst_num(args.num)
    first_dest_directory = os.path.join(".", f"Problem_{src}~{dst}")
    if not os.path.exists(first_dest_directory):
        os.makedirs(first_dest_directory)
    
    # copy
    shutil.copytree(
        os.path.join(find_directory),
        os.path.join(first_dest_directory, f"Problem_{args.num}")
    )