import httpx

async def check_https(url):

    if url.startswith("https://"):
        severity = "Secure"
        desc = "HTTPS is enabled."
    else:
        severity = "Critical"
        desc = "HTTPS is not enabled."

    return {
        "id": "https_enabled",
        "name": "HTTPS Configuration",
        "severity": severity,
        "description": desc,
        "why_it_matters": "HTTPS protects data between user and server.",
        "recommendation": "Enable HTTPS with a valid SSL certificate."
    }