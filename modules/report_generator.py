import logging
from datetime import datetime

def format_metrics(metrics):
    """Format Prometheus metrics into structured JSON."""
    if not metrics:
        logging.warning("No metrics data available.")
        return {"error": "No data available"}
    
    return [{"metric": metric.get("metric", {}), "values": metric.get("values", [])} for metric in metrics]

def generate_report(service_name, queries, prometheus_url, chatgpt_api_key, start_time, end_time, query_function, analyze_function):
    """Fetch metrics, analyze each separately, and generate a report."""
    logging.info(f"Generating report for {service_name}")

    report_sections = [f"# Performance Report for {service_name} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"]
    report_sections.append("## Summary\nThis report analyzes key Prometheus metrics and provides insights into system performance.")

    for query in queries:
        metrics = query_function(query, start_time, end_time, prometheus_url)
        if not metrics:
            report_sections.append(f"\n### Analysis for Query: {query}\nNo data available. Verify Prometheus configuration.")
            continue

        formatted_metrics = format_metrics(metrics)
        analysis = analyze_function(chatgpt_api_key, query, formatted_metrics)
        report_sections.append(f"\n### Analysis for Query: {query}\n{analysis}")

    report_text = "\n".join(report_sections)

    with open("performance_report.txt", "w") as f:
        f.write(report_text)

    logging.info("Formalized report generated: performance_report.txt")