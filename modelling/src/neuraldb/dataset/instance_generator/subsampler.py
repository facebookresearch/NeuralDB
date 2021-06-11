import random


class Subsampler:

    # Take a list of sample types and probability of keeping
    def __init__(self, sample_types):
        self.sample_types = sample_types

    #
    def maybe_drop_sample(self, query):
        if query["type"] in self.sample_types:
            sample_rate = self.sample_types[query["type"]]
            rand = random.random()

            if isinstance(sample_rate, list):
                if not len(query["answer"]):
                    sample_rate = sample_rate[2]
                else:
                    if "TRUE" in query["answer"]:
                        sample_rate = sample_rate[0]
                    else:
                        sample_rate = sample_rate[1]

            # Drop sample if needed
            return rand < sample_rate

        return False
