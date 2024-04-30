import multiprocessing as mp
import os


class Parallel_Utils():
    @staticmethod
    def run_process(func, args_list: list):
        num_processes = max(1, mp.cpu_count() - 1)
        with mp.Pool(processes=num_processes) as pool:
            try:
                return pool.map(func, args_list)
            except Exception as e:
                print(f"Error in multiprocessing: {e}")
        pool.close()