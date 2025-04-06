import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_data():
    base_signal = 50 + 10 * np.sin(np.linspace(0, 20, 1000))
    cpu_usage = base_signal + np.random.normal(0, 5, 1000)
    memory_usage = 0.8 * base_signal + np.random.normal(0, 3, 1000)
    disk_io = 0.5 * base_signal + np.random.normal(0, 2, 1000)

    metrics = pd.DataFrame({
        'timestamp': pd.date_range(start='2025-01-01', periods=1000, freq='5min'),
        'cpu_usage': cpu_usage,
        'memory_usage':memory_usage,
        'disk_io': disk_io,
        'network_in': np.random.normal(20, 5, 1000),
        'network_out': np.random.normal(18, 6, 1000),
        'db_queries': np.random.normal(100, 30, 1000),
        'db_latency': np.random.normal(5, 2, 1000),
        'app_errors': np.random.normal(2, 1, 1000),
        'response_time': np.random.normal(200, 50, 1000),
        'active_users': np.random.normal(500, 100, 1000)
    })

    metrics.to_csv('metrics.csv', index=False)