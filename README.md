# ethRE

Reverse Engineering tool for Ethereum EVM.
It is based on miasm and needs EVM architecture implementation https://github.com/jbcayrou/miasm/tree/evm


Example:
```python
python ethre/ethre.py -x./example/in.hex -o ./mygraph.dot
xdot ./mygraph.dot

python ethre/ethre.py --account 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae -o ./mygraph.dot
```


Features
---------
* Disassemble EVM bytecode from binary or from hexadecimal representation
* Resolve simple JUMP/JUMPI (search PUSH xxxxx JUMP pattern)
* Get bytecode from ethereum blockchain (`--account` argument)


TODO
-----
* Add support of text asm
* Add Semantic analysis (need improve the miasm implementation)
* Detect functions with contract ABI declaration
* Execution with Miasm emulation
* Contract execution replay
* Pattern vulnerability detection
