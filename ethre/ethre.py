import argparse
import binascii
import logging
import sys

from miasm2.core import parse_asm, asmbloc
from miasm2.arch.evm.disasm import dis_evm, cb_evm_funcs
from miasm2.arch.evm.arch import mn_evm # Need : https://github.com/jbcayrou/miasm/tree/evm
from miasm2.arch.evm.env import evm_env
from miasm2.analysis.machine import Machine
from miasm2.analysis.binary import Container



class ethRE:

    def __init__(self):
        self.machine = Machine("evm")
        self.mn = self.machine.mn

    def get_bytecode(self, account_addr):
        code = evm_env.code(int(account_addr[2:],16))
        code = code[2:] # To remove '0x'..
        if len(code) % 2 == 1:
            code  = "0"+code
        code = binascii.unhexlify(code)
        return code

    def from_bytecode(self, bytecode):

        container = Container.from_string(bytecode)

        mdis = self.machine.dis_engine(container.bin_stream)
        self.blks = mdis.dis_multibloc(0)

    def from_asm(self, asm_text):
        all_bloc, symbol_pool = parse_asm.parse_txt(self.mn,0, asm_text)
        self.blks = all_bloc
        raise Exception("Not correctly implemented")

    def graph(self):
        if not self.blks:
            raise Exception("Need to parse bytecode before")
        return self.blks.dot()




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ethRE an Ethereum EVM Reverse Engineering tool')
    parser.add_argument('-i','--file',help="Input binary bytecode file to analyze")
    parser.add_argument("-x" ,"--file-hex",help="Input binary bytecode file to analyze in ascii hexadecimal format")
    parser.add_argument("-a" ,"--account",help="Ethereum contract account to get the bytecode")
    parser.add_argument("-o" ,"--output",help="output file to save the dot graph")

    args = parser.parse_args()
    re = ethRE()

    if args.file:
        f = open(args.file)
        code = f.read()
        code = code.strip()

    if args.file_hex:
        f = open(args.file_hex)
        code = f.read()
        code = code.strip()
        code = binascii.unhexlify(code)
    elif args.account:
        code = re.get_bytecode(args.account)

    re.from_bytecode(code)

    g = re.graph()

    if args.output:
        open(args.output, "w").write(g)
    else:
        print g
