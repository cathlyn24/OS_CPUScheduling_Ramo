#!/usr/bin/env python3
"""
Ultra Simplified SJF Scheduling
All processes arrive at time 0
"""

def simple_sjf():
    print("SJF Scheduling (All processes arrive at time 0)")
    print("=" * 45)
    
    # Get number of processes
    n = int(input("Enter number of processes: "))
    
    # Get burst times
    burst_times = []
    for i in range(n):
        bt = int(input(f"Enter burst time for P{i+1}: "))
        burst_times.append(bt)
    
    # Create processes with names and burst times
    processes = []
    for i in range(n):
        processes.append({
            'name': f'P{i+1}',
            'bt': burst_times[i]
        })
    
    # SJF: Sort by burst time (shortest first)
    processes.sort(key=lambda x: x['bt'])
    
    # Calculate metrics
    current_time = 0
    results = []
    
    print("\nSJF Scheduling Results:")
    print("Process\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    print("-" * 65)
    
    total_tat = 0
    total_wt = 0
    
    for i, process in enumerate(processes):
        completion_time = current_time + process['bt']
        turnaround_time = completion_time  # Since AT=0, TAT=CT
        waiting_time = turnaround_time - process['bt']
        
        total_tat += turnaround_time
        total_wt += waiting_time
        
        print(f"{process['name']}\t{process['bt']}\t\t{completion_time}\t\t{turnaround_time}\t\t{waiting_time}")
        
        current_time = completion_time
        results.append((process['name'], process['bt'], completion_time, turnaround_time, waiting_time))
    
    # Averages
    avg_tat = total_tat / n
    avg_wt = total_wt / n
    
    print("-" * 65)
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    
    # Gantt Chart
    print("\nGantt Chart:")
    current = 0
    for process in processes:
        print(f"| P{process['name'][1:]} ", end="")
    print("|")
    
    print("0", end="")
    current = 0
    for process in processes:
        current += process['bt']
        print(f"    {current}", end="")
    print()

# Run the program
if __name__ == "__main__":
    simple_sjf()