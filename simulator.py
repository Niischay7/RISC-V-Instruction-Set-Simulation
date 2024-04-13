registers = {
    'x0': '00000',
    'x1': '00001',
    'x2': '00010',
    'x3': '00011',
    'x4': '00100',
    'x5': '00101',
    'x6': '00110',
    'x7': '00111',
    'x8': '01000',
    'x9': '01001',
    'x10': '01010',
    'x11': '01011',
    'x12': '01100',
    'x13': '01101',
    'x14': '01110',
    'x15': '01111',
    'x16': '10000',
    'x17': '10001',
    'x18': '10010',
    'x19': '10011',
    'x20': '10100',
    'x21': '10101',
    'x22': '10110',
    'x23': '10111',
    'x24': '11000',
    'x25': '11001',
    'x26': '11010',
    'x27': '11011',
    'x28': '11100',
    'x29': '11101',
    'x30': '11110',
    'x31': '11111'
}


registers['zero'] = registers['x0']  # Hard-wired zero
registers['ra'] = registers['x1']    # Return address
registers['sp'] = registers['x2']    # Stack Pointer
registers['gp'] = registers['x3']    # Global Pointer
registers['tp'] = registers['x4']    # Thread Pointer
registers['t0'] = registers['x5']    # Temporary/alternate link register
registers['t1'] = registers['x6']    # Temporary register
registers['t2'] = registers['x7']    # Temporary register
registers['s0'] = registers['x8']    # Saved register/frame pointer
registers['s1'] = registers['x9']    # Saved Register
registers['a0'] = registers['x10']   # Function argument/return value
registers['a1'] = registers['x11']   # Function argument/return value
registers['a2'] = registers['x12']   # Function argument
registers['a3'] = registers['x13']   # Function argument
registers['a4'] = registers['x14']   # Function argument
registers['a5'] = registers['x15']   # Function argument
registers['a6'] = registers['x16']   # Function argument
registers['a7'] = registers['x17']   # Function argument
registers['s2'] = registers['x18']   # Saved register
registers['s3'] = registers['x19']   # Saved register
registers['s4'] = registers['x20']   # Saved register
registers['s5'] = registers['x21']   # Saved register
registers['s6'] = registers['x22']   # Saved register
registers['s7'] = registers['x23']   # Saved register
registers['s8'] = registers['x24']   # Saved register
registers['s9'] = registers['x25']   # Saved register
registers['s10'] = registers['x26']  # Saved register
registers['s11'] = registers['x27']  # Saved register
registers['t3'] = registers['x28']   # Temporary register
registers['t4'] = registers['x29']   # Temporary register
registers['t5'] = registers['x30']   # Temporary register
registers['t6'] = registers['x31']   # Temporary register





























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
