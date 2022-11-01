import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto0 = Varasto(-1)
        self.varasto_saldo0 = Varasto(0, alku_saldo = -1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_0(self):
        self.assertAlmostEqual(self.varasto0.tilavuus, 0)

    def test_negatiivinen_lisays_palauttaa_oikean_saldon(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(2)
        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_liian_suuri_lisays_palauttaa_alkuperaisen_maaran(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto_palauttaa_oikean_maaran(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_liian_suuri_otto_palauttaa_mita_voidaan(self):
        self.varasto.lisaa_varastoon(2)
        self.assertAlmostEqual(self.varasto.ota_varastosta(3), 2)

    def test_liian_suuri_otto_antaa_saldoksi_0(self):
        self.varasto.lisaa_varastoon(2)
        self.varasto.ota_varastosta(3)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_alkusaldo_palauttaa_0(self):
        self.assertAlmostEqual(self.varasto_saldo0.saldo, 0)

    def test_string_antaa_oikean_tekstin(self):
        self.assertEqual(self.varasto.__str__(), 'saldo = 01, vielä tilaa 10')