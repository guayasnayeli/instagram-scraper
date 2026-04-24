def generate_report(metrics, followers):
    report = "\n=== ANÁLISIS FINAL ===\n\n"

    report += f"Seguidores: {followers}\n"
    report += f"Promedio de likes: {metrics['avg_likes']}\n"
    report += f"Promedio de comentarios: {metrics['avg_comments']}\n"
    report += f"Engagement: {metrics['engagement']:.5f}\n\n"

    if metrics["engagement"] < 0.01:
        engagement_text = "bajo nivel de interacción"
    else:
        engagement_text = "nivel normal de interacción"

    if 1 in metrics["benford"] and metrics["benford"][1] < 0.25:
        benford_text = "posibles anomalías (Ley de Benford)"
    else:
        benford_text = "comportamiento natural"

    report += "CONCLUSIÓN:\n\n"
    report += f"El perfil presenta {engagement_text}. "
    report += f"Además, el análisis indica {benford_text}. "

    if metrics["engagement"] < 0.01:
        report += "Esto podría indicar comportamiento no orgánico.\n"
    else:
        report += "El comportamiento parece orgánico.\n"

    return report