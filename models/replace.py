def  replace(H_cutting,L_cutting,H_tmp,L_tmp,
                        if_H1 = True,
                        if_H2 = True,
                        if_H3 = True,
                        if_L1 = True,
                        if_L2 = True,
                        if_L3 = True):
    seq_name_list = ['CDR1','CDR2','CDR3']
    if_Hseq_list = [if_H1,if_H2,if_H3]
    if_Lseq_list = [if_L1,if_L2,if_L3]
    
    H_tmp_cut = cut(H_tmp,H_cutting)
    L_tmp_cut = cut(L_tmp,L_cutting)

    for i in range(3):
        seq_name = seq_name_list[i]
        if_Hseq = if_Hseq_list[i]
        if_Lseq = if_Lseq_list[i]
        if if_Hseq:
            H_cutting[seq_name] = H_tmp_cut[i]
        if if_Lseq:
            L_cutting[seq_name] = L_tmp_cut[i]

    H_pred = form(H_cutting)
    L_pred = form(L_cutting)

    return H_pred,L_pred

def cut(tmp_seq,cutting):
    part1_seq,part2_seq,part3_seq,part4_seq = cutting['other_parts']
    cdr1_start = len(part1_seq)
    cdr1_end = cdr1_start + len(cutting['CDR1'])
    cdr2_start = cdr1_end + len(part2_seq)
    cdr2_end = cdr2_start + len(cutting['CDR2'])
    cdr3_start = cdr2_end + len(part3_seq)
    cdr3_end = cdr3_start + len(cutting['CDR3'])

    cdr1 = tmp_seq[cdr1_start:cdr1_end]
    cdr2 = tmp_seq[cdr2_start:cdr2_end]
    cdr3 = tmp_seq[cdr3_start:cdr3_end]
    return cdr1,cdr2,cdr3

def form(cutting):
    cdr1 = cutting['CDR1']
    cdr2 = cutting['CDR2']
    cdr3 = cutting['CDR3']
    part1_seq,part2_seq,part3_seq,part4_seq = cutting['other_parts']
    return part1_seq+cdr1+part2_seq+cdr2+part3_seq+cdr3+part4_seq
