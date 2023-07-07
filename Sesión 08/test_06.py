def fileManipulation(dir, mode):
    try:
        file = open(dir, mode)
        print(file.read())
        file.close()
        return file
    except OSError:
        print(OSError)

fileWrite1 = "test_06.txt"
fileManipulation(fileWrite1, "r")
