





























with open(r'C:\Users\HP\OneDrive\Desktop\c++\project_co\co_simulator\text.txt',"r") as f:
    data=f.readlines()
    for lines in data:
        l1.append(lines.strip())

for i in l1:
    opcode=i[25:]
    if opcode in r_opcode:
        r_func()
    if opcode in s_opcode:
        s_func()
    if opcode in i_opcode:
        i_func()
    if opcode in j_opcode:
        j_func()
    if opcode in b_opcode:
        b_func()
    if opcode in u_opcode:
        u_func()
