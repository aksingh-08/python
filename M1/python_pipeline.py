import ast
import dis
source = "result = sum(range(5))"

# Stage 1:Source
print("=== STAGE 1: Source Code ===")
print(source)

# Stage 2: AST
print("\n=== STAGE 2: Abstract Syntax Tree ===")
tree = ast.parse(source)
print(ast.dump(tree, indent=2))

# Stage 3:Bytecode
print("\n=== STAGE 3: Bytecode ===")
code_obj = compile(source, "<string>", "exec")
dis.dis(code_obj)

# Stage 4: Execution
print("\n=== STAGE 4: Execution ===")
namespace = {}
exec(code_obj, namespace)
print(f"result = {namespace['result']}")

# Source Code (.py) -> Tokenizer/Parser -> AST -> Compiler -> Bytecode (.pyc) -> PVM (executes)
# 
# 1. Source code: The .py text file you write.
# 2. AST (Abstract Syntax Tree): The parser converts tokens into a tree structure.
#   ast.parse() exposes this. Each node represents a language construct (assignment, function call, binary operation).
#   The AST is what linters and code formatters operate on.
# 3. Bytecode: The compiler walks the AST and emits a flat sequence of bytecode
#   instructions (a code object). This is what gets cached in .pyc files. compile() does this step.
# 4. PVM execution: The Python Virtual Machine reads bytecode instructions one by one,
#   using a stack-based evaluation model. LOAD_NAME pushes values, CALL_FUNCTION invokes callables, STORE_NAME binds results to names.
# 