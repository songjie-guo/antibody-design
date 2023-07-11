from scalop.predict import assign

def cut_CDR(H_seq,L_seq,num_scheme,def_scheme):
    H_cut = assign(H_seq,num_scheme,def_scheme)[0]['outputs']
    H1 = H_cut['H1'][1]
    H2 = H_cut['H2'][1]

    # if chothia
    H3 = get_H3(H_seq,H2,def_scheme)

    L_cut = assign(L_seq,num_scheme,def_scheme)[0]['outputs']
    L1 = L_cut['L1'][1]
    L2 = L_cut['L2'][1]
    L3 = L_cut['L3'][1]

    H_parts = get_nonCDR(H_seq,H1,H2,H3)
    L_parts = get_nonCDR(L_seq,L1,L2,L3)

    H_cutting = {'CDR1':H1,'CDR2':H2,'CDR3':H3,'other_parts':H_parts}
    L_cutting = {'CDR1':L1,'CDR2':L2,'CDR3':L3,'other_parts':L_parts}

    return H_cutting,L_cutting


def get_H3(H_seq,H2,def_scheme):
    if def_scheme != "chothia":
        return
    after_H2 = H_seq.split(H2)[1]
    H3_ = after_H2.split('C')[1][2:]
    H3 = H3_.split('WG')[0]
    return H3

def get_nonCDR(seq,cdr1,cdr2,cdr3):
    cdr1_start = seq.find(cdr1)
    cdr1_end = cdr1_start + len(cdr1)
    cdr2_start = seq.find(cdr2)
    cdr2_end = cdr2_start + len(cdr2)
    cdr3_start = seq.find(cdr3)
    cdr3_end = cdr3_start + len(cdr3)

    part1_seq = seq[:cdr1_start]
    part2_seq = seq[cdr1_end:cdr2_start]
    part3_seq = seq[cdr2_end:cdr3_start]
    part4_seq = seq[cdr3_end:]
    
    parts = [part1_seq,part2_seq,part3_seq,part4_seq]
    return parts