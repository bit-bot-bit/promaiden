import openai
import logging

def analyze_with_chatgpt(api_key, query, metrics_json):
    """Send the metric data to ChatGPT for analysis with logging."""
    client = openai.OpenAI(api_key=api_key)
    
    prompt = f"""
    You are an expert in system performance analysis. Given the following Prometheus metric data for '{query}', generate a structured performance report with the following sections:
    
    1. **Overview**: Explain what this metric measures and its importance.
    2. **Key Findings**: Summarize trends or anomalies observed.
    3. **Impact Analysis**: Describe possible impacts on performance.
    4. **Recommendations**: Provide actionable insights.

    ### Prometheus Data:
    {metrics_json}

    Format the response professionally.
    """
    
    logging.info(f"Sending data to ChatGPT for analysis: {query}")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert in system performance analysis."},
                {"role": "user", "content": prompt}
            ]
        )
        chatgpt_response = response.choices[0].message.content
        logging.info(f"Received ChatGPT response for {query}")
        return chatgpt_response
    except Exception as e:
        logging.error(f"Error communicating with ChatGPT API: {e}")
        return "Error generating analysis from ChatGPT."