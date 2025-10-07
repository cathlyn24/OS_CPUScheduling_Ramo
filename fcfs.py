#!/usr/bin/env python3
"""
FCFS scheduling
Input: json or interactive
Outputs: table, averages, ASCII Gantt
"""
import json
import sys

def fcfs(processes, at, bt):
    # assume processes list already sorted by arrival time order provided
    n = len(processes)
    # pair and sort by arrival time then original order
    items = sorted(zip(processes, at, bt), key=lambda x: x[1])
    CT = [0]*n
    TAT = [0]*n
    WT = [0]*n
    timeline = []
    time = 0
    for i,(p,a,b) in enumerate(items):
        if time < a:
            # CPU idle until arrival
            timeline.append(("idle", time, a))
            time = a
        start = time
        time += b
        end = time
        CT[i] = end
        TAT[i] = CT[i] - a
        WT[i] = TAT[i] - b
        timeline.append((p, start, end))

    # map outputs back to original process order
    out = {}
    for i,(p,a,b) in enumerate(items):
        out[p] = {"AT":a,"BT":b,"CT":CT[i],"TAT":TAT[i],"WT":WT[i]}

    avg_tat = sum([v["TAT"] for v in out.values()])/n
    avg_wt = sum([v["WT"] for v in out.values()])/n
    return out, avg_tat, avg_wt, timeline

def print_table(result):
    keys = sorted(result.keys(), key=lambda x: x)  # alphabetical P1,P2...
    print("Process\tAT\tBT\tCT\tTAT\tWT")
    for k in keys:
        v = result[k]
        print(f"{k}\t{v['AT']}\t{v['BT']}\t{v['CT']}\t{v['TAT']}\t{v['WT']}")

def print_gantt(timeline):
    # timeline: list of (proc, start, end)
    print("\nGantt Chart:")
    for proc,start,end in timeline:
        print(f"| {proc} ", end="")
    print("|")
    # time markers
    for proc,start,end in timeline:
        print(f"{start}".ljust(6), end="")
    # print final end
    if timeline:
        print(f"{timeline[-1][2]}")
    else:
        print()

def load_input(path=None):
    if path:
        with open(path) as f:
            data = json.load(f)
    else:
        # interactive fallback
        n = int(input("Number of processes: "))
        procs = []
        at = []
        bt = []
        for i in range(n):
            procs.append("P"+str(i+1))
            at.append(int(input(f"AT of P{i+1}: ")))
            bt.append(int(input(f"BT of P{i+1}: ")))
        data = {"processes":procs,"AT":at,"BT":bt}
    return data

def main():
    path = None
    if len(sys.argv) >= 2:
        path = sys.argv[1]
    data = load_input(path)
    res, avg_tat, avg_wt, timeline = fcfs(data['processes'], data['AT'], data['BT'])
    print_table(res)
    print(f"\nAverage TAT = {avg_tat:.2f}")
    print(f"Average WT = {avg_wt:.2f}")
    print_gantt(timeline)

if __name__=="__main__":
    main()
