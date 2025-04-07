# Project : Implement Time2vec on time series data and fetch top 3 correlations 

## 🔹 1. Synthetic Dataset Creation

- Dataset consists of **1000 rows** and **10 metrics**.
- Three metrics are intentionally correlated by fitting them to a shared base signal:
  - `cpu_usage`
  - `memory_usage`
  - `disk_io`
- Remaining metrics are generated using Gaussian noise:
  - `network_in`
  - `network_out`
  - `db_queries`
  - `db_latency`
  - `app_errors`
  - `response_time`
  - `active_users`

    Dataset saved as `data/metrics.csv`  
    Data generation logic is in `create_data.py`

---
## 🔹 2. Time2Vec Model

- Time2Vec implementation inspired by: [Time2Vec-PyTorch](https://github.com/ojus1/Time2Vec-PyTorch)
- Based on the formulation in the [original paper](https://arxiv.org/pdf/1907.05321.pdf):
t2v(τ)[i] = ωᵢτ + ϕᵢ, if i = 0
F(ωᵢτ + ϕᵢ), if 1 ≤ i ≤ k

## 🔹 3. Inference & Embedding

- Normalized time values are passed to the Time2Vec model.
- Outputs a time embedding vector for each timestamp.
- These embeddings are used to assess similarity between time series.

---
## similarity search :
- Pearsons correlation is used to find similar vectors 

## alternatives : 
- we can use the faiss similarity search as well as cosine similarity.

## project structure 
## 📂 Project Structure

- `Data/`  
  &nbsp;&nbsp;&nbsp;&nbsp;├── `create_data.py` – Script to generate synthetic data  
  &nbsp;&nbsp;&nbsp;&nbsp;└── `metrics.csv` – Generated synthetic multivariate time-series dataset

- `Readme.md` – Project documentation

- `Time_vector_correlation.ipynb` – Main notebook implementing Time2Vec and correlation analysis
