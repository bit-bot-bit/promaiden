import logging
from datetime import datetime
from modules.config_loader import load_config
from modules.prometheus_client import list_available_metrics, query_prometheus
from modules.chatgpt_client import analyze_with_chatgpt
from modules.report_generator import generate_report

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    config = load_config()
    service_name = config.get("service_name", "Unknown Service")
    prometheus_url = config.get("prometheus_url", "http://localhost:9090/api/v1/query")
    queries = config.get("metrics", [])
    chatgpt_api_key = config.get("chatgpt_api_key", "your_openai_api_key")
    start_time = config.get("start_time", "now-6h")
    end_time = config.get("end_time", "now")

    list_available_metrics(prometheus_url)

    generate_report(
        service_name=service_name,
        queries=queries,
        prometheus_url=prometheus_url,
        chatgpt_api_key=chatgpt_api_key,
        start_time=start_time,
        end_time=end_time,
        query_function=query_prometheus,
        analyze_function=analyze_with_chatgpt
    )

logging.info("Promaiden has successfully completed the report generation.")