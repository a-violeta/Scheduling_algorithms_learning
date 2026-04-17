from fastapi import APIRouter
from typing import List
from models.process import Process
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.sjf_preemp import sjf_preemptive
from algorithms.rr import round_robin
from algorithms.priority import priority_non_preemptive
from algorithms.priority_preemp import priority_preemptive
from algorithms.priority_rr import priority_round_robin

router = APIRouter()

@router.post("/fcfs")
def run_fcfs(processes: List[Process]):
    result : dict = fcfs(processes)
    avg_wait = sum(p["waiting_time"] for p in result["results"]) / len(result["results"])
    result["average_waiting_time"] = avg_wait
    return result

@router.post("/sjf")
def run_sjf(processes: List[Process]):
    result : dict = sjf(processes)
    avg_wait = sum(p["waiting_time"] for p in result["results"]) / len(result["results"])
    result["average_waiting_time"] = avg_wait
    return result

@router.post("/sjf_preemptive")
def run_sjf_preemptive(processes: List[Process]):
    result : dict = sjf_preemptive(processes)
    avg_wait = sum(p["waiting_time"] for p in result["results"]) / len(result["results"])
    result["average_waiting_time"] = avg_wait
    return result

@router.post("/round_robin")
def run_round_robin(processes: List[Process], quantum: int):
    result : dict = round_robin(processes, quantum)
    avg_wait = sum(p["waiting_time"] for p in result["results"]) / len(result["results"])
    result["average_waiting_time"] = avg_wait
    return result

@router.post("/priority_non_preemptive")
def run_priority_non_preemptive(processes: List[Process]):
    result : dict = priority_non_preemptive(processes)
    avg_wait = sum(p["waiting_time"] for p in result["results"]) / len(result["results"])
    result["average_waiting_time"] = avg_wait
    return result

@router.post("/priority_preemptive")
def run_priority_preemptive(processes: List[Process]):
    result : dict = priority_preemptive(processes)
    avg_wait = sum(p["waiting_time"] for p in result["results"]) / len(result["results"])
    result["average_waiting_time"] = avg_wait
    return result

@router.post("/priority_round_robin")
def run_priority_round_robin(processes: List[Process], quantum: int):
    result : dict = priority_round_robin(processes, quantum)
    avg_wait = sum(p["waiting_time"] for p in result["results"]) / len(result["results"])
    result["average_waiting_time"] = avg_wait
    return result