# mpi_sum.py
import mpi4py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

value = rank + 1
total = comm.reduce(value, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Hello from process {rank}. The total sum from all {size} ranks is: {total}")