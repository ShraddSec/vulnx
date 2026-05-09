async def check_sql_injection(url):

    payloads = [
        "'",
        "' OR '1'='1",
        "'--"
    ]

    error_patterns = [
        "sql syntax",
        "mysql",
        "postgresql",
        "syntax error"
    ]

    import httpx

    async with httpx.AsyncClient(verify=False) as client:

        for payload in payloads:

            test_url = f"{url}?id={payload}"

            try:
                r = await client.get(test_url)

                text = r.text.lower()

                for error in error_patterns:

                    if error in text:
                        return {
                            "id": "sql_injection",
                            "name": "SQL Injection",
                            "severity": "Critical",
                            "description": "Possible SQL Injection detected",
                            "why_it_matters": "Attackers can access database data.",
                            "recommendation": "Use parameterized queries."
                        }

            except:
                pass

    return {
        "id": "sql_injection",
        "name": "SQL Injection",
        "severity": "Secure",
        "description": "No SQL injection patterns detected",
        "why_it_matters": "SQL injection can compromise databases.",
        "recommendation": "Continue using prepared statements."
    }