import os
import subprocess

is_valid = False
duration = 10
selected_instance = 1

# Function to display available instance files
def display_instances():
    print("\n")
    print(' |', 'ID'.ljust(5), ' | ', 'File Name'.ljust(16), " |")
    print(' |:', '-'*3, ':|:', '-'*15, ':|')
    for num in range(1, 6):
        filename = f'instance-{num}.asp'
        print(' |', str(num).ljust(5), ' | ', filename.ljust(16), " |")
    print()

# Main loop for instance selection
while not is_valid:
    display_instances()
    selected_instance = input('Select the instance file number: ')
    if selected_instance.isdigit() and int(selected_instance) in range(1, 6):
        is_valid = True
    else:
        print("\n" + "-"*10 + " INVALID INPUT " + "-"*10)
        print("Enter a number between 1 and 5")

print("\n" + "-"*10 + " PROCESSING " + "-"*10 + "\n\n")

# Logic to run the subprocess and check for satisfiability
while is_valid:
    process_args = ['clingo', 'demo.asp', os.path.join('test-instances', f'instance-{selected_instance}.asp'), '-c', f'n={duration}']
    process = subprocess.Popen(process_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, errors = process.communicate()

    if 'UNSATISFIABLE' in output.decode("utf-8"):
        duration += 2
    else:
        is_valid = False
        print(output.decode("utf-8"))
