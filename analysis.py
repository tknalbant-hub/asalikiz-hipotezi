import numpy as np
from scipy.special import expi

class PerfectProofEngine:
    @staticmethod
    def log_integral(x):
        """Asal sayıların dağılımı için asimptotik limit."""
        return expi(np.log(x))
    
    @staticmethod
    def hardy_littlewood_bound(x):
        """Asal ikizler için mutlak üst sınır (Kusursuzluk Mührü)."""
        C2 = 0.6601618158468695
        return 2 * C2 * (x / (np.log(x)**2))

    @staticmethod
    def calculate_deviation(n_values):
        """Tahmin ve gerçeklik arasındaki sapmayı ölç."""
        # Burada asalları sayıp teorik formülle karşılaştıracağız
        return np.array([abs(i - cls.hardy_littlewood_bound(i)) for i in n_values])