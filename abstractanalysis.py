x=input()
f=open(x)
read=f.readline()
print(read)
for abstract in read:
    if read.__contains__("Automated") or read.__contains__("automated") :
        print(1,"Contains automated")
    if read.__contains__("Security") or read.__contains__("security"):
        print(2,"Contains security")
    if read.__contains__("vehicle") or read.__contains__("Vehicle") or read.__contains__("Vehicles") or read.__contains__("vehicles"):
        print(3,"Contains vehicle")
    if read.__contains__("Privacy") or read.__contains__("privacy"):
        print(4,"Contains privacy")
    if read.__contains__("misuse") or read.__contains__("Misuse"):
        print(5,"Contains misuse")
    if read.__contains__("Self") or read.__contains__("self"):
        print(6,"Contains self")
    if read.__contains__("driven") or read.__contains__("Driven") or read.__contains__("Driving") or read.__contains__("driving") or read.__contains__("Drive") or read.__contains__("drive") :
        print(7,"Contains drive")
    if read.__contains__("autonomous") or read.__contains__("Autonomous"):
        print(8,"Contains autonomous")
    if read.__contains__("data") or read.__contains__("Data"):
        print(9,"Contains data")
    if read.__contains__("cyber") or read.__contains__("Cyber"):
        print(10,"Contains cyber")
    if read.__contains__("connected") or read.__contains__("Connected"):
        print(11,"Contains connected")
    if read.__contains__("vulnerability") or read.__contains__("Vulnerability") or read.__contains__("Vulnerabilities") or read.__contains__("vulnerabilities") :
        print(12,"Contains vulnerability")
    if read.__contains__("threat") or read.__contains__("Threat") or read.__contains__("threats") or read.__contains__("Threats"):
        print(13,"Contains threat")
    if read.__contains__("taxonomy") or read.__contains__("Taxonomy"):
        print(14,"Contains taxonomy")
    if read.__contains__("attacks") or read.__contains__("attack") or read.__contains__("Attacks") or read.__contains__("Attack"):
        print(15,"Contains attacks")
    if read.__contains__("defences") or read.__contains__("defence") or read.__contains__("Defences") or read.__contains__("Defence"):
        print(16,"Contains defence")
    if read.__contains__("physical") or read.__contains__(" Physical"):
        print(17,"Contains physical")
    if read.__contains__("system") or read.__contains__("System"):
        print(18,"Contains system")
    break
