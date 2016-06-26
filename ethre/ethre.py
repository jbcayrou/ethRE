import argparse
import binascii
import logging
import sys

from miasm2.core import parse_asm, asmbloc
from miasm2.arch.evm.disasm import dis_evm, cb_evm_funcs
from miasm2.arch.evm.arch import mn_evm # Need : https://github.com/jbcayrou/miasm/tree/evm
from miasm2.analysis.machine import Machine
from miasm2.analysis.binary import Container



class ethRE:

    def __init__(self):
        self.machine = Machine("evm")
        self.mn = self.machine.mn

    def from_bytecode(self, bytecode):

        container = Container.from_string(bytecode)

        mdis = self.machine.dis_engine(container.bin_stream)
        self.blks = mdis.dis_multibloc(0)

    def from_asm(self, asm_text):
        all_bloc, symbol_pool = parse_asm.parse_txt(self.mn,0, asm_text)
        self.blks = all_bloc
        raise Exception("Not correctly implemented")

    def graph(self, out_file):
        if not self.blks:
            raise Exception("Need to parse bytecode before")
        open(out_file, "w").write(self.blks.dot())




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ethRE an Ethereum EVM Reverse Engineering tool')
    parser.add_argument("in_file",help="Binary bytecode to analyze")
    parser.add_argument("-asm", action="store_true", help="If input is test assembly")
    parser.add_argument("-hex", action="store_true", help="If input is in hexa")
    parser.add_argument("out_file",help="output file to save the dot graph")

    args = parser.parse_args()

    f = open(args.in_file)
    code = f.read()
    code = code.strip()

    if(args.hex):
        code = binascii.unhexlify(code)

    re = ethRE()

    if(args.asm):
        re.from_asm(code)
    else:
        re.from_bytecode(code)

    re.graph(args.out_file)