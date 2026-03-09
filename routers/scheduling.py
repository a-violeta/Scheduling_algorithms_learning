from fastapi import APIRouter
from typing import List
from models.process import Process
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.sjf_preemp import sjf_preemptive
from algorithms.rr import round_robin

router = APIRouter()

@router.post("/fcfs")
def run_fcfs(processes: List[Process]):
    return fcfs(processes)

@router.post("/sjf")
def run_sjf(processes: List[Process]):
    return sjf(processes)

@router.post("/sjf_preemptive")
def run_sjf_preemptive(processes: List[Process]):
    return sjf_preemptive(processes)

@router.post("/round_robin")
def run_round_robin(processes: List[Process], quantum: int):
    return round_robin(processes, quantum)