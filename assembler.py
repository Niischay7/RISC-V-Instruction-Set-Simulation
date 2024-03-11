import sys
program_counter=0
error1=" "
pc=-1
flag=0
def complement(binarynumber):
    ans = ""
    while binarynumber and binarynumber[-1] != "1":
        ans = binarynumber[-1] + ans
        binarynumber = binarynumber[0:-1]
    ans = binarynumber[-1] + ans
    binarynumber = binarynumber[0:-1]

    while binarynumber:
        if binarynumber[-1] == "0":
            ans = "1" + ans
        elif binarynumber[-1] == "1":
            ans = "0" + ans
        binarynumber = binarynumber[0:-1]
    return ans

def decimal_binary_32bits(b):
    a=int(b)
    if a>0:
        ans=""
        cnt=0
        while(a!=0):
            ans = str(a%2)+ans
            a = a//2
            cnt+=1
        ans="0"*(32-cnt)+ans
        return ans
    elif a==0:
        answer=32*"0"
        return answer
    elif a<0:
        a=abs(a)
        ans=""
        cnt=0
        while(a!=0):
            ans = str(a%2)+ans
            a = a//2
            cnt+=1
        ans="0"*(32-cnt)+ans
        ans=complement(ans)
    return ans

opcode_R = {"add":"0110011","sub":"0110011","sll":"0110011","slt":"0110011","sltu":"0110011","xor":"0110011","srl":"0110011","or":"0110011","and":"0110011"}
R_func7={"add":"0000000", "sub":"0100000", "sll":"0000000", "slt":"0000000", "sltu":"0000000", "xor":"0000000", "srl":"0000000", "or":"0000000", "and":"0000000"}
R_func3={"add":"000", "sub":"000", "sll":"001","slt":"010","sltu":"011","xor":"100","srl":"101","or":"110","and":"111"}
list_R = ["add","sub","sll","slt","sltu","xor","srl","or","and"]


opcode_I={"lw":"0000011","addi":"0010011","sltiu":"0010011","jalr":"1100111"}
I_func3={"lw":"010","addi":"000","sltiu":"011","jalr":"000"}
list_I=["lw","addi","sltiu","jalr"]

opcode_B={"beq":"1100011","bne":"1100011","blt":"1100011","bge":"1100011","bltu":"1100011","bgeu":"1100011"}
list_B=["beq","bne","blt","bge","bltu","bgeu"]
B_func3={"beq":"000","bne":"001","blt":"100","bge":"101","bltu":"110","bgeu":"111"}

opcode_S={"sw":"0100011"}
S_func3={"sw":"010"}
list_S=["sw"]

opcode_U={"lui":"011011", "auipc": "0010111"}
list_U=["lui","auipc"]

opcode_J={"jal":"1101111"}
list_J=["jal"]


register_encoding = {"zero": "00000","ra":"00001","sp":"00010","gp":"00011","tp":"00100","t0":"00101","t1":"00110","t2":"00111","s0":"01000","fp":"01000","s1":"01001","a0":"01010","a1":"01011","a2":"01100","a3":"01101","a4":"01110","a5":"01111","a6":"10000","a7":"10001","s2":"10010","s3":"10011","s4":"10100","s5":"10101","s6":"10110","s7":"10111","s8":"11000","s9":"11001","s10":"11010","s11":"11011","t3":"11100","t4":"11101","t5":"11110","t6":"11111"}
def func_U(instruction):
    global program_counter
    try:

        answer=""
        imm_bin=decimal_binary_32bits(instruction[2])
        answer= imm_bin[:-11]+register_encoding[instruction[1]] +opcode_U[instruction[0]]
        program_counter+=4
        return answer
    except: 
        global program_counter
        flag=1
        error1="no operation belongs to the above code snippet error in"
        pc=program_counter
        
def func_R(instruction):
    global program_counter
    try:
        answer = ""
        answer=R_func7[instruction[0]]+register_encoding[instruction[3]]+register_encoding[instruction[2]]+R_func3[instruction[0]]+register_encoding[instruction[1]]+opcode_R[instruction[0]]
        program_counter+=4
        return answer
    except:
        global program_counter
        flag=1
        error1="no operation belongs to the above code snippet error in"
        pc=program_counter

