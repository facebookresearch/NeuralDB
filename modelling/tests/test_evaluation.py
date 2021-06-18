#
# Copyright (c) 2021 Facebook, Inc. and its affiliates.
#
# This file is part of NeuralDB.
# See https://github.com/facebookresearch/NeuralDB for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import unittest
from neuraldb.evaluation.scoring_functions import (
    precision,
    recall,
    compute_f1,
    average_score,
)


class PrecisionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.gold_reference = ["a", "b", "c", "d", "e"]

        self.precision_fail1 = ["a", "b", "c", "d", "e", "f"]
        self.precision_fail2 = ["f"]
        self.precision_fail3 = ["a", "f"]

    def testPrecisionExact(self):
        self.assertEqual(precision(self.gold_reference, self.gold_reference), 1)

    def testPrecisionFailOneTooMany(self):
        self.assertEqual(precision(self.gold_reference, self.precision_fail1), 5 / 6)

    def testPrecisionFailOnlyWrong(self):
        self.assertEqual(precision(self.gold_reference, self.precision_fail2), 0)

    def testPrecisionFailHalfWrong(self):
        self.assertEqual(precision(self.gold_reference, self.precision_fail3), 0.5)

    def testPrecisionNoPredictions(self):
        self.assertEqual(precision(self.gold_reference, []), 1)

    def testPrecisionNoSourceNoPredictions(self):
        self.assertEqual(precision([], []), 1)

    def testPrecisionNoSourceBadPredictions(self):
        self.assertEqual(precision([], self.precision_fail2), 0)


class RecallTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.gold_reference = ["a", "b", "c", "d", "e"]

        self.recall_ok1 = ["a", "b", "c", "d", "e", "f"]
        self.recall_fail1 = ["f"]
        self.recall_fail2 = ["a", "f"]
        self.recall_fail3 = ["a"]

    def testRecallExact(self):
        self.assertEqual(recall(self.gold_reference, self.gold_reference), 1)

    def testRecallTooMany(self):
        self.assertEqual(recall(self.gold_reference, self.recall_ok1), 1)

    def testRecallNoPredictions(self):
        self.assertEqual(recall(self.gold_reference, []), 0)

    def testRecallNoSourceNoPredictions(self):
        self.assertEqual(recall([], []), 1)

    def testRecallOnlyOne(self):
        self.assertEqual(recall(self.gold_reference, self.recall_fail3), 1 / 5)

    def testRecallOnlyWithFalsePositive(self):
        self.assertEqual(recall(self.gold_reference, self.recall_fail2), 1 / 5)

    def testRecallOnlyFalsePositive(self):
        self.assertEqual(recall(self.gold_reference, self.recall_fail1), 0)


class F1Test(unittest.TestCase):
    def testBothOne(self):
        self.assertEqual(compute_f1(1, 1), 1.0)

    def testBothZero(self):
        self.assertEqual(compute_f1(0, 0), 0.0)

    def testOneZero(self):
        self.assertEqual(compute_f1(1, 0), 0.0)

    def testBothHalf(self):
        self.assertEqual(compute_f1(0.5, 0.5), 0.5)

    def testHalfAndOne(self):
        self.assertEqual(compute_f1(0.5, 1), 2 / 3)


class AverageScoreTest(unittest.TestCase):
    @staticmethod
    def passThroughA(a, b):
        return a

    def setUp(self):
        self.scores0 = [0, 0, 0, 0]
        self.scores1Quarter = [0, 0, 0, 1]
        self.scores1 = [1, 1, 1, 1]

    def testScoresZero(self):
        self.assertEqual(
            average_score(self.scores0, self.scores0, self.passThroughA), 0
        )

    def testScores1Quarter(self):
        self.assertEqual(
            average_score(self.scores1Quarter, self.scores1Quarter, self.passThroughA),
            1 / 4,
        )

    def testScores1(self):
        self.assertEqual(
            average_score(self.scores1, self.scores1, self.passThroughA), 1
        )

    def testScoresNoInstances(self):
        self.assertEqual(average_score([], [], self.passThroughA), 0)
