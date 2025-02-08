import requests
import logging

def list_available_metrics(prometheus_url):
    """Fetch available Prometheus metrics."""
    logging.info("Fetching available metrics from Prometheus...")
    try:
        response = requests.get(f"{prometheus_url.replace('/api/v1/query', '/api/v1/label/__name__/values')}")
        if response.status_code == 200:
            metrics = response.json().get("data", [])
            logging.info(f"Available metrics: {', '.join(metrics[:20])}...")
        else:
            logging.warning(f"Failed to fetch available metrics. HTTP {response.status_code}: {response.text}")
    except requests.RequestException as e:
        logging.error(f"Error fetching available metrics: {e}")

def query_prometheus(query, start_time, end_time, prometheus_url):
    """Query Prometheus for metrics."""
    logging.info(f"Querying Prometheus: {query} from {start_time} to {end_time}")
    response = requests.get(prometheus_url, params={
        "query": query,
        "start": start_time,
        "end": end_time
    })
    data = response.json()

    if "data" not in data or "result" not in data.get("data", {}):
        logging.warning(f"No data returned for query: {query}.")
        return []
    
    logging.info(f"Received {len(data['data']['result'])} results for query: {query}")
    return data["data"].get("result", [])