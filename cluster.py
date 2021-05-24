

class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
        for sample in other.samples:
            self.samples.append(sample)
        self.samples.sort(key=lambda x: x.s_id)
        del other

    def print_details(self, silhouette):
        pass

    def compute_dominant_label(self):
        list_of_labels = []
        for sample in self.samples:
            if sample not in list_of_labels:
                list_of_labels.append(sample)
        labels_histogram = []


    # def compute_in(self, sample):
    #     cluster_size = len(self.samples)
    #     sum_of_distances = 0
    #     for other_sample in self.samples:
    #         if sample is not other_sample:
    #             sum_of_distances = sum_of_distances + sample.compute_euclidean_distance(other_sample)
    #     return sum_of_distances / (cluster_size - 1)


