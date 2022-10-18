def check_relation(net, first, second):
    if first == second:
        return True
    len_net = len(net)
    for i in range(len_net):
        if second in net[i]:
            if second ==net[i][0]:
                a = check_relation(net[0:i] + net[i + 1:], first, net[i][1])
            else:
                a = check_relation(net[0:i] + net[i + 1:], first, net[i][0])
            if a:
                return True
    return False
