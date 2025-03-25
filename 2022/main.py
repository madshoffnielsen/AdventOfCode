import subprocess

file_name = input("Enter the day you want to run or 'all': ")

try:
    if file_name == "all":
        for i in range(1, 26):
            file = "2022/code/Day" + str(i).zfill(2) + ".py"
            subprocess.run(["python", file], check=True)
    else:
        file = "2022/code/Day" + str(file_name).zfill(2) + ".py"

    subprocess.run(["python", file], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error executing the script: {e}")
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")