job_queue = ["parse_data", "validate_scehma", "write_output", "notify_client"]

while job_queue:
    job = job_queue.pop(0)
    print(f"Processing: {job}")

print(f"All {len(job_queue)} remaining jobs: done")