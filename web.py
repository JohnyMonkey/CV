from flask import Flask, render_template, Response, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('srt-resume.html')

import pdfkit

@app.route("/download")
def route_download():
    
    # Get the HTML output
    out = render_template("srt-resume.html")
    
    # PDF options
    options = {
        "orientation": "landscape",
        "page-size": "A4",
        "margin-top": "1.0cm",
        "margin-right": "1.0cm",
        "margin-bottom": "1.0cm",
        "margin-left": "1.0cm",
        "encoding": "UTF-8",
    }
    
    # Build PDF from HTML 
    pdf = pdfkit.from_string(out, options=options)
    
    # Download the PDF
    return Response(pdf, mimetype="application/pdf")
    
