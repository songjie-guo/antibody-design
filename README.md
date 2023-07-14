# antibody-design

## Intro
We use the idea of "sequence-structure-sequence" to design a new antibody. In the "sequence-structure" and "structure-sequence", we use IgFold and PiFold separately.

To maintain a reasonable 2/3D structure of the antibody, our design restricts the changes of CDR regions only.

As a result, we generate new antibody structures and sequences, providing potentially better solutions. Subsequent work can implement docking (e.g. HADDOCK) to evaluate the new binding between antibodies and antigens.

If you are interested in getting antibody and antigen data pairs, please check my repo bio-data [https://github.com/songjie-guo/bio-data.git].

## Try it!
You can try the python noteboook in Google Colab below. 

<a href="https://colab.research.google.com/drive/1DCNtI3ov0weBPXnsrvthyyd4xOR6EORm#scrollTo=qZLWE2jbUe0M?usp=sharing" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

A sample result folder is uploaded. Please check `sample_result.zip`

NOTE: 

- The `pred_ori.pdb` is the predicted pdb of the original H/L sequences you input, with the related `prmsd_ori.png`.
- The `pred0.pdb`, `pred0.fasta` are all results after the 1st re-design and so on.

## Citation
Credit to "IgFold" and "PiFold" used in this repositry. 

```bibtex
@article{ruffolo2023fast,
  title={Fast, accurate antibody structure prediction from deep learning on massive set of natural antibodies},
  author={Ruffolo, Jeffrey A and Chu, Lee-Shin and Mahajan, Sai Pooja and Gray, Jeffrey J},
  journal={Nature communications},
  volume={14},
  number={1},
  pages={2389},
  year={2023},
  publisher={Nature Publishing Group UK London}
}
@article{ruffolo2021deciphering,
    title = {Deciphering antibody affinity maturation with language models and weakly supervised learning},
    author = {Ruffolo, Jeffrey A and Gray, Jeffrey J and Sulam, Jeremias},
    journal = {arXiv},
    year= {2021}
}
@inproceedings{
  gao2023pifold,
  title={PiFold: Toward effective and efficient protein inverse folding},
  author={Zhangyang Gao and Cheng Tan and Stan Z. Li},
  booktitle={International Conference on Learning Representations},
  year={2023},
  url={https://openreview.net/forum?id=oMsN9TYwJ0j}
}
@article{gao2022pifold,
  title={PiFold: Toward effective and efficient protein inverse folding},
  author={Gao, Zhangyang and Tan, Cheng and Li, Stan Z},
  journal={arXiv preprint arXiv:2209.12643},
  year={2022}
}
```
