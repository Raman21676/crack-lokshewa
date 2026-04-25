#!/usr/bin/env python3
import json, random, os

random.seed(42)

IT_Q = [
    # Computer basics (20)
    ("What does CPU stand for?", ["Central Processing Unit","Computer Personal Unit","Central Processor Utility","Central Program Unit"], 0, "CPU = Central Processing Unit.", "Computer Basics"),
    ("What does RAM stand for?", ["Random Access Memory","Read Access Memory","Random Allocation Memory","Rapid Access Memory"], 0, "RAM = Random Access Memory.", "Computer Basics"),
    ("What does ROM stand for?", ["Random Output Memory","Read Only Memory","Rapid Output Module","Read Output Memory"], 1, "ROM = Read Only Memory.", "Computer Basics"),
    ("What is the brain of the computer?", ["Monitor","CPU","Keyboard","Mouse"], 1, "CPU is the brain of the computer.", "Computer Basics"),
    ("Which device is used to input data?", ["Monitor","Printer","Keyboard","Speaker"], 2, "Keyboard is an input device.", "Computer Basics"),
    ("Which device is used to output data?", ["Keyboard","Mouse","Monitor","Scanner"], 2, "Monitor is an output device.", "Computer Basics"),
    ("What does HDD stand for?", ["High Density Disk","Hard Disk Drive","High Data Drive","Hard Drive Disk"], 1, "HDD = Hard Disk Drive.", "Computer Basics"),
    ("What does SSD stand for?", ["Solid State Drive","Super Speed Disk","Standard Storage Device","Solid Storage Disk"], 0, "SSD = Solid State Drive.", "Computer Basics"),
    ("Which is faster: HDD or SSD?", ["HDD","SSD","Same","Depends on brand"], 1, "SSD is significantly faster than HDD.", "Computer Basics"),
    ("What does USB stand for?", ["Universal Serial Bus","Universal System Bus","Uniform Serial Bus","Universal Storage Bus"], 0, "USB = Universal Serial Bus.", "Computer Basics"),
    ("What is the function of the motherboard?", ["Display images","Connect all components","Store files","Process data"], 1, "Motherboard connects all computer components.", "Computer Basics"),
    ("What does GPU stand for?", ["General Processing Unit","Graphics Processing Unit","Global Processing Unit","General Purpose Unit"], 1, "GPU = Graphics Processing Unit.", "Computer Basics"),
    ("What is the purpose of a power supply unit?", ["Store data","Cool the computer","Provide power to components","Connect to internet"], 2, "PSU provides power to all components.", "Computer Basics"),
    ("Which port is commonly used for Ethernet?", ["USB","HDMI","RJ45","VGA"], 2, "RJ45 is the standard Ethernet port.", "Computer Basics"),
    ("What does BIOS stand for?", ["Basic Input Output System","Basic Internal Operating System","Binary Input Output System","Basic Internet Operating System"], 0, "BIOS = Basic Input Output System.", "Computer Basics"),
    ("What is cache memory?", ["Permanent storage","Fast temporary memory","Slow storage","External memory"], 1, "Cache is fast temporary memory near the CPU.", "Computer Basics"),
    ("What does VGA stand for?", ["Video Graphics Array","Visual Graphics Adapter","Video General Array","Visual General Adapter"], 0, "VGA = Video Graphics Array.", "Computer Basics"),
    ("What does HDMI stand for?", ["High Definition Multimedia Interface","High Data Media Interface","High Definition Media Input","High Digital Multimedia Input"], 0, "HDMI = High Definition Multimedia Interface.", "Computer Basics"),
    ("What is a pixel?", ["A type of software","A small dot on screen","A computer virus","A file format"], 1, "Pixel = picture element, a small dot on screen.", "Computer Basics"),
    ("What does LAN stand for?", ["Local Area Network","Large Area Network","Local Access Node","Long Area Network"], 0, "LAN = Local Area Network.", "Computer Basics"),
    # Software/Operating Systems (20)
    ("Which of these is an operating system?", ["Microsoft Word","Windows","Excel","Chrome"], 1, "Windows is an operating system.", "Software"),
    ("Which is a Linux distribution?", ["Windows","macOS","Ubuntu","iOS"], 2, "Ubuntu is a Linux distribution.", "Software"),
    ("What does OS stand for?", ["Open Software","Operating System","Online Service","Output System"], 1, "OS = Operating System.", "Software"),
    ("Which Microsoft Office application is used for documents?", ["Excel","PowerPoint","Word","Access"], 2, "Word is for documents.", "Software"),
    ("Which Microsoft Office application is used for spreadsheets?", ["Word","Excel","PowerPoint","Outlook"], 1, "Excel is for spreadsheets.", "Software"),
    ("Which Microsoft Office application is used for presentations?", ["Word","Excel","PowerPoint","Publisher"], 2, "PowerPoint is for presentations.", "Software"),
    ("What is open-source software?", ["Software you pay for","Software with source code available","Software without updates","Software only for businesses"], 1, "Open-source software has publicly available source code.", "Software"),
    ("Which is an example of open-source software?", ["Windows","Microsoft Office","Linux","Adobe Photoshop"], 2, "Linux is open-source.", "Software"),
    ("What does API stand for?", ["Application Programming Interface","Advanced Program Integration","Application Process Interface","Automated Programming Interface"], 0, "API = Application Programming Interface.", "Software"),
    ("What is a database?", ["A type of computer","Organized collection of data","A programming language","A network protocol"], 1, "A database is an organized collection of data.", "Software"),
    ("Which is a relational database?", ["MongoDB","Redis","MySQL","Cassandra"], 2, "MySQL is a relational database.", "Software"),
    ("What does SQL stand for?", ["Simple Query Language","Structured Query Language","Standard Query Language","System Query Language"], 1, "SQL = Structured Query Language.", "Software"),
    ("What is a spreadsheet cell address?", ["A1","Cell1","Sheet1","Row1"], 0, "Cells are addressed like A1, B2, etc.", "Software"),
    ("What does PDF stand for?", ["Portable Document Format","Personal Data File","Print Document Format","Portable Data File"], 0, "PDF = Portable Document Format.", "Software"),
    ("What is a web browser?", ["A search engine","Software to access websites","A type of website","An email service"], 1, "A browser is software to access websites.", "Software"),
    ("Which is NOT a web browser?", ["Chrome","Firefox","Photoshop","Edge"], 2, "Photoshop is not a browser.", "Software"),
    ("What does URL stand for?", ["Uniform Resource Locator","Universal Resource Link","Uniform Resource Link","Universal Resource Locator"], 0, "URL = Uniform Resource Locator.", "Software"),
    ("What is a cookie in web terms?", ["A food item","Small data stored by browser","A type of virus","A web page"], 1, "Cookies are small data files stored by browsers.", "Software"),
    ("What is cloud computing?", ["Computing using weather data","Computing over the internet","Computing with water cooling","Computing in airplanes"], 1, "Cloud computing delivers services over the internet.", "Software"),
    ("What does SaaS stand for?", ["Software as a Service","System as a Software","Service as a System","Software and Service"], 0, "SaaS = Software as a Service.", "Software"),
    # Networking/Internet (20)
    ("What does IP stand for?", ["Internet Protocol","Internal Process","Internet Provider","Internal Protocol"], 0, "IP = Internet Protocol.", "Networking"),
    ("What is an IP address?", ["A website name","A unique network identifier","A password","An email address"], 1, "IP address uniquely identifies a device on a network.", "Networking"),
    ("What does HTTP stand for?", ["HyperText Transfer Protocol","High Transfer Text Protocol","HyperText Transmission Protocol","High Text Transfer Protocol"], 0, "HTTP = HyperText Transfer Protocol.", "Networking"),
    ("What does HTTPS mean?", ["HyperText Transfer Protocol Secure","High Transfer Text Secure","HyperText Transmission Protocol Standard","High Text Transfer Protocol Secure"], 0, "HTTPS is the secure version of HTTP.", "Networking"),
    ("What is a firewall?", ["A physical wall","Network security system","A type of virus","A web browser"], 1, "A firewall is a network security system.", "Networking"),
    ("What is a router?", ["A type of cable","Device that forwards data packets","A web server","A printer"], 1, "A router forwards data between networks.", "Networking"),
    ("What does DNS stand for?", ["Digital Name System","Domain Name System","Data Name Service","Digital Network Service"], 1, "DNS = Domain Name System.", "Networking"),
    ("What is the function of DNS?", ["Encrypt data","Translate domain names to IP addresses","Store files","Send emails"], 1, "DNS translates domain names to IP addresses.", "Networking"),
    ("What does Wi-Fi stand for?", ["Wireless Fidelity","Wireless Finder","Wireless Fiber","Wireless Frequency"], 0, "Wi-Fi = Wireless Fidelity.", "Networking"),
    ("What is bandwidth?", ["Width of a network cable","Data transfer capacity","Number of users","Physical distance"], 1, "Bandwidth is the data transfer capacity.", "Networking"),
    ("What is a virus in computer terms?", ["A biological virus","Malicious software","A computer component","A network cable"], 1, "A computer virus is malicious software.", "Networking"),
    ("What is malware?", ["Hardware component","Malicious software","Network protocol","File format"], 1, "Malware = malicious software.", "Networking"),
    ("What does VPN stand for?", ["Virtual Private Network","Virtual Public Network","Very Private Network","Virtual Protected Network"], 0, "VPN = Virtual Private Network.", "Networking"),
    ("What is the purpose of a VPN?", ["Increase internet speed","Secure and private connection","Store files","Create websites"], 1, "VPN provides secure and private internet connection.", "Networking"),
    ("What is phishing?", ["A type of fish","Fraudulent attempt to obtain sensitive data","A network protocol","A programming language"], 1, "Phishing is a fraudulent attempt to steal data.", "Networking"),
    ("What does SMTP stand for?", ["Simple Mail Transfer Protocol","Standard Mail Transfer Protocol","System Mail Transfer Protocol","Secure Mail Transfer Protocol"], 0, "SMTP = Simple Mail Transfer Protocol.", "Networking"),
    ("What is the full form of FTP?", ["File Transfer Protocol","Fast Transfer Protocol","File Transmission Process","File Transport Protocol"], 0, "FTP = File Transfer Protocol.", "Networking"),
    ("What does MAC address identify?", ["A website","A network interface","An email","A file"], 1, "MAC address identifies a network interface.", "Networking"),
    ("What is a proxy server?", ["A backup server","An intermediary server","A game server","A file server"], 1, "A proxy server acts as an intermediary.", "Networking"),
    ("What is a DDoS attack?", ["Distributed Denial of Service","Data Destruction on Server","Digital Defense of System","Direct Data Overload Service"], 0, "DDoS = Distributed Denial of Service.", "Networking"),
    # Programming basics (15)
    ("What is a variable in programming?", ["A fixed value","A named storage location","A type of function","A program output"], 1, "A variable is a named storage location.", "Programming"),
    ("What is a function in programming?", ["A mathematical equation","A reusable block of code","A type of variable","A file format"], 1, "A function is a reusable block of code.", "Programming"),
    ("What is a loop in programming?", ["A network cable","Repetition of code","A type of virus","A file system"], 1, "A loop repeats a block of code.", "Programming"),
    ("What does HTML stand for?", ["HyperText Markup Language","HighText Markup Language","HyperText Makeup Language","Hyper Transfer Markup Language"], 0, "HTML = HyperText Markup Language.", "Programming"),
    ("What is CSS used for?", ["Database management","Styling web pages","Server configuration","Network security"], 1, "CSS is used for styling web pages.", "Programming"),
    ("What is JavaScript?", ["A type of coffee","A programming language","A database","An operating system"], 1, "JavaScript is a programming language.", "Programming"),
    ("What is a bug in programming?", ["An insect","An error in code","A feature","A file type"], 1, "A bug is an error in code.", "Programming"),
    ("What is debugging?", ["Writing code","Finding and fixing errors","Designing interfaces","Testing hardware"], 1, "Debugging is finding and fixing errors.", "Programming"),
    ("What does IDE stand for?", ["Integrated Development Environment","Internal Development Engine","Integrated Design Environment","Interface Development Editor"], 0, "IDE = Integrated Development Environment.", "Programming"),
    ("What is an algorithm?", ["A programming language","A step-by-step procedure","A type of computer","A network protocol"], 1, "An algorithm is a step-by-step procedure.", "Programming"),
    ("What is a compiler?", ["Hardware device","Software that translates code","A web browser","An operating system"], 1, "A compiler translates source code to machine code.", "Programming"),
    ("What is an array?", ["A network","Collection of similar data items","A file format","A database"], 1, "An array is a collection of similar data items.", "Programming"),
    ("What does OOP stand for?", ["Object Oriented Programming","Online Operating Protocol","Open Output Process","Object Output Program"], 0, "OOP = Object Oriented Programming.", "Programming"),
    ("What is inheritance in OOP?", ["Money from parents","Acquiring properties of parent class","Creating new objects","Deleting objects"], 1, "Inheritance allows a class to acquire properties of another class.", "Programming"),
    ("What is a database query?", ["A question to user","A request for data from database","A network request","A file operation"], 1, "A query is a request for data from a database.", "Programming"),
]

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "it")

def build_set(questions, set_num, total_sets=7):
    shuffled = questions[:]
    random.seed(200 + set_num)
    random.shuffle(shuffled)
    start = ((set_num - 4) * 50) % len(shuffled)
    result = []
    for i in range(50):
        q, opts, corr, expl, sub = shuffled[(start + i) % len(shuffled)]
        result.append({"id": i+1, "question": q, "options": opts, "correctIndex": corr, "subject": sub, "explanation": expl})
    return result

for set_num in range(4, 11):
    en = build_set(IT_Q, set_num)
    ne = []
    for q in en:
        ne_q = q.copy()
        ne_q["options"] = q["options"][:]
        ne.append(ne_q)
    
    en_path = os.path.join(BASE_DIR, f"set{set_num}.json")
    ne_path = os.path.join(BASE_DIR, f"set{set_num}_ne.json")
    os.makedirs(BASE_DIR, exist_ok=True)
    
    with open(en_path, "w", encoding="utf-8") as f:
        json.dump(en, f, ensure_ascii=False, indent=2)
    with open(ne_path, "w", encoding="utf-8") as f:
        json.dump(ne, f, ensure_ascii=False, indent=2)
    
    print(f"Generated it/set{set_num}")

print("Done generating IT sets!")
