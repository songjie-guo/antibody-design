import os
import gzip
import numpy as np
from collections import defaultdict

import torch
import torch.nn.functional as F
from ProDesign.API.dataloader_gtrans import featurize_GTrans

AAMAP = {
    'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C', 'GLN': 'Q',
    'GLU': 'E', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K',
    'MET': 'M', 'PHE': 'F', 'PRO': 'P', 'SER': 'S', 'THR': 'T', 'TRP': 'W',
    'TYR': 'Y', 'VAL': 'V',
    'ASX': 'B', 'GLX': 'Z', 'SEC': 'U', 'PYL': 'O', 'XLE': 'J', '': '-'
}

def getSequence(resnames):
    """Returns polypeptide sequence as from list of *resnames* (residue
    name abbreviations)."""

    get = AAMAP.get
    return ''.join([get(rn, 'X') for rn in resnames])

def gzip_open(filename, *args, **kwargs):
    if args and "t" in args[0]:
        args = (args[0].replace("t", ""), ) + args[1:]
    if isinstance(filename, str):
        return gzip.open(filename, *args, **kwargs)
    else:
        return gzip.GzipFile(filename, *args, **kwargs)

def parsePDB(pdb, chain=['A']):
    title, ext = os.path.splitext(os.path.split(pdb)[1])
    title, ext = os.path.splitext(title)
    if pdb[-3:] == '.gz':
      pdb = gzip_open(pdb, 'rt')
      lines = defaultdict(list)
      for loc, line in enumerate(pdb):
          line = line.decode('ANSI_X3.4-1968')
          startswith = line[0:6]
          lines[startswith].append((loc, line))
    else:
      pdb = open(pdb)
      lines = defaultdict(list)
      for loc, line in enumerate(pdb):
          # line = line.decode('ANSI_X3.4-1968')
          startswith = line[0:6]
          lines[startswith].append((loc, line))


    pdb.close()

    sequence = ''

    CA_coords, C_coords, O_coords, N_coords = [], [], [], []

    # chain_id = []
    for idx, line in lines['ATOM  ']:
        if line[21:22].strip() not in chain:
            continue
        if line[13:16].strip() == 'CA':
            CA_coord = [float(line[30:38]), float(line[38:46]), float(line[46:54])]
            CA_coords.append(CA_coord)
            sequence += ''.join(getSequence([line[17:20]]))
        elif line[13:16].strip() == 'C':
            C_coord = [float(line[30:38]), float(line[38:46]), float(line[46:54])]
            C_coords.append(C_coord)
        elif line[13:16].strip() == 'O':
            O_coord = [float(line[30:38]), float(line[38:46]), float(line[46:54])]
            O_coords.append(O_coord)
        elif line[13:16].strip() == 'N':
            N_coord = [float(line[30:38]), float(line[38:46]), float(line[46:54])]
            N_coords.append(N_coord)



    return {'title': title,
            'seq': sequence,
            'CA': np.array(CA_coords),
            'C': np.array(C_coords),
            'O': np.array(O_coords),
            'N': np.array(N_coords),
            'score' : 100.0}

def pred(data,exp):
    with torch.no_grad():
        alphabet='ACDEFGHIKLMNPQRSTVWY'
        batch = featurize_GTrans([data])
        X, S, score, mask, lengths = batch # cuda(batch, device = exp.device)
        X, S, score, h_V, h_E, E_idx, batch_id, mask_bw, mask_fw, decoding_order = exp.method.model._get_features(S, score, X=X, mask=mask)
        log_probs, logits = exp.method.model(h_V, h_E, E_idx, batch_id, return_logit = True)

        temperature = 0.1
        probs = F.softmax(logits/temperature, dim=-1)
        S_pred = torch.multinomial(probs, 1).view(-1)

    recovery = torch.mean((S==S_pred).float())
    S_design = ''.join([alphabet[i] for i in S_pred])
    S_true = data['seq']

    return recovery, S_design, S_true

def pred_fasta(exp):
    input_pdb = 'cache/tmp.pdb'
    H_data = parsePDB(input_pdb, ['H'])
    H_recovery,H_pred,_ = pred(H_data,exp)
    L_data = parsePDB(input_pdb, ['L'])
    L_recovery,L_pred,_  = pred(L_data,exp)

    return H_pred,L_pred
