#LANG

##What is this?

This is a playground for tinkering with and learning about lexers, parsers, virtual machines, etc. It began as a virtual machine that ran a bytecode-language with 3 instructions. Several more have been added, bringing the total for the virtual machine up to 10 (See *VM*).

The project draws inspiration from @charliesome's twostroke javascript implementation among others.

It currently houses two separate but related projects which may be joined in the future. 

1. VM - a simple virtual machine
2. Everything else - a lexer and parser that generates an AST for a currently unspecified higher-level language

##VM

The virtual machine is stack-based and currently has 10 instructions that operate on the stack. All values are floating-point numbers, just like the One True Language.

- `set`
    Associates the symbol given with the stack's top value
    
    **Usage**: `set #hello`
        
    
- `get`
    Pushes the value associated with the given symbol onto the stack to be used in further operations
    
    **Usage**: `get #hello`
        
    
- `push`
    Pushes the given number onto the stack to be used in further operations. Can also be used as an alias for `get`
    
    **Usage**: `push 42`

- `mul`
    Multiplies the top two values on the stack and pushes the product
    
- `add`
    Adds the top two values on the stack and pushes the sum
    
- `sub`
    Subtracts the second value on the stack from the top value and pushes the difference
    
- `print`
    Prints either a string literal or the value of a variable to standard output

- `rjmp`
    Relative Jump - Adds the given value to the instruction pointer and explodes if the new IP is greater than the length of the code
    
- `jmp`
    Unconditional Jump - Sets IP to given address

- `jmpne`
    Conditional Jump - Sets IP to given address if top 2 values on the stack are not equal
    
    
##Parser, Lexer, and AST
- Single line comments begin with a hash (e.g. `#blah blah`)
- Multi line comments begin with `/#` and end with `#/`

Current Parser Output for `expression_test.txt`:

```
<lang.ast.binary_ops.Addition object at 0x108622d30>
  <lang.ast.binary_ops.Division object at 0x108622438>
    <lang.ast.primitives.Number object at 0x10861ec88>
    <lang.ast.primitives.Number object at 0x10861e9e8>
  <lang.ast.binary_ops.Multiplication object at 0x108622cf8>
    <lang.ast.binary_ops.Multiplication object at 0x108622cc0>
      <lang.ast.binary_ops.Addition object at 0x108622978>
        <lang.ast.primitives.Number object at 0x1086074e0>
        <lang.ast.primitives.Number object at 0x108622908>
      <lang.ast.symbol.Symbol object at 0x1086229b0>
    <lang.ast.binary_ops.Multiplication object at 0x108622da0>
      <lang.ast.primitives.Number object at 0x108622940>
      <lang.ast.primitives.Number object at 0x108622128>
```
todo

##Contributing
If you know nothing about language design and implementation, it is likely you know
more than me, so any contributions, whether code, advice, or anything else, are more than welcome.
