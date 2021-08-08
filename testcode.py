from reportlab.pdfgen import canvas 
fileName = 'MyDoc.pdf'
canvas = canvas.Canvas(fileName)
docTitle = 'Document Title'
docExcerpt = 'Document Excerpt'
textLines = list
textLines = [
    'This is text line 1', 
    'this is text lines 3',
    'this is text lines 3'
]

canvas.setTitle(docTitle)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)
canvas.drawString(30,750,'OFFICIAL COMMUNIQUE')
canvas.drawString(30,735,'OF ACME INDUSTRIES')
canvas.drawString(500,750,"12/12/2010")
canvas.line(480,747,580,747)
canvas.drawString(275,725,'AMOUNT OWED:')
canvas.drawString(500,725,"$1,000.00")
canvas.line(378,723,580,723)
canvas.drawString(30,703,'RECEIVED BY:')
canvas.line(120,700,580,700)
canvas.drawString(120,703,"JOHN DOE")
canvas.save()


def export_pdf(request):
    fs = FileSystemStorage()
    filename = 'pythonpdf.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="pythonpdf.pdf"'
            return response
    else:
        return HttpResponseNotFound("The Requested PDF is unavailable in our Database")