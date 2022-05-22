def interpret(command: str) -> str:
    # for i in range(0, len(str)):
    command = command.replace('()', 'o')
    command = command.replace('(al)', 'al')
    print(command)

test_target = command = "(al)G(al)()()G"
test = interpret(test_target)
