import subprocess
import datetime

numerals = open("roman","r")
count = 0
report = open("report "+str(datetime.datetime.now()),"a")
err_dec=[]
err_oct=[]
err_hex=[]

for line in numerals:
    s =  line.split("=")
    
    number = s[0]
    expected = s[1]
    octal = str(oct(int(s[0])))
    octal = '0x'+octal[2:]
    hexal = str(hex(int(s[0])))
    hexal = '0X'+hexal[2:]
    
    result = subprocess.check_output(["./a.out",str(number)]).decode("UTF-8")
    if expected != result:
        err_dec.append("number decimal: %s. expected: %s got: %s" %(number,expected,result))
        
    result2 = subprocess.check_output(["./a.out",str(octal)]).decode("UTF-8")
    if expected != result2:
        err_oct.append("number octal: %s (%s). expected: %s got: %s" %(number,octal,expected, result2))
        
    result3 = subprocess.check_output(["./a.out",str(hexal)]).decode("UTF-8")
    if expected != result3:
        err_hex.append("number hexal: %s (%s). expected: %s got: %s" %(number,hexal,expected, result3))

errors = [err_dec,err_oct,err_hex]

for item in errors:
    for err in item:
        report.write(err)
        
print("Report finished. Found %d unexpected results."% (len(err_dec) + len(err_oct) + len(err_hex)))


    
    
