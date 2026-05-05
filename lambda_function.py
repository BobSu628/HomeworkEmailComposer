from app.job import run_job

def handler(event, context):
    run_job()
    return {"status": "ok"}