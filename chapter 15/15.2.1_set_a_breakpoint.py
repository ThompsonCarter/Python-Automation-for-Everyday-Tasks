import pdb

def calc_total(prices):
    pdb.set_trace()          # <— execution pauses here
    return sum(prices)

print(calc_total([19.9, 4.5, -2]))
(Pdb) prompt appears:

n next line
s step into
p variable print
c continue
q quit