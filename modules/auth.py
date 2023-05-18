def getAuth(file):
    authDict = {}
    try:
        with open(file) as authFile:
            for line in authFile:
                name,var = line.partition(": ")[::2]
                authDict[name.strip()] = str(var.strip())
        return authDict
    except Exception as e:
        raise Exception(f"Invalid Path Exception -> {file} not found")
         
