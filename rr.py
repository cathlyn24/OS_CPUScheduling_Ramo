#!/usr/bin/env python3
"""
Round Robin Scheduling with Time Quantum = 2
User inputs number of processes and burst times
All processes arrive at time 0
"""

def round_robin_scheduling():
    """
    Round Robin scheduling with time quantum 2
    """
    print("Round Robin Scheduling Calculator")
    print("Time Quantum = 2")
    print("All processes arrive at time 0")
    print("=" * 50)
    
    # Get number of processes from user
    while True:
        try:
            n = int(input("Enter number of processes: "))
            if n <= 0:
                print("Please enter a positive number of processes")
                continue
            break
        except ValueError:
            print("Please enter a valid integer")
    
    # Get burst times from user
    processes = []
    print(f"\nEnter burst times for {n} processes:")
    for i in range(n):
        while True:
            try:
                bt = int(input(f"Burst Time for P{i+1}: "))
                if bt <= 0:
                    print("Burst time must be greater than 0")
                    continue
                processes.append({
                    'name': f'P{i+1}',
                    'at': 0,  # All processes arrive at time 0
                    'bt': bt,
                    'remaining_bt': bt,
                    'ct': 0,
                    'tat': 0,
                    'wt': 0
                })
                break
            except ValueError:
                print("Please enter a valid integer")
    
    time_quantum = 2
    current_time = 0
    completed = 0
    ready_queue = []
    timeline = []
    
    
    # Initialize ready queue with all processes
    ready_queue = processes.copy()
    
    print(f"\nExecution Timeline (Time Quantum = {time_quantum}):")
    print("Time\tProcess\tExecution\tRemaining BT")
    print("-" * 50)
    
    # Round Robin Algorithm
    while completed < n:
        if ready_queue:
            current_process = ready_queue.pop(0)
            
            # Execute for min(time_quantum, remaining_bt)
            execution_time = min(time_quantum, current_process['remaining_bt'])
            start_time = current_time
            current_time += execution_time
            current_process['remaining_bt'] -= execution_time
            
            # Display execution details
            print(f"{start_time}-{current_time}\t{current_process['name']}\t{execution_time} unit(s)\t{current_process['remaining_bt']}")
            timeline.append((current_process['name'], start_time, current_time))
            
            if current_process['remaining_bt'] > 0:
                # Process not completed, add back to ready queue
                ready_queue.append(current_process)
            else:
                # Process completed
                current_process['ct'] = current_time
                current_process['tat'] = current_process['ct'] - current_process['at']  # TAT = CT - AT
                current_process['wt'] = current_process['tat'] - current_process['bt']  # WT = TAT - BT
                completed += 1
        else:
            # No processes in ready queue
            current_time += 1
    
    # Display Results Table
    print("\n" + "=" * 70)
    print("ROUND ROBIN SCHEDULING RESULTS")
    print("=" * 70)
    print("Process\tAT\tBT\tCT\tTAT\tWT")
    print("-" * 50)
    
    total_tat = 0
    total_wt = 0
    
    # Sort processes by name for consistent display
    sorted_processes = sorted(processes, key=lambda x: x['name'])
    
    for process in sorted_processes:
        print(f"{process['name']}\t{process['at']}\t{process['bt']}\t{process['ct']}\t{process['tat']}\t{process['wt']}")
        total_tat += process['tat']
        total_wt += process['wt']
    
    # Calculate averages
    avg_tat = total_tat / n
    avg_wt = total_wt / n
    
    print("-" * 50)
    print(f"Average Turnaround Time (TAT): {avg_tat:.2f}")
    print(f"Average Waiting Time (WT): {avg_wt:.2f}")
    
    # Display Gantt Chart
    print("\n" + "=" * 50)
    print("GANTT CHART")
    print("=" * 50)
    
    # Text-based Gantt chart
    for proc, start, end in timeline:
        print(f"| {proc} ", end="")
    print("|")
    
    # Time markers
    print("0", end="")
    for proc, start, end in timeline:
        print(f"    {end}", end="")
    print()
    
    
    # Execution sequence
    print(f"\nExecution Sequence: ", end="")
    sequence = [proc for proc, start, end in timeline]
    print(" → ".join(sequence))
    
    # Performance summary
    print(f"\nPerformance Summary:")
    print(f"- Time Quantum: {time_quantum}")
    print(f"- Total Processes: {n}")
    print(f"- Total Execution Time: {current_time}")
    print(f"- Number of Context Switches: {len(timeline) - 1}")

def main():
    """
    Main function with option to run multiple times
    """
    while True:
        round_robin_scheduling()
        
        print("\n" + "=" * 70)
        again = input("\nDo you want to calculate another schedule? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break
        print()

if __name__ == "__main__":
    main()