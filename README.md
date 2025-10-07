# OS_CPUScheduling_Ramo
CPU Scheduling Algorithms - FCFS, SJF, Round Robin
 # CPU Scheduling Algorithms

This repository contains implementations of three fundamental CPU scheduling algorithms used in Operating Systems: **First Come First Serve (FCFS)**, **Shortest Job First (SJF)**, and **Round Robin (RR)**.

### 1. First Come First Serve (FCFS)
**Type**: Non-preemptive  
**Principle**: Processes are executed in the order of their arrival time.  
**Characteristics**:
- Simplest scheduling algorithm
- Uses FIFO (First-In-First-Out) queue
- No priority considerations
- Can lead to convoy effect (short processes wait behind long ones)

**Advantages**:
- Easy to implement and understand
- Fair in terms of arrival order

**Disadvantages**:
- Poor performance for short processes
- Not suitable for time-sharing systems
- Average waiting time is often high
  
In the laboratory, the FCFS CPU scheduling algorithm processes jobs in strict chronological order based on their arrival times. The implementation begins by accepting process data either through JSON files or interactive user input, collecting process names along with their arrival and burst times. The algorithm first sorts all processes by their arrival time to establish the correct execution sequence, then systematically processes each job in this predetermined order. For each process, it checks if the CPU is available at the process's arrival time—if not, it accounts for idle periods before commencing execution. The core calculation involves computing completion time by adding burst time to the current timeline, then deriving turnaround time as the difference between completion and arrival times, and finally calculating waiting time by subtracting burst time from turnaround time. Throughout execution, the algorithm maintains a detailed timeline for Gantt chart visualization and compiles comprehensive results including individual process metrics and overall averages. The output presents a clear table showing arrival time, burst time, completion time, turnaround time, and waiting time for each process, followed by average performance metrics and a visual Gantt chart that illustrates the exact execution sequence and timing, providing a complete analysis of the scheduling behavior under FCFS policy.

  ## Screenshots input/output
  ## FCFS Scheduling Results
  ![FCFS Scheduling Output](images/FCFS%20input_output.jpg)

 ## Gantt Chart 
 
Gantt Chart:
| P1  |  P2 |  P3 |
0     5     8     16

### 2. Shortest Job First (SJF) - Non-Preemptive
**Type**: Non-preemptive  
**Principle**: Process with the smallest burst time executes next.  
**Characteristics**:
- Optimal for minimizing average waiting time
- Requires knowledge of burst times in advance
- Can cause starvation of longer processes

**Advantages**:
- Minimum average waiting time among non-preemptive algorithms
- Efficient for batch systems

**Disadvantages**:
- Impossible to implement in interactive systems
- Long processes may starve
- Requires accurate burst time estimation

  **Shortest Job First (SJF)** is a non-preemptive CPU scheduling algorithm that prioritizes processes with the smallest burst times to optimize system performance. This implementation begins by collecting user input for the number of processes and their respective burst times, assuming all processes arrive simultaneously at time zero for simplicity. The core logic involves sorting all processes in ascending order based on their burst times, ensuring that the shortest tasks are scheduled first in the execution sequence. The algorithm then sequentially processes each job, calculating completion time by accumulating burst times chronologically, while turnaround time equals completion time due to zero arrival times, and waiting time derives from subtracting burst time from turnaround time. Throughout execution, the program maintains running totals for computing average turnaround and waiting times, providing comprehensive performance metrics. Finally, it generates a visual Gantt chart illustrating the exact execution order and timing, demonstrating how SJF minimizes average waiting time by ensuring shorter jobs complete quickly, though this approach requires advance knowledge of burst times and may cause longer processes to experience significant delays in systems with continuous job arrivals.

  
  ## Screenshots input/output
  
  ## SJF Scheduling Results
![SJF Scheduling Output](images/SJF%20input_output.jpg)

 ## Gantt Chart 
 
 Gantt Chart:
| P1  |  P2 |  P3 |
0     3     8     16

### 3. Round Robin (RR) - Time Quantum = 2
**Type**: Preemptive  
**Principle**: Each process gets a fixed time slice (quantum) to execute.  
**Characteristics**:
- Designed for time-sharing systems
- Fair allocation of CPU time
- No process starvation
- Performance depends on time quantum size

**Advantages**:
- No starvation - every process gets regular CPU access
- Good for interactive systems
- Fair treatment of all processes

**Disadvantages**:
- High context switching overhead
- Performance depends on time quantum selection
- Not optimal for average waiting time

**Round Robin** is a preemptive scheduling algorithm designed for time-sharing systems that allocates a fixed time slice (quantum) of 2 time units to each process in circular fashion. When a process's time quantum expires, it's moved to the back of the ready queue, and the CPU is assigned to the next waiting process, ensuring fair treatment and preventing starvation. This approach provides excellent response times for interactive applications since every process gets regular access to the CPU, but it introduces significant overhead from frequent context switches between processes. The performance of Round Robin heavily depends on the time quantum size—too small increases context switching overhead, while too large makes it behave like FCFS—making the choice of time quantum crucial for balancing responsiveness and efficiency in multi-user environments.


 ## Screenshots input/output
  
  ## SJF Scheduling Results
![RR Scheduling Output](images/RR%20input_output1.jpg)
![RR Scheduling Output](images/RR%20input_output2.jpg)
 ## Gantt Chart 
 
 Gantt Chart:
| P1  |  P2 |  P3 |  P1  |  P2 |  P3 | P1  |  P3 |  P3 |
0     2     4     6      8     9     11    12    14    16


## ⚙️ Implementation Details

### Metrics Calculated:
- **Completion Time (CT)**: Time when process finishes execution
- **Turnaround Time (TAT)**: CT - Arrival Time (total time in system)
- **Waiting Time (WT)**: TAT - Burst Time (time spent waiting)
- **Average TAT and WT**: Overall system performance metrics

### Key Features:
- All processes arrive at time 0 for simplicity
- Comprehensive output including tables and Gantt charts
- Modular code structure for easy understanding
- Error handling for invalid inputs


## 🖥️ How to Run

### Prerequisites
- Python 3.13.7
- No external dependencies required
