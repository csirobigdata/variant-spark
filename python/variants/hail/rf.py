'''
Created on 10 Nov 2017

@author: szu004
'''
from hail import  KeyTable

class ImportanceAnalysis:
    """ Model for random forest based importance analysis
    """
    def __init__(self, hc, _jia):
        self.hc = hc
        self._jia = _jia
        
    @property
    def oob_error(self):
        """ OOB (Out of Bag) error estimate for the model
        """
        return self._jia.oobError()
    
    def important_variants(self, n_limit = 1000):
        """ Gets the top n most important loci. 
        
        :param: int n_limit: the limit of the number of loci to return
        
        :return: A KeyTable with the locus in the first column and importance in the second.
        :rtype: :py:class:`KeyTable`
        """
        return KeyTable(self.hc, self._jia.variantImportance(n_limit))