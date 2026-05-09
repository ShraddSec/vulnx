import httpx
async def check_headers(url):

    headers_needed = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "Strict-Transport-Security",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]

    results = []

    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(url)

    for header in headers_needed:

        if header in response.headers:
            severity = "Secure"
            desc = f"{header} is configured"
        else:
            severity = "Warning"
            desc = f"{header} header missing"

        results.append({
            "id": header.lower(),
            "name": header,
            "severity": severity,
            "description": desc,
            "why_it_matters": "Security headers protect against attacks.",
            "recommendation": f"Configure {header} header."
        })

    return results