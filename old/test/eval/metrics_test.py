import unittest

from eval import metrics


class TestAccuracy(unittest.TestCase):
    # [
    #     {
    #         "updates": [],
    #         "queries": [
    #             [1, "For which company does the Inna work?", "China Eastern Airlines Corp. Ltd."],
    #             [2, "Is Inna hard-working?", "Yes"],
    #             [2, "Is Susan a computer scientist at AdvantExcel.com Communications Corp.?", "None"],
    #             [3, "Is Susan a computer scientist at AdvantExcel.com Communications Corp.?", "Yes"],
    #             [3, "Is Susan hard-working?", "None"],
    #             [4, "Is Susan hard-working?", "Yes"],
    #             [4, "For which company does the Iman work?", "None"],
    #             [5, "For which company does the Iman work?", "Comunicacion Celular S.A."],
    #             [5, "Is Iman hard-working?", "None"],
    #         ]
    #     },
    # ]

    def test_1(self):
        gold_data = ['yes', 'no', 'none']
        prediction_data = ['yes', 'no', 'none']

        scores = metrics.calculate_scores(gold_data, prediction_data)
        self.assertEqual(scores['classification'], 1.0)

    def test_2(self):
        gold_data = ['yes', 'none', 'no']
        prediction_data = ['yes', 'no', 'none']

        scores = metrics.calculate_scores(gold_data, prediction_data)
        self.assertEqual(scores['classification'], 1 / 3)
        self.assertEqual(scores['intersection'], None)

    def test_3(self):
        gold_data = ['yes', 'none', 'Adam']
        prediction_data = ['yes', 'no', 'none']

        scores = metrics.calculate_scores(gold_data, prediction_data)
        self.assertEqual(scores['classification'], 1 / 3)
        self.assertEqual(scores['intersection'], 0)

    def test_4(self):
        gold_data = ['yes', 'none', 'Adam']
        prediction_data = ['yes', 'no', 'John']

        scores = metrics.calculate_scores(gold_data, prediction_data)
        self.assertEqual(scores['classification'], 2 / 3)
        self.assertEqual(scores['intersection'], 0)
        self.assertEqual(scores['exact'], 0)

    def test_5(self):
        gold_data = ['Adam']
        prediction_data = ['Adam']

        scores = metrics.calculate_scores(gold_data, prediction_data)
        self.assertEqual(scores['intersection'], 1)
        self.assertEqual(scores['exact'], 1)

    def test_6(self):
        gold_data = ['Adam Jones']
        prediction_data = ['Adam']

        scores = metrics.calculate_scores(gold_data, prediction_data)
        self.assertEqual(scores['intersection'], 1 / 2)
        self.assertEqual(scores['exact'], 0)

    def test_6(self):
        gold_data = ['Adam Jones Smith']
        prediction_data = ['Adam Smith']

        scores = metrics.calculate_scores(gold_data, prediction_data)
        self.assertEqual(scores['intersection'], 2 / 3)
        self.assertEqual(scores['exact'], 0)

    def test_7(self):
        gold_data = ['Adam, Smith', 'Limited Company']
        prediction_data = ['Adam Smith!', 'Company']

        scores = metrics.calculate_scores(gold_data, prediction_data)
        self.assertEqual(scores['exact'], 1 / 2)


if __name__ == '__main__':
    unittest.main()
