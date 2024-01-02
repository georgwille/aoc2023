# this is still very slow
# idea: make a recursive version that splits intervall
# and treats the halves as needed

rules_raw, parts = open('input_19.txt').read().split('\n\n')

rules = {}

for rule_raw in rules_raw.split('\n'):
    l = rule_raw.index('{')
    r = rule_raw.index('}')
    rule_n = rule_raw[:l]
    rules[rule_n] = []
    for subrule in rule_raw[l+1:r].split(','):
        if ':' not in subrule:
            rules[rule_n].append(subrule)
        else:
            q,r = subrule.split(':')
            var = q[0]
            comp = q[1]
            num = int(q[2:])
            rules[rule_n].append((':',var,comp,num,r))


x_tab = [1, 4001]
m_tab = [1, 4001]
a_tab = [1, 4001]
s_tab = [1, 4001]

for rulename, rulecontent in rules.items():
    for subrule in rulecontent:
        if ':' not in subrule:
            continue
        var,comp,number = subrule[1:-1]
        if var == 'x':
            if comp == '<':
                x_tab.append(number)
            else:
                x_tab.append(number+1)
        if var == 'm':
            if comp == '<':
                m_tab.append(number)
            else:
                m_tab.append(number+1)
        if var == 'a':
            if comp == '<':
                a_tab.append(number)
            else:
                a_tab.append(number+1)
        if var == 's':
            if comp == '<':
                s_tab.append(number)
            else:
                s_tab.append(number+1)

x_tab = list(set(x_tab))
x_tab.sort()

m_tab = list(set(m_tab))
m_tab.sort()

a_tab = list(set(a_tab))
a_tab.sort()

s_tab = list(set(s_tab))
s_tab.sort()

results={}
acceptcount = 0

print(x_tab)

for idx_x, x in enumerate(x_tab[:-1]):
    xsize = x_tab[idx_x+1] - x
    for idx_m, m in enumerate(m_tab[:-1]):
        msize = m_tab[idx_m+1] - m
        print(x,m,end='\r')
        for idx_a, a in enumerate(a_tab[:-1]):
            asize = a_tab[idx_a+1] - a
            for idx_s, s in enumerate(s_tab[:-1]):
                ssize = s_tab[idx_s+1] - s
                fsize = xsize*msize*asize*ssize

                current_rule = 'in'
                processing_running = True
                while processing_running:
                    for subrule in rules[current_rule]:
                        if subrule == 'R':
                            processing_running = False
                            break
                        if subrule == 'A':
                            processing_running = False
                            acceptcount += fsize
                            break
                        if ':' not in subrule:
                            current_rule = subrule
                            break
                        var, comp, num, r = subrule[1:]
                        if var == 'x':
                            if (comp == '>' and x > num) or (comp == '<' and x < num):
                                if r == 'R':
                                    processing_running = False
                                    break
                                if r == 'A':
                                    processing_running = False
                                    acceptcount += fsize
                                    break
                                current_rule = r
                                break
                        if var == 'm':
                            if (comp == '>' and m > num) or (comp == '<' and m < num):
                                if r == 'R':
                                    processing_running = False
                                    break
                                if r == 'A':
                                    processing_running = False
                                    acceptcount += fsize
                                    break
                                current_rule = r
                                break
                        if var == 'a':
                            if (comp == '>' and a > num) or (comp == '<' and a < num):
                                if r == 'R':
                                    processing_running = False
                                    break
                                if r == 'A':
                                    processing_running = False
                                    acceptcount += fsize
                                    break
                                current_rule = r
                                break
                        if var == 's':
                            if (comp == '>' and s > num) or (comp == '<' and s < num):
                                if r == 'R':
                                    processing_running = False
                                    break
                                if r == 'A':
                                    processing_running = False
                                    acceptcount += fsize
                                    break
                                current_rule = r
                                break

print(acceptcount)
