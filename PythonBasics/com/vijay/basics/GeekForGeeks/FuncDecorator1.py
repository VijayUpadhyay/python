def welcomeMsg(nameVal):
    def defaultMsg():
        return "Welcome To "
    return defaultMsg()+nameVal+" !!"
print(welcomeMsg("Vijay"))