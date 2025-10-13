#!/usr/bin/env python3
"""
Simple Parallel Processing Tutorial
===================================
Learn parallel processing basics using number squaring examples.
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor


def square_number(number):
    """
    Square a number with a small delay to simulate work.
    """
    print(f"Squaring {number}...")
    time.sleep(0.5)  # Simulate some work
    result = number ** 2
    print(f"Result: {number}² = {result}")
    return result


def demo_sequential():
    """
    Sequential approach: Process numbers one by one.
    Each number waits for the previous one to complete.
    """
    print("\n1. SEQUENTIAL APPROACH")
    print("-" * 30)
    numbers = [2, 3, 4, 5]
    start = time.time()
    
    results = []
    for num in numbers:
        result = square_number(num)
        results.append(result)
    
    end_time = time.time() - start
    print(f"Sequential time: {end_time:.1f}s")
    print(f"Results: {results}")


def demo_separate_threads():
    """
    Separate threads approach: Create individual threads manually.
    Each number gets its own thread that runs independently.
    """
    print("\n2. SEPARATE THREADS")
    print("-" * 30)
    numbers = [2, 3, 4, 5]
    start = time.time()
    
    threads = []
    results = [None] * len(numbers)  # Pre-allocate results list
    
    def worker(index, number):
        results[index] = square_number(number)
    
    # Create and start threads
    for i, num in enumerate(numbers):
        thread = threading.Thread(target=worker, args=(i, num))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    end_time = time.time() - start
    print(f"Separate threads time: {end_time:.1f}s")
    print(f"Results: {results}")


def demo_threadpool():
    """
    ThreadPoolExecutor approach: Use a managed pool of threads.
    Python handles thread creation and management automatically.
    """
    print("\n3. THREADPOOL EXECUTOR")
    print("-" * 30)
    numbers = [2, 3, 4, 5]
    start = time.time()
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Submit all tasks and get future objects
        futures = [executor.submit(square_number, num) for num in numbers]
        # Get results as they complete
        results = [future.result() for future in futures]
    
    end_time = time.time() - start
    print(f"ThreadPool time: {end_time:.1f}s")
    print(f"Results: {results}")


def main():
    """
    Compare three approaches to parallel processing.
    """
    print("🔢 SIMPLE PARALLEL PROCESSING")
    print("=" * 40)
    print("Task: Square numbers [2, 3, 4, 5]")
    
    demo_sequential()      # ~2.0 seconds (4 × 0.5s)
    demo_separate_threads() # ~0.5 seconds (parallel)
    demo_threadpool()      # ~0.5 seconds (parallel)
    
    print("\n" + "=" * 40)
    print("📊 SUMMARY:")
    print("• Sequential: Tasks run one after another")
    print("• Separate Threads: Manual thread management")
    print("• ThreadPool: Automatic thread management (recommended)")
    print("=" * 40)


if __name__ == "__main__":
    main()
