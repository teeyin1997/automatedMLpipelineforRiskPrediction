import threading
import multiprocessing
import os

def init(lock):
    global starting
    starting = lock

def run_model(ipynb):
    starting.acquire() # no other process can get it until it is released
    threading.Timer(5, starting.release).start() # release in a second
    script = "jupyter notebook " + ipynb
    os.system(script)

if __name__=="__main__":
   ipynb = ['deployment/run_deployment.ipynb', 'experiment/experiment.ipynb', 'pipeline/stage1_alert.ipynb', 'pipeline/stage2_trigger_pipeline.ipynb', 'pipeline/stage3_validation.ipynb', 'monitor/run_monitor_ui.ipynb']
   pool = multiprocessing.Pool(processes=12, 
               initializer=init, initargs=[multiprocessing.Lock()])
   for _ in pool.imap_unordered(run_model, ipynb):
       pass