rules_raw, parts = open('input_19.txt').read().split('\n\n')

rules = {}

for rule_raw in rules_raw.split('\n'):
    l = rule_raw.index('{')
    r = rule_raw.index('}')
    rule_n = rule_raw[:l]
    rules[rule_n] = rule_raw[l+1:r].split(',')

acceptcount = 0

for part in parts.strip().split('\n'):
    for sub in part[1:-1].split(','):
        if sub.startswith('x'):
            x = int(sub[2:])
        elif sub.startswith('m'):
            m = int(sub[2:])
        elif sub.startswith('a'):
            a = int(sub[2:])
        elif sub.startswith('s'):
            s = int(sub[2:])
        else:
            assert False, "unexpected attribute"
    current_rule = 'in'
    processing_running = True
    while processing_running:
        for subrule in rules[current_rule]:
            if subrule == 'R':
                processing_running = False
                break
            if subrule == 'A':
                processing_running = False
                acceptcount += x+m+a+s
                break
            if ':' not in subrule:
                current_rule = subrule
                break
            q,r = subrule.split(':')
            if eval(q):
                if r == 'R':
                    processing_running = False
                    break
                if r == 'A':
                    processing_running = False
                    acceptcount += x+m+a+s
                    break
                current_rule = r
                break

print(acceptcount)
