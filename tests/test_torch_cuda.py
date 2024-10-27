import unittest


class test_torch_cuda(unittest.TestCase):

    def setUp(self):
        pass

    def test_torch_cuda(self):
        """
        Teste si la librairie PyTorch est installée et si CUDA est disponible.
        """
        import torch
        # Vérifier si CUDA est disponible
        self.assertTrue(torch.cuda.is_available())
        # Afficher le nombre de GPU disponibles
        print(f"Nombre de GPU disponibles: {torch.cuda.device_count()}")
        # Afficher le nom du GPU
        print(f"Nom du GPU: {torch.cuda.get_device_name(0)}")
        # Afficher la version de CUDA
        print(f"Version de CUDA: {torch.version.cuda}")
        # Afficher la version de PyTorch
        print(f"Version de PyTorch: {torch.__version__}")

if __name__ == '__main__':
    unittest.main()
