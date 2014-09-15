
# coding: utf-8

# In[1]:

pwd


# In[2]:

get_ipython().system(u'head C:\\Users\\user\\Documents\\IPython_Notebooks\\Pm_genes.fasta')


                #Pm_genes.fasta is the patiria miniata (bat star) transcriptom available for download from http://www.spbase.org/SpBase/download/
                
# In[3]:

get_ipython().system(u'wc C:\\Users\\user\\Documents\\IPython_Notebooks\\Pm_genes.fasta')


# In[4]:

get_ipython().system(u"fgrep -c 'PMI' C:\\Users\\user\\Documents\\IPython_Notebooks\\Pm_genes.fasta")


# In[5]:

get_ipython().system(u'C:\\\\Users\\\\user\\\\Documents\\\\IPython_Notebooks\\blast\\bin\\blastn -h')


# In[6]:

get_ipython().system(u'blastn -query C:\\Users\\user\\Documents\\IPython_Notebooks\\Pm_genes.fasta -db C:\\Users\\user\\Documents\\IPython_Notebooks\\blast\\bin\\databases\\Phel_transcriptome_clc -out C:\\Users\\user\\Documents\\IPython_Notebooks\\Output\\batstar_hel_ntblast2 -evalue 1E-05 -max_target_seqs 5 -outfmt 6 -num_threads 4 ')


# In[7]:

get_ipython().system(u'wc C:\\Users\\user\\Documents\\IPython_Notebooks\\Output\\batstar_hel_ntblast2')


# In[8]:

get_ipython().system(u'head C:\\Users\\user\\Documents\\IPython_Notebooks\\Output\\batstar_hel_ntblast')


# In[9]:

get_ipython().system(u"fgrep -c 'PMI' C:\\Users\\user\\Documents\\IPython_Notebooks\\Output\\batstar_hel_ntblast")


# In[ ]:



