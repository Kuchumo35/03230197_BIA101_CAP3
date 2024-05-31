###############################
# https://github.com/Kuchumo35/03230197_BIA101_CAP3
# Pema Choden
# BBI B
# 03230197
###############################
# REFERENCES
# reading file
# https://youtu.be/DCaKj3eIrro?si=G5m9idptKfF7y4v5
##############################
# SOLUTION
# 426900


def read_input(line):
    
    if line[:2].isdigit():
        return int(line[:2]) * 2  
    
    
    if line[-2:].isdigit():
        return int(line[-2:]) * 2  
    
    
    return 0

def main():
    

    
    file_path = r"197.txt"

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        total_sum = 0

        for line in lines:
            line = line.strip()
            two_digit_number = read_input(line)
            total_sum += two_digit_number

        print("The sum of all processed numbers is:", total_sum)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "_main_":
    main()