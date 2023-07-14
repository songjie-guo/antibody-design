# download codes/data 
import os,sys
os.chdir('./models')

def get_parser():
  import argparse
  parser = argparse.ArgumentParser()
  # Set-up parameters
  parser.add_argument('--device', default='cpu', type=str, help='Name of device to use for tensor computations (cuda/cpu)')
  parser.add_argument('--display_step', default=10, type=int, help='Interval in batches between display of training metrics')
  parser.add_argument('--res_dir', default='ProDesign/results', type=str)
  parser.add_argument('--ex_name', default='ProDesign', type=str)
  parser.add_argument('--use_gpu', default=False, type=bool)
  parser.add_argument('--gpu', default=0, type=int)
  parser.add_argument('--seed', default=111, type=int)

  # CATH
  # dataset parameters
  parser.add_argument('--data_name', default='CATH', choices=['CATH', 'TS50'])
  parser.add_argument('--data_root', default='ProDesign/data/')
  parser.add_argument('--batch_size', default=8, type=int)
  parser.add_argument('--num_workers', default=8, type=int)

  # method parameters
  parser.add_argument('--method', default='ProDesign', choices=['ProDesign'])
  parser.add_argument('--config_file', '-c', default=None, type=str)
  parser.add_argument('--hidden_dim',  default=128, type=int)
  parser.add_argument('--node_features',  default=128, type=int)
  parser.add_argument('--edge_features',  default=128, type=int)
  parser.add_argument('--k_neighbors',  default=30, type=int)
  parser.add_argument('--dropout',  default=0.1, type=int)
  parser.add_argument('--num_encoder_layers', default=10, type=int)

  # Training parameters
  parser.add_argument('--epoch', default=100, type=int, help='end epoch')
  parser.add_argument('--log_step', default=1, type=int)
  parser.add_argument('--lr', default=0.001, type=float, help='Learning rate')
  parser.add_argument('--patience', default=100, type=int)

  # ProDesign parameters
  parser.add_argument('--updating_edges', default=4, type=int)
  parser.add_argument('--node_dist', default=1, type=int)
  parser.add_argument('--node_angle', default=1, type=int)
  parser.add_argument('--node_direct', default=1, type=int)
  parser.add_argument('--edge_dist', default=1, type=int)
  parser.add_argument('--edge_angle', default=1, type=int)
  parser.add_argument('--edge_direct', default=1, type=int)
  parser.add_argument('--virtual_num', default=3, type=int)
  args = parser.parse_args([])
  return args

import sys
sys.path.append(sys.path[0]+'/models/ProDesign')
sys.path.append(sys.path[0]+'/models')

from ProDesign.main import Exp
args = get_parser()
exp = Exp(args)

os.chdir('../')
