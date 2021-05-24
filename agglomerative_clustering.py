import cluster


class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link
        self.clusters = [cluster.Cluster(s.s_id, [s]) for s in samples]

    def compute_silhoeutte(self):
        sil_dict = {}
        for c in self.clusters:
            for samp in c.samples:
                in_val = self.compute_cluster_d(samp, c, True)
                outs_values = [self.compute_cluster_d(samp, out_c, False)
                               for out_c in self.clusters if c != out_c]
                out_val = min(outs_values)
                sil_val = (out_val - in_val) / max(in_val, out_val)
                sil_dict[samp.s_id] = sil_val
        return sil_dict

    def compute_summary_silhoeutte(self):
        sil_dict = self.compute_silhoeutte()
        summary_dict = {}
        population_size = 0
        population_sum = 0
        for c in self.clusters:
            cluster_sum = sum([sil_dict[s.s_id] for s in c.samples])
            population_sum += cluster_sum
            population_size += len(c.samples)
            cluster_sil = cluster_sum / len(c.samples)
            summary_dict[c.c_id] = cluster_sil
        summary_dict[0] = population_sum / population_size

    def compute_rand_index(self):
        pass

    def run(self, max_clusters):
        pass

    def compute_cluster_d(self, sample, cluster_to, is_sample_cluster):
        cluster_size = len(cluster_to.samples) - 1 if is_sample_cluster else len(cluster_to.samples)
        if cluster_size == 0:
            return 0
        sum_of_distances = 0
        for other_sample in cluster_to.samples:
            if sample is not other_sample.samples:
                sum_of_distances = sum_of_distances + sample.compute_euclidean_distance(other_sample)
        return sum_of_distances / cluster_size






