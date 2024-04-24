def greedy_job_scheduling(jobs):
    # Sort the jobs based on their finish times
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)
    schedule = []

    # Initialize the current time
    current_time = 0

    for i, job in enumerate(jobs):
        start_time, finish_time = job
        if start_time >= current_time:
            # If the job can be scheduled without overlap, schedule it
            schedule.append((i+1, start_time, finish_time))
            current_time = finish_time

    return schedule

def main():
    jobs = []
    num_jobs = int(input("Enter the number of jobs: "))
    for i in range(num_jobs):
        start_time = int(input(f"Enter start time for job {i+1}: "))
        finish_time = int(input(f"Enter finish time for job {i+1}: "))
        jobs.append((start_time, finish_time))

    schedule = greedy_job_scheduling(jobs)
    print("\nOptimized Schedule:")
    for job in schedule:
        print("Job", job[0], ":", job[1], "-", job[2])

main()
