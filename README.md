# ethRE

Reverse Engineering tool for Ethereum EVM.
It is based on miasm add need evm implementation https://github.com/jbcayrou/miasm/tree/evm


Example:
```python
python ethre/ethre.py ./example/in.hex ./mygraph.dot -hex
xdot ./mygraph.dot
```


Features
---------
* Disassemble EVM bytecode from binary of hexadecimal representation
* Resolve simple JUMP/JUMPI (search PUSH xxxxx JUMP pattern)


TODO
-----
* Add support of text asm
* Get bytecode from ethereum blockchain
* Semantic analysis (need improve the miasm implementation)
* Detect functions with contract ABI declaration
* Execution with Miasm emulation
* Contract execution replay
* Pattern vulnerability detection
