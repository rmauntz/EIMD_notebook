
.. code:: python

    pwd



.. parsed-literal::

    u'C:\\Users\\user\\Documents\\IPython_Notebooks'



.. code:: python

    !head C:\Users\user\Documents\IPython_Notebooks\Pm_genes.fasta

.. parsed-literal::

    >PMI_010847-RA
    GCTAACATAGAGATCTTCCTGCCACGGATCGAGGCAGTGGTCCTGTTCGGTGAGCCGGTC
    AGGTGGGAGACCAATCTCCAGCTGATTTTGGACATGTTGATCACCAACGGTCAGCTAAAC
    CACACCCCTGACCACGTCCCGTACCCTAACATGCCGGTCCTTGGATGCAACGTGGATCTC
    ATGTGGATGTCCGAGGCTCATCTACCAAGGTTAGGACATGGCTCTTTCATGGTGTGCCTA
    GAATCACTTTACAAGAAAATCACAGGTCGGGATCTGCTGTACACCGTTCTGACGGGCAAA
    CCTAGTCAGATAACGTACCACTGTGCTGAGAATGTACTAAGCCAACAAGCGAGGGCCATG
    GGATGTCAGGGCCCACTCCGAACACTCTATGCCATTGGTGACAACCCGATGACCGACATC
    TACGGGGCCAATCTGTACAACCAGTACCTCACAGCGAAAGCTGCTAAAGGCCTACAGAAA
    CCAGGTAGCCGCCAGCCAGCGGCCATACGCCAGGGCGTGGTCATGTCCGATCCCCACGAC
    

                #Pm_genes.fasta is the patiria miniata (bat star) transcriptom available for download from http://www.spbase.org/SpBase/download/
                
.. code:: python

    !wc C:\Users\user\Documents\IPython_Notebooks\Pm_genes.fasta

.. parsed-literal::

      613310   613310 35186335 C:\Users\user\Documents\IPython_Notebooks\Pm_genes.fasta
    

.. code:: python

    !fgrep -c 'PMI' C:\Users\user\Documents\IPython_Notebooks\Pm_genes.fasta

.. parsed-literal::

    29805
    

.. code:: python

    !C:\\Users\\user\\Documents\\IPython_Notebooks\blast\bin\blastn -h

.. parsed-literal::

    USAGE
      blastn [-h] [-help] [-import_search_strategy filename]
        [-export_search_strategy filename] [-task task_name] [-db database_name]
        [-dbsize num_letters] [-gilist filename] [-seqidlist filename]
        [-negative_gilist filename] [-entrez_query entrez_query]
        [-db_soft_mask filtering_algorithm] [-db_hard_mask filtering_algorithm]
        [-subject subject_input_file] [-subject_loc range] [-query input_file]
        [-out output_file] [-evalue evalue] [-word_size int_value]
        [-gapopen open_penalty] [-gapextend extend_penalty]
        [-perc_identity float_value] [-xdrop_ungap float_value]
        [-xdrop_gap float_value] [-xdrop_gap_final float_value]
        [-searchsp int_value] [-max_hsps int_value] [-sum_statistics]
        [-penalty penalty] [-reward reward] [-no_greedy]
        [-min_raw_gapped_score int_value] [-template_type type]
        [-template_length int_value] [-dust DUST_options]
        [-filtering_db filtering_database]
        [-window_masker_taxid window_masker_taxid]
        [-window_masker_db window_masker_db] [-soft_masking soft_masking]
        [-ungapped] [-culling_limit int_value] [-best_hit_overhang float_value]
        [-best_hit_score_edge float_value] [-window_size int_value]
        [-off_diagonal_range int_value] [-use_index boolean] [-index_name string]
        [-lcase_masking] [-query_loc range] [-strand strand] [-parse_deflines]
        [-outfmt format] [-show_gis] [-num_descriptions int_value]
        [-num_alignments int_value] [-html] [-max_target_seqs num_sequences]
        [-num_threads int_value] [-remote] [-version]
    
    DESCRIPTION
       Nucleotide-Nucleotide BLAST 2.2.29+
    
    Use '-help' to print detailed descriptions of command line arguments
    

.. code:: python

    !blastn \
    -query C:\Users\user\Documents\IPython_Notebooks\Pm_genes.fasta \
    -db C:\Users\user\Documents\IPython_Notebooks\blast\bin\databases\Phel_transcriptome_clc \
    -out C:\Users\user\Documents\IPython_Notebooks\Output\batstar_hel_ntblast2 \
    -evalue 1E-05 \
    -max_target_seqs 5 \
    -outfmt 6 \
    -num_threads 4 \
.. code:: python

    !wc C:\Users\user\Documents\IPython_Notebooks\Output\batstar_hel_ntblast2

.. parsed-literal::

      3460  41520 279940 C:\Users\user\Documents\IPython_Notebooks\Output\batstar_hel_ntblast2
    

.. code:: python

    !head C:\Users\user\Documents\IPython_Notebooks\Output\batstar_hel_ntblast

.. parsed-literal::

    PMI_005730-RA	Phel_clc_contig_14067	77.94	408	86	4	52	457	2552	2147	4e-066	  252
    PMI_028366-RA	Phel_clc_contig_1561	77.05	183	40	2	2038	2219	3895	4076	3e-021	  104
    PMI_018581-RA	Phel_clc_contig_7180	78.08	689	135	13	748	1425	946	263	5e-117	  422
    PMI_016388-RA	Phel_clc_contig_9391	73.66	391	97	6	22	409	1305	918	1e-034	  147
    PMI_016388-RA	Phel_clc_contig_17473	80.32	188	30	7	163	347	35	218	3e-031	  135
    PMI_016388-RA	Phel_clc_contig_9910	73.53	374	89	10	52	420	1974	1606	1e-030	  134
    PMI_016388-RA	Phel_clc_contig_14428	79.56	181	33	4	34	212	1855	2033	2e-028	  126
    PMI_007351-RA	Phel_clc_contig_29013	84.98	233	35	0	319	551	202	434	2e-061	  237
    PMI_007347-RA	Phel_clc_contig_5857	82.88	917	157	0	181	1097	1123	207	0.0	  824
    PMI_012824-RA	Phel_clc_contig_13029	84.10	283	44	1	1	282	61	343	2e-072	  272
    

.. code:: python

    !fgrep -c 'PMI' C:\Users\user\Documents\IPython_Notebooks\Output\batstar_hel_ntblast

.. parsed-literal::

    3407
    

