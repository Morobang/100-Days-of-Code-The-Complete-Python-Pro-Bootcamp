# Day 70 — Data Pipeline — SOLUTIONS
import requests, sqlite3, csv, logging

logging.basicConfig(level=logging.INFO)

def fetch_data(url):
    try:
        r=requests.get(url,timeout=10); r.raise_for_status(); return r.json()
    except Exception as e:
        logging.error(f'Fetch failed: {e}'); return []

def transform(records):
    cleaned=[]
    for r in records:
        clean={k.lower().strip():v.strip() if isinstance(v,str) else v for k,v in r.items()}
        cleaned.append(clean)
    return cleaned

def load_to_db(records,db_path,table_name):
    if not records: return 0
    cols=list(records[0].keys())
    conn=sqlite3.connect(db_path)
    cols_def=','.join(f'{c} TEXT' for c in cols)
    conn.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({cols_def})')
    placeholders=','.join('?'*len(cols))
    conn.executemany(f'INSERT INTO {table_name} VALUES ({placeholders})',[tuple(r[c] for c in cols) for r in records])
    conn.commit(); n=conn.execute(f'SELECT COUNT(*) FROM {table_name}').fetchone()[0]; conn.close(); return n

def export_csv(db_path,table_name,output_path):
    conn=sqlite3.connect(db_path); conn.row_factory=sqlite3.Row
    rows=conn.execute(f'SELECT * FROM {table_name}').fetchall()
    conn.close()
    if not rows: return 0
    with open(output_path,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows([dict(r) for r in rows])
    return len(rows)

def run_pipeline(url,db_path,csv_path):
    logging.info('Starting pipeline')
    raw=fetch_data(url); logging.info(f'Fetched {len(raw)} records')
    clean=transform(raw); logging.info(f'Transformed {len(clean)} records')
    loaded=load_to_db(clean,db_path,'pipeline_data'); logging.info(f'Loaded {loaded} rows')
    exported=export_csv(db_path,'pipeline_data',csv_path); logging.info(f'Exported {exported} rows')
    return {'fetched':len(raw),'loaded':loaded,'exported':exported}
