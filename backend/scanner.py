import time
from security import check_https
from headers import check_headers
from sql import check_sql_injection
from scoring import calculate_score


async def run_scan(url, scan_id, scans):

    start = time.time()

    logs = []
    vulnerabilities = []

    def log(message):
        logs.append(message)
        scans[scan_id]["logs"] = logs

    log("Initializing scan")

    https_result = await check_https(url)
    log("Checking HTTPS configuration")
    vulnerabilities.append(https_result)

    scans[scan_id]["progress"] = 30

    header_results = await check_headers(url)
    log("Analyzing security headers")
    vulnerabilities.extend(header_results)

    scans[scan_id]["progress"] = 60

    sql_result = await check_sql_injection(url)
    log("Testing SQL injection")
    vulnerabilities.append(sql_result)

    scans[scan_id]["progress"] = 90

    score_data = calculate_score(vulnerabilities)

    scan_time = round(time.time() - start, 2)

    result = {
        "target": url,
        "scan_time": f"{scan_time} seconds",
        "risk_score": score_data["score"],
        "risk_level": score_data["level"],
        "summary": score_data["summary"],
        "vulnerabilities": vulnerabilities
    }

    scans[scan_id]["result"] = result
    scans[scan_id]["progress"] = 100
    scans[scan_id]["status"] = "completed"

    log("Scan completed")