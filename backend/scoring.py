def calculate_score(vulnerabilities):

    score = 100

    summary = {
        "secure": 0,
        "warning": 0,
        "critical": 0
    }

    for v in vulnerabilities:

        if v["severity"] == "Critical":
            score -= 30
            summary["critical"] += 1

        elif v["severity"] == "Warning":
            score -= 10
            summary["warning"] += 1

        else:
            summary["secure"] += 1

    score = max(score, 0)

    if score >= 80:
        level = "Low"
    elif score >= 50:
        level = "Medium"
    else:
        level = "High"

    return {
        "score": score,
        "level": level,
        "summary": summary
    }