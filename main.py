import os

from igfold.utils.visualize import *
from models.pifold_model import exp
from models.CDR import cut_CDR
from models.predPDB import pred_pdb
from models.predFasta import pred_fasta
from models.replace import replace

########################## list all params ############################
H_seq = 'QVQLQESGPGLVAPSQSLSITCTVSGFSLTGYGVNWVRQPPGKGLEWLGMIWGDGNTDYNSALKSRLSISKDNSKSQVFLKMNSLHTDDTARYYCARERDYRLDYWGQGTTLTVSS'
L_seq = 'DIVLTQSPASLSASVGETVTITCRASGNIHNYLAWYQQKQGKSPQLLVYYTTTLADGVPSRFSGSGSGTQYSLKINSLQPEDFGSYYCQHFWSTPRTFGGGTKLEIK'

print(os.getcwd())

# cache_path = '/data/project/cache'
# result_path = '/data/project/results'

# num_loops = 10

# num_scheme = 'chothia'
# def_scheme = 'chothia'

# if_H1 = True
# if_H2 = True
# if_H3 = True
# if_L1 = True
# if_L2 = True
# if_L3 = True

# # paths
# import sys
# sys.path.append('/data/project/models/ProDesign')
# sys.path.append('/data/project/models')

# # igfold model params
# do_refine = True # Perform structural refinement with OpenMM
# do_renum = False # Renumber predicted antibody structure (Chothia) with AbNumber
# single_model = False # Use only a single model for predictions (instead of model ensemble)

# # create model for pifold
# model = exp
# # cut H&L
# H_cutting,L_cutting = cut_CDR(H_seq,L_seq,num_scheme,def_scheme)


# def run_a_loop(i):
#     # for a loop
#     sequences, pred = pred_pdb(H_seq,L_seq,do_refine,do_renum,single_model)
#     # get_rmsd
#     prmsd_fig_file = f'{result_path}/pdb/prmsd{i}.png'
#     plot_prmsd(sequences, pred.prmsd.cpu(), prmsd_fig_file, shade_cdr=do_renum, pdb_file=pred_pdb)
    
#     # get_fasta_pred
#     H_tmp,L_tmp = pred_fasta(model)
#     H_pred,L_pred = replace(H_cutting,L_cutting,H_tmp,L_tmp,
#                             if_H1 = True,
#                             if_H2 = True,
#                             if_H3 = True,
#                             if_L1 = True,
#                             if_L2 = True,
#                             if_L3 = True)
#     # store fasta_file
#     fasta_file = f'{result_path}/fasta/pred{i}.fasta'
#     with open(fasta_file, "w") as f:
#         f.write(f'>:H\n')
#         f.write(H_pred+'\n')
#         f.write(f'>:L\n')
#         f.write(L_pred+'\n')
    
#     # store pdb_file
#     if (i-1)>=0:
#         import shutil
#         src_file = '/data/project/cache/tmp.pdb'
#         dest_folder = f'/data/project/results/pdb/pred{i-1}.pdb'
#         shutil.move(src_file, dest_folder)

#     return H_pred,L_pred

# for i in range(num_loops):
#     H_seq,L_seq = run_a_loop(i)