def write_ticket(line):
    file_name="Json_Changes"
    extention = ".txt"
    name = file_name + extention
    try:
        file = open(name,"r")
        lines = file.readlines()
        file.close()
        file_w = open(name, "a")
        if len(lines) == 1:
            file_w.writeline(line+"\n")         
        else:
            file_w.write(line+"\n")
        print("Added to "+ file_name+": "+line)
        file_w.close()
    
    except:
            file_a = open(name, "a")
            file_a.write(line+"\n")
            print("Added to "+ file_name+": "+line)
            file_a.close()
