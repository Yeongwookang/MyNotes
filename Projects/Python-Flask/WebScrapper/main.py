from flask import Flask, render_template, request, redirect, send_file
from indeed_extractor import extract_indeed_jobs
from job_to_save_csv import job_to_csv

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    limit = request.args.get("limit")
    
    # 검색어 없으면 홈으로
    if keyword == None or limit == None:    
        return redirect("/")
    
    limit = int(limit)
    file_name = f"{keyword}_{limit}"
    
    if file_name in db:
        jobs = db[file_name]
    
    else: 
        jobs = extract_indeed_jobs(keyword, limit)
        db[file_name] = jobs
    return render_template("search.html", keyword = keyword, limit = limit, jobs = jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    limit = request.args.get("limit")
    limit = int(limit)
    
    file_name = f"{keyword}_{limit}"
    
    if keyword == None or file_name not in db:    
        return redirect("/")
    
    else:
        job_to_csv(file_name, db[file_name])
        return send_file(f"{file_name}.csv", as_attachment=True)

app.run("localhost")