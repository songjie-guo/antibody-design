from igfold.utils.visualize import *
from igfold import IgFoldRunner

def pred_pdb(H_seq,L_seq,do_refine,do_renum,single_model):
    sequences = {'H':H_seq, 'L':L_seq}
    num_models = 1 if single_model else 4
    igfold = IgFoldRunner(num_models=num_models)
    output_pdb_path = 'cache/tmp.pdb'
    pred = igfold.fold(
        output_pdb_path,
        sequences=sequences,
        do_refine=do_refine,
        use_openmm=True,
        do_renum=do_renum,
    )
    return sequences, pred
