try:
    with open('modules') as fb:
        file_data = fb.read()
        print(file_data)
except FileNotFoundError:
    print("File couldn't be found")
except PermissionError:
    print("Lack of permission")
except Exception as err:
    print("Some other issue:", str(err))