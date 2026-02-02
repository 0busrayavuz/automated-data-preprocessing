from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(path, metrics):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(path)
    story = []

    story.append(Paragraph("AI Data Cleaning Report", styles["Title"]))

    for stage, values in metrics.items():
        story.append(Paragraph(f"<b>{stage.upper()}</b>", styles["Heading2"]))
        for k, v in values.items():
            story.append(Paragraph(f"{k}: {v}", styles["Normal"]))

    doc.build(story)
