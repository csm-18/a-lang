def compile(filename: str):
    code = "" 
    #read .a source file to string
    try:
        with open(filename, "r") as f:
            code = f.read()
    except:
        print("error: Unable to read file",filename)        

    print(code)    