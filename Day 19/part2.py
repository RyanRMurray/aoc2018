#operations
ops = {
    'addi' : (lambda reg, instr : reg[instr[0]] + instr[1]),
    'addr' : (lambda reg, instr : reg[instr[0]] + reg[instr[1]]),
    'muli' : (lambda reg, instr : reg[instr[0]] * instr[1]),
    'mulr' : (lambda reg, instr : reg[instr[0]] * reg[instr[1]]),
    'bani' : (lambda reg, instr : reg[instr[0]] & instr[1]),
    'banr' : (lambda reg, instr : reg[instr[0]] & reg[instr[1]]),
    'bori' : (lambda reg, instr : reg[instr[0]] | instr[1]),
    'borr' : (lambda reg, instr : reg[instr[0]] | reg[instr[1]]),
    'seti' : (lambda reg, instr : instr[0]),
    'setr' : (lambda reg, instr : reg[instr[0]]),
    'gtri' : (lambda reg, instr : (1 if reg[instr[0]] > instr[1] else 0)),
    'gtir' : (lambda reg, instr : (1 if instr[0] > reg[instr[1]] else 0)),
    'gtrr' : (lambda reg, instr : (1 if reg[instr[0]] > reg[instr[1]] else 0)),
    'eqri' : (lambda reg, instr : (1 if reg[instr[0]] == instr[1] else 0)),
    'eqir' : (lambda reg, instr : (1 if instr[0] == reg[instr[1]] else 0)),
    'eqrr' : (lambda reg, instr : (1 if reg[instr[0]] == reg[instr[1]] else 0))
}

def get_input(f_path):
    input = open(f_path, 'r')
    instructions = []
    ip = int(input.readline()[3:-1])

    for line in input:
        instructions.append([
            line[0:4],
            [int(x) for x in line.rstrip()[5:].split(' ')]
        ])
    return [ip, instructions]

def div_sum(n):
    div_sum = 0
    limit = (n / 2) + 2
    for i in range(1, limit):
        if n % i == 0:
            div_sum += i
    return div_sum


def simulate(init_state):
    input = get_input('input.txt')
    registers = [init_state,0,0,0,0,0]
    instructions = input[1] #[code,[instruction]]
    ip_reg = input[0]
    ip = 0

    while ip < len(instructions):
        instr = instructions[ip]
        registers[ip_reg] = ip
        registers[instr[1][2]] = ops[instr[0]](registers, instr[1])
        ip = registers[ip_reg] + 1
        if instr[1][2] == 0:
            print('bigger output:', max(registers) + div_sum(max(registers)))
            break

    print('output:', registers)

def main():
    simulate(1)
main()
