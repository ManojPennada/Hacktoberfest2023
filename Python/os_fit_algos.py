def best_fit(partitions, processes):
    """Allocates partitions to processes using Best-fit algorithm"""
    allocation = {}
    for process in processes:
        best_fit_partition = None
        for partition in partitions:
            if partition >= process:
                if not best_fit_partition or partition < best_fit_partition:
                    best_fit_partition = partition
        if best_fit_partition:
            allocation[process] = best_fit_partition
            partitions.remove(best_fit_partition)
    return allocation

def first_fit(partitions, processes):
    """Allocates partitions to processes using First-fit algorithm"""
    allocation = {}
    for process in processes:
        for partition in partitions:
            if partition >= process:
                allocation[process] = partition
                partitions.remove(partition)
                break
    return allocation

def worst_fit(partitions, processes):
    """Allocates partitions to processes using Worst-fit algorithm"""
    allocation = {}
    for process in processes:
        worst_fit_partition = None
        for partition in partitions:
            if partition >= process:
                if not worst_fit_partition or partition > worst_fit_partition:
                    worst_fit_partition = partition
        if worst_fit_partition:
            allocation[process] = worst_fit_partition
            partitions.remove(worst_fit_partition)
    return allocation


partitions = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

best_fit_allocation = best_fit(partitions, processes)
print("Best-fit Allocation: ", best_fit_allocation)

partitions = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

first_fit_allocation = first_fit(partitions, processes)
print("First-fit Allocation: ", first_fit_allocation)

partitions = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

worst_fit_allocation = worst_fit(partitions, processes)
print("Worst-fit Allocation: ", worst_fit_allocation)
