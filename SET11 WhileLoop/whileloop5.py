import random

def random_number_generator():
    target = 7
    attempts = 0

    while True:
        number = random.randint(1, 10)
        attempts += 1
        
        print(f"Attempt {attempts}: Generated {number}")
        
        if number == target:
            print(f"Target {target} found after {attempts} attempts!")
            break

# Run the function
random_number_generator()